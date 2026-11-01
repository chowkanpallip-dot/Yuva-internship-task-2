#!/usr/bin/env python3
"""Print SHA-256 hashes for evidence files."""
from pathlib import Path
import hashlib,sys
for name in sys.argv[1:]:
 p=Path(name); print(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p}")
