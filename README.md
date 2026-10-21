![雾港与调查员：项目起源于COC开发实践](assets/readme/coc-hero.png)

# CocSWSkill · 通用剧本开发技能套件

把故事设想发展成可读、可选择、可执行和可维护的剧本。以一般叙事与互动游戏设计为基础，COC是目前有详细设计方法的规则适配之一。

本项目来自持续的COC开发、通用方法整理、文献转译和独立AI审修。人物、线索、地图、规则与交付常在多轮修改中互相影响，因此保留P0—P8依赖循环，并将独立任务组织为 **1个统筹入口＋9个专项skill**。使用者可以直接阅读，也可以让助手按目标调用；使用无需Python或开发脚本。

## 目标与适用范围

一般舞台／影视等叙事：人物因果、冲突、主题、结构、实际正文与相应呈现。互动作品：玩家可接触的信息、可做／可选、状态反馈、合作与成果。COC及其他规则作品：按实际系统配置角色、行动、数据和机制。无主持／无骰也明确决定权和结果；其他外部系统尚未完成的详细适配如实登记，不因通用接口存在就宣称全面支持。

推理、战斗、探索和交际按本作目的与规则调整重点、深度、描述和策略；保设计职责，不强造谜题、战斗数值或全部媒体。

## 十个入口

|你要做什么|skill|
|---|---|
|开始／继续项目、整阶段或跨域开发|[scenario-writing](skills/scenario-writing/SKILL.md)|
|故事、主支线、人物构建与展现、角色接入|[scenario-narrative](skills/scenario-narrative/SKILL.md)|
|游戏任务、行动选择、事件场景与战斗策略|[scenario-play](skills/scenario-play/SKILL.md)|
|推理目标、认识、线索证明、投放与赋能|[scenario-inference](skills/scenario-inference/SKILL.md)|
|空间玩法、真实布局、地图与公开图|[scenario-space](skills/scenario-space/SKILL.md)|
|所选规则、角色一致性与特殊机制配置|[scenario-rules](skills/scenario-rules/SKILL.md)|
|肖像、场景、手卡及所需音视频实际制作|[scenario-media](skills/scenario-media/SKILL.md)|
|独立估时、参与、节奏、疲劳及路线比较|[scenario-pacing](skills/scenario-pacing/SKILL.md)|
|完整成品、玩家材料、文件与已有载体交付|[scenario-production](skills/scenario-production/SKILL.md)|
|实际版本审核、迁移、独立模拟与复验|[scenario-review](skills/scenario-review/SKILL.md)|

“开发任务”归统筹，“游戏内任务”归游玩，“需要形成的判断”归推理。明确局部请求可直达专项，不先运行全流程，也不一次加载全部领域。共同合同只维护一份，实际项目事实与场次留在项目目录。

## 简要流程与循环

**P0大纲与角色耦合／介入 → P1代表体验 → P2逐线发展与叙事卡 → P3世界事实 → P4进程与信息 → P5场景与互动落实 → P6规则与角色配置 → P7验证修订 → P8完整成品。**

后续设计缺条件或发现冲突时，回责任阶段补足／实改，按影响同步复核后返回继续；不是一次完成的固定流水线。P5六项仍覆盖约束、空间组成、实际地图草稿、场景与线索、文字／材料及重要图片草稿、互动与跨区变化；P8依最新采用稿制作最终正文、卡片、完整使用说明和实际资源。

查看[完整工作流](skills/scenario-writing/references/common/workflow.md)与[阶段产物标准](skills/scenario-writing/references/common/deliverables.md)。

![调查桌上的笔记、地图与多面骰](assets/readme/investigator-desk.png)

## 方法特点

