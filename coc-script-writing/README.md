# COC剧本撰写技能

`coc-script-writing` 是面向中文剧本开发的 Codex skill，覆盖一般叙事剧本、互动游戏剧本及《克苏鲁的呼唤》（COC）模组。它把故事、人物、调查、玩家行动、主持交付及维护放在同一套按任务加载的方法中。

使用入口是 [SKILL.md](SKILL.md)。让助手读取入口并说明本轮目标，即可开始。无需运行脚本或安装 Python。

原项目文档、个人技能目录和其他会话用于来源追溯，核心方法可独立使用。辅助技能及专用工具按实际任务和当前可用性调用。

## 适用范围

| 任务层 | 支持的工作 |
|---|---|
| L1 一般叙事 | 人物与事件因果、支线意义、主题、结构、场景表达、诊断和重写 |
| L2 互动游戏 | 参与前提、选择与条件、人物响应、节点、状态、依赖、反馈及持续成果 |
| L3 COC | 调查员参与、证据与认知、异常与恐怖、规则接口、KP材料、手证与主持交付 |

按任务增加相应能力。例如，固定游戏过场可使用一般叙事方法；公开救援类COC任务着重行动、条件和后果，无需另造隐藏谜题。

文中 **KP** 指主持人（Keeper），**SAN** 指理智相关规则。具体系统数值在需要时核对规则书。

本技能不替代正式规则书、影视／舞台行业格式规范、游戏引擎实现，也不提供独立的投骰或车卡工具。具体史实、规则数值、医疗与工程可行性需要按实际问题核验。

## 快速使用

### 直接使用文档

让助手读取本目录的 `SKILL.md`，说明当前任务、已有材料、固定事实和需要交付的内容。助手再按任务读取相关参考，无需一次读完全部文件。

示例：

```text
读取 coc-script-writing/SKILL.md，分析这段人物行动的因果和玩家介入。
只交付诊断与两个修改方向，不改已确认的往事，也不直接改母版。
```

```text
使用 $coc-script-writing，将现有COC大纲发展成场景候选。
保留固定事实，写玩家可见现场、NPC响应、条件与反馈；规则未核处单列。
```

```text
使用 $coc-script-writing，检查这段反转的公平性。
对照揭晓前实际可取得的材料，说明能证明什么、仍不能排除什么，列修订顺序。
```

### 安装为个人技能

将整个 `coc-script-writing` 文件夹复制到当前 Codex 技能目录，保留 `SKILL.md`、`agents`、`references` 与审计文件的相对位置。安装后检查技能是否可见，再使用 `$coc-script-writing`。本地开发副本中的 `scripts/` 无需复制。

默认目录为 `~/.codex/skills/`；若设置了 `CODEX_HOME`，使用该目录下的 `skills/`。以下 PowerShell 示例从仓库根目录执行，仅在目标尚不存在时复制：

```powershell
$skillHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' }
$skillRoot = Join-Path $skillHome 'skills'
$skillTarget = Join-Path $skillRoot 'coc-script-writing'
if (Test-Path -LiteralPath $skillTarget) { throw '目标技能已存在，请先比较版本并安排更新。' }
New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
New-Item -ItemType Directory -Path $skillTarget | Out-Null
foreach ($item in 'SKILL.md', 'README.md', 'ARCHITECTURE.md', 'LICENSE.md', 'agents', 'references', 'audit') {
    Copy-Item -LiteralPath (Join-Path './coc-script-writing' $item) -Destination $skillTarget -Recurse
}
```

安装是部署副本。后续更新应从统一源稿同步，不同时维护两套方法。直接读文档不要求安装；本仓库上传不代表已自动安装到用户环境。

## 按目标查阅

| 目标 | 参考 |
|---|---|
| 识别媒介、任务、阶段与材料状态 | [scope.md](references/scope.md) |
| 故事、人物、关系、支线与结构 | [narrative.md](references/narrative.md) |
| 玩家选择、人物响应、节点与状态 | [interactive.md](references/interactive.md) |
| 证据总览与七类推理／行动联系 | [investigation.md](references/investigation.md) |
| 推理目标、双层认知、线索分布、推理体验及P4 | [inference-design.md](references/inference-design.md) |
| 游玩时间、节奏、疲劳与复盘 | [play-evaluation.md](references/play-evaluation.md) |
| 主题及线索／痕迹呈现 | [theme-presentation.md](references/theme-presentation.md) |
| 异常、恐怖、规则接口与KP交付 | [coc.md](references/coc.md) |
| 整阶段或整轮开发 | [workflow.md](references/workflow.md) |
| 表达、研究、编辑、候选与筛选 | [craft.md](references/craft.md) |
| 填写人物、节点、线索等记录表，或查看完整短例 | [contracts.md](references/contracts.md) |
| 审核、反例、独立验收与收束 | [review.md](references/review.md) |
| 版本、授权、连续性与技能更新 | [maintenance.md](references/maintenance.md) |
| 联用研究、编辑、专项审核、主持和资产工具 | [skill-integration.md](references/skill-integration.md) |

