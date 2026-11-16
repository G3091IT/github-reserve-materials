# sunkaifei/FlyCms

- **仓库名**：sunkaifei/FlyCms
- **原文链接**：https://github.com/sunkaifei/FlyCms
- **Star 数**：657（取自 GitHub 搜索 API；本环境数值可能偏高，待核实）
- **最近更新时间**：2026-10-24T02:36:01Z
- **许可证**：MIT
- **语言**：Java
- **质量分 / 适配分 / 混合分**：91.1 / 52.9 / 73.9
- **结论**：ADOPT
- **标记**：无
- **领域适配**：领域词:知识库/检索/问答

## 用途摘要
FlyCms 是一个类似知乎以问答为基础的完全开源的JAVA语言开发的社交网络建站程序，基于 Spring Boot+Bootstrap3+MyBatis+MySql+Solr +Ehcache应用架构，专注于社区内容的整理、归类和检索，它集合了问答，digg，wiki 等多个程序的优点，帮助用户轻松搭建专业的知识库和在线问答社区。业务模块包括：权限管理，会员管理，角色管理，定时任务管理（调度管理），问答管理，文章管理，分享管理，短信接口管理和邮件系统发送（注册、找回密码、邮件订阅），跨域登录，消息推送，全文检索、前端国际化等等众多模块，等您自己来体验！

## 适配理由
✓ 命中任务词：知识/识库/检索；△ 未命中：招投/投标/标文/文档/档分/分析/评标/库检/与投/标资/资料/料仓/仓库/库关/关联/联泛/泛化/化检

## README 要点
# FlyCms

> 一套**前后端分离**的开源内容建站系统：后台是 Vue 3 单页控制台，前台是 Freemarker 模板站。
> **核心技术 = 自定义模型引擎**：文章、图片、下载、问答、链接……系统的一切内容模块都由后台**在线建模**生成（建模 → 自动建表 → 字段配置 → 模板渲染），不做第二套硬编码实现。目标是**万能系统**——用户只靠后台设置，就能生成任何想要的程序模块。历史上硬编码的内容模块正在按规划逐个退役并迁入模型引擎（见 `docs/01-规划/主流CMS对标与全项目优化开发方案.md` §9.4 阶段 U）。

```
后端 346 个 Java 文件 / 25 个业务模块 / 21 个 REST 控制器
前端 Vue 3 + TypeScript + Ant Design Vue，73 个页面组件
内容生产：fly_model（模型注册）→ fly_model_field（字段元数据）→ fly_cmodel_{code}（动态数据表）→ 通用管理页 + cmodel 模板通道
```

---

## 一、它现在是什么

FlyCms 最早是一个仿知乎的问答社区程序。经过持续重构，现在的内核是一套**五面分离**的 CMS 底座：

| 面 | 解决什么 | 对应能力 |
|----|---------|---------|
| **内容面** | 内容从哪来、长什么样 | **自定义模型引擎（唯一内容生产方式）**：建模 + 字段（含关联引用 relate/relates、URL 型图片 image_url/file_url、附件、地区等 19 种类型）+ 动态建表 + 通用数据管理；存量硬编码模块（文章/问答/分享/话题）退役中，评论/收藏收敛为平台能力 |
| **结构面** | 内容挂在哪、URL 怎么走 | 统一栏目树（列表 / 单页 / 外链 / 聚合，聚合可跨模型混排） |
| **呈现面** | 页面怎么渲染 | 模板中心（在线编辑 / 版本快照 / 一键回滚 / 皮肤导入导出）、碎片位与推荐位、模板标签手册 |
| **交互面** | 访客怎么参与 | 表单系统（可视化配字段）、站内信、公告、收藏、关注与 Feed、WebSocket 推送 |
| **运营面** | 站点怎么管 | SEO（sitemap / robots）、投稿与评论审核、敏感词过滤、审计日志、定时任务、菜单 / 角色 / 权限 |

---

## 二、技术栈

### 后端

