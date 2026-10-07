# 辅助技能整合架构独立审查

日期：2026-10-07。审核者未参与本轮方案与证据清单编写。本报告只验收架构，未修改方案、来源或运行正文。

## 结论

**当前架构通过，无未解决必须修复项。** 可按 09 的第二阶段迁移；正文迁移、实际使用与外部资产仍须分别取得新证据，本结论不替代这些验收。审核绑定下方 SHA，后续对象改变后按影响重查。

## 实际读取及证据限度

全文读取当前 09、skill-session-evidence.json、六项 r3-behavior-inputs.md；全文读取当前 fiction-workshop 及 developmental-editing、character-work、continuity-tracking 三份引用，creative-research、historical-fiction-research、mystery-payoff-and-fairness-judge 及 scorecard、coc-trpg-skill 及 scenario_design、chinese-writing、当前 superpowers 6.4.2 的 brainstorming 与 verification-before-completion。另读取 coc-kp-host 的触发、默认运行及资产/记录协议部分；该次合并输出发生截断，不将其计作全文读完。

全文读取本仓库 2026-09-30_S2安娜线继续诊断.md、2026-09-04_阶段1建筑线路与状态原型.md。独立读取“地图设计会话”实际历史输出，核对 exec-a4a5bd02-7594-4516-a535-e07d0495206f 的合并命令确实读取 using-superpowers 和 imagegen，状态 completed、exitCode 0，并核对后续用途判断文本。首次原输出过长，后以解析后限量摘取命令与消息完成核对；未把截断全文当作穷尽历史。

证据 JSON 的八个不同会话、十页取样及分页游标与方案范围相符。成功阅读记录只支持“曾读取”；本审查没有逐一重新取回其余七个会话所有原始命令，不为全部记录赋予逐条独立复核资格。交接记录支持作者记载的使用，与原始命令区分；当前源文件只解释现在可迁移的方法，不能证明旧会话读取时的字节或效果。失败阅读项保留且不进入成功依据。未确认的 critical-thinking、coc-kp-host、humanizer 被列为条件增强，未冒称历史常用。由此可以支持选材与分组，不能支持完整频率排行榜或历史效果统计。

## 分组、归属与适配判断

1. **领域归属成立。** 人物/关系诊断归 narrative，研究与结构/表达分工归 craft，证据评审与修订顺序归 review，连续性归 maintenance，COC 信息可见与运行接口归已有 coc/interactive。新增 skill-integration 只路由与交接，不复制领域权威定义；一种源技能的不同能力分别落在相应领域，不等于同一方法多头定义。
2. **研究边界成立。** creative-research 对可靠性、冲突、缺口的要求，以及 historical-fiction-research 对纹理效用和事实/语气/观念错位的检查可互补。09 明确效用不是可靠性，防止把日记的生动性当成事实优先级或把文学候选写成已核史实。
3. **小说方法适配成立。** 原 fiction-workshop 不覆盖舞台/影视与轻量单场；新方案明确只是转译人物、结构、编辑方法。Want/Need/Wound/Lie、三幕百分比、候选数量保留可选地位；不预写玩家成长或悲剧。结构先于文字修订、人物关系因果与冷读是适合迁移的能力。
4. **悬疑与 COC 冲突边界成立。** 谜题承诺决定公平检查的范围，量表仍服从已有项目阶段与证据；源 scorecard 不能另立必然合格分。三线索、场景数量及每项氛围必须有谜底功能均未变成统一配额。信息可见性和运行接口可迁移，但车卡、投骰、存档与开团依实际请求路由。
5. **过程与主持协议适配成立。** brainstorming 的软件硬闸门、分支/提交和代理配额不直接变成创作规则；verification 的实际证据原则可保留。两个 KP 技能的菜单、伙伴、音乐、房规与持久化默认值不同，09 要求选一套主持协议并以约定为准，写作请求不自动执行主持初始化。
6. **外部资产边界成立。** historical-map 适用真实地理，虚构地点不制造现实坐标；imagegen 的阅读/用途判断没有被抬成生成实测。地图几何、氛围图及 Word/PDF 可分别交接，正文版本、玩家可见性与布局检查不混为一次合格。原技能缺失时核心方法可工作，专用能力仍须标记待完成。

## 审查期间关闭的问题

- 原 evidence JSON 的地图会话合并命令漏列 imagegen。独立核对原命令后通知主编，最新 JSON 已补在该 item 的 skills 中。09 始终只声称阅读与用途判断；未发现需撤回的生成实测声明。此项已关闭。
- 09 最新稿明确补上 fiction-workshop 原范围排除及“转译方法不等于完整调用许可”。现架构不会因借用方法而错误扩大原技能触发范围。此边界已具备，无剩余修复要求。

## 验收设计判断

架构—实际稿迁移—实际使用三步分别独立审核，先改必修再复验，并以当前对象、实际输入与实际产物绑定，足以防止旧 R2 的通过自动覆盖新内容。新增 skill-sources.json 将路径、SHA、读取范围、依据等级、处理方式和实际标题分别登记，适合维持九个原来源与新增技能来源的分界。迁移阶段仍须实际确认十一参考清单、链接、来源目标及具体语义，当前架构通过不证明未来清单正确。

