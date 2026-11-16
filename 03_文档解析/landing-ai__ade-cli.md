# landing-ai/ade-cli

- **仓库名**：landing-ai/ade-cli
- **原文链接**：https://github.com/landing-ai/ade-cli
- **Star 数**：2424（取自 GitHub 搜索 API；本环境数值可能偏高，待核实）
- **最近更新时间**：2026-10-30T20:47:49Z
- **许可证**：Apache-2.0
- **语言**：Python
- **质量分 / 适配分 / 混合分**：95.4 / 50.0 / 75.0
- **结论**：ADOPT
- **标记**：无
- **领域适配**：领域词:pdf/extract

## 用途摘要
The official CLI for Agentic Document Extraction (ADE) by LandingAI — parse documents and extract schema-shaped data from your terminal

## 适配理由
✓ 命中任务词：pdf；△ 未命中：word/excel/比对/对与/与文/文档/档转/转换/换的/的库

## README 要点
# ade-cli

[![Release](https://img.shields.io/github/v/release/landing-ai/ade-cli)](https://github.com/landing-ai/ade-cli/releases)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

**Agentic Document Extraction (ADE), from your terminal.** Run `ade parse` to
turn documents with tables, figures, and charts into grounded Markdown and
elements, and `ade extract` to pull schema-shaped fields with page-and-box
evidence. Both save to a local store at `~/.ade`, so re-running an identical
command consumes no credits.

**[CLI documentation](https://docs.landing.ai/cli/quickstart)** ·
**[Playground](https://ade.landing.ai)** ·
**[Get an API key](https://ade.landing.ai/settings/api-key)**

## Install

Each release ships self-contained binaries for macOS, Linux, and Windows
(arm64 and x86_64). No Python or `uv` needed.

**macOS / Linux**

```sh
curl -fsSL https://raw.githubusercontent.com/landing-ai/ade-cli/main/scripts/install.sh | sh
```

**Windows (PowerShell)**

```powershell
irm https://raw.githubusercontent.com/landing-ai/ade-cli/main/scripts/install.ps1 | iex
```

**Windows (CMD)**

```bat
curl -fsSL https://raw.githubusercontent.com/landing-ai/ade-cli/main/scripts/install.cmd -o install.cmd && install.cmd && del install.cmd
```

To develop or install from source, see [CONTRIBUTING.md](CONTRIBUTING.md).

## First run

Log in once per machine, parse a document, then extract the fields you want
from it. The parse summary prints the job item ID that `extract` takes.

```sh
ade login
ade parse -d invoice.pdf
ade extract JOB_ITEM_ID --schema schema.json
```

The [CLI Quickstart](https://docs.landing.ai/cli/quickstart) walks through the
same three steps with a sample document and a sample schema, and ends in the
viewer that shows where each extracted value came from.

## Commands

Every command takes `--json` for one stable JSON object on stdout. Run
`ade help COMMAND` for its flags and result shape, or see the
[CLI Reference](https://docs.landing.ai/cli/reference).

| command | what it does |
|---|---|
| `ade parse` | Parse a document into Markdown, elements, and grounding |
| `ade extract` | Pull schema-shaped fields from a parse, with per-field evidence |
| `ade find` | Search a parse's elements locally, with no API call |
| `ade crop` | Save an element's region of the page as a PNG |
| `ade view` | Build and open a self-contained HTML viewer for a job item |
| `ade history list` | List stored job items, newest first |
| `ade history clear` | Delete stored job items |
| `ade login` / `ade auth login` | Log in with your browser or an API key |
| `ade auth status` | Show how you are authenticated and where |
| `ade auth org list` / `switch` / `clear` | Choose which organization your runs act in |
| `ade logout` / `ade auth logout` | Log out of one environment, or all of them |
| `ade version` | Print the version and install mode |
| `ade update` | Self-update to the latest release |
| `ade help` | Print the whole command surface, including `--json` result shapes |

The documentation covers what these tables cannot: how job items work and why
re-runs are free ([CLI Concepts](https://docs.landing.ai/cli/concepts)),
[parsing](https://docs.landing.ai/cli/parse) and
[extraction](https://docs.landing.ai/cli/extract) in depth,
[searching and cropping evidence](https://docs.landing.ai/cli/find-crop-view),
[authentication and organizations](https://docs.landing.ai/cli/authentication),
and [scripting the CLI](https://docs.landing.ai/cli/scripting-automation).

## For agents

Agents are first-class callers. Running `ade help --json` returns the entire
shipped surface in one call: every command, flag, result shape, topic, exit
state, and the store layout. Every command then takes `--json` and emits one
stable object whose shape is published per verb, and the full result is always
on stdout rather than only in a store file.
[`SKILL.md`](SKILL.md) ships the agent contract: the loop, the conventions, and
the sharp edges.

A process that is already running keeps the environment it started with, so
`ade` may not be on the PATH inside CI, cron, or an agent harness. Call the
absolute path instead: `~/.ade/bin/ade` on macOS and Linux, or
`%USERPROFILE%\.ade\bin\ade.exe` on Windows. For credentials, set
`ADE_API_KEY`.

## Managing your install

|  | macOS and Linux | Windows |
|---|---|---|
| App | `~/.ade/bin/ade` | `%USERPROFILE%\.ade\bin\ade.exe` |
| Store | `~/.ade` | `%USERPROFILE%\.ade` |
| Reaches your PATH via | a symlink in `~/.local/bin` | a user PATH entry |

Set `ADE_HOME` to move the app and the store, `ADE_CLI_VERSION` to pin a
version, and `ADE_CLI_INSTALL_DIR` to change the destination.

Run `ade update` to self-update, with `--yes` to skip the confirmation. For a
`uv` or `pipx` install it points at `uv tool upgrade ade-cli` instead. The CLI
mentions new releases on stderr once a day. Set `ADE_NO_UPDATE_CHECK=1` to turn
that off.

To uninstall, remove the app directory, and on macOS and Linux the
`~/.local/bin/ade` symlink too. Never delete all of `.ade`: the rest of that
directory holds results that already consumed credits.

## Project history

This repository was **`agentic-doc`**, the original Agentic Document Extraction
SDK. That SDK is preserved unchanged, and no longer developed, on the
[`legacy`](https://github.com/landing-ai/ade-cli/tree/legacy) branch. Since
2026-07-31 this repository ships the ADE CLI.

## License

[Apache-2.0](LICENSE).


## 核心代码片段（来源：LICENSE）
```python
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this 
...（截断，原文见链接）
```
