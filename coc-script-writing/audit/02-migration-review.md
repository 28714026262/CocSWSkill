# 阶段 B 独立迁移验收

日期：2026-10-07。验收员：独立代理 `migration_acceptance`。未参与方法编写，只写本报告；未修改来源、参考正文或映射。

**裁定：阻断，阶段 B 尚未通过。** 十份参考已保留主要方法，未发现项目配额泛化或来源变更；但逐章迁移登记及部分MEM主归属与实际正文不符。135章登记齐全不能抵消错误落位。须先修复下面的问题、重新核映射及对象指纹，再进入阶段 C。本报告不把未来 SKILL.md／校验脚本尚未创建列为阶段 B 缺陷。

## 实际读取与检查

全文读取九份 design-guides 文件，包含备忘录全部历史段落、讨论稿及学习方案；全文读取十份 references、ARCHITECTURE.md、01-architecture-review.md、source-map.md。长文件分批读：正式流程分两批，调查框架分三批，学习方案分两批，备忘录分两批，source-map分两批；未用标题代替正文。source-manifest.json 全部字段通过解析后逐章展开读取，避免序列化深度不足掩盖targets。

程序独立核验：目录九来源与清单相符，九个实际SHA256全部匹配；实际Markdown标题与清单的标题及行号逐项比较，135项、差集为空。程序检查只证明登记与指纹，以下语义裁定来自实际全文对照。

## 已成立部分

- 前置＋八阶段、玩家体验上限与最大成功的区别、逐线强化、世界痕迹生命周期、两分册后合成、联合施工样段、后期KP手册、分规格验证均实质迁入workflow，未把讨论稿待确认口径留下为另一套现行规则。
- interactive保留参与前提与局内选择、五部分人物及空间分型、听到／相信／确认区别、实际消息延迟、在屏离屏一致、合作真实损失、节点七属性及错过入口／取消条件区别、依赖补救和错时起算；contracts提供对应字段。
- investigation实际维护七类联系、同源转述、有限证明、真正否定、最低充分集、认知阶段与累计／跨线组合。源框架“档案只能钉死已提出理论”等旧绝对措辞按使用前校准处理；固定三路径、误区数、文件钉子数未变成通用配额。
- narrative与craft保留研究提案的独有内容：删除四维、重要性／复杂度／展示量分别控制、十种影响机制、强弱边、并置意义、主线反向压力、揭晓后余波；未声称单一学派原话或跨项目实测。
- 项目名单、年代、两主四支、行政动作禁令、9分／9.5分和候选数量未进入通用默认。scope注明L1／数字L2属于编辑性转译；review区分AI文本审读、模拟、非作者KP与真人桌测。
- 备忘录50项均有相关正文或合理合并位置；下述问题主要是登记失真与局部边界需更明确，并非50项整体遗漏。

## B-01：逐章targets错误，须同时修source-map与manifest

严重度：阶段 B 阻断。现登记声称“映射同时标出主归属及必要关联文件”，但以下源章不能在指定文件找到定义或足够内容。例如支线能力第49行A1—A4全部指maintenance，而四类真正的操作定义在investigation的“七类推理／行动联系”；框架第262行“最低充分集”也指maintenance，实际定义在investigation“线索作用与最低充分集”。作者知道正文放在哪里不能替代真实追溯。

下表逐项列出需要修正或补足的登记。目标写文件及实际节名；可使用标题锚点或独立target_heading字段，不能只改为另一个模糊兜底文件。主归属与必要关联允许并列，不要求复制正文。

