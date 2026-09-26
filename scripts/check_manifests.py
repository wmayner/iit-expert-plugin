"""Fail if the plugin's manifests disagree with each other.

Claude Code reads ``.claude-plugin/`` and ``.mcp.json``; Codex reads
``.claude-plugin/`` and the Agent Plugins ``mcp.json``, whose ``type`` it
requires; Cursor reads ``.cursor-plugin/``, whose ``plugin.json`` declares the
connector inline because Cursor expects no ``type``. The fields every agent
shows a user must match, and every MCP entry must name the same connector.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHARED = ("name", "version", "description", "homepage", "repository", "license", "author")
MANIFESTS = ("plugin.json", ".claude-plugin/plugin.json", ".cursor-plugin/plugin.json")
MCP_FILES = (".mcp.json", "mcp.json")
MARKETPLACES = (".claude-plugin/marketplace.json", ".cursor-plugin/marketplace.json")


def load(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def problems() -> list[str]:
    found = []
    reference, *others = (load(path) for path in MANIFESTS)
    for path, manifest in zip(MANIFESTS[1:], others):
        for field in SHARED:
            if manifest.get(field) != reference.get(field):
                found.append(f"{path}: {field} differs from {MANIFESTS[0]}")
    urls = {
        path: {server["url"] for server in load(path)["mcpServers"].values()}
        for path in (*MCP_FILES, ".cursor-plugin/plugin.json")
    }
    if len({frozenset(value) for value in urls.values()}) != 1:
        found.append(f"MCP files name different servers: {urls}")
    for path in MARKETPLACES:
        names = [entry["name"] for entry in load(path)["plugins"]]
        if names != [reference["name"]]:
            found.append(f"{path}: lists {names}, expected [{reference['name']!r}]")
    if not (ROOT / "skills" / reference["name"] / "SKILL.md").is_file():
        found.append(f"skills/{reference['name']}/SKILL.md is missing")
    return found


if __name__ == "__main__":
    found = problems()
    for line in found:
        print(line)
    sys.exit(1 if found else 0)
