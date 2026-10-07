# CocSWSkill

面向中文COC模组、互动游戏及一般叙事剧本的撰写、诊断与开发技能。按媒介、工作目标和开发阶段加载方法，覆盖人物因果、调查推理、玩家选择、场景运行、审核及长期维护。

完整技能保存在 [`coc-script-writing/`](coc-script-writing/)，可独立复制使用。

- [使用与安装说明](coc-script-writing/README.md)
- [技能入口 SKILL.md](coc-script-writing/SKILL.md)
- [参考文档与技能协同](coc-script-writing/references/skill-integration.md)
- [架构方案](coc-script-writing/ARCHITECTURE.md)
- [当前独立验收台账](coc-script-writing/audit/acceptance.md)

克隆后，从仓库根目录执行结构检查：

```powershell
git clone https://github.com/28714026262/CocSWSkill.git
cd CocSWSkill
python ./coc-script-writing/scripts/validate_package.py
```

检查脚本只需Python 3.10或以上标准库。核心使用不依赖原项目文档或其他技能安装；专用主持、投骰、地图、图像和Word／PDF工具按实际请求调用。

本仓库包含来源与独立AI验收记录。文字审核和纸面试用的通过不代表真人桌测、外部工具运行或跨项目稳定性已验证，具体范围见验收台账。
