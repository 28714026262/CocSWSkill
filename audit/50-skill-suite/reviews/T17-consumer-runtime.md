# T17：实际消费者运行验收

2026-10-21，测试执行者：独立消费者运行测试代理。结论：**修订后最小内容资源包通过本次实际 API 接入、文件读取及纯剧本导出往返；有限浏览器任务通过。** 这是 `runtime-2` 新制测试小样的运行资格，**不是** `tests/end-to-end-output` 微项目完整 P8 已导入，也不是全部工作台功能、平台自动发现或真人游玩通过。

## 对象与方法

- 原消费者：`D:/SZK/Personal/COC/keeper-workbench`，绑定 HEAD `1104e4f7d440ddeeeb673afcec9c52ad2bd1e91d`。依 `compatibility.json` 核对的 8 个源码 SHA256 全部吻合，测试末复核仍相同。
- 测试根：`D:/SZK/Personal/COC/echo/research/2026-10-21-skill拆分实施/tests/consumer-runtime`（以下记作 T）。本报告之外，全部新文件、数据库、依赖副本、日志、浏览器 profile/socket/temp 和进程记录均在 T。
- 只读 `git archive HEAD backend frontend README.md docs scripts tests .gitignore` 获取受控源码；没有复制或读取原 `data/`、`content/`、`sample/`、场次、运行凭据。未调用原实例端口、未操作原服务、未改原仓库、全局代理、hosts 或系统服务。
- 先读 `scenario-production/SKILL.md`，按窄接入任务选择 P8 README → integration、compatibility、maps-media，再读空间 map-construction、map-qa 的实际图件分支。没有读取许可待定教学素材。方法指纹与前后对照保存在 `T/evidence/method-fingerprints*.json`。
- 浏览器依 `agent-browser` 技能和已安装 CLI 的 `skills get core` 工作流，独立命名会话；从真实页面快照选择入口，无页面响应桩。

## 隔离实例与实际运行

预检确认 `127.0.0.1:14317`、`:19879` 未占用后才启动。Java 17 / Spring Boot 3.5.16 应用监听 19879；独立 MySQL 9.6 监听 14317，数据库 `keeper_t17`。`keeper.root` 指向 T，MySQL datadir 为 `T/runtime/mysql-data`。未启动 MinIO；未调用任何 MinIO 接口。读现成 Maven/npm 依赖缓存并复制到 T，再离线构建绑定源码；未借用原预构建 JAR 冒充本次源码构建。

实际启动前遇到并保留的修正：默认 Maven 缓存缺 MySQL/MinIO 依赖，改复制仓库现成依赖到独立缓存；MySQL 对含中文路径初始化失败，使用同一 T 的 Windows 短路径 `D:/SZK/Personal/COC/echo/research/20D8F8~1/tests/CONSUM~1`，以同一源码包哈希交叉核验别名；Vite 首次误用 `--root`，改为位置参数后前端和后端构建成功。原失败未作为成功证据。

初轮进程为 Java 启动器 44836 / 实际 JVM 18604、MySQL 启动器 36900 / 实际服务 28204。修订轮为 Java 启动器 42396 / 实际 JVM 17412、MySQL 启动器 36784 / 实际服务 47852。原始命令行、父进程和绝对存储地址见 `T/evidence/processes-before-stop.json`、`T/round2/evidence/processes-before-stop.json`，均仅含测试实例路径。

两轮均正常停止：向已核对归属的应用控制台发送 Ctrl-C，日志出现 JVM shutdown hook、`Graceful shutdown complete` 与 Hikari 正常关闭；MySQL 通过指向独立配置的 `mysqladmin shutdown`，日志出现 `Normal shutdown` / `Shutdown complete`。首次附加应用控制台后同一 PowerShell 的 console handle 失效，MySQL 停止改从新 shell 正常执行；未强制杀进程。最终 14317、19879 均无监听。末次停止时间 `2026-10-21T07:40:50Z` 左右；全部测试数据保留，凭据不写入本报告。

## 实际候选与返修

测试小样新写 4 个章节（5/6/8/9）、1 人物、1 图纸/图集、4 地点、1 线索/来源、1 手卡、1 玩家材料索引。SVG 为本次新绘公开几何示意；便条为本题虚构原文；不存在外部许可待定资产。图件与原稿授权说明同包，玩家目录两件普通文件：`index.html` 与 `public-plan.svg`，HTML 自含文字、无依赖。

**初轮有制作缺陷，不授玩家原件合格：** `index.html` 在完整便条原文后附了“本件仅证明曾有交付安排。”解释。root 复核指出它是证明限度而非世界内原文。初轮 ZIP、响应、空间、截图和 API 结果全部保留，不能作为最终玩家件证据。

**修订轮实际修复：** 玩家 HTML 仅保留非故事标题“便条”及原句“明早开馆后把封存箱交给周先生。”，删除解释；证明限度仍在 KP `clues[].meaning_and_limit`。重算 `playerPackages` 主件和 entries 的字节数/哈希，生成新 ZIP，在两个全新测试空间实际导入与往返。新脚本、包和证据均在 `T/round2/`，没有覆盖初轮。

