#!/usr/bin/env python3
"""Parse synthetic incident logs and produce a concise event summary."""
from pathlib import Path
import re, json, sys
root=Path(sys.argv[1] if len(sys.argv)>1 else 'sample-logs')
rows=[]
for p in sorted(root.glob('*.log')):
    for line in p.read_text().splitlines():
        if line.startswith('#') or not line.strip(): continue
        m=re.match(r'^(\S+) (\S+) (.+)$',line)
        if m: rows.append({'timestamp':m.group(1),'asset':m.group(2),'event':m.group(3),'source':p.name})
summary={'synthetic_input':True,'events':len(rows),'alerts':[r for r in rows if 'FAIL' in r['event'] or 'SUSPICIOUS' in r['event'] or 'SIMULATED' in r['event'] or 'RENAME' in r['event']]}
print(json.dumps(summary,indent=2))
