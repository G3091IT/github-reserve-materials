# -*- coding: utf-8 -*-
"""AI 投标技术文件 · GitHub 自动采集归档器（v1.0）。

目标：自动收集与"AI 投标技术文件"相关的 GitHub 公开仓库，经领域闸门+质量打分
过滤后，归档摘要到 04_投标技术文件/，并更新 README 总索引。

设计（与 scout_runner.py 同源机制，职责单一、互不影响）：
- 引擎：复用 github_scout（纯标准库、零新依赖），token 走本机凭据文件（5000/时）。
- 关键词：本脚本专用，经 2026-11-16 系统检索验证有效（中英文双线 + topic 维度）。
- 闸门：领域必含词 + 负向过滤词（与 scout_runner 同源），杜绝无关/敏感仓库混入。
- 结论：仅收录 verdict 为 ADOPT / REVIEW 的候选；AVOID（弃坑/无许可证/超2年）不入库。
- 归档：owner__repo.md（带 frontmatter），格式与既有归档一致。
- 幂等：文件已存在即跳过；跨关键词去重。
- 限流：核心 API 硬预算 + 搜索间隔 + 403 即停顺延。
- 边界：空结果/接口报错/字段缺失/仓库不存在均安全跳过并记日志，不中断整体。

用法：
    python ai_bid_tech_runner.py            # 跑全部关键词
    python ai_bid_tech_runner.py "技术标 编写"   # 只跑指定关键词
"""
import sys, os, re, json, base64, time, datetime, urllib.parse as up

SCOUT = "C:/Users/远见1号/.workbuddy/plugins/marketplaces/experts/plugins/github-tool-scout-expert-plus/skills/github-tools-scout/scripts/github_scout.py"
sys.path.insert(0, os.path.dirname(SCOUT))
import github_scout as gs

RESERVE = "E:/图谱工作包/GitHub储备资料仓库"
OUT_DIR = os.path.join(RESERVE, "04_投标技术文件")
DATE = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).strftime("%Y-%m-%d")
TOKEN = gs._get_token()

CALLS = {"n": 0, "search": 0}
RATE_HIT = {"v": False}
CORE_BUDGET = 100        # 认证核心 5000/时，预留余量
SEARCH_SLEEP = 8         # 搜索 30/分，留足余量

# 专用关键词集（2026-11-16 系统检索验证有效）
KEYWORDS = [
    "标书 生成",
    "投标技术文件",
    "施工组织设计 AI",
    "技术标 编写",
    "bid document AI generator",
    "tender technical proposal",
    "construction bidding AI",
    "topic:bid-document",
    "rag 招投标",
    "标书 查重 废标",
]

# 领域必含词（命中其一即通过领域闸门）
DOMAIN_TERMS = [
    "投标", "标书", "技术标", "招标", "评标", "暗标", "标讯", "施工组织设计",
    "bid", "tender", "bidding", "proposal",
]

# 负向过滤词（命中即弃，与 scout_runner 同源）
NEG_TERMS = [
    "tendermint", "cosmos", "blockchain", "区块链",
    "六四", "法轮功", "新疆改造", "dictatorship", "propaganda", "反中共", "包子露宪",
    "修宪", "heil xi", "文革", "民运", "疆独", "藏独", "台独", "terrorist", "isis",
    "毛泽东", "邓小平", "王沪宁", "习近平",
]

TASK = "AI投标技术文件生成与编写工具"
MIN_STARS = 5
TOP = 10

# 强制收录清单：本会话人工核验过、与 AI 投标技术文件直接相关的仓库。
# 即使关键词检索未命中，也按全名直接拉取归档（仅在 verdict=AVOID 时跳过）。
FORCE = [
    "tiettuo/claude-bid-gen",
    "zeronezer/bidcraft",
    "hello-fengsir/godbiao",
    "Get00/BiaoShu-SKILL",
    "liwg1995/YuduBid",
    "hanbon-labs/wenbiao",
    "fb-labs/ZhiBiao",
    "longsky21/dsh-bidding",
    "lukaizj/SmartBid-Pro",
]


def fn_replace(name):
    return name.replace("/", "__") + ".md"


def api_get(url, is_search=False):
    if RATE_HIT["v"]:
        return None, "rate_limit_guard"
    CALLS["n"] += 1
    if is_search:
        CALLS["search"] += 1
    data, err = gs._http_json(url, TOKEN)
    if err and "403" in str(err):
        RATE_HIT["v"] = True
    return data, err


