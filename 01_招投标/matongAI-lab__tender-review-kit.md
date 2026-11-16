# matongAI-lab/tender-review-kit

- **仓库名**：matongAI-lab/tender-review-kit
- **原文链接**：https://github.com/matongAI-lab/tender-review-kit
- **Star 数**：52
- **最近更新时间**：2026-09-30T05:15:12Z
- **许可证**：MIT
- **语言**：Python
- **质量分 / 适配分 / 混合分**：78.4 / 47.9 / 64.7
- **结论**：ADOPT
- **标记**：无
- **命中子查询**：见适配理由

## 用途摘要
投标审核工具包，用关键词、规则和自动化检查辅助识别投标风险。

## 适配理由
✓ 命中任务词：投标；△ 未命中：招投/电子/子投/标相/相关/关的/的开/开源/源库/库与/与工/关注/注投/标助/助手/暗标/标书/书生

## README 要点
# tender-review-skill · 招标文件审标 skill(为投标人服务)

> **这不是一个独立软件,是给 AI agent 用的 skill(技能包)**:程序管确定性(取数/扫描/护栏/出 Excel),AI 管判断(读懂条款、分清真假废标项)——**必须配一个 AI agent 一起用**(任何能操作本地文件的 AI 编程助手均可)。怎么装、怎么触发见下面[「怎么开始」](#怎么开始按你的情况选一条路)。
>
> **审的是招标方发的招标文件,服务的是要去投标的人。**
>
> 输入:招标文件(PDF/Word) → 输出:**投标核对清单**(废标项 + 评分项 + 证明材料 + ▲ 标识参数 + 时间节点 + **合同条款要点**),每条带行号出处。
> 帮投标人在**动手写投标文件之前**,把招标方的游戏规则全部吃透——不踩废标、不漏评分、不缺材料、不错节点。
>
> **产清单和事实,不下"投/不投"结论。** 决策是投标人自己的事,工具的本分是让他看见全部要求。
>
> ⭐ **招标要求 vs 合同要求严格分开**:废标清单 = 投标递交时雷区(漏一条 = 今天废标);合同条款·要点 = 中标后约束(漏看不会今天死,但中标后受罚)。两类独立清单,投标人按需查看(很多人不看合同,我们尊重这个选择)。

> ⚠️ **当前状态:开发中(WIP)**
>
> 接口与判词库仍在迭代,这是早期快照——生产使用请自行评估、先跑通自家标书。
>
> 本项目按 **MIT 许可开源**(见文末 License),可自由使用 / 修改 / 商用。欢迎试用、提 PR、扩词库。

## 怎么开始(按你的情况选一条路)

### 🤖 路 1:你已经在用 AI 助手 ⭐ 最省心

**第一次用·尝鲜(零安装)**:不用看任何文档,把下面这段话原样发给你的 AI(点代码块右上角即可复制):

```text
请帮我下载并运行这个审标工具:
https://github.com/matongAI-lab/tender-review-kit
仓库里有一份 FOR_AI.md,是写给你的操作手册——先读它,然后带着我把流程跑完。
我可能不懂技术:每一步用大白话告诉我你在干什么;要安装任何东西,先问我。
我的招标文件稍后发给你。
```

剩下的全是 AI 的事:下载项目、装环境、要你的标书、审完、把 Excel 交到你手上。你只需要回答它的提问。

**用顺了·装成常驻 skill(以后一句话触发)**:

把仓库 clone 到你 AI 工具的 skills 目录(各家工具的 skills 目录位置不一样,查你工具的文档),目录名统一用 `tender-review-kit`:

```bash
git clone https://github.com/matongAI-lab/tender-review-kit.git <你的 AI 工具 skills 目录>/tender-review-kit
```

不确定你的工具 skills 目录在哪、或工具不支持本地 skill?继续用上面的 `FOR_AI.md` 咒语入口即可,效果一样。

- **怎么触发**:装好后,在支持 skill 的客户端里直接说人话——「帮我审这份招标文件」「看看这份标书的废标点」,它会按 [SKILL.md](SKILL.md) 开头的 description 识别该用这个 skill;想点名也行:「用 tender-review-skill 审这份标书」。
- **首次使用**:AI 会先跑环境自检(`scripts/check_env.py`),缺什么会问你「装/不装」,不用自己研究。
- **怎么更新**(顺便拉到别人贡献的判词,见[互惠机制](#怎么贡献互惠机制)):
  ```bash
  cd <你的 tender-review-kit skill 目录> && git pull
  ```
- 只想在某个项目里用?按你的客户端规则装到项目级 skills 目录;如果不确定,就使用 `FOR_AI.md` 咒语入口。

### 🐣 路 2:完全不懂技术,也没用过 AI 助手

这个工具的"判断"环节需要一个 **能操作你电脑文件的 AI 编程助手**——市面上有很多家(桌面版 / 编辑器版 / 命令行版都行),挑一个装上即可(只装这一次)。
⚠️ 注意要装**能读写本地文件的版本**,**纯网页聊天版不行**(网页版碰不到你电脑上的标书文件)。

装好后回到上面 **路 1**,把那段话发给它。

> 不想用 AI 助手、想自己手动装环境跑程序?看 [INSTALL.md](INSTALL.md)——全程只回答「装」或「不装」。

### 👨‍💻 路 3:工程师,自己跑

直接看下面的 [5 分钟上手](#5-分钟上手);架构看 [ARCHITECTURE.md](ARCHITECTURE.md)。

## 版本路线

**当前版本:Community Edition v0.1.10(社区开源版)**——本仓库内容,**MIT 许可,免费使用 / 修改 / 商用**。
- 8 个核心程序(取数 / 撒网 / 补词×2 / 查漏 / 完整性 / 跨文件 / Excel)+ 3 个辅助(环境自检 / 候选词入库 / 脱敏贡献)+ 一键编排 `run_pipeline.py`
- **回扫检查衔接修复(v0.1.10 新增)**：verify 使用本次 AI 回扫与原始命中的合并结果完成两项护栏检查；候选仍需原文判断。详见 [变更说明](CHANGELOG.md) 和 [issue 分类记录](references/keyword-triage-v0.1.10.md)。
- **贡献隐私声明强化(v0.1.9 新增)**:明确告诉用户贡献完全自愿,不上传标书/Excel/原文/项目名,只提交判词短语和分类/scope,并默认通过 Issue 由维护者审核。
- **开源判词库扩展(v0.1.8 新增)**:并入 5 个用户确认过、已脱敏的通用判词,提升无效响应/中标资格/联合体/分包转包/实质响应类命中。
- **AI 发现词当前补漏回扫(v0.1.7 新增)**:AI 发现疑似判词后,先用临时词库回扫当前标书,不等用户入库;用户接受/拒绝只决定未来是否自动扫到。
- **词库贡献提醒强化(v0.1.7 新增)**:verify 收尾固定说明本地词库/开源词库互惠机制,让 agent 稳定提醒用户可脱敏贡献新词。
- **▲/★ 长表格行拆分增强(v0.1.6 新增)**:Word 表格摊平成一行时,同一行多个 `▲/★/※` 会逐条进入 `hits.json`;同时收窄目录页排除规则,避免正文参数里的"目录"字样误伤。
- **小白零门槛入口(v0.1.5 新增)**:一段咒语发给任意 AI 助手即可全程代办(操作手册 [FOR_AI.md](FOR_AI.md));「怎么开始」三路分流 + 装成常驻 skill 的安装/触发说明
- **判词库分两层**:开源词库(共享,~170+ 词)+ 用户本地词库(私有积累,gitignored)
- **AI 发现新词的用户审批流**:不再自动入库,用户拍板决定是否接受
- **互惠贡献闭环**:你贡献几个,以后别人贡献的你也能拉到
- 4 类常见标书的类型特化规则(工程·合理低价 / 货物·综合评分 / 政采服务 / 央企货物,并入审标对照清单)
- 完整的两层防线 + 红蓝对抗方法论
- **够用,但你要的"省心 / 不漏 / 跨行业"得靠社区一起攒(欢迎贡献)**

**规划中:Professional Edition(专业版,正在开发)**——商业产品,不在本仓库:
- **更全的判词库**:几百至上千词,带行业细分 scope(医疗 / 军工 / 海外 / 科研…)和实战准确率证明
- **更全的类型规范**:几十类标书的完整机制档案(单一来源 / 询价 / 竞争性磋商 / 海外英标 / 政府购买服务 / 工程总承包 / 框架协议 等)
- **云端补词服务**:扫一份标书 → AI 自动提候选词 + 验证 + 入库,贡献给同订阅级别的所有用户(集体智能)
- **类型自动识别 + 定制化指南 API**
- **准确率验证服务**:你的清单 vs 专家答案库 → 给质量评分

**Enterprise / 定制版**:私有部署、行业专版、团队协作、一对一类型校准。

> Community Edition 是地基,够任何人验证方法论、试用流程、跑通自家标书。
> 想要"省心 + 不漏 + 跨行业",请关注 Professional Edition。

## 这个项目的价值在哪

市面上现在有两种东西:
- **老牌投标软件**:靠关键词匹配。死板,不会读——"无效投标"和"无效数据"分不清,误报一大堆。
- **新的 AI 标书工具**:让大模型读。会读,但**漏了你不知道、这次和下次不一样、攒不下东西**。

**tender-review-skill 把两者长处缝起来,而且把"准确/不漏"摆在第一**:
> **判词库**(确定的底盘,保证该找的不漏) × **大模型读懂**(分清"无效投标"vs"无效数据") × **程序护栏**(防压缩 + 反向校验) × **A/B 红蓝对抗**(防判断死角)

**核心优势**:
1. **判词库是核心资产** —— 几百次实战攒的判决词,代码能开源,**判词库越用越厚是真护城河**。
2. **可复现的扫描** —— 同样一份标书,跑十次结果一样。判词扫描是确定性的;准确率量化需专家真值集(路线图中)。
3. **两层防漏机制** —— 反向校验防"漏抄",红蓝对抗防"判断死角"。
4. **跨工具** —— 线性主干在任何 AI agent 上都能跑;支持子代理(subagent)的工具还能额外开并行 + 红蓝对抗增强。

## 5 分钟上手

> 详细版见 [QUICKSTART.md](QUICKSTART.md)。下面是最短路径(给想自己敲命令的人)。
> **不想敲命令?**回到上面的[「怎么开始」](#怎么开始按你的情况选一条路)路 1,把那段话发给你的 AI 就行。手动装环境见 [INSTALL.md](INSTALL.md)。

```bash
# 0. 环境自检 ⭐ 首次必跑(自动告诉你缺什么 + 怎么装)
python scripts/check_env.py
# → 全 ✓ 就直接跳到 1;有 ✗ 会显示对应平台的安装命令,装好再跑一次确认

# 1. 装依赖(若 check_env 提示缺,跑这一行即可)
pip install -r requirements.txt
# (PDF 提取建议装 pdftotext: Windows xpdf-tools / mac brew install poppler / ubuntu apt install poppler-utils。不装也能跑,自动回退 pypdf)

# 2. 程序自动跑(取数 + 撒网 + 补词,几秒)
python run_pipeline.py prep <招标文件.docx 或 .pdf>

# 3. 把 prep 结尾打印的那段提示发给你的 AI agent
#    → agent 按 SKILL.md 步骤产出 workspace/<项目>.工作区.md
#    → 含 AI 新发现的疑似判词(标 [AI发现])

# 4. 程序自动跑(护栏 + 出 Excel,几秒)
python run_pipeline.py verify workspace/<项目>.工作区.md

# 5. 如果 AI 发现了新判词,先看待审清单再拍板
python scripts/harvest_ai_words.py workspace/<项目>.工作区.md --accept "词A,词B"
#    (选着收 --accept "词A,词B" / 全收 --accept-all / 全弃 --reject-all)
#    (接受的进 data/local_keywords.json 用户本地积累,下次扫别的标书自动用上)

# 6. (可选) 把普遍适用的新词加进开源词库,以后别人贡献的你也能拉到
python scripts/export_contribution.py --github
```

**自带 sample 试跑**(不需要真标书):
```bash
python run_pipeline.py prep tests/fixtures/sample_tender.docx
```

## 项目结构

```
tender-review-kit/
├── FOR_AI.md             # 给 AI agent 的操作手册(小白只发一段话,AI 全程代跑)
├── QUICKSTART.md         # 30 秒上手指南
├── SKILL.md              # skill 定义(AI 的触发条件 + 端到端工作流)
├── ARCHITECTURE.md       # 设计纲领(六层栈 + Python/LLM 分工 + 数据驱动)
├── run_pipeline.py       # 一键编排: prep(取数+扫描) / verify(护栏+Excel)
├── scripts/              # 程序层(确定性 + 护栏,纯标准库+少量 pip)
│   ├── check_env.py           # 环境自检: 缺什么依赖 + 怎么装(首次必跑)
│   ├── extract_text.py        # 取数: PDF/Word → 带行号文本
│   ├── scan_keywords.py       # 判词撒网: 自动合并加载开源 + 本地词库
│   ├── scan_candidates.py     # 补词引擎(程序通道): 正则扫疑似新判决词
│   ├── harvest_ai_words.py    # 补词引擎(AI通道): AI 发现的词 → 待审 → 用户拍板 → 入本地
...（截断，原文见链接）

## 核心代码片段（来源：run_pipeline.py）
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""run_pipeline.py — 一键串联程序步骤，让 AI agent 只需专注判断

两个阶段：
  prep   — 取数 + 撒网 + 补词（全自动，几秒跑完）
  verify — 护栏检查 + 出 Excel（agent 写完工作区 md 后跑）

用法：
  python run_pipeline.py prep   <招标文件.docx/.pdf> [--outdir workspace]
  python run_pipeline.py verify <工作区.md> [--out 输出.xlsx]

示例（用自带测试样本跑通全流程）：
  python run_pipeline.py prep   tests/fixtures/sample_tender.docx
  python run_pipeline.py verify workspace/sample_tender.工作区.md
"""
import sys
import subprocess
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

SCRIPTS = Path(__file__).resolve().parent / "scripts"


def run(cmd, label):
    print("\n" + "=" * 60)
    print("▶ %s" % label)
    print("  %s" % " ".join(str(c) for c in cmd))
    print("-" * 60)
    r = subprocess.run([sys.executable] + [str(c) for c in cmd])
    if r.returncode != 0:
        print("✗ %s 失败 (exit %d)" % (label, r.returncode))
        return False
    return True


def prep(tender_file, outdir):
    tender = Path(tender_file)
    if not tender.exists():
        print("✗ 文件不存在: %s" % tender)
        sys.exit(1)

    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    stem = tender.stem

    ok = run([SCRIPTS / "extract_text.py", str(tender), "--outdir", str(outdir)],
             "Step 0 · 取数：%s → 带行号文本" % tender.name)
    if not ok:
        sys.exit(1)

    lines_file = outdir / (stem + ".lines.txt")
    if not lines_file.exists():
        print("✗ 取数后未找到 %s" % lines_file)
        sys.exit(1)

    ok = run([SCRIPTS / "scan_keywords.py", str(lines_file)],
             "Step 3a · 撒网：扫判决词 → hits.json")
    if not ok:
        sys.exit(1)

    hits_file = outdir / (stem + ".hits.json")

    hits_arg = ["--hits", str(hits_file)] if hits_file.exists() else []
    run([SCRIPTS / "scan_candidates.py", str(lines_file)] + hits_arg,
        "Step 3b · 补词：扫候选新词 → candidates.json")

    print("\n" + "=" * 60)
    print("✓ prep 完成！产出文件在 %s/" % outdir)
    print()
    print("接下来：")
    print("  1. 把下面这段话发给你的 AI agent：")
    print()
    print('  ─── 复制开始 ───')
    print('  请按 SKILL.md 的步骤 1-2-4-5 审核这份招标文件。')
    print('  - 带行号文本：%s' % lines_file)
    if hits_file.exists():
        print('  - 撒网命中：%s' % hits_file)
    print('  - 参考文档在 references/ 目录')
    print('  - 输出写到：%s' % (outdir / (stem + ".工作区.md")))
    print('  ─── 复制结束 ───')
    print()
    print("  2. agent 写完工作区 md 后，跑：")
    print("     python run_pipeline.py verify %s" % (outdir / (stem + ".工作区.md")))


def verify(worklist_file, out_xlsx):
    worklist = Path(worklist_file)
    if not worklist.exists():
        print("✗ 工作区文件不存在: %s" % worklist)
        print("  请先让 AI agent 按 SKILL.md 步骤 1-2-4-5 写完工作区 md")
        sys.exit(1)

    ws_dir = worklist.parent
    stem = worklist.stem.replace(".工作区", "")
    hits_file = ws_dir / (stem + ".hits.json")

    lines_file = ws_dir / (stem + ".lines.txt")
    rescan_file = ws_dir / (stem + ".ai_rescan.hits.json")
    # Never select an artifact from a previous verify invocation.
    rescan_file.unlink(missing_ok=True)
    harvest_args = [SCRIPTS / "harvest_ai_words.py", str(worklist), "--hits", str(hits_file)]
    if lines_file.exists():
        harvest_args += ["--lines", str(lines_file)]
    ok = run(harvest_args,
             "Step 5+ · 收割 + 补扫：AI 发现的疑似判词 → 候选库 + 回扫当前标书")
    if not ok:
        print("✗ verify 中止：新词收割/补扫失败，未生成 Excel。")
        sys.exit(1)

    if rescan_file.exists():
        hits_file = rescan_file

    if hits_file.exists():
        ok = run([SCRIPTS / "check_coverage.py", str(hits_file), str(worklist)],
                 "Step 6a · 查漏：撒网命中 vs 废标清单覆盖反查")
        if not ok:
            print("✗ verify 中止：查漏护栏失败，未生成 Excel。")
            sys.exit(1)

        ok = run([SCRIPTS / "check_completeness.py", str(worklist), "--hits", str(hits_file)],
                 "Step 6b · 完整性：条数 / 梯度 / ▲ 覆盖校验")
        if
...（截断，原文见链接）
```
