# 批次A：P8、教学资产与交付来源验收

2026-10-21。原P8／多媒体交付席独立核对，未参与基线建立或方案编写。结论：本席范围的批次A来源准备通过，可按已采用v0.3继续本地迁移；本报告列出的执行约束纳入后续E／F／G验收。此结论不表示新技能、资产复制或接入已经验收。

## 1. 实际对象与执行范围

实施目录：`D:/SZK/Personal/COC/echo/research/2026-10-21-skill拆分实施`。主要实际对象为其中`baseline/coc-script-writing/references/p8/`、`assets/p8-examples/`、`audit/49-p8-publication/`、基线根和旧skill两份LICENSE／README；对照实施台账及已采用v0.3的明确子项归属。

`01-实施输入基线.json`实际SHA256：`bfcfd4779c8bcfb4573c79ee33b43aa6c95be2d8d168f6bf145edd04b313e271`。该记录捕获旧工作区HEAD `23f59519be6eac536b1d0c9add6105e05440c155`及既有未提交变化，不把工作区内容误作已发布版本。

本席只读并写本报告，未改正式仓库、原始来源或基线；未暂存、提交、推送、生成媒体、安装、导入或改真实场次。检查包括文件存在／指纹、文本来源／许可、活动链接盘点和ZIP目录只读查看；没有重新解码、视觉检查或听审资产，也没有复跑原162／81项检查。

## 2. 来源事实

|对象|实际结果|迁移资格|
|---|---|---|
|正式P8参考|十个文件（九Markdown含入口＋compatibility JSON）与01记录逐件核SHA，0项不符|可作本轮方法迁移主输入；新活动页改写后另记新指纹及源→目标，不重写基线|
|教学范例|47文件，合计14,412,914字节；与01记录逐件核SHA，0项不符|可按授权本地复制；不表示取得公开分发许可|
|根LICENSE与旧skill LICENSE|二者同SHA `d1cfc5cfa243396e8a3cd25180487f0ba1f04954848c1106572a7ec13002c553`，均与01一致|保CC BY-NC-ND 4.0原文本、SuzeKip署名和已有适用说明，不另改许可|
|教学README及制作记录|明确公开许可待定，图像生成、矢量制作、合成雨声及历史修订可追溯|不因AI生成、自制或加入方法套件而变成可公开素材|
|范例release.zip|只读列出16个普通文件成员，无显式目录成员；内含`sessions.json=[]`和keeper-backup v2清单|只是既有格式教学对象；未导入消费者。它含素材，不能绕过素材发布边界|
|现有Git状态|只读`git ls-files`在旧`assets/p8-examples`下无追踪条目；`git diff --cached --stat`为空，工作区仍有基线记录的既有未提交内容|旧本地文件存在不等于已提交／已公开；后续不能用笼统全量add将其带出|

原LICENSE与README给仓库原创内容既有许可；旧skill README和范例入口对本次教学素材另留公开许可待定例外。实施采用的是用户授权的本地整合，不因该例外停止方法编写或重复索取本地确认；发布范围仍按素材的专属状态处理。

历史资格继续是：样例不是完整可开团剧本；未实际导入工作台、未完整可玩／历史认证、无真人桌测。雨声仅解码和静音播放时钟推进，未实际听审。旧verification／render JSON的原状态、payload、ZIP、作者源和指纹保原对象，复制／改链不补授新资格。

## 3. 本地迁移与公开包的执行要求

1. 将基线47件按原相对结构、原字节复制到`skills/scenario-production/assets/p8-examples/`，逐件与01核对；保旧资产及audit原字节。不批量替换资源JSON、ZIP、SVG或历史验证中的路径、日期、许可或pending字样。需要描述当前迁移时另写当前索引／说明，记录新旧位置和原指纹。
2. 本地方法、资产和公开候选分别登记。待定资源不能因“用户已授权推送”或“整个套件”被自动纳入公开候选；检查旧、新两处目录及任何另存ZIP、截图、data URI、嵌入图片／音频的衍生文件。`release.zip`与原PNG／WAV适用相同边界。
3. 在暂存前采用明确文件清单，暂存后实际查看`git diff --cached --name-only`及待定路径的`git ls-files --stage`，确认公开候选未带上述素材；若用忽略／本地排除规则，仍以索引实际结果核验，不能只看规则文本。本报告不要求删除原文件、移除历史或重写Git历史。
4. 公开方法包若不附素材，入口明确“教学素材未随包、许可待定”，区分方法仍可用的任务及需要本地资源的示例任务；不保留宣称可直接打开而实际缺失的活动链接。可保来源／限制文字与条件索引，不能把提示词或缺文件目录称完整教学资源。获准本地组合应实际提供被选用资源并闭合引用。
5. 保根许可证及署名；复制安装时也须能查到同一许可与专属例外，可在每skill放原字节LICENSE并在README说明资产例外，或提供经安装闭包验证的本地可读许可位置。不能让安装目录只有仓库外LICENSE链接；也不将套件维护授权解释为改变第三方权利或给待定素材重新许可。

