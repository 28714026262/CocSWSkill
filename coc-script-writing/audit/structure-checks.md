# 阶段C结构检查与故障探针

执行者：主编，非独立验收；独立验收员须另行运行并核查。Python标准库，真实子进程退出码验证。临时副本均在audit内，绝对路径核实后自动清理，未修改原文。

原目录校验：通过，10参考／9来源／135章节／329目标节／437链接。

首次便携包探针发现测试副本遗漏audit/acceptance.md，正确报断链；补齐夹具后再执行以下八例。不是运行包错误。

skill-creator官方quick_validate.py已实际尝试，但系统Python缺PyYAML，退出1；本包不安装环境依赖。采用仅支持本包双引号字符串元数据的标准库校验器，未冒称通用YAML解析。

| 情境 | 实际退出码 | 判定 |
|---|---|---|
| 独立复制包无原目录时的结构验证 | 0 | 符合预期 |
| 断链必须拒绝 | 1 | 符合预期 |
| 无效元数据必须拒绝 | 1 | 符合预期 |
| 无效锚点必须拒绝 | 1 | 符合预期 |
| 未迁移章节必须拒绝 | 1 | 符合预期 |
| 清单与索引不一致必须拒绝 | 1 | 符合预期 |
| 显式原目录来源校验 | 0 | 符合预期 |
| 来源变化必须拒绝且不更新指纹 | 1 | 符合预期 |

## 实际校验输出

### 独立复制包无原目录时的结构验证

```text
{"status": "passed", "references": 10, "sources": 9, "source_sections": 135, "mapped_target_sections": 329, "markdown_links": 437, "source_hashes_checked": false, "yaml_scope": "package quoted-string schema only; no general YAML parser", "semantic_review": "not performed by this validator"}
```

### 断链必须拒绝

```text
FAIL: Broken link in SKILL.md: references/missing.md
```

### 无效元数据必须拒绝

```text
FAIL: Unsupported YAML syntax: use key: JSON-compatible quoted string
```

### 无效锚点必须拒绝

```text
FAIL: Missing anchor in narrative.md: investigation.md#missing-anchor
```

### 未迁移章节必须拒绝

```text
FAIL: Unmapped source section: # COC完整开发流程
```

### 清单与索引不一致必须拒绝

```text
FAIL: Source map row mismatch: # COC完整开发流程
```

### 显式原目录来源校验

```text
{"status": "passed", "references": 10, "sources": 9, "source_sections": 135, "mapped_target_sections": 329, "markdown_links": 437, "source_hashes_checked": true, "yaml_scope": "package quoted-string schema only; no general YAML parser", "semantic_review": "not performed by this validator"}
```

### 来源变化必须拒绝且不更新指纹

```text
FAIL: Source changed, semantic migration required: COC完整开发流程.md
```
