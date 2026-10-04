"""Create a content-preserving TSV/prose view; never rewrite language meanings."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / 'glossary-migrated.md'


def cells(line):
    return [cell.strip() for cell in re.split(r'(?<!\\)\|', line.strip())[1:-1]]


def separator(line):
    return line.startswith('|') and all(re.fullmatch(r':?-+:?', c) for c in cells(line))


def convert(source):
    lines = source.splitlines(keepends=True)
    output, blocks = [], []
    i = 0
    while i < len(lines):
        if (lines[i].startswith('|') and i + 1 < len(lines)
                and separator(lines[i + 1])):
            header = cells(lines[i])
            rows = []
            start = i
            i += 2
            while i < len(lines) and lines[i].startswith('|'):
                row = cells(lines[i])
                assert len(row) == len(header), (i + 1, row, header)
                assert all('\t' not in cell and '\n' not in cell for cell in row)
                rows.append(row)
                i += 1
            block = '\t'.join(header) + '\n'
            block += ''.join('\t'.join(row) + '\n' for row in rows)
            output.append(block)
            blocks.append({'kind': 'table', 'source_line': start + 1,
                           'headers': header, 'rows': rows, 'rendered': block})
        else:
            output.append(lines[i])
            blocks.append({'kind': 'prose', 'text': lines[i]})
            i += 1
    return ''.join(output), blocks


def main():
    raw = SOURCE.read_bytes()
    source = raw.decode('utf-8')
    compact, blocks = convert(source)
    # Verify every table field independently against the emitted TSV; every
    # non-table line, including examples, must remain exactly unchanged.
    for block in blocks:
        if block['kind'] == 'table':
            actual = [line.split('\t') for line in block['rendered'].splitlines()]
            assert actual == [block['headers']] + block['rows']
    reconstructed_content = ''.join(b['rendered'] if b['kind'] == 'table'
                                    else b['text'] for b in blocks)
    assert reconstructed_content == compact
    table_rows = sum(len(b['rows']) for b in blocks if b['kind'] == 'table')
    # Structural examples contain no tables; compare their entire contents.
    assert re.findall(r'```[\s\S]*?```', source) == re.findall(r'```[\s\S]*?```', compact)
    # Compare symbol inventories using the existing format-only index builder.
    import importlib.util
    spec = importlib.util.spec_from_file_location('kit_builder', ROOT.parent / 'mid-model-language-kit' / 'build_kit.py')
    builder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(builder)
    index = builder.make_index(builder.sections(source))
    inventory = [o for e in index for o in e['occurrences']
                 if o['section_title'].startswith('Inventory: ')]
    assert all('\t'.join(o['cells']) in compact for o in inventory)
    data = compact.encode('utf-8')
    (ROOT / 'glossary-compact.txt').write_bytes(data)
    report = {
        'source': '../glossary-migrated.md',
        'source_sha256': hashlib.sha256(raw).hexdigest(),
        'compact_sha256': hashlib.sha256(data).hexdigest(),
        'source_bytes': len(raw), 'compact_bytes': len(data),
        'byte_reduction_percent': round(100 * (1 - len(data) / len(raw)), 2),
        'source_characters': len(source), 'compact_characters': len(compact),
        'tables': sum(b['kind'] == 'table' for b in blocks),
        'table_data_rows_preserved': table_rows,
        'inventory_occurrences_preserved': len(inventory),
        'indexed_search_keys_preserved': len(index),
        'verification': 'All table headers/cells preserved in order; all non-table text and code examples unchanged. Formatting is not byte-identical to source.',
        'tokens': None,
        'token_note': 'No model tokenizer installed. Byte savings do not establish token savings or model usability.',
    }
    (ROOT / 'compression-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False))


if __name__ == '__main__':
    main()