## 4. 复制后的活动链接修订清单

这些是新活动方法要修的引用，不是修改旧audit／payload的命令。路径示例按实际目标文件所在目录计算，实施后须核文件和锚点。

|当前链接／区域|新活动位置的处理|
|---|---|
|P8 README、content中`../deliverables.md`的S8／character-final|从`scenario-production/references/p8/`指向`../../../scenario-writing/references/common/deliverables.md`相应锚点；保实际合同标题／稳定锚点|
|P8 README／maps-media中`../spatial-design.md`|指向`../../../scenario-space/references/spatial-design.md`；制图详细方法再指空间实际map-construction／QA，旧maps-media保任务导航|
|P8 README中`../review.md`与production-qa第4—5节|指向`../../../scenario-review/references/review.md`及实际production-verification；成品页保执行入口和必须完成结果，修本页目录与旧锚点|
|content的`../narrative.md`、`../craft.md`|依内容指向新narrative的模型／构建／展现／craft唯一方法；第10节方法迁craft，制作页保达标检查与精确引用，不沿用不存在的旧兄弟页|
|content的`../inference-design.md`|指新inference相关定义／材料／证明方法或薄入口，保证明边界，不将整理论复制进content|
|P8内部同名链接|delivery、content、integration、workbench、compatibility等同目录链接可保，但maps-media变薄导航、QA拆出后要核每个锚点和加载入口；project-template的地图和审核引用随之改|
|P8到教学资源的`../../assets/p8-examples/...`|production保同样references/p8与assets层级时仍成立；空间／媒体新参考若需用例，改为`../../scenario-production/assets/p8-examples/...`，并把合法资源承载纳入条件依赖|
|教学范例内部相对链接|47件整树原样复制，maps／waystation互链、files、HTML同目录图片及ZIP保持原对象；不为新目录重写运行资源根|
|README的`../../audit/49-p8-publication/...`|不能在production安装内继续承诺该不存在目录。当前方法指向随底座提供的出处摘要／当前导航，完整历史在旧仓库位置以路径＋指纹可查；不批量改旧报告|
|旧入口、仓库README、协作表与架构入口|改为实际十skill任务路由和薄兼容说明，保许可例外和真实部署状态；旧目录可导航新入口，不保第二套活动领域正文|

integration文中的`read.html?chapter=...`、`data-action`、`sources/original.md`和JSON内`files/`相对根是消费者合同／示例语法，不能被普通Markdown文件存在检查误判后自动改名。安装引用、作者资源路径、内容资源根、ZIP成员根和独立玩家HTML路径分别核；尤其不能把独立手卡HTML原样塞入章节后假定其相对图片仍可用。

## 5. 地图消费者子项的唯一落点

落实已采用v0.3的明确覆盖规则：maps-media第2.4当前消费映射／说明、第5.1工作台内联SVG和下载件一致要求、第5.2完整当前绑定、第8.1工作台／承诺交互的绑定及操作，统一整合至`scenario-production/references/p8/integration.md`，与已有同义项合并。空间保格式中立作者源、几何、同源视图、图面／公开检查和定向引用。

保原实际限制：内联`maps[].svg`与文件path各负其责，图集ID／地点对应，热点依`data-room`，键盘和拖动实际操作资格不能从字段存在推出。纯静态件不增加工作台点击门槛。`compatibility.json`的消费者HEAD及八文件指纹不因移动而改成当前实测；规则数据正确、内容能导入、工具能计算、界面实际可用分别记录。

后续E／F至少核：P5图文和媒体草稿仍集成实际产物；P8保连续正文、七职责／可选十部分／消费章号分层、完整手册独立入口和参考游玩；玩家包白名单／字节净化、单件依赖闭包，纯剧本无真实场次。若实际任务只承诺文件，按文件核；本次技能迁移不触发工作台服务测试。G再核当前源→目标、原资产字节及公开候选清单，不能用本A报告代替未来文件验收。

## 6. 批次A结论

输入存在、指纹吻合，方法／资源／历史与许可边界可定位；本席未发现阻止已授权本地迁移的来源缺口。批次A本席通过。以上是可执行迁移与发布约束，不是重复审批请求，也不表示相应动作已完成。实际E成果与G终验仍由原席读取新文件，按实际问题修复复验。
