#!/usr/bin/env python3
"""Safe containment simulation: writes a plan; does not disable real accounts or networks."""
from pathlib import Path
Path('evidence/sample-outputs/containment-actions.txt').write_text("""SIMULATION ONLY\n1. Mark workstation-07 as isolated in the case record.\n2. Block synthetic destination 192.0.2.55 in the simulated policy.\n3. Disable employee1 only in the simulated identity record.\n4. Preserve logs and hashes before cleanup.\nNo real account, interface, firewall, or process was changed.\n""")
print('Wrote simulated containment actions; no real system was modified.')