| 组件 | 版本 / 选型 | 说明 |
|------|------------|------|
| 运行时 | **JDK 24** | `maven-compiler-plugin` 开启 `proc:full` 以支持 Lombok |
| 框架 | **Spring Boot 4.1.1** | Jakarta 命名空间 |
| ORM | MyBatis（`mybatis-spring-boot-starter` 4.1.0） | XML 与 Mapper 同目录打包 |
| 模板 | Freemarker | 前台站点渲染，开启 `ALLOWS_NOTHING_RESOLVER` 沙箱 |
| 缓存 | **Caffeine** | 已替代原 EhCache 2 |
| 连接池 | Druid 1.2.28 | Boot 4 下由 `DruidConfig` 手动装配 |
| 调度 | Quartz 2.3.2 | 后台可启停任务、查看执行日志 |
| 数据库 | MySQL 8（utf8mb4） | SQL 仅适配 MySQL |
| 检索 | Lucene 7.4 | **当前为技术中立接缝**：原 Solr 已移除，`SearchService` 保留空实现，规划接入 Elasticsearch |
| 其它 | Hutool 5.8、jsoup 1.17、BCrypt、Log4j2、阿里云短信 SDK | 验证码、XSS 清洗、密码散列 |

### 前端

| 组件 | 版本 |
|------|------|
| Vue | 3.5.41 |
| TypeScript | 6.0 |
| Vite | 8.3 |
| Ant Design Vue | 4.2 |
| 状态 / 路由 | Pinia 4、Vue Router 5 |
| 基座 | Vue Vben Admin 5（`@vben/*` 内部包） |
| 工程 | pnpm 11 workspace + turbo，Node `^22.18 \|\| ^24.12` |

后台是 SPA（`apps/web-antd`），通过 `/api/**` 与后端通信；前台仍是服务端渲染的 Freemarker 模板站，两者互不干扰。

---

## 三、功能清单

### 前台

- **栏目**：列表 / 单页 / 外链 / 聚合四种形态，目录名即 URL，支持无限层级与移动改挂
- **内容模型**：后台建模后自动生成数据表，前台按模型 `code` 路由，列表自带分页条
- **问答**：发布问题、悬赏积分邀请回答、答案列表与统计
- **文章**：分类无限级、话题聚合、评论、顶踩、收藏
- **分享**：分享资源地址赚取积分，支持积分兑换
- **表单**：`<@fly_form code="...">` 输出表单，提交走 `POST /api/form/submit/{code}`
- **用户**：注册（手机 / 邮箱）、登录验证码与失败次数限制、密码找回、手机 / 邮箱绑定、邀请注册奖励、积分充值
- **互动**：关注、粉丝、Feed 动态、收藏、站内信、WebSocket 实时推送
- **SEO**：`/sitemap.xml`、`/robots.txt` 由配置键 `fly_sitemap_status` / `fly_sitemap_limit` / `fly_robots` 控制

### 后台（Vue 控制台）

| 分组 | 功能 |
|------|------|
| 系统管理 | 管理员、角色组、菜单权限（后端动态菜单）、站内信、公告、审计日志、附件库、导航、友情链接 |
| 内容 | 内容模型（模型 / 字段 / 数据 CRUD）、栏目、文章、评论审核、**投稿审核**（先审后发开关 + 批量通过 / 驳回） |
| 呈现 | 模板中心（文件树编辑、版本快照与回滚、皮肤导入导出、标签手册）、碎片位 / 推荐位 |
| 交互 | 表单管理（表单 + 字段 + 数据 + CSV 导出） |
| 运营 | 网站配置、定时任务、积分规则、订单、敏感词过滤、用户管理 |
| 统计 | 仪表盘 |

### 平台能力

- **动态菜单与权限**：菜单、角色、权限点全部数据驱动，`actionKey` 同时用于前端按钮显隐（`accessCodes`）和后端 403 兜底
- **模板版本化**：每次保存自动快照，改坏模板可一键回滚
- **定时发布**：`TimingPublishJob` + `publish_time` 字段，`status=4` 为待定时发布
- **审计日志**：`AdminLogInterceptor` 记录后台操作，含敏感字段脱敏
- **定时任务**：后台启停、Cron 配置、执行日志

---

## 四、安全设计