核心方法已吸收人物与结构编辑、创作与历史研究、悬疑公平性审核、COC模组设计、构思筛选及清晰中文表达的适用经验。地图、图像、Word／PDF、角色卡和主持等专用能力按需交接；逻辑批评与文风润色用于有相应需要的任务。

来源中的候选数量、线索配额和主持默认值各有原使用条件。本技能按当前故事需要选择方法，具体适配见[技能协同](references/skill-integration.md)。

## 文件结构

```text
coc-script-writing/
  SKILL.md                    技能入口
  README.md                   使用、结构和维护说明
  ARCHITECTURE.md              架构与分步建设方案
  agents/openai.yaml          技能显示信息
  references/                 按任务加载的领域与专项参考
  audit/                      来源映射、实际试用及独立验收证据
```

[ARCHITECTURE.md](ARCHITECTURE.md) 用于建设维护，[当前验收台账](audit/acceptance.md) 汇总验证范围，[审计导航](audit/README.md)说明历史文件如何查阅。普通创作从入口和任务参考开始即可。

审计保留历史版本、文件指纹、有限会话取样及原维护环境路径，用于追溯当时的判断。

## 校验与验收范围

检查技能更新时，维护者需要确认：入口和参考文件齐全、本地链接与来源映射有效、受影响任务仍能正确完成。

开发校验脚本仅在本地保存，并由仓库 `.gitignore` 排除。仓库使用与安装均不依赖该脚本；历史报告中的脚本命令记录当时实际执行的检查，不是当前安装步骤。原 `design-guides` 及辅助技能源也不随仓库发布。

已完成的建设记录包括架构、来源迁移、分类复审、辅助技能整合及实际文字试用的独立AI验收。最新对象与具体范围以验收台账为准，旧报告不自动覆盖后续修订。AI文字审核、纸面状态推演、实际工具运行、非作者KP与真人桌测分别登记。本技能未因文字验收而获得真人桌测或跨项目稳定性认证。

历史本地校验器只检查本包支持的元数据格式、链接和登记关系，不能证明设计语义正确。官方 `quick_validate.py` 在原维护环境中因缺 PyYAML 未能运行，详情保留在审计记录中。

2026-10-10推理设计扩展的当前方法、两轮委员会、实际调用与官方格式检查见[audit/inference](audit/inference/README.md)，不沿用上述历史资格。

## 后续维护

新增经验先确定适用层、任务、领域归属和成熟度，改唯一权威位置及其路由，再更新对应来源登记。原九文映射与其他技能来源分别维护，不用更新哈希掩盖尚未处理的源文变化。

修订后检查结构与链接，执行受影响的实际请求；若任务约定独立验收，由未参与该步编写者读实际产物，问题实改后再复验。保留旧结论及对象指纹，记录当前资格、开放项和下一步。达到本轮目标后收束，普通扩展建议不变成无限加料。

仓库保留原文件字节，以支持审计指纹核对。编辑已验收文件会产生新对象，应重新登记相应验证；无需为了统一换行而批量重写历史审计文件。


## 背景、目标与方法特点

本技能来自COC开发实践与通用方法整理，目标是把故事设想发展成可读、可调查、可选择、可主持、可维护的剧本。它按媒介、任务和阶段选方法；从剧情用途连接推理目标、证据与行动；共同检查时间、体验、疲劳和主题呈现。方法特色是已有研究与实践的工程整合，不宣称学术首创或已证明真人效果。

简要流程：前置大纲→体验设计→逐线融合→世界事实→推理／事件章程→场景施工→规则工具→测试修订→编辑交付。局部任务按需调用，不必完整走一遍；完整阶段、验收和返修路径见[工作流总图](references/workflow.md#工作流总图)。

## 授权：仅允许自用

有权授权的原创内容采用[个人非商业使用许可 v1.1](LICENSE.md)：可个人下载、私下修改、安装并用于自己的非商业创作与跑团准备。除法律例外、适用平台条款或另行书面授权外，商业使用、收费服务、重新发布或分发须另获许可。许可不垄断抽象方法，不取得独立创作产物的版权；商业项目调用本内容仍须另行授权。第三方材料沿用原权利，GitHub平台内查看与Fork遵循其服务条款。