| 最终产物 | SHA256 |
|---|---|
| `T/round2/candidate.zip` | `99637c3191baab4155112aaa5accd8314de24602ebc7747947e06809688342f5` |
| `T/round2/consumer-export.zip`（实际工作台生成并下载） | `8543cf5b4e3cbdb809a21dabddc29d64ab3bbc052ad1afde5e71ebd99a449811` |
| 修订玩家 `index.html` | `a3bcf65ac6f9effa6dee22aebdd2b6a590e109499377e9de804cc0026aa6b388` |
| 公开 SVG（主图及玩家副本相同） | `756c6748721ffa9ab198833101f944a05e01e9d1b3db5ae8c264935a8a2e624d` |

## API 资格与隔离证据

实际调用消费者的 `GET /api/health`、`POST /api/restore`（multipart `file`）、读回 content、files、sessions，调用 `POST /api/spaces/{id}/export?includeSessions=false`，实际下载返回地址，再 `POST /api/restore`。没有自写解析器替代消费者处理；Python 只制作候选、发 HTTP、比较真实响应与 SHA。

修订轮 29 个记录请求均成功，详见 `T/round2/evidence/api-trace.json` 和 `api-result.json`：

| 检查 | 实际结果 |
|---|---|
| 正式格式 | `keeper-backup` v2，根 content 本体、sessions `[]`、普通文件条目，无显式目录；消费者真实接受 |
| 修订轮首次导入空间 | `7bf7aa30-b242-477c-a366-73306a7d61c1` |
| 消费者导出后的重新导入空间 | `30c91511-e497-4a00-bc7d-933f7db85edc` |
| 正文比较 | 两次读回结构深比较一致；每章 HTML 字符串逐字相同，map 内联 SVG 同源 |
| 资源比较 | 主 SVG、玩家原件 HTML、玩家 SVG 副本、来源说明共 4 文件，在两个空间均由文件 API 实际取回并逐字节相同 |
| 导出包 | 实际下载 SHA 与导出 API 返回值相符；manifest 覆盖恰好等于普通文件集，逐文件哈希通过，正文一致，sessions `[]` |
| 消费者新增索引 | 导出多出 `files/player-packages.json`，为现有创建流程从 `playerPackages` 生成；明确记录，未误判为作者资源丢失或未知字段支持 |
| 纯剧本场次 | 两个修订空间均为零；没有用户实况、角色卡或私人便笺 |
| 旧测试空间隔离 | 初轮 `cf3f6ad0-5cd2-44f1-bb09-63094f5cb932`、`9dd024f5-c04a-4a5e-90d9-6ff831cd5819` 保留；修订轮前快照内容/场次，后复查不变；另将旧四资源的实际响应逐件比对初轮留存 SHA，8 次检查均一致 |

初轮 API 往返原本通过，但玩家原件含解释，故只保留其格式/往返与浏览器过程证据。初轮浏览需新建一个空白 `T17临时浏览核验` 场次；仅操作该测试场次，浏览器关闭后按当前 revision 删除；保存其测试 JSON 至 `T/evidence/temporary-ui-session.json`。随后实际 API 确认初轮两空间重新为空场次。修订轮未新建任何场次。最终保留四个互相隔离测试空间。

## 浏览器覆盖与边界

真实页面显示初轮同名两空间均为 0 场次；创建临时测试场次进入既有工作台，打开第5章看到完整对应段落；点击“查看便条”打开 CL01，显示载体原文与后台条件/限度。打开图集后见真实 SVG，以缩小按钮四次显示全图与图例，深色皮肤下图面保留浅色填充。点击 SVG 入口区热点打开 R01；聚焦实际 `g[data-room="R02"]` 后 Enter 打开 R02 主廊详情。搜索“明早开馆”返回第8章、CL01 和 H01。截图已实际查看，记录在 `T/evidence/browser-*.txt/png`。

初轮玩家件截图明确保留有解释的失败版本。**修订后**浏览器从新空间真实文件 API 再次打开玩家 HTML，截图及 DOM 仅有“便条”标题和完整原句，已实际查看：`T/round2/evidence/browser-player-note.txt/png`。修订轮 SVG 与初轮已浏览 SVG 字节同 SHA，且已从两个修订空间实际取回；玩家目录无后台条件/证明限度，地图仅公开地点/对象，无隐藏图层、秘密文字或外部资源依赖，见 `player-public-check.json`。

本次未验证：地图拖动/拖后误点、所有热点和完整关联链、全部跨章锚点、窄窗、独立打印/PDF、音视频播放、角色/骰子/参考时间轴工具、任意自定义字段展示、完整微项目所有 P8 文件、真人主持/游玩。最小示意图仍非正式图面质量验收（如家具标签与形状重叠）；不因有截图把这些未测项判通过。

## 交付与可复查入口

最终运行候选与实际消费者导出包：`T/round2/candidate.zip`、`T/round2/consumer-export.zip`；编辑源/实体和实际玩家文件在 `T/round2/candidate/`；测试驱动在 `T/round2/runtime-test.py`。核心证据 `T/round2/evidence/api-result.json`、`api-trace.json`、`export-manifest.json`、`prior-spaces.json`、`prior-resource-checks.json`、`player-public-check.json`、`owned-processes.json`、`processes-before-stop.json`、`shutdown.json`；源码和方法指纹在 `T/evidence/`。构建日志在 `T/runtime/logs/`，修订轮应用日志在 `T/round2/evidence/app.stdout.log`，MySQL 两轮日志在 `T/runtime/logs/mysql.log`。

所有运行测试均绑定上述包、消费者源码和本地隔离实例。方法文件的历史 `compatibility.json.scope` 保持“仅源码检查”的原记录，未改写历史资格；本报告新增本轮独立运行证据。
