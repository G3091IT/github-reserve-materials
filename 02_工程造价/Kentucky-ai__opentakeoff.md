# Kentucky-ai/opentakeoff

- **仓库名**：Kentucky-ai/opentakeoff
- **原文链接**：https://github.com/Kentucky-ai/opentakeoff
- **Star 数**：786（取自 GitHub 搜索 API；本环境数值可能偏高，待核实）
- **最近更新时间**：2026-11-07T07:22:31Z
- **许可证**：AGPL-3.0
- **语言**：TypeScript
- **质量分 / 适配分 / 混合分**：91.7 / 12.0 / 55.8
- **结论**：ADOPT
- **标记**：无
- **领域适配**：领域词:takeoff

## 用途摘要
Open-source (AGPL-3.0) PDF takeoff for construction & flooring — the first engine an AI agent drives natively over MCP, not bolted on. Rooms measured on the wall faces, symbol sweeps, materials + quantities with full provenance, built for preconstruction. Runs entirely in your browser.

## 适配理由
⚠ 未命中任何任务关键词，可能不相关

## README 要点
<div align="center">

<a href="https://opentakeoff.kentucky-ai.com"><img src="docs/img/brand/hero.svg" alt="OpenTakeoff: the scan star beside the wordmark, and an agent tracing two rooms of a floor plan on their wall faces" width="100%"></a>

**Measure construction plans in your browser, or hand the same engine to your AI agent.**<br/>
Free, open source and local. Nothing uploads, and nobody has to sign up.

