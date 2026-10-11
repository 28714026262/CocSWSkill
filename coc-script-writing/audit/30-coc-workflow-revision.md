# 30 · 第2步干扰发展与COC第6步设计修订记录

日期：2026-10-11。基线为发布提交ca77efdb3de6d466e0474dd6fb05db86e8c1c8d8。用户先要求委员会细化讨论，再明确“根据这次内容更新技能”，本轮据此实施；方案讨论期间未修改文件。仅修改方法、入口、图和相关通用源接口，不改作品故事或已采用玩家角色数据。

## 方案与维护归属

- 第2步在工作流维护通用六工序、干扰分类和最小记录；不干扰进程也受条件约束，干扰效果不是统一检定等级。
- 第6步实际设计游戏数据、判定与特殊处理，不再仅收束。本轮仅细化COC；新[COC第6步专页](../references/coc-rules-design.md)维护七工序、规则依据、KP表、两个示例及返修。其他系统只保留适配接口。
- 第5步落实行动、场景和反馈并列配置需求；承诺可主持样段时先完成相关第6步，再回场景复核与验证。前序保留决定性可行性边界核验，不要求完成全部数据。
- coc.md主持手册从第6步同版已完成设计提取；SKILL、scope、contracts、两README、架构和图同步路由。原项目流程升v1.17，源导航和统筹接口同步；COC详细工序只维护在专页，源流程引用便携副本。

## 独立停点与实际修正

架构由committee_causality_v6独立首审，通过后实施。内容复验见[31内容验收](31-coc-workflow-content-review.md)，规则复验见[32规则验收](32-coc-rules-review.md)。内容初审发现第1步骰点仍归场景、第5步无条件要求样段可运行、scope施工入口仍要求可运行样段三处残留；实改后独立复验通过，无剩余必修。

committee_clues_v6未编写运行正文，从实际入口执行四个合成纸面用例，见[33使用产物](33-coc-workflow-use-check.md)。执行者参与过方案讨论，非盲测。因果席另读验收U1/U2/U4及U3因果；规则席另核U3计算与裁定边界，均通过。实际对象及追加复核以各独立收据绑定为准，执行者自评不代替外审核。

基础门槛与规则依据只来自核验过的官方条目；重要／超前不自动升难度，RP按实际方法和条件调整。当地技能中的固定三路径配额及简化SAN阈值未直接继承；有意偏离正式规则的机制明确标为特例或房规。

## 检查与资格

作者对12份运行／入口与源导航文本检查232个本地链接／锚点，零错误；SVG XML解析通过，图重新生成并实际查看。7个冻结方法／许可对象字节与本轮开始一致。独立审查图示及正文的一致性另见31。使用与安装无需新增脚本，生成和检查工具只放本地临时目录。

通过限本轮受影响文本、图示、基础规则接口与指定AI纸面例；不重授全篇历史来源资格，不授具体模组数值平衡、实际掷骰、完整扩展规则、非作者KP运行、真人桌测或引擎资格。未给时间、成本、孤注风险等保持待配置。

## 运行对象SHA256

| 对象 | SHA256 |
|---|---|
| README.md | `3a8d2c3f0757a8a91442cc1920135c3c1f7913fde029a94bcf09f3d995f48a8b` |
| coc-script-writing/SKILL.md | `fbb5f9ca2d958fbd5c084b6970d18b1f828d1533cb9a70ebec5c7a467b6187ca` |
| coc-script-writing/README.md | `89261deb618a7bfbc16829480bee0a0e1e001f13be6c0d4826f25c6f5e8bc588` |
| coc-script-writing/ARCHITECTURE.md | `81797d937a60bc4feb3da9ad741996560e1ac11ea32c1245880129b8277acbb3` |
| coc-script-writing/references/workflow.md | `b13e682b1590af0c343d0e498c85e5fc1c140ecd3e2e6c0908bac7ce025b72b0` |
| coc-script-writing/references/coc-rules-design.md | `d7971d0ea9f4e197165d93e63f7a5d0f05d13b77191771cae1691834f861b132` |
| coc-script-writing/references/coc.md | `73ade2112bec89286a4d5543395c22707627e5e6e18c54fb6a2696eed8771703` |
| coc-script-writing/references/contracts.md | `39d220044ebbe3f8a019ffb479233c6037177253334d2ae91920b2cab4f8d377` |
| coc-script-writing/references/scope.md | `f97858155e75dc24a62fc440d44bc2b75b6ef061bbfefb9cd290b045f26206af` |
| coc-script-writing/assets/workflow-overview.png | `59db92178f2be5ba572879b1c57bd112b9c581151f1bbe8405424aed74822347` |
| coc-script-writing/assets/workflow-overview.svg | `8f656b4075d201c84287193ea498757be810d28130805afc17cd5831e75ebec9` |

## 源文前后指纹

源文保留在echo/design-guides，不把echo工程其他改动纳入发布。历史来源清单保留旧对象，本轮另记实际接口修订：

| 源文件 | 修订前SHA256 | 修订后SHA256 |
|---|---|---|
| design-guides/COC完整开发流程.md | `9410eea57b6124646ca93bf05c77a8aec3e3657c955d8f7a8df22e3bf72c112c` | `faffc75e458934828743ca3fa8b324bea34c215152487bcc6ea8608113803e3a` |
| design-guides/README.md | `38d9eb7917266785e849bb81412ef870a6ec1f657b081b92b87812109819f4f4` | `ebbe932bcfea183b9883b0e3973924611464b110be93d4900a91ef550edd98c1` |
| design-guides/通用方案统筹与维护.md | `04c35fddf70234cf2eec83ddc11cb39f9c50de1977a49d799021c1f33598dc70` | `cc7992504879404e0a93d3cd86d1f62b4fc6e7c2735222bea697f4c2b4ead411` |

## 冻结核验

| 对象 | SHA256 |
|---|---|
| coc-script-writing/references/inference-design.md | `32b8fe360740cd033c466267546f6183d2425604fb5e513197e1430b1f51f9ae` |
| coc-script-writing/references/play-evaluation.md | `6f35760ab4544feda372e84cce99ab8bf7937f034e9b1194ed8b2b42c2fdb550` |
| LICENSE.md | `d1cfc5cfa243396e8a3cd25180487f0ba1f04954848c1106572a7ec13002c553` |
| coc-script-writing/LICENSE.md | `d1cfc5cfa243396e8a3cd25180487f0ba1f04954848c1106572a7ec13002c553` |
| coc-script-writing/output/pdf/LICENSE-CC-BY-NC-ND-4.0.zh-CN.pdf | `b310400ac8c4d1b6ba995499f01f53533d71dd80bef647afeb2b52b6575789de` |
| design-guides/推理目标与线索分布设计通用能力.md | `bf0dca0963574a5e5ec3d364b6bb0306663b6dfe3ee6589cca209a970ae66d64` |
| design-guides/游玩时间与节奏评估通用能力.md | `7d40caceae3e4150a3041c8844e038464305064cf89f97e1edf1e05a91e63483` |
