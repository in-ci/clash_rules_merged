# clash_rules_merged

Clash / Mihomo 规则聚合（Domain 规则集与 MRS 二进制规则集）。

每日自动抓取上游规则源，并合并用户自定义规则，经过子域名收割与去重优化后自动生成。

---

## 架构说明：双轨发布机制 (Dual-Track)

本项目采用**双轨发布机制**，同时兼顾国内 CDN 加速与页面直观下载，且 Git 源码仓库**永不膨胀**：

1. **`main` 源码分支**：纯文本代码与自定义规则配置（不到 30 KB），日常开发随便 `pull/push` 永不冲突。
2. **轨道一：jsDelivr CDN 加速（`release` 分支）**：每次单 Commit 强制覆盖推送，专供 `testingcf.jsdelivr.net` / `cdn.jsdelivr.net` 加速，大小固定不累加。
3. **轨道二：GitHub Releases 滚动发布（Tag: `latest`）**：附件直接存放在云存储，零占用 Git 仓库磁盘配额，直链永久固定。

---

## 订阅链接配置指南

### 轨道一：jsDelivr CDN 加速链接（国内免翻墙首选）

原先的 `testingcf.jsdelivr.net` 依然完美支持（分支名由 `main` 调整为 `release`）：

#### 1. 代理域名 (Proxy)
- **MRS 格式**:
  ```
  https://testingcf.jsdelivr.net/gh/in-ci/clash_rules_merged@release/clash_proxy_domain_rules_merged.mrs
  ```
- **YAML 格式**:
  ```
  https://testingcf.jsdelivr.net/gh/in-ci/clash_rules_merged@release/clash_proxy_domain_rules_merged.yaml
  ```

#### 2. 国外 AI 代理域名 (AI Proxy)
- **MRS 格式**:
  ```
  https://testingcf.jsdelivr.net/gh/in-ci/clash_rules_merged@release/clash_ai_proxy_domain_rules_merged.mrs
  ```
- **YAML 格式**:
  ```
  https://testingcf.jsdelivr.net/gh/in-ci/clash_rules_merged@release/clash_ai_proxy_domain_rules_merged.yaml
  ```

#### 3. 直连域名 (Direct)
- **MRS 格式**:
  ```
  https://testingcf.jsdelivr.net/gh/in-ci/clash_rules_merged@release/clash_direct_domain_rules_merged.mrs
  ```
- **YAML 格式**:
  ```
  https://testingcf.jsdelivr.net/gh/in-ci/clash_rules_merged@release/clash_direct_domain_rules_merged.yaml
  ```

#### 4. 广告拦截域名 (Reject)
- **MRS 格式**:
  ```
  https://testingcf.jsdelivr.net/gh/in-ci/clash_rules_merged@release/clash_reject_domain_rules_merged.mrs
  ```
- **YAML 格式**:
  ```
  https://testingcf.jsdelivr.net/gh/in-ci/clash_rules_merged@release/clash_reject_domain_rules_merged.yaml
  ```

---

### 轨道二：GitHub Releases 附件直链

页面直接访问：[Releases · in-ci/clash_rules_merged](https://github.com/in-ci/clash_rules_merged/releases/tag/latest)

* **官方直链（客户端走代理时）**：
  * Proxy MRS: `https://github.com/in-ci/clash_rules_merged/releases/download/latest/clash_proxy_domain_rules_merged.mrs`
  * AI Proxy MRS: `https://github.com/in-ci/clash_rules_merged/releases/download/latest/clash_ai_proxy_domain_rules_merged.mrs`
  * Direct MRS: `https://github.com/in-ci/clash_rules_merged/releases/download/latest/clash_direct_domain_rules_merged.mrs`
  * Reject MRS: `https://github.com/in-ci/clash_rules_merged/releases/download/latest/clash_reject_domain_rules_merged.mrs`
* **Release 镜像加速（如 ghfast.top）**：
  * 前缀加 `https://ghfast.top/` 即可，例如：
    `https://ghfast.top/https://github.com/in-ci/clash_rules_merged/releases/download/latest/clash_proxy_domain_rules_merged.mrs`

---

## 自定义规则说明

如需在对应分类中添加自定义规则，直接在 `main` 分支编辑对应文件即可：
- `custom_clash_rules_direct.yaml` - 自定义直连规则
- `custom_clash_rules_porxy.yaml` - 自定义代理规则
- `custom_clash_rules_reject.yaml` - 自定义拦截规则
- `custom_clash_rules_ai_porxy.yaml` - 自定义国外 AI 代理规则
