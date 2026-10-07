---
name: "coc-script-writing"
description: "Use when drafting, revising, planning, or reviewing Chinese Call of Cthulhu scenarios, investigative tabletop adventures, interactive game narratives, or general stage/screen story outlines; also use when organizing their development workflow, principles, writing craft, or continuity. Not for standalone dice or rules lookup, novel style imitation, or game engine implementation."
---

# 剧本撰写与开发

先读[范围与任务](references/scope.md)，恢复已有约定，确认媒介、任务、阶段、固定内容、指定产物及验收安排。一般剧本使用叙事与表达；互动游戏增加选择、条件与状态；COC按任务增加调查、异常和主持。未明确事项标为假设／待核，集中询问决定性缺口，其余在授权范围继续。

## 按任务加载

| 当前工作 | 读取 |
|---|---|
| 故事、人物因果、支线用途、主题与交织 | [叙事](references/narrative.md)；互动动作联系按需加[七类局部节](references/investigation.md#seven-links) |
| 参与前提、人物响应、合作、节点、依赖和成果 | [互动](references/interactive.md) |
| 证据、推论、认知、信息释放及七类联系 | [调查](references/investigation.md) |
| 异常、恐怖、系统接口、KP手册和成品 | [COC](references/coc.md) |
| 整阶段或整轮开发 | [流程](references/workflow.md)，随后逐阶段加载相关领域 |
| 大纲、场景、重写、可读性、候选发展 | [技巧](references/craft.md)及当前领域 |
| 填写必要卡表或最小交付 | [字段与例子](references/contracts.md) |
| 评审、返修、测试和收束 | [验收](references/review.md)及被审领域 |
| 改既定内容、交接或更新技能 | [维护](references/maintenance.md) |
| 联用文学研究、编辑、专项审核、主持或资产工具 | [技能协同](references/skill-integration.md)，只选与实际请求相符的分支 |

只加载当前任务需要的参考；目标与最小加载由scope维护。一般非互动作品不加玩家分支、SAN或KP手册；数字互动交付条件／状态接口，实际引擎测试另记；非调查COC不强造推理章程。整轮开发先按workflow媒介适配替换阶段产物与完成门槛。

## 贯穿的边界

- 先核既有事件、行为与处境，补因果缺口，再发展心理和新情节。按scope分别记材料角色、采纳、事实约束与验证记录；跨线素材不自动成为历史。
- 人物按实际知情、目标、关系与能力行动。证据标来源和证明范围；听到、相信、确认分别处理，检定失败不能证明不存在。
- 故事需求先于数量与功能标签；人物目标独立成立。既有项目人数、年代、禁令、评分和候选数量不作为通用配额。
- 互动尊重实际条件及选择，保留已取得知识、救援、取消和延迟成果。错过入口可找合法入口，成立条件取消不能补演；补救有依据、时间、成本和反馈。
- 按当前阶段与承诺评价，核心可行性风险及时核；未施工细节不整体否决大纲。固定事实调整列差异与影响，按已有授权执行。
- 用户要求写或修，就实写正文；先连续可读，再用表辅助核查。分析交付诊断与建议，候选未采用时不改母版。

## 完成与验证

依流程确定输入、实际工作、产物及完成依据。独立验收按用户约定逐步执行：验收员未参与该步编写，读实际稿，写证据；未通过先实改复验再进入下一步。没有实际独立验收时如实记录，不模拟多人通过。

交付说明完成对象、当前状态、主要变化与必要开放项。旧分只归旧稿；当前稿复核、AI模拟、非作者KP运行和真人桌测分别登记。达本轮标准后收束，不能抬分包装失败，也不无限加料。

本技能可独立复制使用。建设架构在[ARCHITECTURE.md](ARCHITECTURE.md)；来源与分步资格在[audit/acceptance.md](audit/acceptance.md)，仅维护或审核技能时读取。结构／链接检查运行 `python scripts/validate_package.py`；核原目录变化追加 `--check-sources`，独立部署时追加 `--source-root <原目录>`。具体规则、医疗工程及外部事实按实际任务核可信来源，参考正文不代替规则书。
