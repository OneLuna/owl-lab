#!/usr/bin/env python3
"""Check local Markdown links in source QMD files."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
missing = []
published = [
    root / "index.qmd", root / "research/index.qmd", root / "people.qmd",
    root / "notebook/index.qmd", root / "news.qmd", root / "about/index.qmd", root / "en/index.qmd",
    root / "en/research/index.qmd", root / "en/people.qmd",
    root / "en/notebook/index.qmd", root / "en/news.qmd", root / "en/about/index.qmd",
]
for source in published:
    for raw in pattern.findall(source.read_text(encoding="utf-8")):
        target = raw.split("#", 1)[0].strip().strip("<>")
        if not target or "://" in target or target.startswith(("mailto:", "#")):
            continue
        if not (source.parent / target).resolve().exists():
            missing.append(f"{source.relative_to(root)} -> {target}")
if missing:
    print("Missing local links:\n" + "\n".join(f"- {item}" for item in missing))
    sys.exit(1)

published_chinese = [
    Path("index.qmd"), Path("research/index.qmd"), Path("people.qmd"),
    Path("notebook/index.qmd"), Path("news.qmd"), Path("about/index.qmd"),
]
for relative in published_chinese:
    mirror = root / "en" / relative
    if not mirror.exists():
        missing.append(f"missing English mirror for {relative}")
if missing:
    print("Architecture errors:\n" + "\n".join(f"- {item}" for item in missing))
    sys.exit(1)
print("All source QMD links resolve and published routes have English mirrors.")
