#!/usr/bin/env python3
"""Validate frozen inputs and optionally build a preview. Never rewrites the thesis."""
from pathlib import Path
import hashlib, json, re
P=Path(__file__).resolve().parents[1]
sources=json.loads((P/'data/sources.json').read_text())
source_ids={s['id'] for s in sources}
baseline=json.loads((P/'data/baseline.json').read_text())
series=json.loads((P/'data/series.json').read_text())
for i in baseline['indicators']:
 assert i['source_id'] in source_ids
 assert all(k in i for k in ['name','value','reference_date','retrieval_date','source_institution','source_url','transformation'])
 assert i['retrieval_date']<=baseline['cutoff']
for c in series:
 assert c==json.loads((P/f'data/series/{c["id"]}.json').read_text())
 assert len(c['labels'])==len(c['values']) and all(isinstance(v,(int,float)) for v in c['values'])
assert series[0]['values']==[i['value'] for i in baseline['indicators'][:4]]
assert series[1]['values'][-1]==baseline['indicators'][4]['value']
assert series[2]['values'][-1]==baseline['indicators'][6]['value']
assert series[3]['values'][0]==baseline['indicators'][9]['value']
assert series[4]['values'][-1]==baseline['indicators'][7]['value']
actual=hashlib.sha256((P/'thesis/THESIS.md').read_bytes()).hexdigest()
assert (P/'thesis/SHA256SUMS').read_text().split()[0]==actual,'Thesis changed: do not silently rehash.'
page=(P/'index.html').read_text();assert actual in page
for path in re.findall(r'(?:src|href)="([^"#]+)"',page):
 if '://' not in path: assert (P/path).exists(),f'Missing local asset: {path}'
expected='window.FAULT_LINES_SERIES = '+json.dumps(series)+';\n'
assert (P/'js/data.js').read_text()==expected,'Browser data differs from source JSON.'
# Exact rendered original-thesis equality, including title and subtitle.
import html
section=re.search(r'<div id="original-thesis-text">(.*?)</div>',page,re.S).group(1)
rendered=[html.unescape(re.sub('<[^>]+>','',t)) for t in re.findall(r'<(?:h3|h4|p)>(.*?)</(?:h3|h4|p)>',section,re.S)]
expected_text=[re.sub(r'^#{1,2} ', '', t) for t in (P/'thesis/THESIS.md').read_text().strip().split('\n\n')]
assert rendered==expected_text, 'Original Thesis differs from THESIS.md'
assert len(re.findall(actual,page))==1
for source in sources:
 assert source['retrieval_date'] <= baseline['cutoff']
 assert source['publication_date'] is None or source['publication_date'] <= baseline['cutoff']
assert next(s for s in sources if s['id']=='brent')['publication_date'] is None
seed=json.loads((P/'data/market-seed.json').read_text())
assert seed['value']==6068.22 and seed['reference_date']=='2026-10-23'
assert len(seed['close_sources'])>=2 and all(s in source_ids for s in seed['close_sources'])
assert 'first' in page and 'FIRST cross' in (P/'METHODOLOGY.md').read_text()
for content in re.findall(r'<meta[^>]+(?:property="og:image"|name="twitter:image")[^>]+content="([^\"]+)"',page):
 if '://' not in content: assert (P/content).is_file()
from PIL import Image
assert Image.open(P/'assets/social-preview.png').size==(1200,630)
print('PASS: exact Original Thesis text, source cutoff, EIA provenance, seed sources, social asset dimensions.')
print(f'PASS: {len(baseline["indicators"])} baseline indicators, {len(series)} charts, source links, local assets, browser dataset and thesis hash.')
print('Final freeze/tag/Pages publication require explicit approval. Social absolute URLs await the verified Pages URL.')

import sys, shutil
if '--build' in sys.argv:
 (P/'dist').mkdir(exist_ok=True)
 for name in ['index.html','css','js','data','thesis','assets','METHODOLOGY.md']:
  src=P/name; dst=P/'dist'/name
  if src.is_dir(): shutil.copytree(src,dst,dirs_exist_ok=True)
  else: shutil.copy2(src,dst)
 print('Built static preview in dist/. No publication performed.')
