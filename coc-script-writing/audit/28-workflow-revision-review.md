# 28 · 工作流依赖循环与按游戏配置修订验收

日期：2026-10-10。基于发布仓库1806b8553cf7387066dbc0b61ffc32665a6be52e，按用户要求修正现有流程，保留前置大纲与八阶段。循环以“后续设计需要前序支持”为触发；最终剧本、美术及其他资源归第8步，不另建资源阶段。

## 改动与独立停点

- 架构：taxonomy_recheck独立审核修订计划，通过。已有支持就在当前步骤落实；缺条件回责任步骤补足；冲突或合理调整按项目授权改当前或前序。同步影响对象、复核并登记版本后，返回需求发起处。
- 内容：taxonomy_recheck独立复验正文、路由、源文与图示，初审发现源流程仍把返修限于硬矛盾、源README版本表仍为v1.15，两项实改后再次审核通过，无剩余必修。阶段表示例加COC适用说明；其他游戏按所选系统配置，一般剧本不强填游戏数值。
- 使用：migration_acceptance独立执行四个具体纸面情境，输出与实际范围见[29使用检查](29-workflow-use-check.md)。执行者未参与本轮方法编写，保留先前审读上下文，不是盲测。taxonomy_recheck另读29实际输出并独立验收四案，通过：A不无谓返工，B保留候选与知情边界，C联查消耗且不把候选称标准，D按媒介分流。

机制设计、规则适配与数据配置沿原阶段执行；决定性规则和数值在依赖之前核验，第6步统一默认配置与工具。固定母版不因后续需求自动解冻，返修遵循现有项目授权。

## 实际检查与范围

独立内容审核读取10份文本，检查208个本地链接／锚点，无错误；SVG XML解析通过，20个Mermaid节点／分组标签均在SVG内；PNG已独立查看，前置八步和三支循环清楚。作者另检查发布改动空白及图示生成结果。

通过限本轮文本、路由和图示内容，不重授全部历史文档资格，不代替真人桌测、排演、引擎运行或项目成品验收。历史R4来源清单保留当时对象，本轮源文前后指纹另列如下。许可、推理和节奏方法未改。

## 发布对象SHA256

| 对象 | SHA256 |
|---|---|
| README.md | `aa49d2244b739ad5f8837f888a84145b8673eca545b2aeb0b5fa0e418fe8e9be` |
| coc-script-writing/ARCHITECTURE.md | `f6c2a9387271d87df3c4e5b3d9ae598b2d6c8e1c9b078e0b1d71e78efb8d6635` |
| coc-script-writing/README.md | `dedc872d5a3a231a803beebf286dd2792f4126910c606de384e14da64eecf9fd` |
| coc-script-writing/SKILL.md | `d7f7e934d85b27394d19ae0973b24a2e52a006f738dc13272ba9958530bb7002` |
| coc-script-writing/references/contracts.md | `58b9468495857a9cdf9a3f6fa04eab2c1277c2626c4c4608419d44357a7c5581` |
| coc-script-writing/references/scope.md | `c89eaca493235dcf02b50920ef3db1e098cc2adf394ff2cd492915a3dddcffb1` |
| coc-script-writing/references/workflow.md | `41148a345c969e8f694e955db218d34d6328832f973f0f2290ea9c154c85133f` |
| coc-script-writing/assets/workflow-overview.png | `d8712bdaa5249417aceb3e6a397644caf1099a7daf21dc525bc0f191b0af1bfd` |
| coc-script-writing/assets/workflow-overview.svg | `0c976c7378211fdf18b0e74a37a21cad306bda8fb13de507aa7db28e7cc18087` |

## 本地通用源文修订指纹

源文保留在echo/design-guides；本轮只同步相应技能方法与入口，不将echo工程的其他内容纳入发布仓库。

| 源文件 | 修订前SHA256 | 修订后SHA256 |
|---|---|---|
| design-guides/COC完整开发流程.md | `368ca26a15545dcbe67797f4e4bf183dc70a8043e90570e2b53b65b9410504d8` | `9410eea57b6124646ca93bf05c77a8aec3e3657c955d8f7a8df22e3bf72c112c` |
| design-guides/README.md | `db319ced137d4d15aac07540bec7797199ec820eaba1a279635df5664e6716cd` | `38d9eb7917266785e849bb81412ef870a6ec1f657b081b92b87812109819f4f4` |
| design-guides/通用方案统筹与维护.md | `1d1bde9048b2d8bf6713d5c1854eb2c9b90ac9992adbd5eb211dc3a2198d36af` | `04c35fddf70234cf2eec83ddc11cb39f9c50de1977a49d799021c1f33598dc70` |

## 冻结方法核验

下列四对象与本轮开始时字节一致：

| 对象 | SHA256 |
|---|---|
| coc-script-writing/references/inference-design.md | `32b8fe360740cd033c466267546f6183d2425604fb5e513197e1430b1f51f9ae` |
| coc-script-writing/references/play-evaluation.md | `6f35760ab4544feda372e84cce99ab8bf7937f034e9b1194ed8b2b42c2fdb550` |
| design-guides/推理目标与线索分布设计通用能力.md | `bf0dca0963574a5e5ec3d364b6bb0306663b6dfe3ee6589cca209a970ae66d64` |
| design-guides/游玩时间与节奏评估通用能力.md | `7d40caceae3e4150a3041c8844e038464305064cf89f97e1edf1e05a91e63483` |

## 收据与使用产物复核

taxonomy_recheck另核28及两份验收导航／台账，转述与指纹匹配，历史资格未扩大。29四案独立验收通过，仅限AI纸面输出，不授工程、真人或引擎资格。受审29报告SHA256：`09088ed74409f5f49b58cfc181326238bc1f9fd7b4edfe3536248e9f3d85c560`。
