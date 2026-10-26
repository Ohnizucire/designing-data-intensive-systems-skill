#!/usr/bin/env python3
"""Offline source and three-agent installation-layout smoke tests."""
from pathlib import Path
import re
import shutil
import tempfile

REPO = Path(__file__).resolve().parents[1]
NAME = "designing-data-intensive-systems"
SOURCE = REPO / "skills" / NAME
assert (SOURCE / "SKILL.md").is_file()
assert len(list(REPO.rglob("SKILL.md"))) == 1
frontmatter = (SOURCE / "SKILL.md").read_text()
assert frontmatter.startswith("---\nname: designing-data-intensive-systems\n")
assert re.search(r"(?m)^description: Use when ", frontmatter)
assert len(list((SOURCE / "references").glob("*.md"))) == 15

with tempfile.TemporaryDirectory() as tmp:
    for agent, path in {
        "claude-code": ".claude/skills",
        "codex": ".agents/skills",
        "hermes-agent": ".hermes/skills",
    }.items():
        installed = Path(tmp) / agent / path / NAME
        shutil.copytree(SOURCE, installed)
        assert (installed / "SKILL.md").exists()
        assert (installed / "references" / "decision-record.md").exists()
        for link in re.findall(r"\]\(([^)]+)\)", (installed / "SKILL.md").read_text()):
            if link.startswith(("http://", "https://", "#")):
                continue
            assert (installed / link.split("#", 1)[0]).exists(), (agent, link)
        print("PASS", agent)
print("3/3 offline agent layout checks passed")
