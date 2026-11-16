# -*- coding: utf-8 -*-
"""GitHub Issue 只读采集器（A2 渠道，v1.0）。

与 scout_runner.py（A1 仓库抓取）配套：scout 抓仓库摘要，本脚本抓 Issue 类资料。
- 渠道：GitHub Issues 搜索 API（/search/issues，is:issue 排除 PR），按评论数排序取活跃讨论。
- 闸门：领域关键词闸门 + 负向过滤（与 scout_runner 同源，杜绝无关/敏感仓库混入）。
- 质量：对过闸候选补拉仓库元数据，星标低于 MIN_REPO_STARS 的仓库其 Issue 不收录。
- 幂等：07_Issues 目录已存在同名文件则跳过；跨主题去重。
- 限流：认证令牌（5000/时核心、30/分搜索）；核心设硬预算，搜索留间隔，403 即停顺延。
- 只读：全程不写入/上传 GitHub，仅写本地 07_Issues/。

用法：
    python issue_runner.py                 # 跑全部主题
    python issue_runner.py 01_招投标       # 只跑指定主题
"""
import sys, os, re, json, time, datetime, urllib.parse as up

SCOUT = "C:/Users/远见1号/.workbuddy/plugins/marketplaces/experts/plugins/github-tool-scout-expert-plus/skills/github-tools-scout/scripts/github_scout.py"
sys.path.insert(0, os.path.dirname(SCOUT))
import github_scout as gs

RESERVE = "E:/图谱工作包/GitHub储备资料仓库"
ISSUE_DIR = os.path.join(RESERVE, "07_Issues")
DATE = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).strftime("%Y-%m-%d")
TOKEN = gs._get_token()

CALLS = {"n": 0, "search": 0}
RATE_HIT = {"v": False}
CORE_BUDGET = 120        # 认证核心 5000/时，预留余量
SEARCH_SLEEP = 8         # 搜索 30/分，留足余量