六项原始请求分别覆盖人物/结构、资料冲突与转译、谜题公平与修订顺序、仅写作的 COC、地图/Word/PDF 任务书、中文润色。输入刻意限定事实、可见性及未完成工作，足以检查主要适配风险；S6 对可能性、证明限度、待核规则和已开出口的保护是有效补充。这组输入仅验证文字任务与交接行为；不调用外部资产、不联网或开团的限制与 09 对外部运行/真人桌测资格的区分相符。

## 可选建议与未验证范围

迁移来源登记时可顺带记明 using-superpowers、writing-for-agents、find-skills 属于元工作/发现工具，阅读记录不自动要求复制成剧本方法。中文写作源中“两项或四项”等格式偏好，悬疑源中“每次推进都须有新弱点/代价”的偏好，历史小说源中的研究比例等，也应在具体迁移审核时防止硬化为事实分类或统一剧情配额；09 的可选模型、证据与范围边界已足以要求这样的适配，无需架构阶段增设阻断项。

未全面复核当前所有条件增强与资产技能引用，未逐条重放其余历史会话命令，未验证历史效果或穷尽统计，未执行新运行正文/外部工具/真人桌测。本报告未将审计文档当运行入口，也未给予未来使用无条件通过。

## 当前审核对象与实际支持文件 SHA-256

下列当前字节用于绑定本次审查，不代表历史会话当时版本。

| 文件 | SHA-256 |
|---|---|
| coc-script-writing/audit/09-skill-integration-plan.md | A8122C1C05E292E8E536374C69500AAA34673DD5DAA1B1E63B8F899729F6A0CC |
| coc-script-writing/audit/skill-session-evidence.json | 8BC5C27C963CB865ED756894867D76275DE4E9D0A3A11D9BD5A365999D1211E2 |
| coc-script-writing/audit/r3-behavior-inputs.md | CF0351741FD6D34C48CA387DF75D7F97CFB03ED1F93C922D5743BB6DB8CD3685 |
| sessions/2026-09-30_S2安娜线继续诊断.md | F2883880F10A3189E71B3F0C0AA482651527AB718C8F0C099522447436671675 |
| sessions/2026-09-04_阶段1建筑线路与状态原型.md | 6228A4DF36C529D3FE0B08E8F3D567567C558D32C1E48BF0B1CE0C823CF7BAE2 |
| C:/Users/T14 Gen 4/.agents/skills/fiction-workshop/SKILL.md | 2DE5FFC914F379CDF976BF9AFB6E277B003CBA679AD13905E18A796033083363 |
| C:/Users/T14 Gen 4/.agents/skills/fiction-workshop/references/developmental-editing.md | 1752019D2BE5AB2DF74F1715F194B184B13C01C6C1C9C743D361EA8BBC3E8BFB |
| C:/Users/T14 Gen 4/.agents/skills/fiction-workshop/references/character-work.md | 2FCFF137B59319D6D466C8886978EC7D1E87775CC5AC488A497EDF94B86660D9 |
| C:/Users/T14 Gen 4/.agents/skills/fiction-workshop/references/continuity-tracking.md | 1A3496B9AE3588CA920D1F0319E9D77783D7292B56664DAE21091398440C89DF |
| C:/Users/T14 Gen 4/.agents/skills/creative-research/SKILL.md | 6D82084BBC50897E751CA457A921C2C5D1B47C5DAF964B036F766CD936CE3657 |
| C:/Users/T14 Gen 4/.agents/skills/historical-fiction-research/SKILL.md | 82B8AC0B6D1D1E119F0C7AE8E3F6A383003386E71AE2C93D23A412B2C4C9C030 |
| C:/Users/T14 Gen 4/.agents/skills/mystery-payoff-and-fairness-judge/SKILL.md | C63753189C59A1D1FA2B50CF981FFBCF71CC45CA71541DC321E9B7296EF4DAB4 |
| C:/Users/T14 Gen 4/.agents/skills/mystery-payoff-and-fairness-judge/references/scorecard.md | D465506F793D4A5672A8F12A5F033D5853C7BB8507881A5DFCCF166FD4259AA9 |
| C:/Users/T14 Gen 4/.agents/skills/coc-trpg-skill/SKILL.md | C9A6CF63ED9BF96FC6CB0B1B0AD96013058F42C331738D5ECBD703676981BD8F |
| C:/Users/T14 Gen 4/.agents/skills/coc-trpg-skill/references/scenario_design.md | 11D5D404A14212362B44DF306E828B035EED23B1246C5F7707E8E34EF5BBBF34 |
| C:/Users/T14 Gen 4/.agents/skills/chinese-writing/SKILL.md | 458219A5CF77974E53698BF3890BD9F0DF4B30A8DEBBD3A5490DE05BEE18FD83 |
| C:/Users/T14 Gen 4/.agents/skills/coc-kp-host/SKILL.md | 33B18DBB9A49D4E90F46F4C48A0AD54B83D3D62F05DD0D754AD86B2298529184 |
| C:/Users/T14 Gen 4/.codex/plugins/cache/openai-curated-remote/superpowers/6.4.2/skills/brainstorming/SKILL.md | A32D2255354775AA124855AA7100CF276BEA096FFF4EBB3A0EDF57BE216E6C72 |
| C:/Users/T14 Gen 4/.codex/plugins/cache/openai-curated-remote/superpowers/6.4.2/skills/verification-before-completion/SKILL.md | 2BEFE7FC55BCADAA3D97DD9E8EFEB633D2561C0EBE74C5A8B17C4D9E7E4520B3 |