| 来源与行 | 当前问题 | 可执行修复／真实落位 |
|---|---|---|
| 学习方案:146 M6 | interactive没有背景特色定义 | 主归属coc“背景特色与知识入口”，关联contracts“场景／事件节点” |
| 学习方案:212 合并产物与施工顺序 | maintenance不能表达三类材料建立时点 | 保留历史追溯，关联workflow第2—6步及contracts；说明旧表已由新流程字段合并 |
| 学习方案:224 测试补充 | 八种接口测试实际不在maintenance | review“定点测试”“验证资格”，保留历史追溯状态 |
| 多线方案:7 这次补什么 | maintenance未保存此节空间叙事、嵌套、并置与真正否定方法 | narrative“重量与删除测试”“多线交织模型”，craft“定向研究与转译”，investigation“证明责任与否定”，coc空间背景；研究来源保持追溯 |
| 多线方案:42 交织单元 | 八字段连接卡实际在contracts，现未指它 | contracts“因果与跨线”，关联investigation“由联系到游玩” |
| 支线回收规范:5 依据与适用边界 | maintenance只含一般溯源原则，没有本节转译内容 | craft“定向研究与转译”，scope“方法状态”，interactive状态／玩家选择；来源归属作为追溯记录 |
| 支线回收规范:15 先辨别是什么 | maintenance没有四材料定义 | narrative“需求先行与材料角色” |
| 支线回收规范:38 接口链 | narrative只概述需求，完整链字段在别处 | contracts“因果与跨线”、investigation“由联系到游玩”，关联narrative |
| 支线能力:7 使用范围与输入 | maintenance只覆盖恢复材料，缺任务触发及输入 | scope“任务模式”“项目最小约定”，关联maintenance“恢复工作与协作” |
| 支线能力:35 七类关系 | narrative仅转引，唯一完整定义未列入 | investigation“七类推理／行动联系”，narrative可留关联 |
| 支线能力:49 行动侧 | maintenance无A1—A4 | investigation“七类推理／行动联系” |
| 支线能力:60 联系落实为游玩 | maintenance无五段关系链及三情形检查 | investigation“由联系到游玩”，interactive“统一事件节点”“合作与玩家作用”，contracts“因果与跨线” |
| 支线能力:72 可玩性与叙事回收 | maintenance无逐线／全局检查完整内容 | review“定点测试”，investigation“由联系到游玩”，narrative“重量与删除测试”，interactive“游戏循环、状态与结局” |
| 支线能力:111 干衣短例 | 原例已被综合，现标合并但无该例落位 | 注明“例子不逐字复制，R1/A1/A2/A4分类及真实分配结果合并至investigation七类／interactive成果”；新柜子例不冒称原例 |
| 调查框架:24 先确定玩家体验 | maintenance没有五个立项问题及体验概念 | workflow“前置”“第1步”，scope“项目最小约定”；封闭、代价限定按适用条件转译 |
| 调查框架:160 玩家主体性 | maintenance没有调查行为与终局方向定义 | investigation“由联系到游玩”，interactive“合作与玩家作用”“游戏循环、状态与结局” |
| 调查框架:168 机制简洁度 | maintenance仅维护联查，不维护此原则 | coc“异常与恐怖”“人数、战斗、伤势与SAN接口”，review“十二项评价框架” |
| 调查框架:176 节奏与负担 | maintenance无急缓／静水与前景负担 | craft“冲突、反转与节奏”，interactive“游戏循环、状态与结局”，coc“人数…” |
| 调查框架:184 结局代价余韵 | maintenance无终局伦理 | narrative“揭晓与结尾”，interactive“游戏循环、状态与结局”，review结局维度；明确旧收费完美结局口径条件化 |
| 调查框架:192 KP与扩展性 | maintenance未提供场景可主持规格 | contracts“场景／事件节点”，coc“KP使用手册”“成品资产与规格”，review“阶段校准” |
| 调查框架:206 第一总共同危机 | maintenance无结构模型 | narrative“结构模型：总—分—总—分”；封闭求生限定题材 |
| 调查框架:262 最低充分集 | maintenance无该方法 | investigation“线索作用与最低充分集”，contracts“世界事实与推理” |
| 调查框架:337 玩家自由与结局伦理 | maintenance无四终局检查或道德边界 | interactive“游戏循环、状态与结局”，narrative“揭晓与结尾”；固定四类改可选方向注明 |
| 调查框架:383 席位 | maintenance无多席职责 | review“先确定审核对象” |
| 调查框架:390 问题等级 | maintenance无问题严重性及阶段闸门 | review“先确定审核对象”“验证资格”；说明P0/P1/P2转为语义级别与当前承诺 |
| 备忘录:122 已归属的内容 | maintenance不承载表中三组实质方法 | narrative材料及揭晓，review阶段，investigation证明／七类；maintenance仅保留状态追溯 |
| 备忘录:173 已整理支线能力 | 七类定义落位未列 | investigation“七类…”，scope“方法状态”，maintenance保留资格追溯 |
| 备忘录:177 行政禁令 | “合并至maintenance”既未明确配置隔离，也未定位通用体验判断 | 混合处置：具体禁令配置隔离，scope“方法状态”；通用部分关联investigation“由联系到游玩”、narrative需求与作用，并注明抽取的是行为用途检查 |
| 备忘录:186 从人物因果进入场景 | 九条横跨五域，单指interactive不完整 | narrative人物／证据认定、maintenance年代与事实、interactive离屏、coc战斗与尾声、review旧评分；逐细项可用MEM-28—35连回 |
| 备忘录:198 人物修订补记 | 备选成本与反应窗口实际interactive遗漏目标 | 补interactive“关键机制依赖与时钟”，其余四目标保留 |
| 备忘录:224 多线研究补记 | 真正否定实际investigation未登记 | 补investigation“证明责任与否定”，关联interactive成果与review检查；narrative／craft可留 |

