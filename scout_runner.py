# -*- coding: utf-8 -*-
"""夜间 GitHub 公开仓库只读采集编排器（v3.3，相关性闸门+强制收录版）。

v3.3 变更（2026-11-11，无人值守默认决策，见 automation memory）：
- 02_工程造价 / 05_工程资料管理 两个长期空额大的 niche 主题：下调 star 门槛至 20、补齐英文同义词
  （takeoff/estimate/estimator/costing/bim、engineer/cms/archive/project management 等），以收录词汇不同但
  实为相关的仓库（如 opentakeoff、OpenConstructionEstimate、engineercms）。
- 新增「强制收录」机制 FORCE：对历史上经人工审计确认相关、却被领域闸门/检索漏掉的 niche 仓库，按全名直接
  拉取（/repos/{full}），仅在 verdict=AVOID 时跳过；优先级高于普通搜索候选，专门补足 02/05 空额。
- 仍全程只读、幂等跳过、跨主题去重、尊重限流（核心 API 预算 50、搜索 10s 间隔、403 即停顺延）。

相较初版改进：
1) 每个主题拆成多个简洁子查询（GitHub 搜索对多词为 AND，长混合查询易返回 0 结果）。
2) 引入「领域关键词闸门」+「负向(无关/敏感)过滤」：仅当仓库名/描述/主题命中本主题领域词、
   且不命中政治等无关词时，才视为候选；从根本上杜绝 china-dictatorship 之类高分无关仓库混入。
3) 闸门判定只用搜索返回的元数据（零额外 API 成本），只在通过闸门后才抓取 README+核心源码。
4) 幂等：主题目录已存在同名文件则跳过，避免重复抓取与浪费限流额度。
5) 全程只读，绝不写入/上传 GitHub；仅写本地储备仓库。尊重限流：核心 API 设硬预算（匿名 60/h），
   搜索调用间留 7s；遇 403 立即停并登记，留待次日继续。
"""
import sys, os, re, base64, time, datetime, urllib.parse as up

SCOUT = "C:/Users/远见1号/.workbuddy/plugins/marketplaces/experts/plugins/github-tool-scout-expert-plus/skills/github-tools-scout/scripts/github_scout.py"
sys.path.insert(0, os.path.dirname(SCOUT))
import github_scout as gs

RESERVE = "E:/图谱工作包/GitHub储备资料仓库"
DATE = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).strftime("%Y-%m-%d")
TOKEN = gs._get_token()

CALLS = {"n": 0, "search": 0}
RATE_HIT = {"v": False}
CORE_BUDGET = 50        # 匿名核心 API 60/h，预留余量
SUBQ_SLEEP = 10         # 搜索 API 匿名 10/min，留足余量
INIT_WAIT = 60          # 开场等 60s，让本分钟搜索额度复位