def search_repos(query, top):
    q = query.strip()
    if MIN_STARS:
        q += " stars:>=%d" % MIN_STARS
    params = up.urlencode({"q": q, "sort": "stars", "order": "desc", "per_page": 30})
    url = gs._API_BASE + "/search/repositories?" + params
    last_err = None
    for attempt in range(4):
        data, err = api_get(url, is_search=True)
        if not err:
            items = (data or {}).get("items", [])
            out = [(it, gs.score_repo(it, task=TASK)) for it in items]
            out.sort(key=lambda x: x[1]["blended"], reverse=True)
            return out[:top], None
        last_err = err
        if "403" in str(err):
            time.sleep(60)
        elif "net_err" in str(err):
            time.sleep(5 * (attempt + 1))
        else:
            break
    return None, last_err


def domain_pass(item, sc):
    name = (sc["full_name"] or "").lower()
    desc = (item.get("description") or "").lower()
    topics = " ".join(str(t).lower() for t in (item.get("topics") or []))
    hay = " ".join([name, desc, topics])
    for nt in NEG_TERMS:
        if nt.lower() in hay:
            return False, "负向词命中:%s" % nt
    hit = [t for t in DOMAIN_TERMS if t.lower() in hay]
    if not hit:
        return False, "未命中领域词"
    return True, "领域词:%s" % "/".join(hit)


def get_readme(full):
    data, err = api_get(gs._API_BASE + "/repos/%s/readme" % full)
    if err or not data:
        return ""
    try:
        return base64.b64decode(data.get("content", "")).decode("utf-8", "replace")
    except Exception:
        return ""


def pick_core_file(full):
    url = gs._API_BASE + "/repos/%s/contents/" % full
    data, err = api_get(url)
    if err or not isinstance(data, list):
        return None, ""
    repo_base = full.split("/")[-1].lower()
    prefs = ["main", "app", "cli", "run", "__init__", "index", "core", "engine", repo_base, "setup"]
    cands = [d for d in data if d.get("type") == "file" and d.get("size", 0) < 25000]
    cands.sort(key=lambda d: (min([d["name"].lower().find(p) for p in prefs if p in d["name"].lower()] + [999]), -d["size"]))
    for c in cands[:3]:
        u2 = gs._API_BASE + "/repos/%s/contents/%s" % (full, up.quote(c["path"]))
        d2, e2 = api_get(u2)
        if e2 or not d2:
            continue
        try:
            code = base64.b64decode(d2.get("content", "")).decode("utf-8", "replace")
        except Exception:
            code = ""
        if code.strip():
            return c["path"], code
    return None, ""


def clip(txt, n=6000):
    if not txt:
        return ""
    return txt if len(txt) <= n else txt[:n] + "\n...（截断，原文见链接）"


os.makedirs(OUT_DIR, exist_ok=True)

# 已收录集合（幂等 + 跨关键词去重）
archived_global = set()
if os.path.isdir(OUT_DIR):
    for _fn in os.listdir(OUT_DIR):
        if _fn.endswith(".md") and "__" in _fn:
            archived_global.add(_fn[:-3].replace("__", "/"))

log_lines = []
archived = []

ONLY = [a for a in sys.argv[1:] if not a.startswith("-")] if len(sys.argv) > 1 else []

# ── 常规关键词检索 ──
merged = {}
for q in KEYWORDS:
    if ONLY and q not in ONLY:
        log_lines.append("[关键词] %s | 本次跳过（命令行指定）" % q)
        continue
    if RATE_HIT["v"]:
        break
    rows, err = search_repos(q, TOP)
    if err:
        log_lines.append("  ✗ 关键词失败 [%s]: %s" % (q, err))
        if RATE_HIT["v"]:
            break
        continue
    for it, sc in (rows or []):
        fn = sc["full_name"]
        if not fn:
            continue
        if fn not in merged or sc["blended"] > merged[fn][1]["blended"]:
            merged[fn] = (it, sc)
    time.sleep(SEARCH_SLEEP)

