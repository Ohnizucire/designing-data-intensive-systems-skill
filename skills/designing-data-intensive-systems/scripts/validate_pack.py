#!/usr/bin/env python3
"""Static integrity of DDIA agent-skill bundle; does not test agent behavior."""
from __future__ import annotations
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT.parents[1]
LINK = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
REFS = sorted((ROOT/'references').glob('*.md'))
FILES = sorted(PACKAGE.rglob('*.md'))
errors: list[str] = []
checks = 0

def verify(condition: bool, description: str) -> None:
    global checks
    checks += 1
    if not condition:
        errors.append(description)
        print(f'FAIL {description}')
    else:
        print(f'PASS {description}')

skill = ROOT/'SKILL.md'
intro = skill.read_text()
verify(intro.startswith('---\nname: designing-data-intensive-systems\n'), 'skill YAML frontmatter and name')
desc = re.search(r'(?m)^description: (.+)$', intro)
verify(bool(desc and desc.group(1).startswith('Use when')), 'model-facing trigger-first description')
verify(bool(desc and len(desc.group(1)) < 500), 'description is concise')
verify('disable-model-invocation' not in intro, 'single model-invoked entrypoint')
verify(len(list((PACKAGE/'skills').rglob('SKILL.md'))) == 1, 'one skill rather than 13 context-heavy skills')
verify(ROOT == PACKAGE/'skills'/'designing-data-intensive-systems', 'canonical skill path')
verify((PACKAGE/'COMPATIBILITY.md').is_file(), 'agent compatibility guide present')
verify(len(REFS) == 15, '13 topical modules plus dependency and decision references')
for i in range(1,14):
    verify(len(list((ROOT/'references').glob(f'{i:02d}-*.md'))) == 1, f'module {i:02d} present')
for link in ['cross-chapter-dependencies.md','decision-record.md']:
    verify((ROOT/'references'/link).exists(), f'{link} present')
for i in range(1,8):
    verify(bool(re.search(rf'(?m)^\s*{i}\. .*\*\*Done:',intro)), f'procedure {i} has explicit completion bound')
for file in REFS:
    if file.name[:2].isdigit():
        t=file.read_text()
        verify('**Trigger:' in t, f'{file.name}: observable trigger')
        verify('**Stop when:' in t, f'{file.name}: local completion criterion')
        verify('## Tests and proof' in t or '## Evidence and failure probes' in t, f'{file.name}: evidence gate')
verify((ROOT/'provenance/whole-book-map.md').exists(),'book-wide conceptual map')
verify((ROOT/'provenance/section-ledger.md').exists(),'all-heading source ledger')
ledger=(ROOT/'provenance/section-ledger.md').read_text()
bookmap=(ROOT/'provenance/whole-book-map.md').read_text()
for i in range(1,15):
    verify(f'## Chapter {i}:' in ledger, f'chapter {i:02} section ledger covered')
    verify(f'### Chapter {i} —' in bookmap, f'chapter {i:02} conceptual argument covered')
verify('## Chapter 14: Doing the Right Thing' in ledger, 'chapter 14 title not shifted')
verify('### Chapter 1 — Trade-Offs' in bookmap, 'chapter 1 provenance title not shifted')
verify('503 indexed headings' in ledger,'full-source heading count matches')
for f in FILES:
    for href in LINK.findall(f.read_text()):
        if re.match(r'^(?:https?://|mailto:|#)',href): continue
        path=(f.parent/href.split('#',1)[0]).resolve()
        verify(path.exists(), f'{f.relative_to(PACKAGE)} points to an existing {href}')
    verify(not re.search(r'\b(?:ficheiro|utilizador|descarregar|capítulos|revisão)\b',f.read_text(), re.I), f'{f.relative_to(PACKAGE)} lacks known Portuguese markers')

scenarios=(ROOT/'tests/agent-scenarios.md').read_text()
verify(len(re.findall(r'^\| \d+ \|',scenarios,re.M))==20,'20 behavioral pressure scenarios are explicitly supplied')
verify('have not been executed' in scenarios, 'agent tests not falsely marked executed')
verify('not a claim that a separate human-style line-by-line commentary' in (PACKAGE/'AUDIT.md').read_text(), 'reading limitations disclosed')
verify('production certification' in (PACKAGE/'AUDIT.md').read_text(), 'production limitations disclosed')
verify('No book text is bundled' in intro, 'book text not distributed')

if '--zip' in sys.argv:
    zipped = PACKAGE.with_suffix('.zip')
    verify(zipped.is_file(), 'zip exists')
    if zipped.is_file():
        with zipfile.ZipFile(zipped) as z:
            verify(z.testzip() is None,'zip integrity')
            paths={x.filename for x in z.infolist() if not x.is_dir()}
            for f in PACKAGE.rglob('*'):
                if f.is_file():
                    verify(f.relative_to(PACKAGE.parent).as_posix() in paths, f'{f.name} included in zip')

print(f'\n{checks-len(errors)}/{checks} structural checks passed.')
if errors:
    print('Failing checks:\n'+'\n'.join(errors),file=sys.stderr)
    sys.exit(1)
