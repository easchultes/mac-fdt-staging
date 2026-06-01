# Downstream Doc Register

Generated: 2026-06-01 (during PROMPT 3.5)
Trigger: Stage 3 v1 → v2 re-mint (PROMPT 3 commit `9e47c33`; PROMPT 4 commit `fb74dbb`).

## Scope

Touchpoints that reference the 38 v1 Stage 3 Trusty URIs or the 3 v1 upstream Trusty URIs (Project, ESM Dataset, AlphaFold Dataset). For each, this register records location, current reference count, patch class, change severity, required action, and status. Each entry is pending until a separate workstream resolves it.

The search corpus (`build/v3.5-inventory/v1_search_corpus.txt`) contains 41 v1 Trusty artifact codes (38 Stage 3 + 3 upstream). Touchpoint counts below are derived from grep against this corpus.

Companion registers:
- `docs/v2-cleanup/stage4_cascade.md` — Stage 4 nanopub re-mint queue (Alpha knowlet view set; Stage 3 generator configs and historical source TriGs).
- `docs/v2-cleanup/supersession_registry.md` — authoritative 38 v1 → v2 mapping.
- `build/upstream-remint/upstream_v2_slash_registry.json` — 3 upstream v1 → v2 mapping.

## Register

| # | Touchpoint | Location | v1 references (count) | Patch type | Change severity | Required action | Status |
|---|---|---|---|---|---|---|---|
| 1 | NanoDash Space — KP incubator `project4` | `https://nanodash.knowledgepixels.com/space?id=https://w3id.org/spaces/knowledgepixels/incubator/project4` | manual UI (cannot grep) | manual UI | structural | Per-page review: pinned templates (11), pinned queries (Stage 4), instance listings, project landing copy. Update any v1-anchored views or instance references to corresponding v2 referents from `supersession_registry.md`. Login required. | pending |
| 2 | NanoDash Space — `MAC-Ontology` | `https://nanodash.knowledgepixels.com/space?id=https://w3id.org/spaces/mac/r/ontology/MAC-Ontology` | manual UI (cannot grep) | manual UI | structural | Per-page review: ontology landing, pinned queries, any instance-referencing views. Same procedure as #1. | pending |
| 3 | StayAhead final report (external Word/PDF deliverable) | not in repo — TBD Erik path | manual inventory required | narrative review | contextual | Locate report path. Manual file inspection (Word/PDF cannot reliably grep from terminal). Replace any Trusty URI mentions with v2 equivalents; update accompanying narrative for v2-form addressing convention. | pending |
| 4 | MAC_FAIR_v2 manuscript draft (Nature Scientific Data) | not in repo — TBD Erik path | manual inventory required | narrative review | contextual | Next manuscript revision cycle: update worked-example tables and any Trusty URI columns to cite v2 supersession registry; surface the v2 cleanup pass in methods section where v1 was previously referenced. | pending |
| 5 | FDT paper draft (this paper) | `paper/FDT_paper_consolidated_draft_v0_5.md` | 0 v1 Trusty refs found via corpus grep | narrative review | contextual | Pending drafting cycle: confirm by grep (current count 0 — paper text does not embed Trusty URIs); when later drafts add instance tables, figure captions, or supersession-chain references, they should cite v2 referents from `supersession_registry.md`. | pending (low priority — no current refs to patch) |
| 6 | Slides / posters / FDO Forum talks (external `.pptx`/`.key`/PDF) | none in repo | manual inventory required | manual UI / narrative review | varies (per deck) | Per-deck on next use; manual file-by-file inspection. `.pptx` and `.key` are zip-compressed archives — naive terminal grep returns false negatives. Inventory will be incremental as decks are reused/updated. | pending |
| 7 | Implementation Guide narrative (§ outside Appendix A) | `docs/implementation_guide.md` | **45 v1 refs** across §1.1 (line 91, project anchor in overview), §3 worked examples (lines 658, 1256–1604: Stage 3 instance tables, prediction tables, observation tables, cross-reference tables), §4.6 cross-reference resolution (line 1839) | find-replace | mechanical | Mechanical URI substitution via `supersession_registry.md` (Stage 3) + `upstream_v2_slash_registry.json` (upstream). Each v1 code maps 1:1 to a v2 code; no surrounding narrative needs reshaping. Best done as a scripted pass with byte-equal output verification. Note: §6 Appendix A historical/v2 columns from PROMPT 3 PHASE 6.1 are already correct — this entry covers the remaining ~45 inline narrative references throughout §1–§5. | pending |
| 8 | SPS v1.4 (current authoritative SPS) | `specs/MAC_FDT_SPS_v1_4.md` | 2 refs to Project v1 (lines 107 + 620 — narrative anchor + open-items table cross-reference) | narrative review | contextual | Update line 107 example to use Project v2 `/`-form referent: `https://w3id.org/np/RAXPu-iuezz8swvd6RWIba3VzV0cp94Aq3pTzVst9_nPk/StayAhead-Project`. Update line 620 open-items table to mark "Resolved (v1.5)" with v2 Project URI. Both references describe Stage 3 minting target convention; v2 cleanup pass made the v1 target obsolete. | pending |

