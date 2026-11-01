#!/usr/bin/env python3
"""Extract documentation-only IOCs from synthetic logs; no live lookup is performed."""
from pathlib import Path
import re, json, sys
root=Path(sys.argv[1] if len(sys.argv)>1 else 'sample-logs')
text='\n'.join(p.read_text() for p in root.glob('*.log'))
iocs=[]
for value in sorted(set(re.findall(r'192\.0\.2\.55',text))): iocs.append({'category':'IP','indicator':value,'status':'synthetic documentation address'})
for value in sorted(set(re.findall(r'[A-Za-z0-9.-]+\.example\.test',text))): iocs.append({'category':'domain','indicator':value,'status':'synthetic documentation domain'})
for value in sorted(set(re.findall(r'sha256=([a-f0-9]{64})',text))): iocs.append({'category':'sha256','indicator':value,'status':'synthetic test hash'})
for value in sorted(set(re.findall(r'image=([^ ]+)',text))): iocs.append({'category':'process','indicator':value,'status':'simulation event'})
print(json.dumps({'synthetic_input':True,'iocs':iocs},indent=2))
