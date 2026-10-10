# 24 · 个人使用许可与工作流图验收

日期：2026-10-10。记录整理：本轮主编；独立审核：taxonomy_recheck，未参与本轮七份对象的编写或图像生成。

## 改动与结论

完善自定义个人非商业使用许可 v1.1，并同步两处README摘要。允许个人非商业下载、安装、私下修改及模板复用；限制文档及改写版的对外传播和商业调用，保留法律与GitHub平台权利。独立产物版权和抽象方法不受文档表达许可垄断。

工作流页新增前置＋八阶段总图、逐阶段共用审核循环和按根源返修映射。默认显示PNG，可打开SVG；折叠保留Mermaid源码，后续维护须同步生成图片。原有正文及方法规则未改。

独立文本初审通过；图形补充验收发现SVG有HTML式未闭合换行标签，主编改用DOM XML序列化后，独立XML复验通过。最终无剩余必须修复项。可选优化：长标签存在单字换行，未遮挡内容。

## 实际检查与边界

独立审核实际查看PNG（1129×1715），确认阶段、审核与返修映射可读；56个本地链接／锚点通过，两份许可字节一致，五份文本使用LF；SVG XML解析通过，无脚本及外部资源引用。

主编用Mermaid 11.12.0及Chrome实际渲染，单独打开SVG无解析错误，git diff --check通过。本地临时渲染脚本不随仓库分发。独立审核未执行真人桌测或律师审查，本报告不认定法律执行效力，也不声称已验证GitHub在线页面渲染。

## 冻结对象 SHA256

| 对象 | SHA256 |
|---|---|
| LICENSE.md | `9a2bc72262a007efec275a827782e2c12b49e7b266a40dd18f87590a0ad3104a` |
| README.md | `de6de5a6350ff588cf2b4e07d8218953febd202220f251b6afe27a3e510f6a0b` |
| coc-script-writing/LICENSE.md | `9a2bc72262a007efec275a827782e2c12b49e7b266a40dd18f87590a0ad3104a` |
| coc-script-writing/README.md | `67cef3248ee1c85278ddfddebae9336f7a68b37e1b9e1a2e783fdd4b36f82090` |
| coc-script-writing/references/workflow.md | `c04119ec450aada4a7e2feb22f058067eae4c182170bb58ec4fc2277853b2bfd` |
| coc-script-writing/assets/workflow-overview.png | `c1e262d7fa2b4e3a642c46fec2dea8974994f71e869c3526c7b8b068b036d5b9` |
| coc-script-writing/assets/workflow-overview.svg | `f24f2727dd1c9cf9864632122525a91ec2b349c0a797b7cabff9bcfa18d7cfd4` |