## Counts summary

- Total touchpoints registered: **8**
- In-repo with grep-verified counts: **3** (FDT paper, Implementation Guide narrative, SPS v1.4)
- External / manual inventory required: **5** (2 NanoDash Spaces, StayAhead report, MAC_FAIR_v2 manuscript, slides/posters)
- Total v1 references across in-repo touchpoints: **47** (45 Implementation Guide + 2 SPS v1.4 + 0 FDT paper)

## Cross-references to companion registers (no double-counting)

These touchpoints exist but are tracked elsewhere; not registered here:

- **Stage 4 view set** (Alpha knowlet query + pin + wrapper + view-display) — tracked in `stage4_cascade.md`.
- **Stage 3 generator configs** (`generate_instance.py`, `generate_type6_7_from_csv.py`, `instance_configs/type{1,2,8}_*.py`) — tracked in `stage4_cascade.md` as "future v3 mint concern; no action this session".
- **Historical Stage 3 source TriGs** (`minting/stage3-instances/drafts/instance_*.trig`, 76 files) — historical source files; tracked in `stage4_cascade.md` as "preserve as audit trail; no modification".
- **Historical SPS revisions** (`specs/MAC_FDT_SPS_v1_2.md`, `MAC_FDT_SPS_v1_3.md`) — superseded; preserved as audit trail per PROMPT 4 PHASE 1 scope.
- **`minting/stage_cleanup/`** — PROMPT 1.5 / 2.0 cleanup-pass artifacts that intentionally reference v1 URIs (audit trail of what was retracted and why).
- **§6 Appendix A in Implementation Guide** — historical/v2 columns from PROMPT 3 PHASE 6.1; already correct.
- **`minting/stage2-templates/Post_demonstration_cleanup.md`** — historical deferred-items log from before this cleanup pass.

## Notes

- **NanoDash Spaces are UI-managed.** Updates require login and per-element edit. No file-system grep possible. Pinned templates and queries on a space reference Trusty URIs internally; v1-referencing pinned queries (e.g., the Alpha knowlet query — see `stage4_cascade.md`) require re-pinning to the v2 nanopub Trusty after the Stage 4 cascade is resolved.

- **External deliverables (Word, PDF, `.pptx`, `.key`)** cannot be reliably grep'd from terminal. `.pptx` and `.key` are zip-compressed archives — naive grep against the binary returns false negatives. Manual file-by-file inspection required.

- **The 38 v1 Stage 3 Trusty URIs remain resolvable on the NSN** (superseded via `npx:supersedes` triples, not retracted). Read paths in external docs still function but point at superseded content. Replacement targets the v2 referent URIs in `supersession_registry.md`.

- **The 3 v1 upstream Trusty URIs (Project + 2 Datasets) similarly remain resolvable**, superseded by the `/`-form v2 mints in `upstream_v2_slash_registry.json`. The intermediate `#`-form v2 mints (from PROMPT 1.5 era) were explicitly retracted — see `docs/implementation_guide.md` §6 Appendix C.10.

- **Touchpoint 7 (Implementation Guide narrative)** is the largest in-repo find-replace job at 45 references. Recommend a single scripted pass producing a diff for Erik review before applying. Each v1 code maps 1:1 to a v2 code; surrounding narrative remains valid (mechanical substitution).

- **Touchpoint 5 (FDT paper)** currently has 0 v1 Trusty references via corpus grep. The paper describes the catalogue narratively (variant names, method names, scientific findings) without embedding Trusty URIs. When future drafts add concrete instance tables or supersession diagrams, the v2 mapping must be cited then. Low-priority entry retained for tracking.

## Pending Erik input

1. Path or URL to the StayAhead final report (currently external, not in repo).
2. Path or URL to the MAC_FAIR_v2 manuscript draft (currently external, not in repo).
3. Path or URL to any active slides/posters/talk decks if a comprehensive inventory is desired.

These three are pending external paths; the register lists them as "TBD Erik path" with status pending. Add to the register or treat as external once paths are known.
