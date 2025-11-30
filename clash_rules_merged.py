#!/usr/bin/env python3
"""
从 GitHub 下载 Clash 规则 → 内存处理 → 去重 → 按首字母分组排序（0-9 → a-z）→ 输出 payload 文件
"""

import requests
import string


def download_text(url):
    """下载远程文本，不写入硬盘，仅返回行列表"""
    print(f"下载: {url}")
    resp = requests.get(url, timeout=20)
    resp.raise_for_status()
    resp.encoding = resp.apparent_encoding
    return resp.text.splitlines()


def extract_rule_lines(lines):
    """
    从 YAML 或 TXT 中提取规则行，只保留以 '-' 开头的 clash 域名规则
    """
    results = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("-"):
            results.append(line.rstrip("\r\n"))
    return results


def get_key_char(line: str):
    """
    获取规则首字母（真正的域名首字母，而不是前面的 "- +."）
    例如：
      - +.0.myikas.com → '0'
      - +.abc.com      → 'a'
    """
    s = line.lstrip("- +.")  # 去掉 "- +." 前缀
    if not s:
        return "~"  # 末尾处理
    return s[0].lower()


def group_sort_stable(lines):
    """
    按首字符分组排序：
    1. 0–9
    2. a–z
    3. 其它字符最后
    组内保持原来顺序（稳定）
    """

    groups = {
        "digit": [],  # 0-9
        "alpha": [],  # a-z
        "other": [],  # 其它
    }

    for line in lines:
        key = get_key_char(line)

        if key in "0123456789":
            groups["digit"].append(line)
        elif key in string.ascii_lowercase:
            groups["alpha"].append(line)
        else:
            groups["other"].append(line)

    # 合并：数字 → 字母 → 其它
    return groups["digit"] + groups["alpha"] + groups["other"]


def dedup_and_output(urls, output_file):
    seen = set()
    merged_lines = []

    total = 0
    unique = 0

    for url in urls:
        lines = download_text(url)
        rule_lines = extract_rule_lines(lines)

        for line in rule_lines:
            total += 1
            if line not in seen:
                seen.add(line)
                unique += 1
                merged_lines.append(line)  # 保序加入

    # print(f"\n已保序合并唯一规则 {unique} 条，开始按首字母分组排序…")

    # 按你的要求排序
    sorted_lines = group_sort_stable(merged_lines)

    # 写入输出
    with open(output_file, "w", encoding="utf-8") as out:
        out.write("payload:\n")
        for line in sorted_lines:
            out.write(line + "\n")

    # print(f"最终写入：{output_file}")
    # print(f"总计读取 {total} 行，唯一 {unique} 行，已按 0-9, a-z 分组排序。")


if __name__ == "__main__":

    direct_output_file = "clash_direct_domain_rules_merged.txt"
    proxy_output_file = "clash_proxy_domain_rules_merged.txt"
    reject_output_file = "clash_reject_domain_rules_merged.txt"

    # 直连域名规则url列表
    direct_urls = [
        "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/direct.txt",
    ]

    # 代理域名规则url列表
    proxy_urls = [
        "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/proxy.txt",
    ]

    # 广告域名规则url列表
    reject_urls = [
        "https://anti-ad.net/clash.yaml",
        "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/reject.txt",
        "https://raw.githubusercontent.com/REIJI007/AdBlock_Rule_For_Clash/main/adblock_reject.yaml",
        # "https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblockmihomolite.yaml",
        # "https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblockmihomo.yaml"
    ]

    dedup_and_output(direct_urls, direct_output_file)
    dedup_and_output(proxy_urls, proxy_output_file)
    dedup_and_output(reject_urls, reject_output_file)