复验标准：对135项逐条以正文确认主归属和关联，source-map与manifest同步；历史／配置处置写明通用部分到哪里、何种旧内容不成为有效规则。上表不是要求只修这些后即称通过，需人工检查整张表并提交实改对象。

## B-02：MEM主归属和细边界

严重度：登记问题并入B-01阻断。MEM表标题“唯一主归属”要求目标实际承载条款，不能把一个混合条目整包指向部分领域。

| ID | 实际检查及修复 |
|---|---|
| MEM-11 阶段评分与证明范围 | review只有阶段评分，证明范围主定义在investigation。拆细项或明确两个职责，不能宣称review承载证明范围。 |
| MEM-12 需求先行与七类关系 | 七类在investigation，需求先行在narrative。拆分或写主定义／关联。 |
| MEM-14 推荐先行与实质候选 | 推荐在maintenance，实质不同因果候选与比较在craft七步循环，补关联。 |
| MEM-23 个人偏好与项目隔离 | scope承载项目配置声明，推荐先行“这是本用户偏好”在maintenance，补此实际位置。 |
| MEM-27 既有成品可降素材 | narrative未说成品降素材；craft七步循环明确失败稿退素材，workflow前置也含淘汰。主归属改craft。 |
| MEM-33 目标战斗与提前取消压力 | 目标战斗在coc，取消对应威胁的通用定义在interactive，补关联。 |
| MEM-39 既有备选机会成本预警 | interactive有新补救依既有能力、付成本留痕、无无限替换，但未明说“已配置的多个备选须事前存在，各有理由、机会、成本和预警”。建议补一句区分事前备选与按既有条件推导的新补救，避免把前者也写成成功后任意补计划；新增计划仍可按最新M7推导，不要求穷尽。修后复核。 |
| MEM-47 删除四维与确认事实护栏 | 删除四维在review，固定事实变更护栏在maintenance，补关联。 |
| MEM-48 共享劳动、重估、反向压力 | 重估／反向压力在narrative，动作承载多个目标在craft“媒介表达”，补关联。 |

其他MEM项已找到对应正文，未要求重写已成立方法。若维持“唯一主归属”表，宜每行只登记一个经验单元，关联列单列；不增加第二套定义。