| 风险 | 处理 |
|------|------|
| 模板 RCE | Freemarker `TemplateClassResolver.ALLOWS_NOTHING_RESOLVER` 沙箱 |
| 上传 getshell | `UploadSafeUtil.safeImage`：扩展名 + MIME + **文件头魔数**三重白名单，强制重命名丢弃原始文件名 |
| SQL 注入 | ORDER BY 走 `OrderbyUtils.check` 白名单；动态建表 / 列名走 `SqlSafeUtil.safeColumnName` / `safeNumber` |
| XSS | 提交内容用 jsoup `Safelist.none()` 清洗（表单模块），页面输出 HTML 转义 |
| 越权 | Session 认证 + `requireAdmin()`（401）/ `requirePermission()`（403）双重校验 |
| 爆破 | 登录验证码 + 失败次数限制；密码 BCrypt 散列 |
| 权限放大 | 表单数据走统一表 + JSON，**不做动态建表**，避免 DDL 权限外溢 |

---

## 五、目录结构

```
FlyCms/
├── backend/                       # Java 后端
│   ├── src/main/java/com/flycms/
│   │   ├── config/                # MVC、CORS、WebSocket、Freemarker 沙箱、Druid
│   │   ├── core/                  # 实体、工具类、全局标签、上传安全
│   │   ├── interceptor/           # 登录拦截、审计日志
│   │   ├── module/                # 26 个业务模块（model / channel / template / form ...）
│   │   └── web/
│   │       ├── api/               # /api/** REST（后台 SPA 用）
│   │       ├── front/             # 前台页面控制器
│   │       └── tags/              # Freemarker 自定义标签
│   ├── src/main/resources/
│   │   ├── application.yml
│   │   └── i18n/                  # 国际化
├── frontend/                      # pnpm workspace
│   ├── apps/web-antd/             # 后台控制台（Vue 3）
│   ├── packages/@core/            # 基础能力包
│   └── internal/                  # 构建配置
├── sql/                           # 数据库全量备份快照（最新一份，含结构+数据）
└── docs/                          # 开发规划、模型手册、改造方案、审查报告、运维配置
```

---

## 六、快速开始

### 环境要求

- JDK 24、Maven 3.6+
- MySQL 8（字符集 `utf8mb4`）
- Node `^22.18 || ^24.12`、pnpm ≥ 11

### 1. 数据库

`sql/` 目录只保留一份**全量备份快照**（表结构 + 全部数据一体，含所有已上线功能与权限节点），无需再按阶段执行增量脚本：

```bash
mysql -u root -p -e "CREATE DATABASE flycms DEFAULT CHARACTER SET utf8mb4;"
mysql -u root -p --default-character-set=utf8mb4 flycms < sql/flycms_20260928_093335.sql
```

> ⚠️ **必须加 `--default-character-set=utf8mb4`**：mysql 客户端在某些终端环境默认 latin1 连接，中文数据会真实乱码（写入即损坏，不是显示问题）。
>
> 备份快照由 MySQL 5.7.44 导出，兼容 MySQL 8 导入。导入后默认管理员：`flycms / admin123`（请登录后立即改密）。

**备份与更新快照**：系统内置纯 Java 全库备份（不依赖 mysqldump），后台「系统工具 → 数据库备份」或直接调用：

```bash
curl -X POST http://localhost/api/system/tools/db/backup   # 需管理员会话
```

备份文件生成于 `backend/backup/flycms_*.sql`；需要刷新 `sql/` 快照时，将最新一份复制过去替换即可。

### 2. 后端

修改 `backend/src/main/resources/application.yml` 的数据库连接，然后：

```bash
cd backend
mvn clean compile        # 编译
mvn spring-boot:run      # 运行
```

默认监听 `http://localhost:80`，前台 `http://localhost/`；管理控制台是前端 Vue SPA（见下一步）。

### 3. 前端控制台

```bash
cd frontend
pnpm install
pnpm dev:antd            # 开发端口 5666
```

`vite.config.ts` 已配置代理：`/api/**` → 后端 80 端口，`/captcha` 直连（验证码接口无 `/api` 前缀）。

### 4. 常用命令

| 命令 | 作用 |
|------|------|
| `mvn -o compile` | 后端编译校验 |
| `pnpm dev:antd` | 启动后台开发服务 |
| `pnpm build:antd` | 构建后台 |
| `pnpm check:type` | 前端类型检查（`vue-tsc`） |
| `pnpm check` | 循环依赖 + 依赖 + 类型 + 拼写全量检查 |

