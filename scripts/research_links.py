#!/usr/bin/env python3
from pathlib import Path
import sys
text=(Path(__file__).resolve().parents[1]/'docs'/'official-source-map.md').read_text()
q=' '.join(sys.argv[1:]).lower()
if not q:
    print(text); raise SystemExit
blocks=text.split('## ')[1:]
for b in blocks:
    title=b.splitlines()[0]
    if any(w in (title+' '+b).lower() for w in q.split()):
        print('## '+b.strip()+'\n')
