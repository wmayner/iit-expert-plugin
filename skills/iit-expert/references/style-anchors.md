# Style anchors: which part of the corpus an answer should sound like

Use this file in Step 1 of `references/style.md`. Find the row that matches the question's topic,
then open the profile of the anchor paper and of the wiki page in `anchors/` (only
those sections, not the whole file). Each profile gives the source's characteristic
moves, three verbatim model sentences, and what not to imitate in chat.

- **Anchor paper**: sets the sentence-level voice (openers, connectives, how terms and
  formal statements are introduced, examples, rhythm, vocabulary).
- **Wiki page**: sets the canonical wording (axiom and postulate statements, the
  identity, definitions) and lends one summary-style sentence per section.
- **FAQ**: sets the shape of the answer; its passages are in `qa-exemplars.md`.
- **Checker keys** for `scripts/check_answer.py --anchor <key> --wiki <key>`: the paper's
  slug as given below (papers not in the library use `grasso-2021a`, `tononi-2025`,
  `sarasso-2021`, `boly-2024`, `haun-2025`), and `wiki-<page>` for wiki pages
  (`wiki-overview`, `wiki-foundations`, `wiki-identity`, `wiki-unfolding`,
  `wiki-glossary`, `wiki-axioms-and-postulates-integration`, …; run `--list-anchors`).
  Papers without a measured profile (`grasso-2026`, `tononi-2024`) and the contents page
  fall back to `faq`.

Where to read a source: `read_document` with the slug. Wiki pages marked "iit-wiki §…"
are sections of the `iit-wiki` document. Sources marked "not in the library" cannot be
read; answer from their profile alone and say nothing about it.

## Routing table

