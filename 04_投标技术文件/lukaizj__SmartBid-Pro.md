---
title: lukaizj/SmartBid-Pro
source: GitHub（lukaizj/SmartBid-Pro）
topic: 04_投标技术文件
date: 2026-07-10
harvest_date: 2026-11-16
url: https://github.com/lukaizj/SmartBid-Pro
tags: [公开学习库, 投标实务, AI投标, GitHub仓库]
---

# lukaizj/SmartBid-Pro

- **仓库名**：lukaizj/SmartBid-Pro
- **原文链接**：https://github.com/lukaizj/SmartBid-Pro
- **Star 数**：3（取自 GitHub 搜索 API，待核实）
- **最近更新时间**：2026-07-10T09:11:07Z
- **许可证**：AGPL-3.0
- **语言**：JavaScript
- **质量分 / 适配分 / 混合分**：55.5 / 55.0 / 55.3
- **结论**：REVIEW
- **标记**：无
- **领域适配**：人工核验相关(强制收录)

## 用途摘要
智标通 SmartBid Pro——智能招投标桌面工作台，集成标书生成、知识库、查重、废标项检查与自研规则检查引擎。

## 适配理由
✓ 命中任务词：ai/投标；△ 未命中：标技/技术/术文/文件/件生/成与/与编/编写/写工

## README 要点
# 智标通 SmartBid Pro

> 智能招投标桌面工作台：标书生成、企业知识库、查重、废标项检查与规则引擎检查。

智标通 SmartBid Pro 是一款本地部署的智能招投标桌面工作台，集成标书编制、企业知识库、标书查重、废标项检查与规则引擎检查。内置规则驱动的检查服务，可对招标文件和投标文件进行完整性、合规性、格式、评分响应与招标条款风险检查。

[English summary](./README.en.md)

## 核心能力

| 模块 | 说明 |
| --- | --- |
| 技术方案生成 | 解析招标文件、组织目录、生成并持续编辑技术方案正文 |
| 企业知识库 | 沉淀企业资料、历史案例和可复用方案素材 |
| 标书查重 | 对元数据、目录、正文和图片进行重复性检查 |
| 废标项检查 | 辅助识别废标风险、错别字和逻辑问题 |
| 规则引擎检查 | 对齐招投标文件，检查完整性、合规性、格式、评分响应和招标条款风险 |
| Word 报告 | 导出规则检查结果，便于复核和归档 |

> 规则检查结果用于辅助复核，不能替代招标文件原文、评标委员会结论或专业法律意见。

## 技术架构

- **桌面端：** Electron 41 + React 19 + TypeScript 5.9 + Vite 7
- **本地能力：** Electron Main / Preload / IPC，负责配置、文件处理、任务和导出
- **规则检查服务：** FastAPI + Python 3.11+，默认监听 `127.0.0.1:8765`
- **本地数据：** 配置、工作区和任务状态保存在 Electron `userData` 目录
- **模型接口：** OpenAI-compatible 文本及图像接口，由用户在本机配置

## 快速开始

### 环境要求

