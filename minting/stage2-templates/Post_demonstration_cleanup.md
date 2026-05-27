<!--
AUTHOR: Erik Schultes
PROJECT: Making MAC FAIR
SESSION: Article - FDT Paper (2)
DATE: 2026-05-27
URL: https://claude.ai/chat/31fe2171-4e02-49d2-ac53-79d3d78c2ee3
CREATED_AT: P113/R113
DESCRIPTION: Items deferred to a coordinated MAC v2 + MAC FDT revision pass before paper submission. Demonstration-grade artifacts (Stage 3 instances) proceed against current MAC v2 drafts; cleanup is consolidated rather than incremental.
-->

# Post-Demonstration Cleanup Log

Items deferred from Stage 3 demonstration to a single coordinated revision pass before paper submission. Rationale: incremental fixes are wasteful; one pass handles both MAC v2 (7 templates + Project + 2 Datasets) and MAC FDT (11 templates + 38 instances) cosmetic, completeness, and provenance issues together.

## Promote draft nanopubs to non-draft

The StayAhead Project FDO and both Dataset FDOs referenced by Stage 3 instances are currently `npx:DraftNanopub`. All 38 FDT instances will inherit draft references via `dct:isPartOf` (Project) and `dct:source` (Datasets).

| Nanopub | Trusty URI | Status |
|---|---|---|
| StayAhead Project FDO | `RAFPOe4OIl_urs-U_7-FostjzcUo8ra6LasfSvGplOvto` | `npx:DraftNanopub` |
| ESM Dataset FDO | `RA9YxiABPRNy3rrJm20p1oanJchBcI22IPpSu36zj2MLs` | `npx:DraftNanopub` |
| AlphaFold Dataset FDO | `RAv6JJe-lvoadhNwml8pzSLs5aOtbU1xbHT5qgFtgwQ-s` | `npx:DraftNanopub`; label typo "AphaFold2" (missing 'l') |

**Action in revision pass:**
1. Mint non-draft v2 of each, using `npx:supersedes` to link to the current drafts.
2. Fix the "AphaFold2" → "AlphaFold2" typo in the AlphaFold dataset label.
3. Update Stage 3 FDT instances (38 nanopubs) to reference the v2 URIs via `npx:supersedes` chain.
4. Coordinate with MAC v2 authors (Max van den Boom et al.) — these are MAC v2 artifacts, not MAC FDT.

## Observation-specific authorities (Types 2–8)

SPS v1.3 introduced `cito:citesAsAuthority` as optional + repeatable on observation Types 2–8 for one-hop attribution to observation-specific publications. For Stage 3 demonstration minting, all 30 observation instances will be minted **without** this predicate; provenance is reached via the two-hop method-attribution pattern (`mac:has{Surveillance,Prediction,Experimental}Method` → method FDO → `cito:citesAsAuthority`).

**Action in revision pass:** for each Type 2–8 observation, identify whether a canonical observation-specific publication exists distinct from the method paper. If yes, add `cito:citesAsAuthority` via `npx:supersedes` of the demonstration instance. Examples likely to warrant addition:

- Type 7 (DMS): Starr et al. 2020 *Cell* — already covered by the two-hop via Type 10 method FDO; one-hop addition is redundant unless variant-specific DMS publications exist.
- Type 8 (WHO classification): situation-report URLs for specific dates would qualify; these belong on the observation itself, not on the Type 11 method FDO.
- Type 2 (real-world occurrence): unlikely; surveillance is collective.

## Process notes

- Track this log alongside `Stage3_pre_minting_notes.md` (pre-minting checklist) and the `SPS_v1_4_update_log.md` (now archived since v1.4 merged).
- The revision pass becomes its own session: SPS v1.5 (if needed), then a coordinated supersession of MAC v2 + MAC FDT artifacts.
- Triggers for opening the revision pass: arXiv submission deadline (23 May 2026 — already passed), or *Scientific Data* submission deadline (14 August 2026).