# 主题： (子目录, task, [子查询], [领域必含词(命中其一即通过领域闸门)], [负向过滤词(命中即弃)])
THEMES = [
    ("01_招投标",
     "招投标、电子投标相关的开源库与工具，关注投标助手、暗标、标书生成",
     ["tender", "e-procurement", "electronic bidding", "bidding automation"],
     ["投标", "标书", "招标", "评标", "暗标", "标讯", "bid", "tender", "bidding"],
     ["tendermint", "cosmos", "blockchain", "区块链",
      "六四", "法轮功", "新疆改造", "dictatorship", "propaganda", "反中共", "包子露宪",
      "修宪", "heil xi", "文革", "民运", "疆独", "藏独", "台独", "terrorist", "isis",
      "毛泽东", "邓小平", "王沪宁", "习近平"]),
    ("02_工程造价",
     "工程造价、工程量清单、算量相关的开源工具与数据集",
     ["quantity takeoff", "cost estimation construction", "bill of quantities", "工程造价",
      "open takeoff estimation", "construction cost estimator"],
     ["造价", "工程量清单", "算量", "定额", "cost estimation", "quantity takeoff",
      "bill of quantities", "boq", "工程量", "takeoff", "estimate", "estimator",
      "costing", "construction cost", "pricing", "bim", "计价", "造价软件"],
     ["六四", "法轮功", "新疆改造", "dictatorship", "propaganda", "反中共", "包子露宪",
      "修宪", "heil xi", "文革", "民运", "疆独", "藏独", "台独", "terrorist", "isis",
      "毛泽东", "邓小平", "王沪宁", "习近平"]),
    ("03_文档解析",
     "PDF/Word/Excel 解析、比对与文档转换的库",
     ["pdf parser", "docx parser", "excel parse python", "document comparison"],
     ["pdf", "word", "excel", "docx", "解析", "比对", "文档转换", "document parse",
      "pdf parser", "extract", "xlsx", "文档解析", "markdown"],
     ["六四", "法轮功", "新疆改造", "dictatorship", "propaganda", "反中共", "包子露宪",
      "修宪", "heil xi", "文革", "民运", "疆独", "藏独", "台独", "terrorist", "isis"]),
    ("04_投标技术文件",
     "施工组织设计、投标技术文件、标书生成相关工具",
     ["bid proposal generator", "tender document", "施工组织设计", "标书"],
     ["施工组织", "标书", "投标技术", "技术标", "施组", "construction proposal",
      "bid proposal", "技术方案", "投标方案", "标书生成"],
     ["tendermint", "cosmos", "blockchain", "区块链",
      "六四", "法轮功", "新疆改造", "dictatorship", "propaganda", "反中共", "包子露宪",
      "修宪", "heil xi", "文革", "民运", "疆独", "藏独", "台独", "terrorist", "isis"]),
    ("05_工程资料管理",
     "工程资料管理、项目文档归档相关的开源系统",
     ["engineering document management", "construction document control", "工程资料", "施工资料",
      "engineering cms", "construction document management system"],
     # v3.3: 移除裸露泛化英文词（engineer/cms/archive/file/project management/construction management）
     # —— 它们会误命中"software engineer/geo flow/anti-DDoS/考研 docs"等无关仓库；仅保留带工程语境的专有短语。
     ["资料管理", "工程资料", "文档归档", "档案管理", "document management",
      "project archive", "工程档案", "资料归档", "施工资料", "document control",
      "engineering document", "construction document", "construction document control",
      "工程文档", "文档系统", "归档系统", "engineering cms"],
     ["六四", "法轮功", "新疆改造", "dictatorship", "propaganda", "反中共", "包子露宪",
      "修宪", "heil xi", "文革", "民运", "疆独", "藏独", "台独", "terrorist", "isis"]),
    ("06_关联检索",
     "招投标文档分析、评标、知识库检索，与投标资料仓库关联泛化检索",
     ["tender evaluation", "procurement analysis", "评标", "知识库 问答"],
     ["招投标文档", "评标", "知识库", "rag", "检索", "合同分析", "contract analysis",
      "文档分析", "knowledge base", "问答", "投标资料", "招投标"],
     # v3.2: 06 主题专用「应用领域负向词」——仅含通用 rag/知识库 但属无关应用领域的仓库（如医疗/HR/CMS/视频平台）判定为误收
     ["六四", "法轮功", "新疆改造", "dictatorship", "propaganda", "反中共", "包子露宪",
      "修宪", "heil xi", "文革", "民运", "疆独", "藏独", "台独", "terrorist", "isis",
      "医疗", "医院", "doctor", "病历", "medical", "health", "健康", "养生",
      "人事", "招聘", "人力资源", "薪资", "payroll", "hrm",
      "cms", "内容管理", "社区", "知乎", "论坛", "blog", "博客",
      "bilibili", "抖音", "youtube", "视频", "直播",
      "电商", "商城", "shop", "课程", "教育", "教务", "考试"]),
]

MIN_STARS = 50
TOP = 8
MAX_PER_THEME = 6

# v3.3: 各主题单独 star 门槛——niche 主题（02/05）长期空额，下调以挖掘中小仓库
MIN_STARS_MAP = {"02_工程造价": 20, "05_工程资料管理": 20}

# v3.3: 强制收录——历史审计确认相关、却被闸门/检索漏掉的 niche 仓库，按全名直接拉取（仅在 AVOID 时跳过）
FORCE = {
    "02_工程造价": [
        "Kentucky-ai/opentakeoff",
        "datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR",
    ],
    # v3.3: engineercms 系真实工程文档管理 CMS（Go/Apache-2.0），但名/描述未含带空格的专有短语，
    # 故以强制项保底，避免被收紧后的闸门误排。
    "05_工程资料管理": [
        "3xxx/engineercms",
    ],
}

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

