#!/usr/bin/env python3
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]/'plugins'/'java-pro-skills'/'skills'
for p in sorted(root.glob('*/SKILL.md')):
    t=p.read_text()
    n=re.search(r'^name:\s*(.+)$',t,re.M).group(1).strip()
    d=re.search(r'^description:\s*(.+)$',t,re.M).group(1).strip()
    print(f"{n:40} {d}")
