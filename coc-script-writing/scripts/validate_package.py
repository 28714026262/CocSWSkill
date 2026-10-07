"""Validate this portable skill using Python's standard library.

The YAML reader intentionally accepts only this package's quoted-string schema;
it is not a general YAML parser or a substitute for semantic review.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

REFERENCE_NAMES = (
    "scope", "narrative", "interactive", "investigation", "coc",
    "workflow", "craft", "contracts", "review", "maintenance", "skill-integration",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def quoted_mapping(text: str) -> dict[str, str]:
    result = {}
    for line in text.splitlines():
        if not line.strip():
            continue
        match = re.fullmatch(r'([a-z_]+): (".*")', line)
        require(bool(match), "Unsupported YAML syntax: use key: JSON-compatible quoted string")
        key, value = match.groups()
        require(key not in result, f"Duplicate YAML key: {key}")
        value = json.loads(value)
        require(isinstance(value, str), f"YAML field is not a string: {key}")
        result[key] = value
    return result


def markdown_anchors(text: str) -> set[str]:
    anchors = set(re.findall(r'<a\s+id="([^"]+)"', text))
    used = {}
    for title in re.findall(r'^#{1,6}\s+(.+)$', text, re.M):
        title = re.sub(r'[`*_]', '', title).lower()
        base = ''.join(c for c in title if c.isalnum() or c in '-_ ').replace(' ', '-')
        count = used.get(base, 0)
        used[base] = count + 1
        anchors.add(base if count == 0 else f"{base}-{count}")
    return anchors


def validate(root: Path, check_sources: bool = False, source_root: Path | None = None) -> dict:
    root = root.resolve()
    runtime = [root / 'SKILL.md', root / 'agents/openai.yaml',
               root / 'scripts/validate_package.py']
    runtime += [root / f'references/{name}.md' for name in REFERENCE_NAMES]
    required = runtime + [root / 'ARCHITECTURE.md', root / 'audit/source-map.md',
                          root / 'audit/source-manifest.json', root / 'audit/validation-cases.md']
    for path in required:
        require(path.is_file(), f"Missing file: {path.relative_to(root)}")
    skill = (root / 'SKILL.md').read_text(encoding='utf-8')
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', skill, re.S)
    require(bool(match), "Missing or malformed SKILL frontmatter")
    metadata = quoted_mapping(match.group(1))
    require(set(metadata) == {'name', 'description'}, "Unexpected SKILL metadata keys")
    require(metadata['name'] == 'coc-script-writing', "Unexpected skill name")
    require(bool(re.fullmatch(r'[a-z0-9-]{1,64}', metadata['name'])), "Invalid skill name")
    require(1 <= len(metadata['description']) <= 1024, "Invalid description length")
    require('<' not in metadata['description'] and '>' not in metadata['description'],
            "Description contains unsupported angle brackets")
    ui_text = (root / 'agents/openai.yaml').read_text(encoding='utf-8')
    require(ui_text.startswith('interface:\n'), "UI metadata must have interface root")
    ui_lines = ui_text.splitlines()[1:]
    require(all(line.startswith('  ') for line in ui_lines if line), "Invalid interface indentation")
    ui = quoted_mapping('\n'.join(line[2:] for line in ui_lines))
    require(set(ui) == {'display_name', 'short_description', 'default_prompt'}, "Unexpected UI keys")
    require(bool(ui['display_name']), "Missing display name")
    require(25 <= len(ui['short_description']) <= 64, "UI short description must be 25–64 characters")
    require('$coc-script-writing' in ui['default_prompt'], "Default prompt must invoke skill")
    # Scan actual Markdown links, not filenames mentioned in prose or code examples.
    markdown = [path for path in required if path.suffix == '.md']
    link_count = 0
    for path in markdown:
        content = path.read_text(encoding='utf-8')
        for target in re.findall(r'!?\[[^\]\n]*\]\(([^)\n]+)\)', content):
            target = target.strip().strip('<>')
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                continue
            name, _, anchor = target.partition('#')
            destination = (path.parent / unquote(name)).resolve() if name else path
            require(destination.is_relative_to(root), f"Link leaves package in {path.name}: {target}")
            require(destination.is_file(), f"Broken link in {path.name}: {target}")
            if anchor:
                require(unquote(anchor) in markdown_anchors(destination.read_text(encoding='utf-8')),
                        f"Missing anchor in {path.name}: {target}")
            link_count += 1
    for name in REFERENCE_NAMES:
        require(f'(references/{name}.md)' in skill, f"Reference absent from router: {name}")
    manifest = json.loads((root / 'audit/source-manifest.json').read_text(encoding='utf-8'))
    sources = manifest['sources']
    require(bool(sources), "Empty source manifest")
    require(len({source['path'] for source in sources}) == len(sources), "Duplicate source paths")
    section_count = 0
    detail_count = 0
    source_map = (root / 'audit/source-map.md').read_text(encoding='utf-8')
    for source in sources:
        require(bool(re.fullmatch(r'[0-9a-f]{64}', source['sha256'])), "Invalid source SHA256")
        require(bool(source['sections']), "Missing source sections")
        for section in source['sections']:
            require(section['disposition'] in {'保留', '合并', '适配', '配置隔离', '历史追溯', '配置隔离+合并'},
                    f"Unresolved disposition: {section['heading']}")
            require(section['line'] >= 1 and section['heading'].startswith('#'), "Invalid source position")
            details = section['target_sections']
            require(bool(details), f"Unmapped source section: {section['heading']}")
            require(section['targets'] == list(dict.fromkeys(x['path'] for x in details)),
                    f"Target/section mismatch: {section['heading']}")
            expected_row = f"| {Path(source['path']).name}:{section['line']} | {section['heading'].lstrip('# ')} | {section['disposition']} | "
            actual_rows = [line for line in source_map.splitlines() if line.startswith(expected_row)]
            require(len(actual_rows) == 1, f"Source map row mismatch: {section['heading']}")
            expected_targets = '；'.join(f"[{Path(x['path']).name}](../{x['path']})：{x['heading'][3:]}" for x in details)
            require(actual_rows[0] == expected_row + expected_targets + ' | ' + section['notes'] + ' |',
                    f"Source map content mismatch: {section['heading']}")
            for detail in details:
                destination = (root / detail['path']).resolve()
                require(destination.is_relative_to(root / 'references'), "Source target outside references")
                require(destination.is_file(), f"Missing source target: {detail['path']}")
                require(detail['heading'] in destination.read_text(encoding='utf-8').splitlines(),
                        f"Missing mapped heading: {detail}")
                detail_count += 1
            section_count += 1
        if check_sources:
            path = source_root / Path(source['path']).name if source_root else root / source['path']
            require(path.is_file(), f"Missing original source: {path}; use --source-root")
            require(hashlib.sha256(path.read_bytes()).hexdigest() == source['sha256'],
                    f"Source changed, semantic migration required: {path.name}")
            lines = path.read_text(encoding='utf-8-sig').splitlines()
            actual = [(n, line) for n, line in enumerate(lines, 1) if re.match(r'^#{1,6}\s', line)]
            registered = [(x['line'], x['heading']) for x in source['sections']]
            require(actual == registered, f"Original heading registration mismatch: {path.name}")
    units = manifest.get('semantic_units', [])
    require(len({unit['id'] for unit in units}) == len(units), 'Duplicate semantic-unit IDs')
    require(set(re.findall(r'^\| (SU-\d+) \|', source_map, re.M)) == {unit['id'] for unit in units},
            'Semantic-unit manifest/map inventory mismatch')
    source_paths = {source['path'] for source in sources}
    for unit in units:
        require(bool(re.fullmatch(r'SU-\d+', unit['id'])), 'Invalid semantic-unit ID')
        require(unit['source'] in source_paths, f"Unknown semantic-unit source: {unit['id']}")
        bounds = unit['lines']
        require(isinstance(bounds, list) and len(bounds) == 2
                and all(isinstance(n, int) for n in bounds) and 1 <= bounds[0] <= bounds[1],
                f"Invalid semantic-unit source range: {unit['id']}")
        require(bool(unit['experience']) and bool(unit['scope']) and bool(unit['status']),
                f"Incomplete semantic-unit metadata: {unit['id']}")
        require(bool(unit['targets']), f"Unmapped semantic unit: {unit['id']}")
        for target in unit['targets']:
            destination = (root / target['path']).resolve()
            require(destination.is_relative_to(root / 'references') and destination.is_file(),
                    f"Missing semantic-unit target: {unit['id']}")
            require(target['heading'] in destination.read_text(encoding='utf-8').splitlines(),
                    f"Missing semantic-unit heading: {unit['id']}")
        expected_targets = '；'.join(f"[{Path(x['path']).name}](../{x['path']})：{x['heading'][3:]}"
                                   for x in unit['targets'])
        expected_row = (f"| {unit['id']} | {Path(unit['source']).name}:{bounds[0]}—{bounds[1]} | "
                        f"{unit['experience']} | {expected_targets} | {unit['status']} |")
        require(expected_row in source_map.splitlines(), f"Semantic-unit map content mismatch: {unit['id']}")
        if check_sources:
            original = source_root / Path(unit['source']).name if source_root else root / unit['source']
            require(bounds[1] <= len(original.read_text(encoding='utf-8-sig').splitlines()),
                    f"Semantic-unit source range outside file: {unit['id']}")
    if check_sources:
        directory = source_root if source_root else (root / manifest['source_root']).resolve()
        require({x.name for x in directory.iterdir() if x.is_file()} == {Path(x['path']).name for x in sources},
                "Original directory inventory changed; review and register new files")
    return {'status': 'passed', 'references': len(REFERENCE_NAMES), 'sources': len(sources),
            'source_sections': section_count, 'mapped_target_sections': detail_count,
            'registered_semantic_units': len(units),
            'markdown_links': link_count, 'source_hashes_checked': check_sources,
            'yaml_scope': 'package quoted-string schema only; no general YAML parser',
            'semantic_review': 'not performed by this validator'}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--check-sources', action='store_true')
    parser.add_argument('--source-root', type=Path)
    args = parser.parse_args()
    try:
        require(args.source_root is None or args.check_sources, '--source-root requires --check-sources')
        print(json.dumps(validate(args.root, args.check_sources, args.source_root), ensure_ascii=False))
        return 0
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
