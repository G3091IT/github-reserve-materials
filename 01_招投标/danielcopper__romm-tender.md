# danielcopper/romm-tender

- **仓库名**：danielcopper/romm-tender
- **原文链接**：https://github.com/danielcopper/romm-tender
- **Star 数**：215（取自 GitHub 搜索 API；本环境数值可能偏高，待核实）
- **最近更新时间**：2026-11-05T00:18:53Z
- **许可证**：GPL-3.0
- **语言**：Python
- **质量分 / 适配分 / 混合分**：85.1 / 12.0 / 52.2
- **结论**：ADOPT
- **标记**：无
- **领域适配**：领域词:tender

## 用途摘要
Tender — your RomM library, running native in Steam. Decky Loader plugin for the Steam Deck: library sync, ROM downloads, BIOS management and save sync.

## 适配理由
⚠ 未命中任何任务关键词，可能不相关

## README 要点
<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/lockup-animated-dark.gif">
  <img src="assets/lockup-animated.gif" alt="Tender" width="300">
</picture>

<h3>Your RomM library, running native in Steam</h3>

[Getting Started](https://danielcopper.github.io/romm-tender/user-guide/getting-started/) ·
[Configuration](https://danielcopper.github.io/romm-tender/user-guide/configuration/) ·
[Syncing](https://danielcopper.github.io/romm-tender/user-guide/syncing-your-library/) ·
[Managing Games](https://danielcopper.github.io/romm-tender/user-guide/managing-games/)

[BIOS &amp; Cores](https://danielcopper.github.io/romm-tender/user-guide/bios-management/) ·
[Save Sync](https://danielcopper.github.io/romm-tender/user-guide/save-sync/) ·
[Troubleshooting](https://danielcopper.github.io/romm-tender/user-guide/troubleshooting/)

<a href="https://danielcopper.github.io/romm-tender/"><img alt="Documentation" src="https://img.shields.io/badge/user%20guide-read-4795c9?style=for-the-badge&labelColor=16202c"></a>
<a href="https://github.com/danielcopper/romm-tender/releases/latest"><img alt="Release" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdanielcopper%2Fromm-tender%2Fmain%2F.release-please-manifest.json&query=%24%5B%27.%27%5D&style=for-the-badge&label=release&color=4795c9&labelColor=16202c"></a>
<a href="https://github.com/danielcopper/romm-tender/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/danielcopper/romm-tender?style=for-the-badge&color=4795c9&labelColor=16202c"></a>
<a href="https://github.com/danielcopper/romm-tender/releases/latest"><img alt="Downloads of the latest release" src="https://img.shields.io/github/downloads/danielcopper/romm-tender/latest/total?style=for-the-badge&label=downloads%20latest&color=4795c9&labelColor=16202c"></a>
<a href="https://github.com/rommapp/romm/releases"><img alt="Requires RomM 5.3.0 or newer" src="https://img.shields.io/badge/RomM-%E2%89%A5%205.3.0-4795c9?style=for-the-badge&labelColor=16202c"></a>

</div>

A [Decky Loader](https://decky.xyz/) plugin that syncs your self-hosted [RomM](https://github.com/rommapp/romm) library
into Steam as non-steam shortcuts. Games appear directly in your Steam library, launch through
[RetroDECK](https://retrodeck.net/), and can keep their saves in sync across devices through your RomM server.

> **Pre-1.0 (v0.x).** The feature set isn't complete yet. Save sync covers standard cartridge saves; the memory-card
> systems — PlayStation, PS2, Dreamcast, GameCube, PSP, 3DS — don't sync their saves yet, and the
> [support matrix](https://danielcopper.github.io/romm-tender/user-guide/save-sync-support-matrix/) has the per-system
> detail.

---

> [!NOTE]
> **How this is built.** The code is written by an AI coding agent working under my direction. The architecture, the
> design decisions and the review are mine, and changes are smoke-tested on real hardware before they ship.

## Features

- **Library sync** — Pulls the platforms and collections you pick from your RomM server into Steam as non-steam
  shortcuts with RomM cover art; later runs are incremental and preview what will change before touching anything
- **SteamGridDB artwork** — Add a free [SteamGridDB](https://www.steamgriddb.com/) key to get hero banners, logos, wide
  capsules and custom icons, and an ARTWORK tab on each game page to choose the game or any image yourself
- **Save sync** — Opt-in save syncing across devices through your RomM server, automatically before launch and after you
  quit; identical saves resolve silently, and if both sides genuinely changed you decide which one wins
  ([not every system syncs yet](https://danielcopper.github.io/romm-tender/user-guide/save-sync-support-matrix/))
- **Save slots & version history** — Multiple named save profiles per game, plus per-file version history with restore
- **ROM downloads** — Download on demand with progress, pause/resume/cancel, and a managed queue
- **BIOS management** — Per-platform BIOS status, download all or only what your active core requires, hash-verified
  against a bundled registry, and delete them again when you're done
- **Game detail page** — Replaces Steam's page for synced games: RomM metadata, RetroAchievements progress, playtime,
  install and BIOS status, save management, and per-game actions
- **Multi-disc & multi-version** — Pick the disc for multi-disc games and switch between regions or revisions of the
  same game, right from its Steam page
- **Emulator cores** — Set the core per system, or override it for a single game
- **Steam Input** — Pick a Steam Input mode (Default / Force On / Force Off) and apply it to every shortcut the plugin
  created
- **Follows RetroDECK moves** — Moved RetroDECK to another drive? The ROMs, BIOS files and saves the plugin manages are
  relocated and your shortcuts repointed — nothing needs re-downloading
- **Cleanup tools** — Remove shortcuts per platform or all at once, uninstall ROMs, and clear orphaned grid images

## Screenshots

|                                                                   Quick Access panel                                                                   |                    Game detail page                    |
| :----------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------: |
|                                                    ![Quick Access panel](assets/screenshot-qam.jpg)                                                    | ![Game detail page](assets/screenshot-game-detail.jpg) |
|                                                                  **Per-game actions**                                                                  |                                                        |
| ![RomM Actions menu with Refresh Artwork, Refresh Metadata, Sync Sav
...（截断，原文见链接）

## 核心代码片段（来源：mise.toml）
```python
[tools]
node = "24"      # major pin — "lts" is a moving alias that silently jumps majors; CI uses node 24
pnpm = "10.29.3" # exact — must match frontend/package.json "packageManager"; bump both together
python = "3.14"  # why 3.14, and every other copy: docs/contributing/dependency-management.md
uv = "0.10.2"    # exact — uv creates the venv AND compiles the dependency locks; pin so the local resolver == the lock author
deno = "2.8"     # minor pin — deno fmt is a formatter; a version jump can reformat Markdown (the CI drift we're killing)

[env]
_.python.venv = { path = ".venv", create = true }

[tasks.setup]
description = "Install JS and Python dependencies"
run = ["pnpm -C frontend install", "uv pip install -r requirements-dev.lock", "git config core.hooksPath .githooks"]

[tasks.lock-update]
description = "Recompile the pinned Python dependency locks from their sources (run after editing a source or bumping a pin)"
# `--output-file=` (not `-o`): Renovate's pip-compile manager parses the uv
# command recorded in each lock header and only recognizes the long `--output-file`
# form with an `=`. `-o` makes it bail with "Option -o not supported (yet)", so it
# can't recompile the lock on a dependency-update PR. `--python-version=` likewise:
# the locks resolve for the oldest Python Tender supports rather than the
# toolchain's, Renovate reads the version it recompiles with from that option, and
# it refuses the option spelled without the `=` (`throwForNoEqualSignInOptionWithArgument`
# in its lib/modules/manager/pip-compile/common.ts).
run = [
    "uv pip compile requirements-dev.txt --python-version=3.12 --output-file=requirements-dev.lock",
    "uv pip compile docs/requirements.txt --python-version=3.12 --output-file=docs/requirements.lock",
]

[tasks.build]
description = "Build frontend (dev: with source maps)"
usage = '''
flag "--surface" help="Build the desktop surface into the panel (build:desktop rather than build:dev). Not remembered: a run without it builds build:dev."
'''
run = '''
if [ "${usage_surface:-}" = true ]; then
  pnpm -C frontend build:desktop
else
  pnpm -C frontend build:dev
fi
'''
depends = ["setup"]

[tasks.test]
description = "Run Python tests"
# Why `-n auto` is here and not in pytest.ini: docs/contributing/development.md, "Testing".
run = "python -m pytest tests/ -q -n auto"

[tasks."test:frontend"]
description = "Run frontend tests"
run = "pnpm -C frontend test"

[tasks."test:frontend:coverage"]
description = "Run frontend tests with coverage report"
run = "pnpm -C frontend test:coverage"

[tasks."lint:md"]
description = "Lint Markdown with markdownlint-cli2 (CI parity)"
# The exclusions are anchored where the trees they name actually sit. A bare
# `node_modules` prunes the top-level one only, so every dependency tree one
# level down was linted — and `.claude/worktrees` holds whole checkouts of this
# repo, each with its own. `.claude` itself may NOT be excluded: `.claude/rules`
# is repo documentation and has to stay in the checked set. Keep this list and
# the markdownlint job in .github/workflows/ci.yml identical.
# Invoked by PATH rather than through `pnpm -C frontend exec`: the globs below are
# anchored at the repository root, and `-C` would move the working directory into
# the package and silently re-scope every one of them. `markdownlint-cli2` is a
# dependency of the frontend package because that is where this repo's only
# node_modules lives — not because linting Markdown belongs to the frontend; most
# of what it reads is under docs/. Why the resolver's recorded machines are left
# out: tests/adapters/atlas_vectors/README.md.
run = "frontend/node_modules/.bin/markdownlint-cli2 \"**/*.md\" \"!**/node_modules\" \"!**/.venv\" \"!.claude/worktrees\" \"!CHANGELOG.md\" \"!site\" \"!tests/adapters/atlas_vectors/vectors\""

[tasks.lint]
description = "Check Cosmic Python architecture rules (layer imports + forbidden service calls) and Markdown"
depends = ["lint:md"]
run = [
    "PYTHONPATH=bac
...（截断，原文见链接）
```