def search_raw(query, min_stars, top, task):
    q = query.strip()
    if min_stars:
        q += " stars:>=%d" % min_stars
    params = up.urlencode({"q": q, "sort": "stars", "order": "desc", "per_page": 30})
    url = gs._API_BASE + "/search/repositories?" + params
    last_err = None
    for attempt in range(4):                      # v3.1: 4 次重试窗口
        data, err = api_get(url, is_search=True)
        if not err:
            items = (data or {}).get("items", [])
            out = [(it, gs.score_repo(it, task=task)) for it in items]
            out.sort(key=lambda x: x[1]["blended"] if task else x[1]["score"], reverse=True)
            return out[:top], None
        last_err = err
        if "403" in str(err):
            time.sleep(60)                         # 搜索限流按分钟复位，等待后重试
        elif "net_err" in str(err):
            time.sleep(5 * (attempt + 1))          # 瞬态网络错误（如 IncompleteRead）退避重试
        else:
            break                                  # 不可恢复错误（422 等）直接放弃
    return None, last_err

def domain_pass(it, sc, domain_terms, neg_terms):
    name = (sc["full_name"] or "").lower()
    desc = (it.get("description") or "").lower()
    topics = " ".join(str(t).lower() for t in (it.get("topics") or []))
    hay = " ".join([name, desc, topics])
    for nt in neg_terms:
        if nt.lower() in hay:
            return False, "负向词命中:%s" % nt
    hit = [t for t in domain_terms if t.lower() in hay]
    if not hit:
        return False, "未命中领域词"
    return True, "领域词:%s" % "/".join(hit)

def get_readme(full):
    url = gs._API_BASE + "/repos/%s/readme" % full
    data, err = api_get(url)
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

# 启动确保目录存在（满足任务规范：父目录在则建子目录）
os.makedirs(RESERVE, exist_ok=True)
for tdir, _task, _subs, _dt, _nt in THEMES:
    os.makedirs(os.path.join(RESERVE, tdir), exist_ok=True)

# v3.1: 跨主题全局去重——扫描所有主题目录，建立已收录集合，避免同一仓库写入多个主题
archived_global = set()
for _td, _t, _s, _d, _n in THEMES:
    _dp = os.path.join(RESERVE, _td)
    if os.path.isdir(_dp):
        for _fn in os.listdir(_dp):
            if _fn.endswith(".md") and "__" in _fn:
                archived_global.add(_fn[:-3].replace("__", "/"))

time.sleep(INIT_WAIT)
archived = []
log_lines = []

# 支持命令行指定只跑部分主题：python scout_runner.py 04_投标技术文件 05_工程资料管理
ONLY = [a for a in sys.argv[1:] if not a.startswith("-")] if len(sys.argv) > 1 else []

