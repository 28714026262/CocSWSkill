# 批次E独立验收 R2：E-P8-1定向复验

2026-10-21。原P8／多媒体交付席复验，未参与修订。结论：E-P8-1关闭；结合R1已读范围，本席批次E通过，无新增必修，无需为轮数继续修改。

## 实际对象与变化

本轮对象清单为`reviews/objects/E-fix1.json`，实际SHA256：`cbed9d20b89a6ecc3c653c9cda4e03c7da9543e2d17ff52294f028c98b6319b1`。对照初审清单`E-initial.json`（SHA256 `48d95ad58f22f55188bd6427df32b09d19c659b207c339f8d26ed4d09e144cfa`），两清单均75对象，只有production的P8 README、integration、workbench三文件指纹变化；本席逐件核fix1当前文件，75匹配，0缺失／指纹不符。

三文件实际读取后的变化另用内存逆向还原核对：每份都恰有一处`[兼容对象](compatibility.json)`，将该处在内存中替回原provenance目标后，逐份SHA256准确还原initial清单中的旧指纹。因此三份相对初审的字节变化确实只为该链接目标替换，没有夹入其他正文变化；未向磁盘写还原件。

## 关闭依据

|活动入口|实际当前目标|结果|
|---|---|---|
|P8 README“兼容对象”|同目录`compatibility.json`|解析到production/references/p8的实际JSON|
|integration“源码版本与核对文件”|同目录`compatibility.json`|同一对象，可直接读取完整依据|
|workbench“按兼容对象核对”|同目录`compatibility.json`|同一对象，未再跳历史摘要|

当前JSON指纹仍为`b1d0f6b01bd8db0c0f6912b445cb3c3bb910d37b61f94d79ec76843f81f27604`，与initial及baseline相同。实际解析／读取确认：HEAD `1104e4f7d440ddeeeb673afcec9c52ad2bd1e91d`、八个源码文件指纹、2026-10-21核对日期、仅源码检查且未服务导入／运行验收的scope、keeper-content v1及keeper-backup v2均保真。没有将修链接改记为重新核查消费者。

重新读取provenance的`history-365ae8828a82`条目，仍保旧coc路径和原JSON指纹作为历史摘要；当前活动引用与出处用途已经分开。本席不据此声明整个provenance文件做过全量前后字节比较。

在本批三个skill的活动方法中定向搜索Markdown JSON链接、兼容对象及相关history目标，发现的当前JSON导航即上述三处，均已修正，未发现其他同类误导。条件教学资源索引中的代码路径不是公开必读活动链接；原47资产及其他方法由75对象清单确认未变，本轮不重复审未改全方法、媒体画面或历史资产内部运行语义。

## 有限结论

E-P8-1有实际修订、当前文件核对与原席复读依据，予以关闭。R1其余文本覆盖与本轮修复共同支持本席批次E通过；这不替代F／G跨域终验。

本轮只读并写本报告，未生成资源、安装、运行服务、导入、修改Git或实际操作消费者；未重跑作者的全套静态／公开副本／官方metadata校验，也未授媒体品质、音频听审、产品运行或真人使用资格。