[![GitHub stars](https://img.shields.io/github/stars/Kentucky-ai/opentakeoff?style=flat&logo=github&label=stars&color=62d4dc)](https://github.com/Kentucky-ai/opentakeoff/stargazers)
[![npm](https://img.shields.io/npm/v/opentakeoff-mcp?label=opentakeoff-mcp&color=62d4dc)](https://www.npmjs.com/package/opentakeoff-mcp)
[![npm downloads](https://img.shields.io/npm/dm/opentakeoff-mcp?label=downloads&color=62d4dc)](https://www.npmjs.com/package/opentakeoff-mcp)
[![MCP registry](https://img.shields.io/badge/MCP_registry-io.github.Kentucky--ai%2Fopentakeoff-0e1a2e)](https://registry.modelcontextprotocol.io)
[![CI](https://github.com/Kentucky-ai/opentakeoff/actions/workflows/ci.yml/badge.svg)](https://github.com/Kentucky-ai/opentakeoff/actions/workflows/ci.yml)
[![License: AGPL-3.0](https://img.shields.io/badge/license-AGPL--3.0-0e1a2e.svg)](LICENSE)
[![Sponsor](https://img.shields.io/badge/sponsor-%E2%99%A5-EA4AAA?logo=githubsponsors&logoColor=white)](https://github.com/sponsors/Kentucky-ai)

### [▶ Try it now](https://opentakeoff.kentucky-ai.com) &nbsp;·&nbsp; [🔌 Plug in your agent](#plug-it-into-your-agent) &nbsp;·&nbsp; [🛠 Send your first PR](#contribute)

[日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-Hans.md)

</div>

---

A **takeoff** is the measuring that every construction bid starts with: how much floor, how
much wall, how many fixtures, at what scale and on which sheet. OpenTakeoff is an open-source
engine for that job. It has two front ends:

- **🧑‍🔧 A browser canvas for people.** Drag in a plan set, set the scale, trace rooms, and
  export a report and a marked-up planset.
- **🤖 An MCP server for agents.** It offers <!--tool-count-->62<!--/tool-count--> tools over
  stdio. An agent drives the same engine with the same math and the same scale gate as the
  canvas, and its work stays a dashed proposal until a person accepts it.

Both front ends share one takeoff format, so you can open an agent's takeoff in the canvas,
check it and fix it. Every shape records the scale it was measured at, the method that drew
it, and whether a person or an agent drew it.

> [!NOTE]
> **One-Click Area is temporarily gated** while the flood engine is re-validated on a wider
> plan corpus. Trace rooms with **Area** (`A`) in the canvas and `measure_polygon` over MCP.
> Every other tool works as normal. See [`docs/design/ONE_CLICK_GATE.md`](docs/design/ONE_CLICK_GATE.md).

## Pick your door

| | You are… | Start here | Time |
|---|---|---|---|
| 🧑‍🔧 | **An estimator with a bid due** | [Open the canvas](https://opentakeoff.kentucky-ai.com), click **Guided first takeoff**, then read the [user manual](docs/USER_GUIDE.md) | 5 min |
| 🤖 | **An AI agent, or the person wiring one up** | Run `npx -y opentakeoff-mcp` (see [Plug it into your agent](#plug-it-into-your-agent)), then read the [agent manual](docs/AGENT_GUIDE.md) | 1 min |
| 🛠 | **A developer** | Read [AGENTS.md](AGENTS.md) for the repo map, [FEATURES.md](FEATURES.md) for where each feature lives in the code, then [Contribute](#contribute) | 10 min |
| 🏗 | **A crew that wants its own copy** | [Fork it](#fork-it). Any static host will run it, and nothing phones home | 5 min |

## Plug it into your agent

The server needs Node 20 or newer. You don't need to clone or build anything. Pick your client:

| Client | Install |
|---|---|
| **Claude Code** | `claude mcp add opentakeoff -- npx -y opentakeoff-mcp` |
| **Codex CLI** | `codex mcp add opentakeoff -- npx -y opentakeoff-mcp` |
| **Cursor** | [![Install in Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en/install-mcp?name=opentakeoff&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsIm9wZW50YWtlb2ZmLW1jcCJdfQ%3D%3D) |
| **VS Code** | [![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_server-0098FF?logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=opentakeoff&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22opentakeoff-mcp%22%5D%7D) |
| **Claude Desktop** | Double-click [`opentakeoff-mcp.mcpb`](https://github.com/Kentucky-ai/opentakeoff/releases/latest/download/opentakeoff-mcp.mcpb) |
| **Docker** (from a clone) | `docker build -f mcp/Dockerfile -t opentakeoff-mcp . && docker run --rm -i opentakeoff-mcp` |
| **Any other stdio client** | Use the JSON below |

```json
{
  "mcpServers": {
    "opentakeoff": { "command": "npx", "args": ["-y", "opentakeoff-mcp"] }
  }
}
```

**If you've cloned the repo**, the root [`.mcp.json`](.mcp.json), [`.cursor/mcp.json`](.cursor/mcp.json)
and [`.vscode/mcp.json`](.vscode/mcp.json) register the server when you open the folder, so
there's nothing else to set up.

**Your first prompt.** Paste this once the server is connected:

> Load `demo/sample-finish-plan.pdf` from the OpenTakeoff repo, read the scale note on the floor
> plan, set the scale, trace room 134 on its wall faces under its finish tag from the
> schedule, check your ring with `view_sheet`, and export the marked-up PDF.

The step-by-step walkthrough for each client is in [Connect OpenTakeoff to your AI](docs/CONNECT.md).
The server can also describe itself: read the `takeoff://wiki` resource before you load a plan.

<details>
<summary><strong>All <!--tool-count-->62<!--/tool-count--> tools, grouped by stage</strong></summary>

<br/>

| Stage | Tools |
|---|---|
| **Open and orient** | `load_plan` · `sheet_info` · `sheet_context` · `get_sheet_vectors` · `read_sheet_text` · `find_text` · `view_sheet` |
| **Scale** | `set_scale` |
| **Measure** | `measure_polygon` · `cut_out` · `measure_lin
...（截断，原文见链接）

## 核心代码片段（来源：README.md）
```typescript
<div align="center">

<a href="https://opentakeoff.kentucky-ai.com"><img src="docs/img/brand/hero.svg" alt="OpenTakeoff: the scan star beside the wordmark, and an agent tracing two rooms of a floor plan on their wall faces" width="100%"></a>

**Measure construction plans in your browser, or hand the same engine to your AI agent.**<br/>
Free, open source and local. Nothing uploads, and nobody has to sign up.

[![GitHub stars](https://img.shields.io/github/stars/Kentucky-ai/opentakeoff?style=flat&logo=github&label=stars&color=62d4dc)](https://github.com/Kentucky-ai/opentakeoff/stargazers)
[![npm](https://img.shields.io/npm/v/opentakeoff-mcp?label=opentakeoff-mcp&color=62d4dc)](https://www.npmjs.com/package/opentakeoff-mcp)
[![npm downloads](https://img.shields.io/npm/dm/opentakeoff-mcp?label=downloads&color=62d4dc)](https://www.npmjs.com/package/opentakeoff-mcp)
[![MCP registry](https://img.shields.io/badge/MCP_registry-io.github.Kentucky--ai%2Fopentakeoff-0e1a2e)](https://registry.modelcontextprotocol.io)
[![CI](https://github.com/Kentucky-ai/opentakeoff/actions/workflows/ci.yml/badge.svg)](https://github.com/Kentucky-ai/opentakeoff/actions/workflows/ci.yml)
[![License: AGPL-3.0](https://img.shields.io/badge/license-AGPL--3.0-0e1a2e.svg)](LICENSE)
[![Sponsor](https://img.shields.io/badge/sponsor-%E2%99%A5-EA4AAA?logo=githubsponsors&logoColor=white)](https://github.com/sponsors/Kentucky-ai)

### [▶ Try it now](https://opentakeoff.kentucky-ai.com) &nbsp;·&nbsp; [🔌 Plug in your agent](#plug-it-into-your-agent) &nbsp;·&nbsp; [🛠 Send your first PR](#contribute)

[日本語](README.ja.md) · [한국어](README.ko.md) · [简体中文](README.zh-Hans.md)

</div>

---

A **takeoff** is the measuring that every construction bid starts with: how much floor, how
much wall, how many fixtures, at what scale and on which sheet. OpenTakeoff is an open-source
engine for that job. It has two front ends:

- **🧑‍🔧 A browser canvas for people.** Drag in a plan set, set the scale, trace rooms, and
  export a report and a marked-up planset.
- **🤖 An MCP server for agents.** It offers <!--tool-count-->62<!--/tool-count--> tools over
  stdio. An agent drives the same engine with the same math and the same scale gate as the
  canvas, and its work stays a dashed proposal until a person accepts it.

Both front ends share one takeoff format, so you can open an agent's takeoff in the canvas,
check it and fix it. Every shape records the scale it was measured at, the method that drew
it, and whether a person or an agent drew it.

> [!NOTE]
> **One-Click Area is temporarily gated** while the flood engine is re-validated on a wider
> plan corpus. Trace rooms with **Area** (`A`) in the canvas and `measure_polygon` over MCP.
> Every other tool works as normal. See [`docs/design/ONE_CLICK_GATE.md`](docs/design/ONE_CLICK_GATE.md).

## Pick your door

| | You are… | Start here | Time |
|---|---|---|---|
| 🧑‍🔧 | **An estimator with a bid due** | [Open the canvas](https://opentakeoff.kentucky-ai.com), click **Guided first takeoff**, then read the [user manual](docs/USER_GUIDE.md) | 5 min |
| 🤖 | **An AI agent, or the person wiring one up** | Run `npx -y opentakeoff-mcp` (see [Plug it into your agent](#plug-it-into-your-agent)), then read the [agent manual](docs/AGENT_GUIDE.md) | 1 min |
| 🛠 | **A developer** | Read [AGENTS.md](AGENTS.md) for the repo map, [FEATURES.md](FEATURES.md) for where each feature lives in the code, then [Contribute](#contribute) | 10 min |
| 🏗 | **A crew that wants its own copy** | [Fork it](#fork-it). Any static host will run it, and nothing phones home | 5 min |

## Plug it into your agent

The server needs Node 20 or newer. You don't need to clone or build anything. Pick your client:

| Client | Install |
|---|---|
| **Claude Code** | `claude mcp add opentakeoff -- npx -y opentakeoff-mcp` |
| **Codex CLI** | `codex mcp add opentakeoff -- npx -y opentakeoff-mcp` |
| **Cursor** | [![Install in Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cur
...（截断，原文见链接）
```