# ── 强制收录（人工核验过的仓库，按全名直接拉取）──
force_cands = []
for full in FORCE:
    if RATE_HIT["v"]:
        break
    if full in archived_global:
        log_lines.append("  ⊘ 强制项已收录，跳过 %s" % full)
        continue
    data, err = api_get(gs._API_BASE + "/repos/%s" % full)
    if err or not data or not isinstance(data, dict):
        log_lines.append("  · 强制项拉取失败 %s: %s" % (full, err or "空响应"))
        continue
    sc2 = gs.score_repo(data, task=TASK)
    if sc2["verdict"] == "AVOID":
        log_lines.append("  · 强制项 verdict=AVOID 跳过 %s (flags=%s)" % (full, ",".join(sc2["flags"])))
        continue
    force_cands.append((data, sc2, "人工核验相关(强制收录)", True))
    log_lines.append("  ✚ 强制项已拉取 %s (%s, %s★)" % (full, sc2["verdict"], sc2["stars"]))

# 合并常规候选（过闸门 + 非 AVOID）
cands = []
for fn, (it, sc) in merged.items():
    if sc["verdict"] == "AVOID":
        log_lines.append("  · AVOID 跳过 %s (flags=%s)" % (fn, ",".join(sc["flags"])))
        continue
    ok, why = domain_pass(it, sc)
    if ok:
        cands.append((it, sc, why, False))
    else:
        log_lines.append("  · 领域闸门排除 %s (%s)" % (fn, why))
cands = force_cands + cands

# 排序：强制项优先，其余按混合分
cands.sort(key=lambda x: (0 if x[3] else 1, -x[1]["blended"]))

