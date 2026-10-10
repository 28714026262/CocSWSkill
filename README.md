# CocSWSkill

面向中文COC模组、互动游戏及一般叙事剧本的撰写、诊断与开发技能。按媒介、工作目标和开发阶段加载方法，覆盖人物因果、调查推理、玩家选择、场景运行、审核及长期维护。

完整技能保存在 [`coc-script-writing/`](coc-script-writing/)，可独立复制使用。让助手读取 `SKILL.md`，说明已有材料和本轮目标，即可开始；无需运行脚本或安装 Python。

- [使用与安装说明](coc-script-writing/README.md)
- [技能入口 SKILL.md](coc-script-writing/SKILL.md)
- [按目标选择参考文档](coc-script-writing/README.md#按目标查阅)
- [通用推理目标与线索分布方法](coc-script-writing/references/inference-design.md)
- [与其他技能协同](coc-script-writing/references/skill-integration.md)
- [架构方案](coc-script-writing/ARCHITECTURE.md)
- [当前独立验收台账](coc-script-writing/audit/acceptance.md)

下载仓库：

```powershell
git clone https://github.com/28714026262/CocSWSkill.git
cd CocSWSkill
```

在仓库目录中，可以这样开始：

```text
读取 coc-script-writing/SKILL.md，检查我的COC大纲。
先分析人物因果与调查员参与，再给出修改建议；保留已确认的背景事实。
```

需要用技能名称直接调用时，按[安装说明](coc-script-writing/README.md#安装为个人技能)复制整个技能目录。核心方法不依赖原项目文档或其他已安装技能；主持、投骰、地图、图像和文档制作工具按实际请求调用。

开发校验脚本仅在维护者本地保存，已加入 `.gitignore`，不随仓库发布。历史报告中的脚本和原环境路径用于追溯当时的检查。

本仓库包含来源与独立AI验收记录。文字审核和纸面试用的通过不代表真人桌测、外部工具运行或跨项目稳定性已验证，具体范围见验收台账。
