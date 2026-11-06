# clash_rules_merged

Clash / Mihomo 规则聚合（Domain 规则集与 MRS 二进制规则集）。

每日自动抓取上游规则源，并合并用户自定义规则，经过子域名收割与去重优化后自动生成。

---

## 规则订阅链接

### 1. 代理域名 (Proxy)

#### MRS 格式:
- 原始链接: `https://raw.githubusercontent.com/in-ci/clash_rules_merged/release/clash_proxy_domain_rules_merged.mrs`
- 加速链接: `https://testingcf.jsdelivr.net/gh/in-ci/clash_rules_merged@release/clash_proxy_domain_rules_merged.mrs`

#### YAML 格式:
- 原始链接: `https://raw.githubusercontent.com/in-ci/clash_rules_merged/release/clash_proxy_domain_rules_merged.yaml`
- 加速链接: `https://testingcf.jsdelivr.net/gh/in-ci/clash_rules_merged@release/clash_proxy_domain_rules_merged.yaml`

---

### 2. 国外 AI 代理域名 (AI Proxy)
涵盖 OpenAI / ChatGPT / Sora、Claude / Anthropic、Google Gemini、Copilot、Perplexity、Grok、Cursor、Midjourney、Hugging Face 等主流海外 AI 服务。

#### MRS 格式:
- 原始链接: `https://raw.githubusercontent.com/in-ci/clash_rules_merged/release/clash_ai_proxy_domain_rules_merged.mrs`
- 加速链接: `https://testingcf.jsdelivr.net/gh/in-ci/clash_rules_merged@release/clash_ai_proxy_domain_rules_merged.mrs`

#### YAML 格式:
- 原始链接: `https://raw.githubusercontent.com/in-ci/clash_rules_merged/release/clash_ai_proxy_domain_rules_merged.yaml`
- 加速链接: `https://testingcf.jsdelivr.net/gh/in-ci/clash_rules_merged@release/clash_ai_proxy_domain_rules_merged.yaml`

---

### 3. 直连域名 (Direct)

#### MRS 格式:
- 原始链接: `https://raw.githubusercontent.com/in-ci/clash_rules_merged/release/clash_direct_domain_rules_merged.mrs`
- 加速链接: `https://testingcf.jsdelivr.net/gh/in-ci/clash_rules_merged@release/clash_direct_domain_rules_merged.mrs`

#### YAML 格式:
- 原始链接: `https://raw.githubusercontent.com/in-ci/clash_rules_merged/release/clash_direct_domain_rules_merged.yaml`
- 加速链接: `https://testingcf.jsdelivr.net/gh/in-ci/clash_rules_merged@release/clash_direct_domain_rules_merged.yaml`

---

### 4. 广告拦截域名 (Reject)

#### MRS 格式:
- 原始链接: `https://raw.githubusercontent.com/in-ci/clash_rules_merged/release/clash_reject_domain_rules_merged.mrs`
- 加速链接: `https://testingcf.jsdelivr.net/gh/in-ci/clash_rules_merged@release/clash_reject_domain_rules_merged.mrs`

#### YAML 格式:
- 原始链接: `https://raw.githubusercontent.com/in-ci/clash_rules_merged/release/clash_reject_domain_rules_merged.yaml`
- 加速链接: `https://testingcf.jsdelivr.net/gh/in-ci/clash_rules_merged@release/clash_reject_domain_rules_merged.yaml`

---

## 备用下载方式：GitHub Releases 滚动发布

本项目同时维护 **Rolling Release**，页面直接下载或 Release 镜像加速：
- 发布页面: [Releases · in-ci/clash_rules_merged (Tag: latest)](https://github.com/in-ci/clash_rules_merged/releases/tag/latest)
- Release 官方直链前缀: `https://github.com/in-ci/clash_rules_merged/releases/download/latest/`
- Release 镜像加速前缀: `https://ghfast.top/https://github.com/in-ci/clash_rules_merged/releases/download/latest/`

---

## 自定义规则说明

如需在对应分类中添加自定义规则，直接在 `main` 分支编辑对应文件即可：
- `custom_clash_rules_direct.yaml` - 自定义直连规则
- `custom_clash_rules_porxy.yaml` - 自定义代理规则
- `custom_clash_rules_reject.yaml` - 自定义拦截规则
- `custom_clash_rules_ai_porxy.yaml` - 自定义国外 AI 代理规则