|特点|解决的问题|
|---|---|
|作品、玩法、题材、规则、阶段分别选择|COC不再是通用方法的顶层；按实际任务加载|
|从处境与用途构建判断|推理引起主动行动、指导行为、启发其他目标，紧迫感接真实用途|
|人物构建、展现与真实认识衔接|构成目录按叙述空间取舍，人物改变与受众后来知道分开|
|真实条件与成果持续|提前识破、救援、取消、拒绝及选择按实际世界回应|
|空间与媒体分工、成品统一整合|精确几何不靠氛围图决定，实际图文不由任务书替代|
|时间与疲劳独立检查|现实／世界／个人时间分开，缺证据不造精确总分|
|单一归属与版本证据|领域方法、阶段合同、项目事实、审核身份各有位置|

这些是经验和理论的融合方法，不宣称统一学术分类或真人效果已验证。评分使用0—100、允许小数、按依据细分；节奏分不代替整体质量与可行性。

## 使用与安装

克隆本仓库后，可以直接让助手读取所选SKILL，例如：

```text
读取 skills/scenario-narrative/SKILL.md，核人物行动依据与实际呈现，保留采用事实并修订正文。
读取 skills/scenario-rules/SKILL.md，为这份自订无骰互动稿完成P6，给默认处理与状态反馈。
读取 skills/scenario-pacing/SKILL.md，只估时并检查等待与疲劳，资料不足时用轻量模式。
```

个人安装将`skills/`内十个`scenario-*`目录同级复制到当前运行环境的技能目录，例如Codex的`~/.codex/skills/`。安装前保留同名旧版本；不要将一个专项孤立复制到不相容目录。原`coc-script-writing`只保兼容显式读取和旧链接，新的安装不需要它。新任务可用`$scenario-writing`或明确专项名称；是否实际自动发现以当前环境为准。

[suite.json](skills/suite.json)列版本、条件依赖和已设计的任务子集，不是自动安装程序。方法、外部工具执行、规则支持与消费者兼容分别确认。只要独立估时等子集时按当前任务求传递依赖闭包；不保证任意“底座＋一个专项”能完成所有扩展任务。

P8教学素材有本地参考副本，**公开许可待定，未随公开方法包附送**；使用方法不依赖这些例子。示例任务的可用条件与范围见[资源说明](skills/scenario-production/references/p8/examples.md)，不能把缺资源或提示词称实际资产。

## 授权：CC BY-NC-ND 4.0

<a href="https://github.com/28714026262/CocSWSkill/tree/main">CocSWSkill</a> © 2026 by <a href="https://github.com/28714026262">SuzeKip</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/">CC BY-NC-ND 4.0</a> <img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="Creative Commons" width="16" height="16"> <img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="署名" width="16" height="16"> <img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" alt="非商业性使用" width="16" height="16"> <img src="https://mirrors.creativecommons.org/presskit/icons/nd.svg" alt="禁止演绎" width="16" height="16">

本仓库有权授权的原创内容采用 **署名—非商业性使用—禁止演绎 4.0 国际许可**：允许非商业复制和分享原文，需按协议保留署名、来源及许可说明；允许非商业私下修改，不得分享改编版本，不授予商业使用权。

这意味着原文可以非商业转载，不再限定个人自用。第三方材料沿用各自权利；许可不垄断抽象方法，也不取得使用者独立创作产物的版权。完整适用范围与官方法律文本见[LICENSE.md](LICENSE.md)。

下载[官方简体中文法律文本PDF](coc-script-writing/output/pdf/LICENSE-CC-BY-NC-ND-4.0.zh-CN.pdf)，便于离线阅读与打印；仅作排版，不增加许可条件。


## 验证与维护

本轮拆分的来源、变更、独立验收及实际已测／未测范围集中于[audit/50-skill-suite](audit/50-skill-suite/README.md)。目录／格式检查、独立文本审阅和隔离实例使用，不等于平台自动发现、真实工作台导入、主持或真人桌测。原审计和素材记录保持原对象资格。

方法维护在十个领域目录与共同底座；原通用文档按来源和采用差异衔接，不双向盲目覆盖。开发脚本只在本地研究目录，不进入使用依赖。仓库名、原署名和CC许可保持。