for tdir, task, subs, domain_terms, neg_terms in THEMES:
    if ONLY and tdir not in ONLY:
        log_lines.append("[主题] %s | 本次跳过（命令行指定主题）" % tdir)
        continue
    # v3.1: 主题已达标则跳过搜索，节约限流额度（幂等续跑时尤其有效）
    dpath = os.path.join(RESERVE, tdir)
    existing = [f for f in os.listdir(dpath) if f.endswith(".md") and "__" in f] if os.path.isdir(dpath) else []
    if len(existing) >= MAX_PER_THEME:
        log_lines.append("[主题] %s | 已收录 %d（达上限 %d），跳过搜索" % (tdir, len(existing), MAX_PER_THEME))
        continue
    log_lines.append("[主题] %s | task=%s（已有 %d/%d）" % (tdir, task[:18], len(existing), MAX_PER_THEME))
    merged = {}
    for q in subs:
        if RATE_HIT["v"]:
            break
        rows, err = search_raw(q, MIN_STARS_MAP.get(tdir, MIN_STARS), TOP, task)
        if err:
            log_lines.append("  ✗ 子查询失败 [%s]: %s" % (q, err))
            if RATE_HIT["v"]:
                break
            continue
        for it, sc in (rows or []):
            fn = sc["full_name"]
            if fn in merged:
                if sc["blended"] > merged[fn][1]["blended"]:
                    merged[fn] = (it, sc)
            else:
                merged[fn] = (it, sc)
        time.sleep(SUBQ_SLEEP)
    # 候选闸门：ADOPT/REVIEW + 领域词命中 + 无负向词
    cands = []
    for fn, (it, sc) in merged.items():
        if sc["verdict"] not in ("ADOPT", "REVIEW"):
            continue
        ok, why = domain_pass(it, sc, domain_terms, neg_terms)
        if ok:
            cands.append((it, sc, why, False))
        else:
            log_lines.append("  · 领域闸门排除 %s (%s)" % (fn, why))
    # v3.3: 强制收录——直接按全名拉取经审计确认相关的 niche 仓库（绕过领域闸门，仅在 AVOID 时跳过）
    for full in FORCE.get(tdir, []):
        if RATE_HIT["v"]:
            break
        if full in archived_global:
            log_lines.append("  ⊘ 强制项已收录/跨主题，跳过 %s" % full)
            continue
        fpath_tmp = os.path.join(RESERVE, tdir, fn_replace(full))
        if os.path.exists(fpath_tmp):
            log_lines.append("  ⊘ 强制项已收录，跳过 %s" % full)
            continue
        data, err = api_get(gs._API_BASE + "/repos/%s" % full)
        if err or not data or not isinstance(data, dict):
            log_lines.append("  · 强制项拉取失败 %s: %s" % (full, err or "空响应"))
            continue
        sc2 = gs.score_repo(data, task=task)
        if sc2["verdict"] == "AVOID":
            log_lines.append("  · 强制项 verdict=AVOID 跳过 %s (flags=%s)" % (full, ",".join(sc2["flags"])))
            continue
        cands.append((data, sc2, "人工预核验相关(强制收录，绕过领域闸门)", True))
        log_lines.append("  ✚ 强制项已拉取 %s (%s, %s★)" % (full, sc2["verdict"], sc2["stars"]))
    # v3.4: 强制项保底——分离强制项后再按上限截取常规项，避免混合分较低的强制项被 MAX_PER_THEME 截断丢弃
    # （本缺陷曾导致 02_工程造价 的强制项 OpenConstructionEstimate-DDC-CWICR 在 11-11 及本次被静默丢弃）
    forced_cands = [c for c in cands if c[3]]
    reg_cands = [c for c in cands if not c[3]]
    reg_cands.sort(key=lambda v: (0 if v[1]["verdict"] == "ADOPT" else 1, -v[1]["blended"]))
    cap = max(0, MAX_PER_THEME - len(forced_cands))
    reg_cands = reg_cands[:cap]
    cands = forced_cands + reg_cands
    log_lines.append("  合并候选 %d，过闸门 %d，强制项 %d，本次处理 %d" % (
        len(merged), len([c for c in merged.values() if c[1]['verdict'] in ('ADOPT','REVIEW')]),
        len(forced_cands), len(cands)))
    for it, sc, why, forced in cands:
        fpath = os.path.join(RESERVE, tdir, fn_replace(sc["full_name"]))
        if os.path.exists(fpath):
            log_lines.append("  ⊘ 已收录，跳过 %s" % sc["full_name"])
            continue
        if sc["full_name"] in archived_global:
            log_lines.append("  ⊘ 已在其他主题收录，跨主题去重跳过 %s" % sc["full_name"])
            continue
        if CALLS["n"] >= CORE_BUDGET:
            log_lines.append("  ⚠ 已达核心 API 预算(%d)，剩余顺延" % CORE_BUDGET)
            break
        full = sc["full_name"]
        verdict = sc["verdict"]
        pushed = it.get("pushed_at", "") or it.get("updated_at", "")
        lic = sc["license"]
        desc = (it.get("description") or "").strip()
        readme = clip(get_readme(full))
        cpath, code = pick_core_file(full)
        code_clip = clip(code, 4000)
        md = []
        md.append("# %s" % full)
        md.append("")
        md.append("- **仓库名**：%s" % full)
        md.append("- **原文链接**：%s" % it.get("html_url", ""))
        md.append("- **Star 数**：%s（取自 GitHub 搜索 API；本环境数值可能偏高，待核实）" % sc["stars"])
        md.append("- **最近更新时间**：%s" % pushed)
        md.append("- **许可证**：%s" % lic)
        md.append("- **语言**：%s" % sc["language"])
        md.append("- **质量分 / 适配分 / 混合分**：%s / %s / %s" % (sc["score"], sc["adapt"], sc["blended"]))
        md.append("- **结论**：%s" % verdict)
        md.append("- **标记**：%s" % (", ".join(sc["flags"]) if sc["flags"] else "无"))
        md.append("- **领域适配**：%s" % why)
        md.append("")
        md.append("## 用途摘要")
        md.append(desc or "（无描述）")
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
        archived.append((tdir, full, verdict))
        log_lines.append("  ✓ 收录 %s (%s, %s★) -> %s" % (full, verdict, sc["stars"], os.path.basename(fpath)))
        if RATE_HIT["v"]:
            break
    if RATE_HIT["v"]:
        log_lines.append("⚠ 触发 403 限流，本次运行终止，剩余主题留待次日。")
        break

