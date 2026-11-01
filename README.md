# Lab configuration

This is a lightweight container topology for demonstrating segmentation concepts. The incident events are generated as synthetic log files on the host; containers do not execute malware, encrypt files, contact external infrastructure, or collect credentials.

On restricted kernels where Docker bridge networking is unavailable, use the Python-only fallback: run the analysis scripts against `sample-logs/`.