# 主题：(子目录, task, [Issue 子查询], [领域必含词], [负向过滤词])
# 领域词/负向词与 scout_runner.py 同源，保持两脚本口径一致。
THEMES = [
    ("01_招投标",
     "招投标、电子投标相关开源工具的 Issue 讨论",
     ["tender is:issue", "投标 is:issue", "标书 is:issue", "bidding is:issue"],
     ["投标", "标书", "招标", "评标", "暗标", "标讯", "bid", "tender", "bidding"],
     ["tendermint", "cosmos", "blockchain", "区块链",
      "六四", "法轮功", "新疆改造", "dictatorship", "propaganda", "反中共", "包子露宪",
      "修宪", "heil xi", "文革", "民运", "疆独", "藏独", "台独", "terrorist", "isis",
      "毛泽东", "邓小平", "王沪宁", "习近平"]),
    ("02_工程造价",
     "工程造价、工程量清单、算量工具的 Issue 讨论",
     ["造价 is:issue", "工程量清单 is:issue", "cost estimation is:issue", "takeoff is:issue"],
     ["造价", "工程量清单", "算量", "定额", "cost estimation", "quantity takeoff",
      "bill of quantities", "boq", "工程量", "takeoff", "estimate", "estimator",
      "costing", "construction cost", "pricing", "bim", "计价", "造价软件"],
     ["六四", "法轮功", "新疆改造", "dictatorship", "propaganda", "反中共", "包子露宪",
      "修宪", "heil xi", "文革", "民运", "疆独", "藏独", "台独", "terrorist", "isis",
      "毛泽东", "邓小平", "王沪宁", "习近平"]),
    ("03_文档解析",
     "PDF/Word/Excel 解析、文档转换库的 Issue 讨论",
     ["pdf parser is:issue", "docx is:issue", "文档解析 is:issue", "markdown is:issue"],
     ["pdf", "word", "excel", "docx", "解析", "比对", "文档转换", "document parse",
      "pdf parser", "extract", "xlsx", "文档解析", "markdown"],
     ["六四", "法轮功", "新疆改造", "dictatorship", "propaganda", "反中共", "包子露宪",
      "修宪", "heil xi", "文革", "民运", "疆独", "藏独", "台独", "terrorist", "isis"]),
    ("04_投标技术文件",
     "施工组织设计、投标技术文件、标书生成工具的 Issue 讨论",
     ["施工组织设计 is:issue", "标书生成 is:issue", "bid proposal is:issue", "tender document is:issue"],
     ["施工组织", "标书", "投标技术", "技术标", "施组", "construction proposal",
      "bid proposal", "技术方案", "投标方案", "标书生成"],
     ["tendermint", "cosmos", "blockchain", "区块链",
      "六四", "法轮功", "新疆改造", "dictatorship", "propaganda", "反中共", "包子露宪",
      "修宪", "heil xi", "文革", "民运", "疆独", "藏独", "台独", "terrorist", "isis"]),
    ("05_工程资料管理",
     "工程资料管理、项目文档归档系统的 Issue 讨论",
     ["工程资料 is:issue", "document management is:issue", "工程档案 is:issue", "construction document is:issue"],
     ["资料管理", "工程资料", "文档归档", "档案管理", "document management",
      "project archive", "工程档案", "资料归档", "施工资料", "document control",
      "engineering document", "construction document", "工程文档", "文档系统", "归档系统", "engineering cms"],
     ["六四", "法轮功", "新疆改造", "dictatorship", "propaganda", "反中共", "包子露宪",
      "修宪", "heil xi", "文革", "民运", "疆独", "藏独", "台独", "terrorist", "isis"]),
    ("06_关联检索",
     "招投标文档分析、评标、知识库检索的 Issue 讨论",
     ["评标 is:issue", "rag is:issue", "知识库 is:issue", "tender evaluation is:issue"],
     ["招投标文档", "评标", "知识库", "rag", "检索", "合同分析", "contract analysis",
      "文档分析", "knowledge base", "问答", "投标资料", "招投标"],
     ["六四", "法轮功", "新疆改造", "dictatorship", "propaganda", "反中共", "包子露宪",
      "修宪", "heil xi", "文革", "民运", "疆独", "藏独", "台独", "terrorist", "isis",
      "医疗", "医院", "doctor", "病历", "medical", "health", "健康", "养生",
      "人事", "招聘", "人力资源", "薪资", "payroll", "hrm",
      "cms", "内容管理", "社区", "知乎", "论坛", "blog", "博客",
      "bilibili", "抖音", "youtube", "视频", "直播",
      "电商", "商城", "shop", "课程", "教育", "教务", "考试"]),
]

MIN_REPO_STARS = 20      # 仓库星标门槛：低于此值的仓库其 Issue 不收录
TOP = 8                  # 每子查询取前 N 条
MAX_PER_THEME = 6        # 每主题收录上限
COMMENT_CLIP = 1500      # 评论截断长度
BODY_CLIP = 4000         # Issue 正文截断长度


def fn_replace(full, num):
    return full.replace("/", "__") + "__issue-%d.md" % num


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


def search_issues(query, top):
    q = query.strip()
    params = up.urlencode({"q": q, "sort": "comments", "order": "desc", "per_page": 30})
    url = gs._API_BASE + "/search/issues?" + params
    last_err = None
    for attempt in range(4):
        data, err = api_get(url, is_search=True)
        if not err:
            return (data or {}).get("items", []), None
        last_err = err
        if "403" in str(err):
            time.sleep(60)
        elif "net_err" in str(err):
            time.sleep(5 * (attempt + 1))
        else:
            break
    return None, last_err


def repo_full_of(item):
    ru = item.get("repository_url") or ""
    return ru.rsplit("/repos/", 1)[-1] if "/repos/" in ru else ""


def domain_pass(item, domain_terms, neg_terms):
    full = repo_full_of(item)
    title = (item.get("title") or "").lower()
    body = (item.get("body") or "").lower()
    hay = " ".join([full.lower(), title, body[:500]])
    for nt in neg_terms:
        if nt.lower() in hay:
            return False, "负向词命中:%s" % nt
    hit = [t for t in domain_terms if t.lower() in hay]
    if not hit:
        return False, "未命中领域词"
    return True, "领域词:%s" % "/".join(hit)


