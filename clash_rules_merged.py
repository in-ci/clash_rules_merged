#!/usr/bin/env python3
import requests
import string
import re

def download_text(url):
    """下载远程文本并返回行列表"""
    print(f"正在下载: {url}")
    try:
        resp = requests.get(url, timeout=20)
        resp.raise_for_status()
        resp.encoding = resp.apparent_encoding
        return resp.text.splitlines()
    except Exception as e:
        print(f"下载失败: {url} | 错误: {e}")
        return []

def get_key_char(line: str):
    """获取规则首字母用于排序 (0-9 -> a-z)"""
    s = line.lstrip("- ' +.")
    if not s:
        return "~"
    return s[0].lower()

def dedup_and_output(urls, output_file):
    """
    核心逻辑：
    1. 提取所有域名并区分是否为通配符 (+.)
    2. 建立通配符母体索引
    3. 剔除所有已被母体覆盖的冗余子域名
    """
    all_entries = set()
    total_raw = 0

    # 第一步：标准化抓取
    for url in urls:
        lines = download_text(url)
        for line in lines:
            # 匹配格式: - +.example.com 或 - example.com (兼容引号)
            match = re.search(r'-\s*[\'"]?(\+\.)?([^\s\'"]+)[\'"]?', line)
            if match:
                total_raw += 1
                is_wildcard = bool(match.group(1))
                domain = match.group(2).lower().strip('.')
                all_entries.add((domain, is_wildcard))

    # 第二步：提取所有的通配符母体
    # 例如：从 +.1.google.com 提取出 1.google.com 存入母体集
    wildcard_parents = {d for d, is_w in all_entries if is_w}

    # 第三步：精简逻辑（子域名收割）
    final_payload = []
    
    for dom, is_w in all_entries:
        if is_w:
            # 通配符条目是最高级，必须保留
            final_payload.append(f"- '+.{dom}'")
        else:
            # 普通域名：检查其所有上级后缀是否存在于通配符母体中
            is_redundant = False
            parts = dom.split('.')
            # 逐级向上检查：52.14.1.google.com -> 14.1.google.com -> 1.google.com
            for i in range(len(parts)):
                parent_suffix = '.'.join(parts[i:])
                if parent_suffix in wildcard_parents:
                    is_redundant = True
                    break
            
            if not is_redundant:
                final_payload.append(f"- '{dom}'")

    # 第四步：排序 (数字 0-9 -> 字母 a-z -> 其它)
    sorted_lines = sorted(list(set(final_payload)), key=lambda x: (
        not get_key_char(x).isdigit(),
        not get_key_char(x).isalpha(),
        x.lower()
    ))

    # 第五步：写入文件
    with open(output_file, "w", encoding="utf-8") as out:
        out.write("payload:\n")
        for line in sorted_lines:
            out.write(line + "\n")

    print(f"[{output_file}] 原始总行数: {total_raw} | 精简后唯一行数: {len(sorted_lines)}")

if __name__ == "__main__":
    # 定义输出文件
    direct_out = "clash_direct_domain_rules_merged.yaml"
    proxy_out = "clash_proxy_domain_rules_merged.yaml"
    reject_out = "clash_reject_domain_rules_merged.yaml"

    # 规则源配置
    direct_urls = [
        "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/direct.txt",
        "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/category-games@cn.yaml",
        "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/category-games-cn.yaml",
        "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/steam@cn.yaml",
        "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/private.yaml"
    ]

    proxy_urls = [
        "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/proxy.txt",
    ]

    reject_urls = [
        "https://anti-ad.net/clash.yaml",
        "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/reject.txt",
        "https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblockmihomolite.yaml",
        "https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblockmihomo.yaml",
    ]

    # 执行合并与精简
    dedup_and_output(direct_urls, direct_out)
    dedup_and_output(proxy_urls, proxy_out)
    dedup_and_output(reject_urls, reject_out)
