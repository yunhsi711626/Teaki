from pathlib import Path
import re,sys
root=Path(__file__).resolve().parent.parent
sources=list((root/'wiki/sources').glob('*.md'))
topics=list((root/'wiki/topics').glob('*.md'))
errors=[]
for f in [root/'wiki/index.md',*sources,*topics]:
 s=f.read_text(encoding='utf-8')
 for link in re.findall(r'\]\(([^)]+\.md)\)',s):
  if not (f.parent/link).resolve().is_file():errors.append(f'broken link: {f} -> {link}')
for f in topics:
 for ref in set(re.findall(r'\b(?:SRC-\d{3}|ALT-\d{3})\b',f.read_text(encoding='utf-8'))):
  if not (root/'wiki/sources'/f'{ref}.md').exists():errors.append(f'missing source {ref} in {f}')
if len(sources)<5:errors.append('fewer than five source pages')
if len(topics)!=6:errors.append('expected six topic pages')
print(f'sources={len(sources)}, topics={len(topics)}, errors={len(errors)}')
for error in errors:print('FAIL:',error)
sys.exit(bool(errors))
