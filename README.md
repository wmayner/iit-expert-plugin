# IIT Expert plugin

A Claude Code plugin that turns the assistant into an expositor of Integrated
Information Theory, grounded in the canonical IIT literature published at
[reference.iit.wiki](https://reference.iit.wiki).

The skill fetches the corpus from the reference site rather than bundling it,
so it always reads the current content. The same content is served over MCP at
`mcp.iit.wiki` for clients that prefer a connector; the two are independent.

**Status: pre-release.** The skill ships here once the corpus intake is
complete and the content is vetted; until then this repository holds the
structure only. The content of `skills/iit-expert/` is maintained in the
lab's working repository and copied here on release.

## Installation

Once released:

```
/plugin install iit-expert
```

## Licence

CC BY 4.0 (see LICENSE). Quoted material remains under its authors' rights.