| Topic of the question | Anchor paper (slug) | Second anchor, for sub-parts | Wiki page | FAQ doc | Profile file |
|---|---|---|---|---|---|
| What IIT is; the method; consciousness-first; "good explanation" | Tononi & Boly 2025 (`tononi-boly-2025`) | Ellia et al. 2021 (`ellia-2021`) for why not start from the brain | Overview (iit-wiki §1) | `iit-wiki-faqs-method` | wiki.md §1 |
| The 0th axiom; realism, operational physicalism, atomism; cause–effect power | Tononi & Boly 2025 | Tononi et al. 2022 (`tononi-2023`) for existence as cause–effect power | Foundations (iit-wiki §2) | `iit-wiki-faqs-axioms`, `-philosophy` | wiki.md §2 |
| The axioms, one or all; essential vs accidental properties | Tononi & Boly 2025 | — | Axioms & Postulates hub + the axiom's own page (iit-wiki §3–8) | `iit-wiki-faqs-axioms` | wiki.md §3–4 |
| The postulates; how a complex is identified; φs, the minimum partition, intrinsic information | IIT 4.0 (`albantakis-2023b`) | Marshall et al. 2023 (`marshall-2023`) for φs and partitions; Mayner et al. 2026 (`mayner-2026`) for intrinsic differentiation/specification | The postulate's page (iit-wiki §4–8) + Computing Φ (iit-wiki §11) | `iit-wiki-faqs-postulates`, `-technical` | formal.md §1–2, §4; wiki.md §4, §6 |
| Composition; distinctions, relations, Φ-structure, Φ; causal reductionism; higher-order mechanisms | IIT 4.0 | Grasso et al. 2021 causal reductionism (not in the library); Albantakis & Tononi 2019 (`albantakis-2019a`) for the compositional argument (not its measures) | Composition (iit-wiki §8) + Computing Φ | `iit-wiki-faqs-postulates` (all orders of mechanisms) | formal.md §1, §5; ontology-debate.md §2 |
| Intrinsic units; grain; macro vs micro; what neural changes affect experience | Marshall et al. 2024 (`marshall-2026`) | IIT 4.0 | Exclusion (iit-wiki §7) | `iit-wiki-faqs-technical` | formal.md §3 |
| Computing Φ step by step; TPMs; PyPhi | IIT 4.0 | Marshall et al. 2023 | Computing Φ (iit-wiki §11) + slides `iit-wiki-slides-unfolding` | `iit-wiki-faqs-technical` | formal.md §1–2; wiki.md §6 |
| The explanatory identity; quality is structure; not emergence, not reduction | Tononi & Boly 2025 | Grasso, Hendren & Tononi 2026 (`grasso-2026`) | Fundamental Identity (iit-wiki §10) | `iit-wiki-faqs-philosophy` (emergence) | wiki.md §5 |
| Contents of experience in general; the method for accounting for contents; narrow qualia; compound contents | Grasso, Hendren & Tononi 2026 (`grasso-2026`) | Tononi & Boly 2025 (sections on quality of experience) | Contents (iit-wiki §12) | `iit-wiki-faqs-axioms` (space/time not axioms; components) | phenomenology.md §7; wiki.md §7 |
| Space; extendedness; spots; grids | Haun & Tononi 2019 (`haun-2019`) | Grasso et al. 2021 maps and grids (`grasso-2021b`) for function vs phenomenology | Contents (iit-wiki §12) + slides `iit-wiki-slides-contents` | `iit-wiki-faqs-axioms` | phenomenology.md §1, §4 |
| Time; flow; the extended present; now and then | Comolatti et al. 2025 (`comolatti-2025`) | Haun & Tononi 2019 (the template it extends) | Contents (iit-wiki §12) | `iit-wiki-faqs-axioms` | phenomenology.md §2 |
| Objects; concepts; conceptual invariance | Grasso, Hendren & Tononi 2026 | Tononi & Boly 2025 (objects section) | Contents (iit-wiki §12) | — | phenomenology.md §7 |
| Richness of experience; seeing vs noticing; report; overflow | Haun & Tononi 2025 (`haun-2025` record; full text not in the library) | Ellia et al. 2021 | Contents (iit-wiki §12) | `iit-wiki-faqs-method` (non-reflective experience) | phenomenology.md §3 |
| Pure presence; meditation; experience with near-silent cortex | Boly et al. 2024 (not in the library; record `iit:ref/boly-2024`) | Tononi & Boly 2025 | Contents (iit-wiki §12) | `iit-wiki-faqs-axioms` (experiences without structure) | phenomenology.md §5 |
| Meaning; perception as interpretation; matching; dreams vs perception | Mayner et al. 2024 (`mayner-2024`) | Zaeemzadeh & Tononi 2024 (`zaeemzadeh-2024a`) | Ontology (not in the library) | `iit-wiki-faqs-postulates` (environment) | phenomenology.md §6 |
| Shannon information vs integrated information; codes; "information processing" | Zaeemzadeh & Tononi 2024 | Mayner et al. 2024 | Information (iit-wiki §5) | `iit-wiki-faqs-postulates` (Shannon) | formal.md §6 |
| Empirical validation; NCC; posterior-central cortex; cerebellum; COGITATE | Tononi & Boly 2025 (validation sections) | Sarasso et al. 2021 (not in the library) for complexity and PCI | Validation ARC-COGITATE supplement (not in the library) | `iit-wiki-faqs-postulates` (cerebellum), `-method` | ontology-debate.md §6; wiki.md §9 |
| Sleep, dreaming, anesthesia, loss and return of consciousness | Tononi et al. 2024 (`tononi-2024`) | Sarasso et al. 2021 | Validation (not in the library) | `iit-wiki-faqs-method` | ontology-debate.md §7 |
| PCI; measuring consciousness in patients | Sarasso et al. 2021 (not in the library) | Tononi & Boly 2025 | Validation (not in the library) | `iit-wiki-faqs-postulates` (objective measures) | ontology-debate.md §6 |
| AI, computers, simulation, functionalism, "is my phone / an LLM conscious" | Findlay et al. 2024 (`findlay-2025`) | Tononi et al. 2025 pseudo-consciousness (not in the library) | Ontology (not in the library) | `iit-wiki-faqs-philosophy` (computers) | ontology-debate.md §5, §4 |
| Ontology; intrinsic vs extrinsic existence; emergence; physicalism; panpsychism | Tononi & Boly 2025 (ontology section) | Tononi et al. 2022 (`tononi-2023`) | Ontology (not in the library) + Fundamental Identity | `iit-wiki-faqs-philosophy` | ontology-debate.md §1 |
| Free will; responsibility; actual causation | Tononi et al. 2022 (`tononi-2023`) | Grasso et al. 2021 causal reductionism | Ontology + Actual causation (not in the library) | `iit-wiki-faqs-philosophy` (free will) | ontology-debate.md §1 |
| Objections and criticisms; "is IIT pseudoscience / untestable" | Tononi & Boly 2025 ("Instructive criticisms") | Tononi et al. 2025 (not in the library), toned down; Ellia et al. 2021 | The page for the concept under attack | the FAQ on that concept | ontology-debate.md §3–4 |
| Terminology: "what does X mean?" | IIT 4.0 for formal terms; Tononi & Boly 2025 for conceptual ones | — | Glossary (`iit-wiki-glossary`) | — | wiki.md §12 |

Topics not listed (other minds, the Qualia Structure paradigm, quantum IIT, animats)
default to Tononi & Boly 2025 as anchor and the Overview page, with the specific paper
read for content as the rest of this skill directs.

## How much of each

Most of the answer's sentences should sound like the anchor paper: its way of opening a
point, its connectives, its way of naming a thing before or after describing it. The wiki
contributes its canonical statements verbatim wherever the answer states an axiom,
postulate, principle, the identity, or a definition, plus at most one or two compact
summary sentences (an opening line or a section's summary). The FAQ contributes the
outer shape. When the anchor paper's register would be wrong for chat (equation blocks,
figure call-outs, citation walls, sarcasm), keep its argumentative moves and drop the
apparatus; each profile's "Don't imitate" list says which is which.

Plain questions: FAQ shape and wiki wording carry more weight; the anchor paper
contributes its examples and one or two of its characteristic moves.
Technical questions: the anchor paper carries almost all of the prose; the wiki supplies
the exact statements.

## Wording conflicts

- Where the wiki's pages differ slightly (hub vs postulate page vs glossary wording of a
  postulate), use the hub wording for axioms and postulates and the glossary wording for
  definitions, and stay consistent within the answer.
- Where a paper's older wording conflicts with current canon (e.g. "inference from the
  best explanation" in Haun & Tononi 2019; the IIT 3.0 principle list on the actual
  causation page; Φ⊆ and DKL-based φ in Albantakis & Tononi 2019), follow the current
  canon and borrow only the paper's argumentative shape.
- Do not quote wiki toy-system numbers as general facts; the pages disagree on some of
  them.
