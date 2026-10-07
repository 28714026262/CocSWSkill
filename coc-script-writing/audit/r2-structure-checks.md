# 第二轮结构校验记录

## 新登记字段的前测

新增semantic_units细项登记后，在audit内独立临时副本将SU-01目标节改成不存在标题，现有校验器仍退出0。实际发现：该新增字段尚未被校验，不把已通过的章节检查冒称细项登记检查。原包与原来源未改。需补结构校验后再跑同一探针。

实际前测输出：

```text
{"status": "passed", "references": 10, "sources": 9, "source_sections": 135, "mapped_target_sections": 333, "markdown_links": 450, "source_hashes_checked": false, "yaml_scope": "package quoted-string schema only; no general YAML parser", "semantic_review": "not performed by this validator"}
```

## 补校验后的同类探针

实际子进程检查，副本均在audit内，核实绝对路径后自动清理。作者检查仍不代替独立语义验收。

| 情境 | 退出码 | 结果 |
|---|---|---|
| 便携正例 | 0 | 符合预期 |
| 不存在语义目标标题 | 1 | 符合预期 |
| 未知语义来源 | 1 | 符合预期 |
| 遗漏细项声明 | 1 | 符合预期 |
| 语义来源倒置范围 | 1 | 符合预期 |
| 旧断链规则未回归 | 1 | 符合预期 |
| 显式来源正例 | 0 | 符合预期 |

## 实际输出

### 便携正例

```text
{"status": "passed", "references": 10, "sources": 9, "source_sections": 135, "mapped_target_sections": 333, "registered_semantic_units": 3, "markdown_links": 450, "source_hashes_checked": false, "yaml_scope": "package quoted-string schema only; no general YAML parser", "semantic_review": "not performed by this validator"}
```

### 不存在语义目标标题

```text
FAIL: Missing semantic-unit heading: SU-01
```

### 未知语义来源

```text
FAIL: Unknown semantic-unit source: SU-01
```

### 遗漏细项声明

```text
FAIL: Semantic-unit manifest/map inventory mismatch
```

### 语义来源倒置范围

```text
FAIL: Invalid semantic-unit source range: SU-01
```

### 旧断链规则未回归

```text
FAIL: Broken link in SKILL.md: references/missing.md
```

### 显式来源正例

```text
{"status": "passed", "references": 10, "sources": 9, "source_sections": 135, "mapped_target_sections": 333, "registered_semantic_units": 3, "markdown_links": 450, "source_hashes_checked": true, "yaml_scope": "package quoted-string schema only; no general YAML parser", "semantic_review": "not performed by this validator"}
```

## 验收台账收束后的实际检查

2026-10-07，主编更新acceptance及06的当前资格后，实际重跑来源结构校验，结果仍为passed：9来源、135章节、333目标节、3重点语义单元，来源指纹不变。04、05、08各自绑定的23、15、13份对象逐项重算SHA，与报告全部一致；未在复验通过后再改方法正文或脚本。

另实际扫描包内全部29份Markdown文件的479个本地链接，检查文件存在、路径留在包内及标题／显式锚点可定位，全部通过。此全包范围包含验收记录，区别于结构校验器规定对象的450个链接。台账收束不扩大三份独立报告的审核资格，也不把作者最后的结构检查当独立语义审核。
