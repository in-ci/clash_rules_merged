# clash_rules_merged

Clash / Mihomo 规则聚合（Domain 规则集与 MRS 二进制规则集）。

每日自动抓取上游规则源，并合并用户自定义规则，经过子域名收割与去重优化后自动生成。

## 架构说明

本项目采用 **GitHub Releases 滚动发布机制 (Rolling Release)**：
- **`main` 仓库代码**：仅包含 Python 源码、Action 构建流程、自定义规则文件，体积仅 ~25 KB。
- **Releases 附件发布**：编译生成的 `.yaml` 文本规则与 `.mrs` 二进制规则文件统一发布在 [GitHub Releases (Tag: latest)](https://github.com/in-ci/clash_rules_merged/releases/tag/latest) 页面作为附件。
- **存储优势**：Release 附件存储在 GitHub 云端对象存储上，**完全零占用 Git 仓库磁盘配额**，且每日滚动覆盖同一版本，永不堆积历史。

---

## 订阅链接（GitHub Releases 直链）

### 1. 直连域名 (Direct)
- **MRS 格式** (Mihomo 推荐):
  ```
  https://github.com/in-ci/clash_rules_merged/releases/download/latest/clash_direct_domain_rules_merged.mrs
  ```
- **YAML 格式**:
  ```
  https://github.com/in-ci/clash_rules_merged/releases/download/latest/clash_direct_domain_rules_merged.yaml
  ```

### 2. 代理域名 (Proxy)
- **MRS 格式**:
  ```
  https://github.com/in-ci/clash_rules_merged/releases/download/latest/clash_proxy_domain_rules_merged.mrs
  ```
- **YAML 格式**:
  ```
  https://github.com/in-ci/clash_rules_merged/releases/download/latest/clash_proxy_domain_rules_merged.yaml
  ```

### 3. 广告拦截域名 (Reject)
- **MRS 格式**:
  ```
  https://github.com/in-ci/clash_rules_merged/releases/download/latest/clash_reject_domain_rules_merged.mrs
  ```
- **YAML 格式**:
  ```
  https://github.com/in-ci/clash_rules_merged/releases/download/latest/clash_reject_domain_rules_merged.yaml
  ```

### 4. 国外 AI 代理域名 (AI Proxy)
涵盖 OpenAI / ChatGPT / Sora、Claude / Anthropic、Google Gemini、Copilot、Perplexity、Grok、Cursor、Midjourney、Hugging Face 等主流海外 AI 服务。
- **MRS 格式**:
  ```
  https://github.com/in-ci/clash_rules_merged/releases/download/latest/clash_ai_proxy_domain_rules_merged.mrs
  ```
- **YAML 格式**:
  ```
  https://github.com/in-ci/clash_rules_merged/releases/download/latest/clash_ai_proxy_domain_rules_merged.yaml
  ```

---

## 自定义规则说明

如需在对应分类中添加自定义规则，直接在 `main` 分支编辑对应文件即可：
- `custom_clash_rules_direct.yaml` - 自定义直连规则
- `custom_clash_rules_porxy.yaml` - 自定义代理规则
- `custom_clash_rules_reject.yaml` - 自定义拦截规则
- `custom_clash_rules_ai_porxy.yaml` - 自定义国外 AI 代理规则