def get_repo_meta(full):
    data, err = api_get(gs._API_BASE + "/repos/%s" % full)
    if err or not data:
        return None
    return data


def get_issue_detail(full, num):
    data, err = api_get(gs._API_BASE + "/repos/%s/issues/%d" % (full, num))
    if err or not data:
        return {}
    return data


def get_comments(full, num, limit=3):
    url = gs._API_BASE + "/repos/%s/issues/%d/comments?per_page=%d" % (full, num, limit)
    data, err = api_get(url)
    if err or not isinstance(data, list):
        return []
    return data


def clip(txt, n):
    if not txt:
        return ""
    txt = txt.strip()
    return txt if len(txt) <= n else txt[:n] + "\n...（截断，原文见链接）"


os.makedirs(ISSUE_DIR, exist_ok=True)

# 跨主题全局去重：已收录的 owner/repo/issue 集合
archived_global = set()
if os.path.isdir(ISSUE_DIR):
    for _fn in os.listdir(ISSUE_DIR):
        if _fn.endswith(".md") and "__issue-" in _fn:
            m = re.match(r"(.+?)__issue-(\d+)\.md$", _fn)
            if m:
                archived_global.add((m.group(1), int(m.group(2))))

log_lines = []
archived = []

ONLY = [a for a in sys.argv[1:] if not a.startswith("-")] if len(sys.argv) > 1 else []