## 对象指纹

本次裁定绑定以下实际内容；修订后必须记录新对象并复核，旧报告不自动继承。

| 对象 | SHA256 |
|---|---|
| references/coc.md | `CD046E8D5C0D60E5FB30420AEA51B54A6FE64AD4940C0A0629D3C61E21A5AC31` |
| references/contracts.md | `A413335755FA3067F6ABC25E0CAD0A4021D84F9E7B832E8D3F84C5B5BEF675D7` |
| references/craft.md | `FD8EF4D3ED748110ACD5B725BD865B8B0F297820C3B381BB0B8974F7C36D27FD` |
| references/interactive.md | `5A279F9A7D8B7A4E8CCF5064F1E4E472367CC2F33E9C1A0B5D44952BD8C44CBF` |
| references/investigation.md | `43E802467FEFC60B162CAF51118A5B579C75A5C1B6AF8C511D5F7EE0AA072883` |
| references/maintenance.md | `F8A8621ED1D5AFC501323070599AA5F35FF47BA49CE9C00FDC0475C28C504CDD` |
| references/narrative.md | `624044B00FD776517B74527B732E2B78AB41E32E67325F3F9A078EC3FE10BF93` |
| references/review.md | `6EAFADB13D71609F3607143D0C7110DCCB856FD146D4A9B8B4B0CDEC30AC5A86` |
| references/scope.md | `ECEF7A8C7D8F7A7A94B840388B93BC95361057CB733E1DB886472A273861E004` |
| references/workflow.md | `1CC126E27FAE3E8A120C9B7E582C6FF6E47D0A74E74E210E4AE90060084E4B84` |
| audit/source-map.md | `31351D4E8F47B5E76CB0EC15043E2DF44AE7A538622D8180780C43CFD19F0545` |
| audit/source-manifest.json | `A94BD35F586AAC05C5EEE0A2CF307C3A89C42F1525DDD74A80A854E48CA91F3E` |

九来源指纹以该manifest为绑定：本验收再次核实际九源全部一致。这里只裁定本轮语义迁移与审计质量，不授予原方法跨项目资格、不验收具体作品、不声称技能行为或真人运行通过。

## 修复后复验（2026-10-07）

**最新裁定：通过阶段 B，可以进入阶段 C 技能封装与行为验收。** 前文阻断及初审指纹作为历史证据保留；本次通过只对应以下新对象。B-01、B-02已实改并复核，无新阻断问题。

复验员仍为独立代理 `migration_acceptance`，未参与修复正文和映射。实际复验范围：分三批全文读取新版source-map，逐项检查全部135章及50项MEM；全文读取新版interactive；解析manifest全部字段并对135项targets、target_sections、disposition及notes与source-map逐行核对。其余九份参考实际SHA与初审相同，沿用本验收员初审的全文读取和语义对照，不声称本轮重新全文读过九个未变文件。九来源再次核SHA及全部标题行号，135章无差集，来源指纹仍全部不变。

### 修复证据及关闭依据

