#!/usr/bin/env python3
from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[1]
v=(root/'VERSION').read_text().strip()
a,b,c=map(int,v.split('.'))
if c<9: c+=1
else: b+=1; c=0
new=f"{a}.{b}.{c}"
(root/'VERSION').write_text(new+'\n')
for path in [root/'plugins/java-pro-skills/.claude-plugin/plugin.json',root/'.claude-plugin/marketplace.json']:
    obj=json.loads(path.read_text())
    if path.name=='plugin.json': obj['version']=new
    else:
        obj['version']=new
    path.write_text(json.dumps(obj,indent=2)+'\n')
print(f'{v} -> {new}')