---
...（截断，原文见链接）

## 核心代码片段（来源：README.md）
```java
# FlyCms

> 一套**前后端分离**的开源内容建站系统：后台是 Vue 3 单页控制台，前台是 Freemarker 模板站。
> **核心技术 = 自定义模型引擎**：文章、图片、下载、问答、链接……系统的一切内容模块都由后台**在线建模**生成（建模 → 自动建表 → 字段配置 → 模板渲染），不做第二套硬编码实现。目标是**万能系统**——用户只靠后台设置，就能生成任何想要的程序模块。历史上硬编码的内容模块正在按规划逐个退役并迁入模型引擎（见 `docs/01-规划/主流CMS对标与全项目优化开发方案.md` §9.4 阶段 U）。

```
后端 346 个 Java 文件 / 25 个业务模块 / 21 个 REST 控制器
前端 Vue 3 + TypeScript + Ant Design Vue，73 个页面组件
内容生产：fly_model（模型注册）→ fly_model_field（字段元数据）→ fly_cmodel_{code}（动态数据表）→ 通用管理页 + cmodel 模板通道
```

---

## 一、它现在是什么

FlyCms 最早是一个仿知乎的问答社区程序。经过持续重构，现在的内核是一套**五面分离**的 CMS 底座：

| 面 | 解决什么 | 对应能力 |
|----|---------|---------|
| **内容面** | 内容从哪来、长什么样 | **自定义模型引擎（唯一内容生产方式）**：建模 + 字段（含关联引用 relate/relates、URL 型图片 image_url/file_url、附件、地区等 19 种类型）+ 动态建表 + 通用数据管理；存量硬编码模块（文章/问答/分享/话题）退役中，评论/收藏收敛为平台能力 |
| **结构面** | 内容挂在哪、URL 怎么走 | 统一栏目树（列表 / 单页 / 外链 / 聚合，聚合可跨模型混排） |
| **呈现面** | 页面怎么渲染 | 模板中心（在线编辑 / 版本快照 / 一键回滚 / 皮肤导入导出）、碎片位与推荐位、模板标签手册 |
| **交互面** | 访客怎么参与 | 表单系统（可视化配字段）、站内信、公告、收藏、关注与 Feed、WebSocket 推送 |
| **运营面** | 站点怎么管 | SEO（sitemap / robots）、投稿与评论审核、敏感词过滤、审计日志、定时任务、菜单 / 角色 / 权限 |

---

## 二、技术栈

### 后端

| 组件 | 版本 / 选型 | 说明 |
|------|------------|------|
| 运行时 | **JDK 24** | `maven-compiler-plugin` 开启 `proc:full` 以支持 Lombok |
| 框架 | **Spring Boot 4.1.1** | Jakarta 命名空间 |
| ORM | MyBatis（`mybatis-spring-boot-starter` 4.1.0） | XML 与 Mapper 同目录打包 |
| 模板 | Freemarker | 前台站点渲染，开启 `ALLOWS_NOTHING_RESOLVER` 沙箱 |
| 缓存 | **Caffeine** | 已替代原 EhCache 2 |
| 连接池 | Druid 1.2.28 | Boot 4 下由 `DruidConfig` 手动装配 |
| 调度 | Quartz 2.3.2 | 后台可启停任务、查看执行日志 |
| 数据库 | MySQL 8（utf8mb4） | SQL 仅适配 MySQL |
| 检索 | Lucene 7.4 | **当前为技术中立接缝**：原 Solr 已移除，`SearchService` 保留空实现，规划接入 Elasticsearch |
| 其它 | Hutool 5.8、jsoup 1.17、BCrypt、Log4j2、阿里云短信 SDK | 验证码、XSS 清洗、密码散列 |

### 前端

| 组件 | 版本 |
|------|------|
| Vue | 3.5.41 |
| TypeScript | 6.0 |
| Vite | 8.3 |
| Ant Design Vue | 4.2 |
| 状态 / 路由 | Pinia 4、Vue Router 5 |
| 基座 | Vue Vben Admin 5（`@vben/*` 内部包） |
| 工程 | pnpm 11 workspace + turbo，Node `^22.18 \|\| ^24.12` |

后台是 SPA（`apps/web-antd`），通过 `/api/**` 与后端通信；前台仍是服务端渲染的 Freemarker 模板站，两者互不干扰。

---

## 三、功能清单

### 前台

- **栏目**：列表 / 单页 / 外链 / 聚合四种形态，目录名即 URL，支持无限层级与移动改挂
- **内容模型**：后台建模后自动生成数据表，前台按模型 `code` 路由，列表自带分页条
- **问答**：发布问题、悬赏积分邀请回答、答案列表与统计
- **文章**：分类无限级、话题聚合、评论、顶踩、收藏
- **分享**：分享资源地址赚取积分，支持积分兑换
- **表单**：`<@fly_form code="...">` 输出表单，提交走 `POST /api/form/submit/{code}`
- **用户**：注册（手机 / 邮箱）、登录验证码与失败次数限制、密码找回、手机 / 邮箱绑定、邀请注册奖励、积分充值
- **互动**：关注、粉丝、Feed 动态、收藏、站内信、WebSocket 实时推送
- **SEO**：`/sitemap.xml`、`/robots.txt` 由配置键 `fly_sitemap_status` / `fly_sitemap_limit` / `fly_robots` 控制

### 后台（Vue 控制台）

| 分组 | 功能 |
|------|------|
| 系统管理 | 管理员、角色组、菜单权限（后端动态菜单）、站内信、公告、审计日志、附件库、导航、友情链接 |
| 内容 | 内容模型（模型 / 字段 / 数据 CRUD）、栏目、文章、评论审核、**投稿审核**（先审后发开关 + 批量通过 / 驳回） |
| 呈现 | 模板中心（文件树编辑、版本快照与回滚、皮肤导入导出、标签手册）、碎片位 / 推荐位 |
| 交互 | 表单管理（表单 + 字段 + 数据 + CSV 导出） |
| 运营 | 网站配置、定时任务、积分规则、订单、敏感词过滤、用户管理 |
| 统计 | 仪表盘 |

### 平台能力

- **动态菜单与权限**：菜单、角色、权限点全部数据驱动，`actionKey` 同时用于前端按钮显隐（`accessCodes`）和后端 403 兜底
- **模板版本化**：每次保存自动快照，改坏模板可一键回滚
- **定时发布**：`TimingPublishJob` + `publish_time` 字段，`status=4` 为待定时发布
- **审计日志**：`AdminLogInterceptor` 记录后台操作，含敏感字段脱敏
- **定时任务**：后台启停、Cron 配置、执行日志

---

## 四、安全设计

| 风险 | 处理 |
|------|------|
| 模板 RCE | Freemarker `TemplateClassResolver.ALLOWS_NOTHING_RESOLVER` 沙箱 |
| 上传 getshell | `UploadSafeUtil.safeImage`：扩展名 + MIME + **文件头魔数**三重白名单，强制重命名丢弃原始文件名 |
| SQL 注入 | ORDER BY 走 `OrderbyUtils.check` 白名单；动态建表 / 列名走 `SqlSafeUtil.safeColumnName` / `safeNumber` |
| XSS | 提交内容用 jsoup `Safelist.none()` 清洗（表单模块），页面输出 HTML 转义 |
| 越权 | Session 认证 + `requireAdmin()`（401）/ `requirePermission()`（403）双重校验 |
| 爆破 | 登录验证码 + 失败次数限制；密码 BCrypt 散列 |
| 权限放大 | 表单数据走统一表 + JSON，**不做动态建表**，避免 DDL 权限外溢 |

---

## 五、目录结构

```
FlyCms/
├── backend/                       # Java 后端
│   ├── src/main/java/com/flycms/
│   │   ├── config/                # MVC、CORS、WebSocket、Freemarker 沙箱、Druid
│   │   ├── core/                  # 实体、工具类、全局标签、上传安全
│   │   ├── interceptor/           # 登录拦截、审计日志
│   │   ├── module/                # 26 个业务模块（model / c
...（截断，原文见链接）
```
