# COC剧本撰写技能

`coc-script-writing` 是面向中文剧本开发的 Codex skill，覆盖一般叙事剧本、互动游戏剧本及《克苏鲁的呼唤》（COC）模组。它把故事、人物、调查、玩家行动、主持交付及维护放在同一套按任务加载的方法中。

运行入口是 [SKILL.md](SKILL.md)。核心方法可独立使用；原项目文档、个人技能目录和其他会话不属于运行依赖。辅助技能及专用工具按实际任务、当前可用性调用。

## 适用范围

| 任务层 | 支持的工作 |
|---|---|
| L1 一般叙事 | 人物与事件因果、支线意义、主题、结构、场景表达、诊断和重写 |
| L2 互动游戏 | 参与前提、选择与条件、人物响应、节点、状态、依赖、反馈及持续成果 |
| L3 COC | 调查员参与、证据与认知、异常与恐怖、规则接口、KP材料、手证与主持交付 |

按任务增加相应能力。一般剧本不自动加入玩家分支或SAN；非调查COC不强造谜题；固定游戏过场可以只用一般叙事方法。

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

将整个 `coc-script-writing` 文件夹复制到当前 Codex 技能目录，保留 `SKILL.md`、`agents`、`references`、`scripts` 与审计文件的相对位置。安装后在新的会话中检查技能是否可见，再使用 `$coc-script-writing`。

默认目录为 `~/.codex/skills/`；若设置了 `CODEX_HOME`，使用该目录下的 `skills/`。以下 PowerShell 示例从仓库根目录执行，仅在目标尚不存在时复制：

```powershell
$skillHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' }
$skillRoot = Join-Path $skillHome 'skills'
$skillTarget = Join-Path $skillRoot 'coc-script-writing'
if (Test-Path -LiteralPath $skillTarget) { throw '目标技能已存在，请先比较版本并安排更新。' }
New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
Copy-Item -LiteralPath './coc-script-writing' -Destination $skillTarget -Recurse
```

安装是部署副本。后续更新应从统一源稿同步，不同时维护两套方法。直接读文档不要求安装；本仓库上传不代表已自动安装到用户环境。

## 按目标查阅

| 目标 | 参考 |
|---|---|
| 识别媒介、任务、阶段与材料状态 | [scope.md](references/scope.md) |
| 故事、人物、关系、支线与结构 | [narrative.md](references/narrative.md) |
| 玩家选择、人物响应、节点与状态 | [interactive.md](references/interactive.md) |
| 证据、线索、误区、认知与行动联系 | [investigation.md](references/investigation.md) |
| 异常、恐怖、规则接口与KP交付 | [coc.md](references/coc.md) |
| 整阶段或整轮开发 | [workflow.md](references/workflow.md) |
| 表达、研究、编辑、候选与筛选 | [craft.md](references/craft.md) |
| 必要卡表字段及完整短例 | [contracts.md](references/contracts.md) |
| 审核、反例、独立验收与收束 | [review.md](references/review.md) |
| 版本、授权、连续性与技能更新 | [maintenance.md](references/maintenance.md) |
| 联用研究、编辑、专项审核、主持和资产工具 | [skill-integration.md](references/skill-integration.md) |

核心方法已吸收人物与结构编辑、创作与历史研究、悬疑公平性审核、COC模组设计、构思筛选及清晰中文表达的适用经验。地图、图像、Word／PDF、角色卡和主持等专用能力按需交接；逻辑批评与文风润色作为条件增强。原技能的候选数量、线索配额、预写人物弧、软件开发闸门和主持默认值不成为通用剧本规定。

## 文件结构

```text
coc-script-writing/
  SKILL.md                    技能入口
  README.md                   使用、结构和维护说明
  ARCHITECTURE.md              架构与分步建设方案
  agents/openai.yaml          技能显示信息
  references/                 十一份按任务加载的参考
  scripts/validate_package.py 结构、链接及原来源登记检查
  audit/                      来源映射、实际试用及独立验收证据
```

[ARCHITECTURE.md](ARCHITECTURE.md) 用于建设维护，[audit/acceptance.md](audit/acceptance.md) 汇总当前资格；普通创作不必先读审计材料。审计保留历史版本、文件指纹、有限会话取样以及原维护环境路径，它们用于追溯，不是便携运行依赖。

## 校验与验收范围

结构校验只需 Python 3.10 或以上标准库，无需安装额外 Python 包。从仓库根目录执行：

```powershell
python ./coc-script-writing/scripts/validate_package.py
```

直接复制本技能后也可在技能目录执行 `python scripts/validate_package.py`。默认检查包结构、支持的元数据、规定对象的本地链接以及原九来源的映射登记；不读取缺失的原项目目录。

如维护者持有原 `design-guides`，可显式核查来源变化：

```powershell
python ./coc-script-writing/scripts/validate_package.py --check-sources --source-root 'D:/path/to/design-guides'
```

该路径需替换为实际原目录。原目录不随本仓库发布，缺少它不影响核心使用。常规脚本不自动检查补充技能源或全部审计Markdown；对应检查与人工语义核对见审计记录。

已完成的建设记录包括架构、来源迁移、分类复审、辅助技能整合及实际文字试用的独立AI验收。最新对象与具体范围以验收台账为准，旧报告不自动覆盖后续修订。AI文字审核、纸面状态推演、实际工具运行、非作者KP与真人桌测分别登记。本技能未因文字验收而获得真人桌测或跨项目稳定性认证。

校验器的YAML处理仅支持本包双引号字符串schema，不是通用YAML解析器或语义证明。官方 `quick_validate.py` 在原维护环境中因缺PyYAML无法运行，已如实记录；这不影响本包标准库检查，也不等于官方校验已通过。

## 后续维护

新增经验先确定适用层、任务、领域归属和成熟度，改唯一权威位置及其路由，再更新对应来源登记。原九文映射与其他技能来源分别维护，不用更新哈希掩盖尚未处理的源文变化。

修订后检查结构与链接，执行受影响的实际请求；若任务约定独立验收，由未参与该步编写者读实际产物，问题实改后再复验。保留旧结论及对象指纹，记录当前资格、开放项和下一步。达到本轮目标后收束，普通扩展建议不变成无限加料。

仓库保留原文件字节，以支持审计指纹核对。编辑已验收文件会产生新对象，应重新登记相应验证；无需为了统一换行而批量重写历史审计文件。
