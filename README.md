# IIT Expert

IIT Expert helps an AI assistant answer questions about Integrated Information
Theory from the theory's primary literature: the IIT wiki, the papers, and a
glossary of the axioms, postulates and measures. The plugin installs two
things. The connector, served at `https://mcp.learniit.org`, gives the
assistant those sources. The `iit-expert` skill tells it to read them before
answering, and to cite where each claim comes from, instead of relying on what
it already believes about IIT. The same content is published at
[learniit.org](https://learniit.org).

## Work in progress

The corpus and glossary are still being checked against the sources, so some
answers will be incomplete. If the assistant says something wrong about IIT, or
can't answer a question it should be able to, please open an issue.

## Installation

**Claude Code**

```
claude plugin marketplace add wmayner/iit-expert-plugin
claude plugin install iit-expert@iit-expert
```

**Codex**

```
codex plugin marketplace add wmayner/iit-expert-plugin
codex plugin add iit-expert@iit-expert
```

**Cursor:** open Customize → From GitHub Repository and enter `wmayner/iit-expert-plugin`.

**claude.ai and Claude Desktop** cannot install plugins from this repository; follow <https://learniit.org/install>.

To compute IIT quantities, pair it with PyPhi's MCP server, described at
<https://pyphi.readthedocs.io/en/latest/howto/ai-assistants.html>.

## Keeping the skill current

The skill's source is maintained in the IIT Expert repository and copied here
with its `build/sync_plugin.py`, which also sets the version in both manifests.
Claude Code offers an update only when the version changes.
`scripts/check_manifests.py` runs on every push and fails if the manifests
disagree.

## Licence

CC BY 4.0 (see LICENSE). Quoted material remains under its authors' rights.