- Node.js 22.12 或更高版本
- npm
- Python 3.11 或更高版本
- [uv](https://docs.astral.sh/uv/)

OpenCode Agent 相关开发能力还需要准备当前平台的 OpenCode binary；未准备时不影响规则检查服务自检，但对应 Agent 页面不可用。

### 一键开发启动

```bash
chmod +x scripts/dev.sh
./scripts/dev.sh
```

脚本会同步规则检查服务依赖、生成本地示例文件、安装客户端依赖，并启动 Electron 开发环境。开发模式下 Electron 会自动拉起规则检查服务。

### 分步启动

```bash
# 1. 安装并验证规则检查服务
cd check-service
uv sync --frozen
uv run python backend/sample/make_sample.py
uv run python backend/selftest.py

# 2. 启动桌面客户端
cd ../client
npm ci
npm run dev
```

启动后进入 **标书检查 → 规则引擎检查**，上传招标文件和投标文件即可执行检查。

## 部署与构建

### 本机部署

```bash
chmod +x scripts/deploy.sh scripts/start-check-service.sh
./scripts/deploy.sh local
```

完成后：

- 规则检查服务：`http://127.0.0.1:8765`
- 桌面客户端开发启动：`cd client && npm run dev`
- 桌面客户端生产构建启动：`cd client && npm start`

### Docker 部署规则检查服务

```bash
./scripts/deploy.sh docker
```

也可以直接运行：

```bash
docker compose up -d --build check-service
```

### 构建客户端

```bash
cd client
npm ci
npm run build
```

### 打包 macOS 客户端

```bash
./scripts/deploy.sh package
```

产物输出到 `client/release/`。安装包已包含规则检查服务源码，但不会捆绑 Python 虚拟环境；运行规则检查仍要求系统已安装 Python 3.11 或更高版本及 [uv](https://docs.astral.sh/uv/)。首次启动时 `uv` 会按锁文件准备依赖，因此需要能够访问依赖源。当前项目未接入代码签名，系统可能提示安装包来自未识别的开发者。

## 项目结构

```text
bid-pro/
├── client/                   # Electron 桌面客户端
│   ├── electron/             # Main、Preload、IPC 与本地服务
│   ├── src/                  # React Renderer 源码
│   └── package.json          # 客户端依赖与打包配置
├── check-service/            # FastAPI 规则检查服务
│   ├── backend/app/          # 解析、规则检查、报告与 API
│   ├── backend/selftest.py   # 端到端自检
│   └── pyproject.toml        # Python 依赖
├── scripts/                  # 开发、部署与服务启动脚本
├── docker-compose.yml        # 规则检查服务容器编排
├── product.config.json       # 产品元数据
├── LICENSE                   # AGPL-3.0
└── NOTICE                    # OpenBidKit 原作者归属声明
```

## 验证

```bash
# OpenAI-only 配置迁移与远程统计开关冒烟测试
cd client
node scripts/smoke-openai-config.cjs
node scripts/smoke-remote-analytics-disabled.cjs
node scripts/smoke-check-service-manager.cjs

# Electron Main / Preload 语法检查
node --check electron/main.cjs
node --check electron/preload.cjs
node --check electron/product.cjs
node --check electron/services/checkServiceManager.cjs

# Renderer / TypeScript 构建
npm run build

# 规则引擎端到端自检
cd ../check-service
uv sync --frozen
uv run python backend/sample/make_sample.py
uv run python backend/selftest.py
```

## 数据与隐私

- 业务文件、配置与任务状态默认保存在本机工作区。
- 本项目不会在仓库中提供 API Key；模型凭证由用户在本机设置。
- 当前 SmartBid Pro 配置关闭上游远程埋点、远程公告、自动更新和许可证检查。
- 是否向模型服务商发送文档内容取决于用户配置和主动使用的 AI 功能，请遵守所选服务商的隐私政策及组织内部规定。

## 许可证

整个仓库依据 [GNU Affero General Public License v3.0](./LICENSE) 发布。使用、修改、分发或通过网络提供修改版本时，请遵守 AGPL-3.0 的源代码公开义务，并保留 [NOTICE](./NOTICE) 中要求的归属信息。

## 贡献

欢迎通过 GitHub Issues 报告可复现问题或提出改进建议。提交代码前请阅读 [CONTRIBUTING.md](./CONTRIBUTING.md) 和 [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)。安全问题请参阅 [SECURITY.md](./SECURITY.md)。


## 核心代码片段（来源：README.md）
```javascript
# 智标通 SmartBid Pro

> 智能招投标桌面工作台：标书生成、企业知识库、查重、废标项检查与规则引擎检查。

智标通 SmartBid Pro 是一款本地部署的智能招投标桌面工作台，集成标书编制、企业知识库、标书查重、废标项检查与规则引擎检查。内置规则驱动的检查服务，可对招标文件和投标文件进行完整性、合规性、格式、评分响应与招标条款风险检查。

[English summary](./README.en.md)

## 核心能力

| 模块 | 说明 |
| --- | --- |
| 技术方案生成 | 解析招标文件、组织目录、生成并持续编辑技术方案正文 |
| 企业知识库 | 沉淀企业资料、历史案例和可复用方案素材 |
| 标书查重 | 对元数据、目录、正文和图片进行重复性检查 |
| 废标项检查 | 辅助识别废标风险、错别字和逻辑问题 |
| 规则引擎检查 | 对齐招投标文件，检查完整性、合规性、格式、评分响应和招标条款风险 |
| Word 报告 | 导出规则检查结果，便于复核和归档 |

> 规则检查结果用于辅助复核，不能替代招标文件原文、评标委员会结论或专业法律意见。

## 技术架构

- **桌面端：** Electron 41 + React 19 + TypeScript 5.9 + Vite 7
- **本地能力：** Electron Main / Preload / IPC，负责配置、文件处理、任务和导出
- **规则检查服务：** FastAPI + Python 3.11+，默认监听 `127.0.0.1:8765`
- **本地数据：** 配置、工作区和任务状态保存在 Electron `userData` 目录
- **模型接口：** OpenAI-compatible 文本及图像接口，由用户在本机配置

## 快速开始

### 环境要求

- Node.js 22.12 或更高版本
- npm
- Python 3.11 或更高版本
- [uv](https://docs.astral.sh/uv/)

OpenCode Agent 相关开发能力还需要准备当前平台的 OpenCode binary；未准备时不影响规则检查服务自检，但对应 Agent 页面不可用。

### 一键开发启动

```bash
chmod +x scripts/dev.sh
./scripts/dev.sh
```

脚本会同步规则检查服务依赖、生成本地示例文件、安装客户端依赖，并启动 Electron 开发环境。开发模式下 Electron 会自动拉起规则检查服务。

### 分步启动

```bash
# 1. 安装并验证规则检查服务
cd check-service
uv sync --frozen
uv run python backend/sample/make_sample.py
uv run python backend/selftest.py

# 2. 启动桌面客户端
cd ../client
npm ci
npm run dev
```

启动后进入 **标书检查 → 规则引擎检查**，上传招标文件和投标文件即可执行检查。

## 部署与构建

### 本机部署

```bash
chmod +x scripts/deploy.sh scripts/start-check-service.sh
./scripts/deploy.sh local
```

完成后：

- 规则检查服务：`http://127.0.0.1:8765`
- 桌面客户端开发启动：`cd client && npm run dev`
- 桌面客户端生产构建启动：`cd client && npm start`

### Docker 部署规则检查服务

```bash
./scripts/deploy.sh docker
```

也可以直接运行：

```bash
docker compose up -d --build check-service
```

### 构建客户端

```bash
cd client
npm ci
npm run build
```

### 打包 macOS 客户端

```bash
./scripts/deploy.sh package
```

产物输出到 `client/release/`。安装包已包含规则检查服务源码，但不会捆绑 Python 虚拟环境；运行规则检查仍要求系统已安装 Python 3.11 或更高版本及 [uv](https://docs.astral.sh/uv/)。首次启动时 `uv` 会按锁文件准备依赖，因此需要能够访问依赖源。当前项目未接入代码签名，系统可能提示安装包来自未识别的开发者。

## 项目结构

```text
bid-pro/
├── client/                   # Electron 桌面客户端
│   ├── electron/             # Main、Preload、IPC 与本地服务
│   ├── src/                  # React Renderer 源码
│   └── package.json          # 客户端依赖与打包配置
├── check-service/            # FastAPI 规则检查服务
│   ├── backend/app/          # 解析、规则检查、报告与 API
│   ├── backend/selftest.py   # 端到端自检
│   └── pyproject.toml        # Python 依赖
├── scripts/                  # 开发、部署与服务启动脚本
├── docker-compose.yml        # 规则检查服务容器编排
├── product.config.json       # 产品元数据
├── LICENSE                   # AGPL-3.0
└── NOTICE                    # OpenBidKit 原作者归属声明
```

## 验证

```bash
# OpenAI-only 配置迁移与远程统计开关冒烟测试
cd client
node scripts/smoke-openai-config.cjs
node scripts/smoke-remote-analytics-disabled.cjs
node scripts/smoke-check-service-manager.cjs

# Electron Main / Preload 语法检查
node --check electron/main.cjs
node --check electron/preload.cjs
node --check electron/product.cjs
node --check electron/services/checkServiceManager.cjs

# Renderer / TypeScript 构建
npm run build

# 规则引擎端到端自检
cd ../check-service
uv sync --frozen
uv run python backend/sample/make_sample.py
uv run python backend/selftest.py
```

## 数据与隐私

- 业务文件、配置与任务状态默认保存在本机工作区。
- 本项目不会在仓库中提供 API Key；模型凭证由用户在本机设置。
- 当前 SmartBid Pro 配置关闭上游远程埋点、远程公告、自动更新和许可证检查。
- 是否向模型服务商发送文档内容取决于用户配置和主动使用的 AI 功能，请遵守所选服务商的隐私政策及组织内部规定。

## 许可证

整个仓库依据 [GNU Affero General Public License v3.0](./LICENSE) 发布。使用、修改、分发或通过网络提供修改版本时，请遵守 AGPL-3.0 的源代码公开义务，并保留 [NOTICE](./NOTICE) 中要求的归属信息。

## 贡献

欢迎通过 GitHub Issues 报告可复现问题或提出改进建议。提交代码前请阅读 [CONTRIBUTING.md](./CONTRIBUTING.md) 和 [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)。安全问题请参阅 [SECURITY.md](./SECURITY.md)。

```
