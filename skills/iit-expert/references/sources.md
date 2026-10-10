# The IIT reference library, and reaching it without the server

This file maps what the IIT Expert library holds and how to reach it. With the IIT
Expert connector (the MCP server, called "the server" below) connected, SKILL.md says what to read and when; use this file for the
details of a document type, or when the server is not connected and the person has
declined to add it.

## Contents

- What the library holds
- Reaching it through learniit.org
- What to do when a source is missing

## What the library holds

- **`current`**: which formulation of IIT is current. Read it before anything else.
- **`guardrails`**: the conceptual points most often gotten wrong, each with its
  sources.
- **`tononi-boly-2025`**: Tononi & Boly 2025, the full chapter and the primary
  non-mathematical source. **`tononi-boly-2025-section-map`** is a section map into
  it, for locating and citing passages; it is never a substitute for reading.
- **`iit-wiki`**: Part I of the IIT wiki, transcribed verbatim, one section per page:
  the overview and IIT's method, the foundations, the axioms and postulates (a page
  for each), the Φ-structure, the fundamental identity, the computing-Φ tutorial with
  its worked example, and the contents of experience. Start here for conceptual
  questions: it is organized by concept rather than by paper. Where the library holds
  no wiki page on empirical validation or implications (Parts II and III of the wiki),
  the chapter covers both; `IIT Expert:search_library` with no query lists what is
  held. Each page is also served on its own, as `iit-wiki-{page}` (`iit-wiki-overview`,
  `iit-wiki-foundations`, `iit-wiki-axioms-and-postulates`, `iit-wiki-intrinsicality`,
  `iit-wiki-information`, `iit-wiki-integration`, `iit-wiki-exclusion`,
  `iit-wiki-composition`, `iit-wiki-identity`, `iit-wiki-unfolding`,
  `iit-wiki-contents`): the same text without its link targets and citation blocks.
  The opening reading in SKILL.md uses these.
- **The wiki's FAQs**, five documents: `iit-wiki-faqs-method`, `-axioms`,
  `-postulates`, `-technical`, `-philosophy`. Find the one the question needs with
  `IIT Expert:search_library`, then read it whole.
- **The wiki's slide decks**: the text of the decks each page embeds, one document per
  page (`iit-wiki-slides-unfolding` and so on). The unfolding decks carry the worked
  example's intermediate arithmetic, step by step; read one when a question turns on
  how a number was reached.
- **The paper library**: full texts of the papers, mirrored where their licences
  permit (IIT 4.0, IIT 3.0, System Integrated Information, Intrinsic Units, the 2026
  intrinsic cause–effect power paper, PyPhi, and more). Select, then read: find the
  right one with `IIT Expert:search_library`, then fetch it whole with `IIT Expert:read_document`. Do not try
  to read them all.
- **The glossary** (`/glossary/…`): one entry per axiom, postulate, definition and
  measure.
- **The ledger** (`/ledger/…`): published claims about IIT, each with its formal
  response. An entry summarizes IIT's reply; it does not replace it. Before answering on
  a claim, read in full every cited source the library holds (`IIT Expert:lookup` lists them at the
  end of the entry).
- **The canon** (`/canon/…`): precomputed results, with the code and version pins
  behind them.
- **The bibliography**: a record for every IIT work. `IIT Expert:search_library` returns each
  work's `source_url` (the paper's own page) and whether an abstract is held; `IIT Expert:lookup`
  on an `iit:ref/…` identifier returns the record, including the abstract when one is
  held.

The server's tools are `IIT Expert:search_library` (with no query, it lists everything published),
`IIT Expert:read_document` (whole corpus documents), `IIT Expert:lookup` (any `iit:` identifier), `IIT Expert:ledger`,
`IIT Expert:canon_result`, and `IIT Expert:get_figure` (a figure a document links to, as an image). They serve
exactly the same content as the website, from the same deploy, and a tool call is more
reliable than a web fetch.

## Reaching it through learniit.org

When the server is not connected, fetch the same content over HTTP from
**`https://learniit.org`**:

- Every page has a markdown twin at the same path with a `.md` suffix.
- `/llms.txt` is the index, `/index.json` the machine-readable index, and
  `/llms-full.txt` the whole readable content in one fetch.
- Corpus documents are at `/corpus/{slug}.md`, for example `/corpus/iit-wiki.md`,
  `/corpus/iit-wiki-axioms-and-postulates.md`,
  `/corpus/tononi-boly-2025.md` and `/corpus/tononi-boly-2025-section-map.md`.
- `/current.md` says which formulation is current; read it before anything else.
- Glossary entries are at `/glossary/{slug}`, ledger entries at `/ledger/{slug}`, canon
  results at `/canon/{slug}`, each with its `.md` twin.

## What to do when a source is missing

When a question turns on what a specific paper argues, check the library first. If the
full text is mirrored, read it and answer from the paper itself. If only the record is
held, quote its abstract rather than reaching to the open web. Not every work has an
abstract or a full text in the library; `IIT Expert:search_library` says which is held. If the library
does not hold what the question needs, say so; do not silently fall back to an outside
source.