# 总索引（合并式：每次运行把已有文件目录重扫后合并写总索引，避免空跑/限流失败覆盖历史）
idx = []
idx.append("# GitHub 储备资料仓库 · 总索引")
idx.append("")
idx.append("- **采集日期**：%s" % DATE)
idx.append("- **采集方式**：只读抓取公开仓库（github_scout 实时搜索+打分 + 领域关键词闸门过滤），全程未上传/未修改用户其他资料")
idx.append("- **API 调用**：核心 %d 次 / 搜索 %d 次" % (CALLS["n"], CALLS["search"]))
idx.append("- **限流状态**：%s" % ("已触发 403，部分主题顺延至次日" if RATE_HIT["v"] else "正常完成"))
idx.append("")
counts = {}
all_archived = []
for tdir, task, subs, dt, nt in THEMES:
    d = os.path.join(RESERVE, tdir)
    if not os.path.isdir(d):
        continue
    for fnm in sorted(os.listdir(d)):
        if fnm.endswith(".md") and "__" in fnm:
            full = fnm[:-3].replace("__", "/")
            verdict = "REVIEW"
            fpath = os.path.join(d, fnm)
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    head = f.read(2000)
                m = re.search(r"结论\*\*：\s*(\w+)", head)
                if m:
                    verdict = m.group(1)
            except Exception:
                pass
            all_archived.append((tdir, full, verdict))
idx.append("## 各主题收录数量（累计，含历史）")
for tdir, task, subs, dt, nt in THEMES:
    idx.append("- %s：%d 个" % (tdir, counts.get(tdir, 0) or len([1 for a in all_archived if a[0] == tdir])))
idx.append("")
idx.append("## 仓库清单（累计）")
if all_archived:
    for tdir, full, verdict in all_archived:
        idx.append("- [%s] **%s** — %s/%s.md" % (verdict, full, tdir, full.replace('/', '__')))
else:
    idx.append("（本次无收录）")
idx.append("")
idx.append("## 本次运行新增")
if archived:
    for tdir, full, verdict in archived:
        idx.append("- [%s] **%s**" % (verdict, full))
else:
    idx.append("- 本次运行无新增（幂等跳过/限流顺延均属正常）")
idx.append("")
idx.append("## 排除说明")
idx.append("- `_excluded/` 目录存放因「领域闸门/负向过滤」判定为无关（如政治类高分噪声仓库）而剔除的候选，保留以供审计。")
idx.append("")
idx.append("本索引由自动化任务每晚更新；采集脚本见仓库根目录 `scout_runner.py`。")
with open(os.path.join(RESERVE, "README.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(idx))

with open(os.path.join(RESERVE, "README.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(idx))

log_full = os.path.join(RESERVE, "采集日志_%s.md" % DATE)
prev_log = ""
if os.path.exists(log_full):
    try:
        with open(log_full, "r", encoding="utf-8") as f:
            prev_log = f.read()
    except Exception:
        prev_log = ""
if archived or not prev_log:
    with open(log_full, "w", encoding="utf-8") as f:
        f.write(prev_log + ("\n\n" if prev_log else "") + "# 补充运行 %s %s\n\n" % (DATE, datetime.datetime.now().strftime("%H:%M")))
        f.write("\n".join(log_lines))
        f.write("\n\n核心 API 调用：%d | 搜索调用：%d | 限流：%s\n" % (CALLS["n"], CALLS["search"], "是" if RATE_HIT["v"] else "否"))
else:
    print("SKIP-LOG: 本次无新增且已有日志，不覆盖。")

print("DONE archived=%d core=%d search=%d rate_hit=%s" % (len(archived), CALLS["n"], CALLS["search"], RATE_HIT["v"]))
print("LOG:\n" + "\n".join(log_lines))
