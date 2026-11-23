#!/usr/bin/env python3
"""Static validations for Tea Wiki educational HTML slide deck."""
from pathlib import Path
from bs4 import BeautifulSoup
import re, sys
root=Path(__file__).resolve().parents[1]
p=root/'slides/deck.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
slides=s.select('.slide')
issues=[]
if not 10<=len(slides)<=12:issues.append('Slide count must be 10–12')
if not all(sl.get('data-title') and sl.select_one('h1,h2') for sl in slides):issues.append('Slide heading missing')
if not all(sl.select_one('.footnotes') for sl in slides):issues.append('Slide notes missing')
for a in s.select('a[href]'):
 href=a['href']
 if href.startswith('../') and not (p.parent/href).resolve().exists():issues.append(f'Broken relative link {href}')
for e in ['prev','next','counter','progress','sourceButton','sourceClose','sourceDetails']:
 if not s.select_one('#'+e):issues.append('Missing UI: '+e)
js=s.select_one('script').get_text()
for token in ['ArrowLeft','ArrowRight','show(index+1)','show(index-1)','sourceContents']:
 if token not in js:issues.append('Missing JS behavior: '+token)
if any(not sl.get_text(strip=True) for sl in slides):issues.append('Empty slide')
if any('https://www.tbrs.gov.tw/' not in str(sl) for sl in slides[-1:]):issues.append('Reference slide missing official source URLs')
print('PASS' if not issues else 'FAIL', ':',len(slides),'slides,',len(s.select('a[href]')),'links;',len(issues),'errors')
for x in issues:print('-',x)
sys.exit(bool(issues))
