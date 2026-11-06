# clash_rules_merged

Clash / Mihomo 规则聚合（Domain 规则集与 MRS 二进制规则集）。

每日自动抓取上游规则源，并合并用户自定义规则，经过子域名收割与去重优化后自动生成。

## 架构说明

本项目采用**双分支架构**：
- **`main` 分支**：纯代码与配置文件（Python 源码、Action 流程、自定义规则），保持轻量，永不膨胀。
- **`release` 分支**：编译生成的 `.yaml` 和 `.mrs` 规则文件（单次提交覆盖，体积稳定在 ~7MB）。

---

## 订阅链接（指向 release 分支）

### 1. 直连域名 (Direct)
- **MRS 格式** (Mihomo 推荐):
  ```
  https://raw.githubusercontent.com/in-ci/clash_rules_merged/release/clash_direct_domain_rules_merged.mrs
  ```
- **YAML 格式**:
  ```
  https://raw.githubusercontent.com/in-ci/clash_rules_merged/release/clash_direct_domain_rules_merged.yaml
  ```

### 2. 代理域名 (Proxy)
- **MRS 格式**:
  ```
  https://raw.githubusercontent.com/in-ci/clash_rules_merged/release/clash_proxy_domain_rules_merged.mrs
  ```
- **YAML 格式**:
  ```
  https://raw.githubusercontent.com/in-ci/clash_rules_merged/release/clash_proxy_domain_rules_merged.yaml
  ```

### 3. 广告拦截域名 (Reject)
- **MRS 格式**:
  ```
  https://raw.githubusercontent.com/in-ci/clash_rules_merged/release/clash_reject_domain_rules_merged.mrs
  ```
- **YAML 格式**:
  ```
  https://raw.githubusercontent.com/in-ci/clash_rules_merged/release/clash_reject_domain_rules_merged.yaml
  ```

### 4. 国外 AI 代理域名 (AI Proxy)
涵盖 OpenAI / ChatGPT / Sora、Claude / Anthropic、Google Gemini、Copilot、Perplexity、Grok、Cursor、Midjourney、Hugging Face 等主流海外 AI 服务。
- **MRS 格式**:
  ```
  https://raw.githubusercontent.com/in-ci/clash_rules_merged/release/clash_ai_proxy_domain_rules_merged.mrs
  ```
- **YAML 格式**:
  ```
  https://raw.githubusercontent.com/in-ci/clash_rules_merged/release/clash_ai_proxy_domain_rules_merged.yaml
  ```

---

## 自定义规则说明

如需在对应分类中添加自定义规则，直接在 `main` 分支编辑对应文件即可：
- `custom_clash_rules_direct.yaml` - 自定义直连规则
- `custom_clash_rules_porxy.yaml` - 自定义代理规则
- `custom_clash_rules_reject.yaml` - 自定义拦截规则
- `custom_clash_rules_ai_porxy.yaml` - 自定义国外 AI 代理规则
