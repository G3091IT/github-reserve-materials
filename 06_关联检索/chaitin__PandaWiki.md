# chaitin/PandaWiki

- **仓库名**：chaitin/PandaWiki
- **原文链接**：https://github.com/chaitin/PandaWiki
- **Star 数**：10460（取自 GitHub 搜索 API；本环境数值可能偏高，待核实）
- **最近更新时间**：2026-11-05T06:40:33Z
- **许可证**：AGPL-3.0
- **语言**：TypeScript
- **质量分 / 适配分 / 混合分**：99.9 / 52.9 / 78.8
- **结论**：ADOPT
- **标记**：无
- **领域适配**：领域词:知识库/问答

## 用途摘要
PandaWiki 是一款 AI 大模型驱动的开源知识库搭建系统，帮助你快速构建智能化的 产品文档、技术文档、FAQ、博客系统，借助大模型的力量为你提供 AI 创作、AI 问答、AI 搜索等能力。

## 适配理由
✓ 命中任务词：文档/知识/识库；△ 未命中：招投/投标/标文/档分/分析/评标/库检/检索/与投/标资/资料/料仓/仓库/库关/关联/联泛/泛化/化检

## README 要点
<p align="center">
  <a target="_blank" href="https://ragcloud.app.baizhi.cloud/?utm_source=github&utm_medium=readme&utm_campaign=saas">
    <img src="/images/saas-cta.svg" width="800" alt="PandaWiki SaaS 版 - 无需部署，立即在线体验" />
  </a>
</p>

<p align="center">
  <img src="/images/banner.png" width="400" />
</p>

<p align="center">
  <a target="_blank" href="https://ly.safepoint.cloud/Br48PoX">📖 官方网站</a> &nbsp; | &nbsp;
  <a target="_blank" href="/images/wechat.png">🙋‍♂️ 微信交流群</a>
</p>

## 👋 项目介绍

PandaWiki 是一款 AI 大模型驱动的**开源知识库搭建系统**，帮助你快速构建智能化的 **产品文档、技术文档、FAQ、博客系统**，借助大模型的力量为你提供 **AI 创作、AI 问答、AI 搜索** 等能力。

<p align="center">
  <img src="/images/setup.png" width="800" />
</p>

## ⚡️ 界面展示

| PandaWiki 控制台                                 | Wiki 网站前台                                    |
| ------------------------------------------------ | ------------------------------------------------ |
| <img src="/images/screenshot-1.png" width=370 /> | <img src="/images/screenshot-2.png" width=370 /> |
| <img src="/images/screenshot-3.png" width=370 /> | <img src="/images/screenshot-4.png" width=370 /> |

## 🔥 功能与特色

- AI 驱动智能化：AI 辅助创作、AI 辅助问答、AI 辅助搜索。
- 强大的富文本编辑能力：兼容 Markdown 和 HTML，支持导出为 word、pdf、markdown 等多种格式。
- 轻松与第三方应用进行集成：支持做成网页挂件挂在其他网站上，支持做成钉钉、飞书、企业微信等聊天机器人。
- 通过第三方来源导入内容：根据网页 URL 导入、通过网站 Sitemap 导入、通过 RSS 订阅、通过离线文件导入等。

## 🚀 上手指南

### 安装 PandaWiki

你需要一台支持 Docker 20.x 以上版本的 Linux 系统来安装 PandaWiki。

使用 root 权限登录你的服务器，然后执行以下命令。

```bash
bash -c "$(curl -fsSLk https://release.baizhi.cloud/panda-wiki/manager.sh)"
```