for tdir, task, subs, domain_terms, neg_terms in THEMES:
    if ONLY and tdir not in ONLY:
        log_lines.append("[主题] %s | 本次跳过（命令行指定主题）" % tdir)
        continue
    existing = [f for f in os.listdir(ISSUE_DIR) if f.endswith(".md") and "__issue-" in f] \
        if os.path.isdir(ISSUE_DIR) else []
    # 按主题统计已有：07_Issues 为渠道型目录，此处以全局已有数判断是否达上限
    if len(existing) >= MAX_PER_THEME * len(THEMES):
        log_lines.append("[主题] %s | 全局 Issue 已达上限，跳过" % tdir)
        continue
    log_lines.append("[主题] %s | task=%s" % (tdir, task[:18]))
    merged = {}
    for q in subs:
        if RATE_HIT["v"]:
            break
        rows, err = search_issues(q, TOP)
        if err:
            log_lines.append("  ✗ 子查询失败 [%s]: %s" % (q, err))
            if RATE_HIT["v"]:
                break
            continue
        for it in (rows or []):
            full = repo_full_of(it)
            num = it.get("number")
            if not full or not num:
                continue
            key = (full, num)
            if key not in merged or (it.get("comments") or 0) > (merged[key].get("comments") or 0):
                merged[key] = it
        time.sleep(SEARCH_SLEEP)

    cands = []
    for (full, num), it in merged.items():
        ok, why = domain_pass(it, domain_terms, neg_terms)
        if ok:
            cands.append((it, why))
        else:
            log_lines.append("  · 领域闸门排除 %s#%s (%s)" % (full, num, why))

    cands.sort(key=lambda x: (x[0].get("comments") or 0), reverse=True)
    for it, why in cands:
        full = repo_full_of(it)
        num = it.get("number")
        key = (full, num)
        if key in archived_global:
            log_lines.append("  ⊘ 已收录/跨主题，跳过 %s#%s" % (full, num))
            continue
        if CALLS["n"] >= CORE_BUDGET:
            log_lines.append("  ⚠ 已达核心 API 预算(%d)，剩余顺延" % CORE_BUDGET)
            break
        # 补拉仓库元数据，星标不足则跳过
        meta = get_repo_meta(full)
        if not meta:
            log_lines.append("  · 仓库元数据拉取失败 %s，跳过" % full)
            continue
        stars = meta.get("stargazers_count") or 0
        if stars < MIN_REPO_STARS:
            log_lines.append("  · 仓库星标不足(%d<%d) %s，跳过" % (stars, MIN_REPO_STARS, full))
            continue
        detail = get_issue_detail(full, num)
        comments = get_comments(full, num, limit=3)
        fpath = os.path.join(ISSUE_DIR, fn_replace(full, num))
        md = []
        md.append("---")
        md.append("title: %s #%d：%s" % (full, num, (it.get("title") or "").strip()))
        md.append("source: GitHub Issue（%s #%d）" % (full, num))
        md.append("topic: %s" % tdir)
        md.append("date: %s" % (it.get("created_at") or "").replace("T", " ").replace("Z", "")[:10])
        md.append("harvest_date: %s" % DATE)
        md.append("url: %s" % (it.get("html_url") or ""))
        md.append("tags: [公开学习库, %s, GitHub Issue]" % tdir)
        md.append("---")
        md.append("")
        md.append("# %s · Issue #%d：%s" % (full, num, (it.get("title") or "").strip()))
        md.append("")
        md.append("- **来源**：%s" % full)
        md.append("- **Issue 编号**：#%d" % num)
        md.append("- **原文链接**：%s" % (it.get("html_url") or ""))
        md.append("- **状态**：%s" % (it.get("state") or "未知"))
        md.append("- **评论数**：%s" % (it.get("comments") or 0))
        md.append("- **仓库星标**：%s（取自 GitHub API，待核实）" % stars)
        md.append("- **仓库许可证**：%s" % ((meta.get("license") or {}).get("spdx_id") or "未知"))
        md.append("- **抓取日期**：%s" % DATE)
        md.append("- **领域适配**：%s" % why)
        md.append("")
        md.append("## Issue 正文")
        md.append(clip((detail.get("body") or it.get("body") or "（无正文）"), BODY_CLIP) or "（无正文）")
        md.append("")
        md.append("## 关键评论")
        if comments:
            for c in comments:
                md.append("- **%s**（%s）：%s" % (
                    (c.get("user") or {}).get("login", "匿名"),
                    (c.get("created_at") or "").replace("T", " ").replace("Z", "")[:10],
                    clip(c.get("body") or "", COMMENT_CLIP)))
        else:
            md.append("（无评论或抓取失败）")
        md.append("")
        md.append("## 出处（MLA）")
        md.append('%s. "Issue #%d：%s." *GitHub Issue, %s*, %s, %s' % (
            (it.get("user") or {}).get("login", "匿名"), num,
            (it.get("title") or "").strip(), full,
            (it.get("created_at") or "")[:10], it.get("html_url") or ""))
        with open(fpath, "w", encoding="utf-8") as f:
            f.write("\n".join(md))
        archived_global.add(key)
        archived.append((tdir, full, num))
        log_lines.append("  ✓ 收录 %s#%s（%s评论, %s★）-> %s" % (
            full, num, it.get("comments") or 0, stars, os.path.basename(fpath)))
        if RATE_HIT["v"]:
            break
    if RATE_HIT["v"]:
        log_lines.append("⚠ 触发 403 限流，本次运行终止，剩余主题留待次日。")
        break

# 采集日志（追加式，无新增且已有日志则不覆盖）
log_full = os.path.join(RESERVE, "采集日志_%s_issue.log" % DATE)
prev_log = ""
if os.path.exists(log_full):
    try:
        with open(log_full, "r", encoding="utf-8") as f:
            prev_log = f.read()
    except Exception:
        prev_log = ""
if archived or not prev_log:
    with open(log_full, "w", encoding="utf-8") as f:
        f.write(prev_log + ("\n\n" if prev_log else "") + "# Issue 采集补充运行 %s %s\n\n" % (
            DATE, datetime.datetime.now().strftime("%H:%M")))
        f.write("\n".join(log_lines))
        f.write("\n\n核心 API 调用：%d | 搜索调用：%d | 限流：%s\n" % (
            CALLS["n"], CALLS["search"], "是" if RATE_HIT["v"] else "否"))
else:
    print("SKIP-LOG: 本次无新增且已有日志，不覆盖。")

print("DONE archived=%d core=%d search=%d rate_hit=%s" % (
    len(archived), CALLS["n"], CALLS["search"], RATE_HIT["v"]))
print("LOG:\n" + "\n".join(log_lines))
