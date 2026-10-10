---
name: "coc-script-writing"
description: "Use when drafting, revising, planning, or reviewing Chinese Call of Cthulhu scenarios, investigative tabletop adventures, interactive game narratives, or general stage/screen story outlines; also use when organizing their development workflow, principles, writing craft, play-time/pacing/fatigue evaluation, thematic clue presentation, or continuity. Not for standalone dice or rules lookup, novel style imitation, or game engine implementation."
---

# 剧本撰写与开发

先读[范围与任务](references/scope.md)，从已有材料和最新用户决定中确认五件事：写哪种作品、当前做什么、哪些事实固定、交付什么、怎样验收。

一般剧本使用叙事与表达方法；互动游戏增加选择、条件和状态；COC按任务增加调查、异常和主持材料。决定性信息缺失时集中询问，其余事项标明假设或待核，并在授权范围内继续。

## 按任务加载

| 当前工作 | 读取 |
|---|---|
| 故事、人物因果、支线用途、主题与交织 | [叙事](references/narrative.md)；互动动作联系按需加[七类局部节](references/investigation.md#seven-links) |
| 参与前提、人物响应、合作、节点、依赖和成果 | [互动](references/interactive.md) |
| 证据总览、七类推理／行动联系 | [调查](references/investigation.md) |
| 推理目标、认知阶段、线索分布、推理体验或P4填充 | [推理设计](references/inference-design.md)；整阶段再加[流程](references/workflow.md)和[互动](references/interactive.md) |
| 游玩估时、节奏、疲劳、版本比较或复盘 | [时间与节奏](references/play-evaluation.md)，先读第18节合同，粗稿用第14节A—D |
| 题材主题及线索／痕迹的呈现 | [主题呈现](references/theme-presentation.md)及当前领域 |
| 异常、恐怖、系统接口、KP手册和成品 | [COC](references/coc.md) |
| 整阶段或整轮开发 | [流程](references/workflow.md)，随后逐阶段加载相关领域 |
| 大纲、场景、重写、可读性、候选发展 | [技巧](references/craft.md)及当前领域 |
| 填写必要卡表或最小交付 | [字段与例子](references/contracts.md) |
| 评审、返修、测试和收束 | [验收](references/review.md)及被审领域 |
| 改既定内容、交接或更新技能 | [维护](references/maintenance.md) |
| 联用文学研究、编辑、专项审核、主持或资产工具 | [技能协同](references/skill-integration.md)，只选与实际请求相符的分支 |

只读取当前任务需要的参考。[范围与任务](references/scope.md#目标与最小加载)说明从哪里开始；[流程](references/workflow.md#媒介与任务适配)说明不同媒介应交付什么。数字互动的文案与状态接口、实际引擎运行是不同的验证对象；COC中的公开救援等非调查任务使用事件进程即可。

## 贯穿的边界

- 先核已有事件、行为和处境，补齐因果，再发展心理和新情节。材料的用途、采纳状态、事实约束与验证记录分别登记，见[范围与任务](references/scope.md#项目最小约定)。
- 人物按实际知情、目标、关系和能力行动。证据注明来源及证明范围；听到、相信、确认分别处理，检定失败不能证明不存在。
- 按故事需求决定人数、结构和候选数量，让人物目标独立成立。旧项目的数量、年代、禁令与评分留在项目配置中。
- 玩家行动改变条件后，兑现取得的知识、救援、取消和延迟成果。错过入口时可设计合理替代入口；事件条件已取消时按新局势推进。补救说明依据、时间、成本和反馈。
- 按本轮阶段和交付承诺评价，及时核验影响核心因果的可行性风险。调整固定事实时列出差异与影响，按已有授权执行；尚未施工的细节列为后续工作。
- 写作或修订任务交付实际正文，先保证连续可读，再用表辅助检查。分析任务交付诊断与建议；尚未采用的候选单独保存。

## 完成与验证

依[流程](references/workflow.md)确定输入、工作、产物和完成依据。用户约定独立验收时，由未参与该步编写的人或代理读取实际稿并记录证据；问题实改、复验通过后再进入下一步。按实际执行情况登记验收身份与范围。

交付说明当前对象、完成状态、主要变化和必要开放项。旧评分只归旧稿；当前文本复核、AI模拟、非作者KP运行和真人桌测分别登记。达到本轮标准后收束，尚未解决的问题如实保留。

本技能可独立复制使用，无需运行脚本。维护技能时再读[架构](ARCHITECTURE.md)、[当前验收台账](audit/acceptance.md)及[审计导航](audit/README.md)。具体规则、医疗工程与外部事实按实际任务核验可信来源。
