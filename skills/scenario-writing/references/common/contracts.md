# 最小产物字段与短例

<a id="src-contracts-1"></a>
## 最小产物字段与短例

本页提供局部记录字段，不替代[阶段产物标准](deliverables.md)中的完整主文、人物卡和成品要求。完整人物卡的阶段归属与结构见[第2步叙事卡](deliverables.md#src-deliverables-135)、[第6步规则卡](deliverables.md#src-deliverables-257)、[第8步最终卡](deliverables.md#src-deliverables-312)；下方短例仅示范最小局部记录，不据此授整阶段资格。

职责：提供输出字段，具体含义由各领域参考维护。按当前任务选字段，可直接合入已有卡表。缺少资料时写“候选”或“待核”，不为填满表格编造事实；小任务只填写有关部分。

<a id="src-contracts-7"></a>
## 项目与阶段

项目约定分三组记录：

- 作品范围：媒介／类型、当前阶段、人数、时长或篇幅、体验与主题。
- 本轮交付：指定产物、固定与可变项、授权范围、验收安排。
- 互动前提：必要起始前提、局内选择从哪里开始。非互动任务可省略这组。

状态字段按[scope四轴](scope.md)分别记录材料角色、采纳状态、事实约束、验证记录／待核。验证记录带对象版本、方法、覆盖与结果。已采用的机制可以技术待核，已撤回的支线也可以保留旧版通过证据，两者都按原范围登记。小修只记受影响对象。

阶段交接要让接手者找到当前工作：先给主动版本、入口和最新决定，再列已完成与已验收的对象／范围、事件或资产ID、开放问题、下一步输入和变更影响。ID是稳定的查阅编号，名称变化时仍可追踪同一对象。若运行有并发要求，另列实际人手和注意力负担。

<a id="src-contracts-19"></a>
## 可玩角色两步交付

前置《角色耦合与介入方案》与P6《一致性配置与角色交付稿》的字段、结构和完成依据分别由[前置角色合同](deliverables.md#src-deliverables-89)和[P6角色合同](deliverables.md#src-deliverables-246)维护；实际方法见[角色设计](../../../scenario-narrative/references/player-design.md)。沿用原角色／人物标识，材料注明受众、时点、角色可用范围；不在此复制第二套模板。

<a id="src-contracts-23"></a>
## 故事与阶段稿

大纲用连续正文说明人物处境与目标、过去及当前的因果、冲突与转折、结果方向，再附主支线和开放项。

互动体验阶段：事件内容、人物行动、参与动力、探索地点与动作、交谈对象与所得、发现与推理、选择与后果、亮点。可写连贯段落而非八个僵硬栏目；粒度在整稿保持一致。

支线诊断先还原现有故事与来源位置，再填写：

- 为什么需要这条线：主要需求、发生阶段、现有缺口。
- 怎样进入整体：参与／接触方式、联系类别与目标、持续结果及回收。
- 怎样修改：建议、事实状态、删除后的损失，以及篇幅投入是否相称。

<a id="src-contracts-137"></a>
## 领域字段入口

<a id="src-contracts-140"></a>

<a id="src-contracts-142"></a>

<a id="src-contracts-143"></a>
## 按游戏配置与依赖需求记录

任务执行与字段选择依据见[流程的机制与配置任务](workflow.md#src-workflow-142)。配置只记录本游戏实际需要的对象、字段含义、单位／类型、默认值、依据、适用条件及版本；不要求所有系统填写同一套角色或战斗数值。

后续需求可合入既有问题表：发起位置与需求、依赖对象／版本、已有支持／缺口／冲突、责任步骤与理由、采用修改、影响范围、复核结果及返回位置。小修只填写相关项，具体循环由[流程](workflow.md#src-workflow-106)维护。

<a id="src-contracts-149"></a>
## 审核与变更

每项问题记录位置与版本、事实或引文，再说明缺陷、影响、级别、修法、复核标准及处理状态。分数可以附在诊断后，不能代替证据。

母版差异记录原位置与原事实、建议和理由、受影响资产、不采纳时的替代办法、授权／采纳状态及待核项目。旧资料的H/D/N/M与F/D/V/M各有语境，本包用中文状态记录，避免混用同字母的不同含义。

<a id="src-contracts-177"></a>
## P5空间、场景与资产记录

按[P5实施最小记录](../../../scenario-play/references/scene-construction.md#src-scene-construction-213)沿用空间、场景、线索、人物和事件标识；资产附用途、读者、状态／视角／精度、实际文件及版本，问题附责任阶段与复核范围。按实际规模合入主稿和附录，不另维护第二套事实。

## 统一交接的最小结构

这些是方法字段定义；实际取值在当前项目目录。沿用已有Markdown／表格即可，需要机器读取再用JSON；不为简单任务建数据库或全量空表。

|字段|约束|
|---|---|
|project_id、object_id、revision|项目、稳定对象与版本；人物／地点／线索跨专项共用ID|
|task、mode、deliverable|做什么、分析／制作／修订／审核、实际承诺|
|source_refs|实际输入位置／版本或指纹、采用状态；候选不当事实|
|fixed、editable、authority|固定项、可设计项和已有权限；范围不变不重复审批|
|audience、knowledge_refs|公开／主持／特定角色、时点；玩家、角色、NPC知道分别记录|
|rules|required system/version/custom terms or not applicable；未知列影响，不默认COC|
|required_conditions|当前任务必需的方法、工具、输入、资源；按条件求传递闭包|
|acceptance|与本轮承诺对应的产物及真实验证级别|
|open_items、impact_refs|缺口、影响对象／位置及下一责任|

返回实际产物入口、采用输入、版本／受众、主要变化、检查证据、未完成及影响。已有角色卡、地图和资产是数据输入，不要求先重跑作者skill。完整阶段由当前主入口按deliverables汇总，表格不替正文、图件或卡片。

领域字段：[人物与关系](../../../scenario-narrative/references/characters.md)、[任务／节点](../../../scenario-play/references/interactive.md)、[推理模板](../../../scenario-inference/references/templates.md)、[规则配置](../../../scenario-rules/references/rules-design.md)、[空间](../../../scenario-space/references/layout-design.md)、[媒体](../../../scenario-media/references/asset-briefs.md)。完整局部例见[柜子动作与原因](../../../scenario-play/references/contract-example.md)。

### 虚构交接例：便条手卡

已采用文字“明早开馆后把封存箱交给周先生。”只支持存在交付安排，不独自证明交付发生、箱中内容或有罪。推理确定原文与证明边界，多媒体可改版式／画风，不能添签名、血迹或时间戳。生成实际文件并核可读性后返回资源、源、版本、受众和许可；交付接入同版正文／玩家包。原文变更先更新采用源再重制，文件存在不等于玩家已看过。

```json
{
  "project_id": "example-archive",
  "object_id": "CL-NOTE-01",
  "revision": "example-r1",
  "mode": "制作",
  "task": "将采用便条制成玩家可读手卡",
  "source_refs": [{"path": "content/clues.md", "anchor": "CL-NOTE-01", "status": "adopted"}],
  "fixed": ["明早开馆后把封存箱交给周先生。"],
  "editable": ["不新增信息的版式、纸张与画风"],
  "audience": "players",
  "rules": {"status": "not_applicable_to_this_asset"},
  "deliverable": ["实际图片", "必要编辑源", "资源与检查记录"],
  "acceptance": ["逐字正确可读", "无后台解释", "实际资源齐全"],
  "open_items": []
}
```

这是方法示例，不是项目事实，也不表示已实际制作图片。
