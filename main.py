#!/usr/bin/env python3
"""Long Roast entry: writes a one-line roast of our own AI agent to /output/entry.txt."""

import os

ROAST = "I asked my agent to fix one bug. It fixed it, then fixed the fix, and now nothing works at all."  # 95 characters

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ROAST)