| 问题 | 已核实的实改 | 裁定 |
|---|---|---|
| B-01错误兜底映射 | source-map现列实际节名，manifest新增target_sections；全部135章共329个具体目标节，目标文件及标题均真实存在。逐行比较标题、处置、说明、目标顺序与去重targets均无差异。章节目标已按正文职责分配，未见原来将方法导向无定义maintenance的问题。 | 关闭 |
| 支线能力行动与游玩联系 | 第49行现指investigation“七类推理／行动联系”；第60行指“由联系到游玩”、interactive节点／合作与contracts连接字段；第72行指review定点测试及叙事、游玩与成果相关节。实际定义与初审已读正文对应。 | 关闭 |
| 调查框架最低充分集及多域条目 | 第262行现指investigation“线索作用与最低充分集”及contracts“世界事实与推理”；节奏、结局、主体性、KP、席位与问题等级各指实际职责。第184／337／390行补适配说明，不保留旧收费结局、固定四类或脱离阶段的问题等级门槛。 | 关闭 |
| 学习方案与研究提案 | M6现指coc背景与contracts场景；第212行具体列workflow第2—6步及字段，第224行指review定点测试／验证资格。多线第7行分别记录空间、编织、真正否定等方法；第42行指连接字段及游玩链。支线回收的材料角色与接口链也修正。 | 关闭 |
| 原例与历史／配置 | 干衣例notes明确不逐字复制，保存R1/A1/A2/A4及实际分配成果，不把柜子新例伪称源例。备忘录第177行改“配置隔离+合并”：D-9行政禁令留配置，通用部分抽取行为用途与实际体验。讨论稿保持历史状态，正式流程没有回退到待确认口径。 | 关闭 |
| B-02混合MEM归属 | MEM表改“主归属及必要关联”。MEM-11/12/14/23/27/33/47/48均已指实际承载文件：例如27主归属craft，11分别指review和investigation，47分别指review和maintenance。其他42项与初审实质落位一致。 | 关闭 |
| MEM-39备选边界 | interactive“关键机制依赖与时钟”新增“若设计已配置多个备选，每个须事前成立，并分别说明理由、机会、成本和预警；保护一人真实取消对应伤害”，并明确事前备选与依据已有条件临场推导的新补救分开，后者仍需能力、时间、资源依据且不得无条件追加后手。既补足旧经验，又保持最新M7允许合理新补救的边界。 | 关闭 |

全135项语义检查以对应源章内容与此前已读目标正文为依据，而非只验证节标题存在。层级标题的概述性映射和历史追溯目标可指现行综合节，不要求把旧段落逐字复印。不同职责并列只是追溯关系，未造成运行定义多头维护。

### 本次通过对象指纹

| 对象 | SHA256 |
|---|---|
| references/coc.md | `CD046E8D5C0D60E5FB30420AEA51B54A6FE64AD4940C0A0629D3C61E21A5AC31` |
| references/contracts.md | `A413335755FA3067F6ABC25E0CAD0A4021D84F9E7B832E8D3F84C5B5BEF675D7` |
| references/craft.md | `FD8EF4D3ED748110ACD5B725BD865B8B0F297820C3B381BB0B8974F7C36D27FD` |
| references/interactive.md | `73937D941B84A08981319E7F7789EA73E48669DEE908BDE8776FEE73B3863FE8` |
| references/investigation.md | `43E802467FEFC60B162CAF51118A5B579C75A5C1B6AF8C511D5F7EE0AA072883` |
| references/maintenance.md | `F8A8621ED1D5AFC501323070599AA5F35FF47BA49CE9C00FDC0475C28C504CDD` |
| references/narrative.md | `624044B00FD776517B74527B732E2B78AB41E32E67325F3F9A078EC3FE10BF93` |
| references/review.md | `6EAFADB13D71609F3607143D0C7110DCCB856FD146D4A9B8B4B0CDEC30AC5A86` |
| references/scope.md | `ECEF7A8C7D8F7A7A94B840388B93BC95361057CB733E1DB886472A273861E004` |
| references/workflow.md | `1CC126E27FAE3E8A120C9B7E582C6FF6E47D0A74E74E210E4AE90060084E4B84` |
| audit/source-map.md | `5976BE81813625AD00A9F66D99738A30E36904665BFD53838E31A59CA1600760` |
| audit/source-manifest.json | `BD8770EB77E1AECDBB72F5E74B2C26B3D9372B5EF5E35928E7F633B74551A29E` |

本次通过证明九来源重要经验已得到可执行的迁移、适配或合理隔离，且审计可真实定位。阶段C入口、链接／结构脚本、行为输出及后续实改仍需独立验收；没有将语义迁移通过扩大为技能行为稳定、具体作品通过或真人测试认证。