根据命令提示的选项进行安装，命令执行过程将会持续几分钟，请耐心等待，更多细节参考 [安装 PandaWiki](https://pandawiki.docs.baizhi.cloud/node/01971602-bb4e-7c90-99df-6d3c38cfd6d5)。

> PandaWiki 目前已提供 SaaS 版本，无需部署 开箱即用  👉 [百智云 AI 知识库](https://ragcloud.app.baizhi.cloud/)


### 登录 PandaWiki

在上一步中，安装命令执行结束后，你的终端会输出以下内容。

```
SUCCESS  控制台信息:
SUCCESS    访问地址(内网): http://*.*.*.*:2443
SUCCESS    访问地址(外网): http://*.*.*.*:2443
SUCCESS    用户名: admin
SUCCESS    密码: **********************
```

使用浏览器打开上述内容中的 “访问地址”，你将看到 PandaWiki 的控制台登录入口，使用上述内容中的 “用户名” 和 “密码” 登录即可。

### 配置 AI 模型

> PandaWiki 是由 AI 大模型驱动的 Wiki 系统，在未配置大模型的情况下 AI 创作、AI 问答、AI 搜索 等功能无法正常使用。
> 
首次登录时会提示需要先配置 AI 模型，可自行选择一键配置或手动配置。

<div align="center">
  <img src="/images/model-config-1.png" width="800" />
  <p><em>一键自动配置 AI 模型</em></p>

  <img src="/images/model-config-2.png" width="800" />
  <p><em>手动自定义配置 AI 模型</em></p>
</div>



> 推荐使用 [百智云模型广场](https://baizhi.cloud/) 快速接入 AI 模型，注册即可获赠 5 元的模型使用额度。
> 关于大模型的更多配置细节请参考 [接入 AI 模型](https://pandawiki.docs.baizhi.cloud/node/01971616-811c-70e1-82d9-706a202b8498)。

### 创建知识库

“知识库” 是一组文档的集合，PandaWiki 将会根据知识库中的文档，为不同的知识库分别创建 “Wiki 网站”。
<img src="/images/createkb.png" width="800" />

### 💪 开始使用

如果你顺利完成了以上步骤，那么恭喜你，属于你的 PandaWiki 搭建成功，你可以：

- 访问 **控制台** 来管理你的知识库并上传文档等待学习成功
- 访问 **Wiki 网站** 使用知识库并测试AI问答效果
<img src="/images/AI-QA.png" width="700" />

### 💬 遇到问题

如在使用产品过程中遇到问题，可通过以下方式获取帮助：
- 📘查阅官方文档：[常见问题](https://pandawiki.docs.baizhi.cloud/node/019b4952-4ed3-7514-ba57-c93a8ca13608)，更多内容请参考文档目录。
- 🤖不想翻文档？试试 [AI 问答](https://pandawiki.docs.baizhi.cloud/node/0197160c-782c-74ad-a4b7-857dae148f84)，快速获取答案。
- 🤝加入社区：扫码加入下方企业微信群，与更多用户及官方人员交流经验、获得帮助。


## 社区交流

欢迎加入我们的微信群进行交流。

<img src="/images/wechat.png" width="300" />

## 🙋‍♂️ 贡献

欢迎提交 [Pull Request](https://github.com/chaitin/PandaWiki/pulls) 或创建 [Issue](https://github.com/chaitin/PandaWiki/issues) 来帮助改进项目。

## 📝 许可证

本项目采用 GNU Affero General Public License v3.0 (AGPL-3.0) 许可证。这意味着：

- 你可以自由使用、修改和分发本软件
- 你必须以相同的许可证开源你的修改
- 如果你通过网络提供服务，也必须开源你的代码
- 商业使用需要遵守相同的开源要求


## Star History

[![Star History Chart](https://star-history.dera.page/svg?repos=chaitin/PandaWiki&type=Date)](https://star-history.dera.page/#chaitin/PandaWiki&Date)


## 核心代码片段（来源：AGENTS.md）
```typescript
# AGENTS.md

This file is for coding agents working in `PandaWiki`.
Prefer small, targeted changes that match the repository's existing patterns.
Communicate with the user in Chinese unless they explicitly ask otherwise.

## Source Of Truth

- There is no existing `AGENTS.md` in this repository.
- No Cursor rules were found in `.cursor/rules/` or `.cursorrules`.
- No Copilot instructions were found in `.github/copilot-instructions.md`.
- Root `CLAUDE.md` exists and should be treated as repository guidance.
- Key note from `CLAUDE.md`: respect backend layer boundaries and use Chinese for communication.

## Repository Layout

- `backend/`: Go backend services, APIs, workers, migrations, docs.
- `web/`: pnpm workspace for frontend apps.
- `web/admin/`: React + Vite admin console.
- `web/app/`: Next.js user-facing web app.
- `sdk/`: SDK-related code.

## Architecture Expectations

- Backend follows a layered structure.
- Put business logic in `backend/usecase/`.
- Keep HTTP-specific logic in `backend/handler/`.
- Keep persistence and external data access in `backend/repo/`.
- Put shared request/response and domain models in `backend/domain/` and `backend/api/`.
- Do not move business rules into handlers just to finish a feature quickly.

## Tooling Versions And Basics

- Go version: `1.24.3` from `backend/go.mod`.
- Frontend package manager: `pnpm` only.
- Admin app build tool: Vite.
- User app build tool: Next.js.
- Backend formatting/linting is driven by `gofmt`, `goimports`, and `golangci-lint`.
- Frontend formatting is primarily Prettier.

## Install Commands

Run these from the repository root unless noted otherwise.

### Backend

- Install Go dependencies: `cd backend && go mod tidy`
- Build all backend packages: `cd backend && go build ./...`

### Frontend

- Install web dependencies: `cd web && pnpm install`
- Start both frontend apps: `cd web && pnpm dev`

## Build Commands

### Backend

- Build all packages: `cd backend && go build ./...`
- Build one package: `cd backend && go build ./usecase`
- Generate swagger/wire code: `cd backend && make generate`
- Generate pro swagger/wire code: `cd backend && make generate_pro`

### Frontend

- Build all web apps: `cd web && pnpm build`
- Build admin only: `cd web/admin && pnpm build`
- Build app only: `cd web/app && pnpm build`
- Analyze admin build: `cd web/admin && pnpm build:analyze`

## Test Commands

### Backend

- Run all tests: `cd backend && go test ./...`
- Run one package: `cd backend && go test ./usecase`
- Run one test by name in one package: `cd backend && go test ./usecase -run TestName`
- Run one test with verbose output: `cd backend && go test ./usecase -run TestName -v`
- Run one package with race detector when needed: `cd backend && go test -race ./usecase`

### Frontend

- `web/admin` currently has no dedicated test script in `package.json`.
- `web/app` currently has no dedicated test script in `package.json`.
- For frontend verification, use lint, typecheck, and build as the practical test substitute.
- Admin typecheck via build pipeline: `cd web/admin && pnpm build`
- App lint: `cd web/app && pnpm lint`

## Lint And Format Commands

### Backend

- Lint backend: `cd backend && golangci-lint run`
- Full backend lint target: `cd backend && make lint`
- Format one file/package: `cd backend && gofmt -w path/to/file.go && goimports -w path/to/file.go`
- `cd backend && make lint` is required before commit for any backend code change.

Notes:

- `make lint` also runs generation steps and `go mod tidy`; it is heavier than `golangci-lint run`.
- `make lint` already covers backend formatting via configured formatters, so agents should treat it as the required backend verification step before commit.
- `backend/.golangci.toml` enables standard linters and formatters.

### Frontend

- Root formatting: `cd web && pnpm exec prettier --write .`
- Admin lint one file or folder: `cd web/admin && pnpm exec eslint src/path/to/file.tsx`
- App format: `cd web/app && pnpm format`

...（截断，原文见链接）
```