for it, sc, why, forced in cands:
    fpath = os.path.join(OUT_DIR, fn_replace(sc["full_name"]))
    if os.path.exists(fpath):
        log_lines.append("  ⊘ 已收录，跳过 %s" % sc["full_name"])
        continue
    if sc["full_name"] in archived_global:
        log_lines.append("  ⊘ 已在其他位置收录，去重跳过 %s" % sc["full_name"])
        continue
    if CALLS["n"] >= CORE_BUDGET:
        log_lines.append("  ⚠ 已达核心 API 预算(%d)，剩余顺延" % CORE_BUDGET)
        break
    full = sc["full_name"]
    readme = clip(get_readme(full))
    cpath, code = pick_core_file(full)
    code_clip = clip(code, 4000)
    md = []
    md.append("---")
    md.append("title: %s" % full)
    md.append("source: GitHub（%s）" % full)
    md.append("topic: 04_投标技术文件")
    md.append("date: %s" % ((it.get("pushed_at") or it.get("updated_at") or "").replace("T", " ").replace("Z", "")[:10] or ""))
    md.append("harvest_date: %s" % DATE)
    md.append("url: %s" % it.get("html_url", ""))
    md.append("tags: [公开学习库, 投标实务, AI投标, GitHub仓库]")
    md.append("---")
    md.append("")
    md.append("# %s" % full)
    md.append("")
    md.append("- **仓库名**：%s" % full)
    md.append("- **原文链接**：%s" % it.get("html_url", ""))
    md.append("- **Star 数**：%s（取自 GitHub 搜索 API，待核实）" % sc["stars"])
    md.append("- **最近更新时间**：%s" % (it.get("pushed_at") or it.get("updated_at") or ""))
    md.append("- **许可证**：%s" % sc["license"])
    md.append("- **语言**：%s" % sc["language"])
    md.append("- **质量分 / 适配分 / 混合分**：%s / %s / %s" % (sc["score"], sc["adapt"], sc["blended"]))
    md.append("- **结论**：%s" % sc["verdict"])
    md.append("- **标记**：%s" % (", ".join(sc["flags"]) if sc["flags"] else "无"))
    md.append("- **领域适配**：%s" % why)
    md.append("")
    md.append("## 用途摘要")
    md.append((it.get("description") or "（无描述）").strip())
    md.append("")
    md.append("## 适配理由")
    md.append("；".join(sc.get("adapt_notes", [])) or "（见打分）")
    md.append("")
    md.append("## README 要点")
    md.append(readme if readme else "（README 抓取失败或为空）")
    md.append("")
    if cpath:
        md.append("## 核心代码片段（来源：%s）" % cpath)
        md.append("```%s" % (sc["language"].lower() if sc["language"] != "—" else ""))
        md.append(code_clip)
        md.append("```")
    else:
        md.append("## 核心代码片段")
        md.append("（未在根目录取到合适源码片段）")
    md.append("")
    with open(fpath, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    archived_global.add(sc["full_name"])
    archived.append((sc["full_name"], sc["verdict"]))
    log_lines.append("  ✓ 收录 %s (%s, %s★) -> %s" % (full, sc["verdict"], sc["stars"], os.path.basename(fpath)))
    if RATE_HIT["v"]:
        break

if RATE_HIT["v"]:
    log_lines.append("⚠ 触发 403 限流，本次运行终止，剩余顺延。")

# ── 更新 README 总索引（合并式：仅更新 04_投标技术文件 计数与清单，保留其他主题）──
def update_readme():
    rd = os.path.join(RESERVE, "README.md")
    if not os.path.exists(rd):
        return
    with open(rd, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    # 统计 04_投标技术文件 现有条目
    dir_files = [f for f in os.listdir(OUT_DIR) if f.endswith(".md") and "__" in f] if os.path.isdir(OUT_DIR) else []
    new_count = len(dir_files)
    # 更新计数行
    for i, ln in enumerate(lines):
        if ln.startswith("- 04_投标技术文件："):
            lines[i] = "- 04_投标技术文件：%d 个" % new_count
            break
    # 更新/追加清单条目（按文件名去重）
    existing_entries = set()
    for ln in lines:
        m = re.search(r"— 04_投标技术文件/(\S+?)\.md", ln)
        if m:
            existing_entries.add(m.group(1))
    new_lines = []
    added_any = False
    for fn in sorted(dir_files):
        stem = fn[:-3]
        if stem in existing_entries:
            continue
        # 从归档文件读结论
        verdict = "REVIEW"
        try:
            with open(os.path.join(OUT_DIR, fn), "r", encoding="utf-8") as f2:
                head = f2.read(2000)
            m = re.search(r"结论\*\*：\s*(\w+)", head)
            if m:
                verdict = m.group(1)
        except Exception:
            pass
        full = stem.replace("__", "/")
        new_lines.append("- [%s] **%s** — 04_投标技术文件/%s.md" % (verdict, full, stem))
        added_any = True
    # 在 04_投标技术文件 相关行之后插入新条目（保持清单分区顺序：插到 05_工程资料管理 行之前）
    insert_at = None
    for i, ln in enumerate(lines):
        if ln.startswith("- [ADOPT] **3xxx/engineercms**") or ln.startswith("- [REVIEW] **3xxx"):
            insert_at = i
            break
    if insert_at is None:
        # 找不到则追加到清单末尾（排除说明之前）
        for i, ln in enumerate(lines):
            if ln.startswith("## 本次运行新增"):
                insert_at = i
                break
    if added_any and insert_at is not None:
        lines[insert_at:insert_at] = new_lines
    # 更新采集方式说明，标注本脚本
    for i, ln in enumerate(lines):
        if ln.startswith("- **采集方式**："):
            lines[i] = "- **采集方式**：只读抓取公开仓库（github_scout 实时搜索+打分 + 领域关键词闸门过滤；AI投标技术文件由 ai_bid_tech_runner.py 专项采集），全程未上传/未修改用户其他资料"
            break
    if added_any:
        for i, ln in enumerate(lines):
            if ln.startswith("## 本次运行新增"):
                lines[i + 1] = "- AI投标技术文件专项：本次新增 %d 个（%s）" % (
                    len(archived), "、".join(f[0] for f in archived) if archived else "无")
                break
    with open(rd, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    if added_any:
        log_lines.append("✓ README 总索引已更新（04_投标技术文件 +%d 条）" % len(new_lines))

update_readme()

# ── 采集日志（追加式）──
log_full = os.path.join(RESERVE, "采集日志_%s_aibid.log" % DATE)
prev_log = ""
if os.path.exists(log_full):
    try:
        with open(log_full, "r", encoding="utf-8") as f:
            prev_log = f.read()
    except Exception:
        prev_log = ""
if archived or not prev_log:
    with open(log_full, "w", encoding="utf-8") as f:
        f.write(prev_log + ("\n\n" if prev_log else "") + "# AI投标技术文件采集补充运行 %s %s\n\n" % (
            DATE, datetime.datetime.now().strftime("%H:%M")))
        f.write("\n".join(log_lines))
        f.write("\n\n核心 API 调用：%d | 搜索调用：%d | 限流：%s\n" % (
            CALLS["n"], CALLS["search"], "是" if RATE_HIT["v"] else "否"))
else:
    print("SKIP-LOG: 本次无新增且已有日志，不覆盖。")

print("DONE archived=%d core=%d search=%d rate_hit=%s" % (
    len(archived), CALLS["n"], CALLS["search"], RATE_HIT["v"]))
print("LOG:\n" + "\n".join(log_lines))
