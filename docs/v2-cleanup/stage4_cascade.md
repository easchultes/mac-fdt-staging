# Stage 4 Cascade Register

Generated: 2026-06-01 (during PROMPT 3 PHASE 5)
Trigger: Stage 3 v1 → v2 re-mint (38 instances published this session)

## Scope

Stage 4 nanopubs and other repository artifacts referencing Stage 3 v1 Trusty URIs. Each entry below requires a future re-mint pointing at the corresponding v2 Trusty, or a documentation update.

The repo-wide search excluded the cleanup-pass directories (`build/`, `docs/v2-cleanup/`, `.git/`) to avoid self-matching the v1 cache, the supersession chain artifacts, and the audit register.

## Stage 4 nanopub artifacts (1 cascade)

### Alpha digital-twin knowlet view set

The Alpha knowlet SPARQL view in Stage 4 hardcodes the Alpha-RBD-Variant v1 Trusty URI as a constant in the query. The other 3 Stage 4 views (catalogue summary, variants by WHO, observations per method) are generic and do not hardcode specific Stage 3 instance URIs — they remain valid.

**Files with v1 reference:**
- `minting/stage4-views/drafts/query_alpha-knowlet_v1.trig` — assertion graph hardcodes `<https://w3id.org/np/RA4BHII2Bz7HfpUkaSJqNmhjF8F7hyWpCJnvXYkA4EP_M/Alpha-RBD-Variant>`
- `minting/stage4-views/drafts/signed/query_alpha-knowlet_v1.trig` — signed counterpart

**Published Stage 4 Trusty URIs (per Appendix A.4):**
| View nanopub | Stage 4 Trusty URI |
|---|---|
| Alpha knowlet query | `https://w3id.org/np/RAecvUbvUWiIOKP7ZEQk7hnUsb8lWWUr1lRbVN2PsSUSA` |
| Sidebar pin-action | `https://w3id.org/np/RAzEolNOqr8I1aiZpafpUxJfqBOQRdTapceYWjXCoEYAE` |
| `gen:View` wrapper | `https://w3id.org/np/RA_zvbVo3VX6Cy3lYOI6LNHJICb1copbCmJHayjpzCeJ0` |
| `gen:ViewDisplay` | `https://w3id.org/np/RA-QuZXXV9ni6b2YW0cM4ADyzYi-Uo4FQDR0p2pdR9tUk` |

**v1 references inside the view set:** the query nanopub references the Alpha-RBD-Variant v1 Trusty. The pin-action, wrapper, and view-display nanopubs reference the query nanopub itself (not the Stage 3 instance), so they cascade indirectly: re-minting the query produces a new query Trusty, which the wrapper would then point at if re-minted.

**Required re-mint:**
- Query: replace `<https://w3id.org/np/RA4BHII2Bz7HfpUkaSJqNmhjF8F7hyWpCJnvXYkA4EP_M/Alpha-RBD-Variant>` with `<https://w3id.org/np/RAngbyT2iZe4xYUcPnTnDFKDaiL5-tSmoUYzF9RK3LHdE/Alpha-RBD-Variant>` (Alpha-RBD-Variant v2 referent from `pass1_referent_map.json`).
- Pin-action / wrapper / view-display: re-mint to point at the new query Trusty. Wrapper local name (`fdt-alpha-knowlet-view`) and pin-action structure preserved.

**Status:** pending (deferred from this session).

**Repo-wide v1 reference confirmation:**
The repo-wide search confirmed only `query_alpha-knowlet_v1.trig` (and its signed counterpart) hardcodes a Stage 3 v1 Trusty among the 16 Stage 4 nanopubs. The other 12 (catalogue, variants-by-WHO, observations-per-method × 4 each) reference templates and ontology terms but not specific Stage 3 instances.

## Other artifact hits (not Stage 4 nanopubs)

The repo-wide search of v1 Trusty codes also surfaced these classes of files. None require nanopub re-mint; some need documentation updates (PHASE 6.1).

### Historical Stage 3 source TriGs

Every v1 Trusty appears in its corresponding Stage 3 v1 source TriG under `minting/stage3-instances/drafts/`. These are the **source files** from which the v1 nanopubs were minted — they ARE the historical Stage 3 v1. By convention, source TriGs are not modified after publish; they remain as historical record.

- `minting/stage3-instances/drafts/instance_*.trig` (38 unsigned)
- `minting/stage3-instances/drafts/signed/instance_*.trig` (38 signed)
- `minting/stage3-instances/drafts/PUBLISHED_*.md` (publication records — historical, not updated)

**Action:** none. These are historical source files. The Stage 3 v2 cleanup intentionally lives in `build/v2-dryrun/` and `docs/v2-cleanup/` rather than rewriting `minting/stage3-instances/drafts/`.

### Stage 3 generator configs

- `minting/stage3-instances/generator/generate_type6_7_from_csv.py` — embeds Stage 3 v1 Trustys as constants (e.g., for the AgMata, BloomLab DMS, GISAID method URI references)
- `minting/stage3-instances/generator/instance_configs/type2_*.py` — reference GISAID-Method v1 Trusty as a config constant

**Action:** none in this session. If a v3 mint or fresh catalogue is built using these generators, the v1 constants would need updating to v2. For the current cleanup pass, the v2 nanopubs were minted by direct TriG transformation (see `/tmp/gen_pass{1,2}_v2_slash.py` produced during PROMPT 2A and PROMPT 2B), bypassing these generators entirely.

### Documentation

- `docs/implementation_guide.md` — references v1 Trustys in §6 Appendix A (the canonical table) and possibly other narrative sections.

**Action:** §6 Appendix A is updated in PHASE 6.1 (this session). Other narrative references throughout the implementation guide may need batch-update in PROMPT 4 (queued).

## Summary

- **Stage 4 nanopub artifacts requiring re-mint:** 1 view set (Alpha knowlet × 4 nanopubs)
- **Doc references requiring update this session:** 1 (`docs/implementation_guide.md` §6 Appendix A)
- **Historical source files (not modified):** 76 (38 unsigned + 38 signed Stage 3 source TriGs) + 11 PUBLISHED_*.md + N generator configs
- **No Stage 4 cascades discovered beyond the Alpha knowlet view set.**

## Known deferred items (entered here for tracking)

| Item | File / Trusty | v1 reference | Required v2 reference | Status |
|---|---|---|---|---|
| Alpha knowlet query | `RAecvUbvUWiIOKP7ZEQk7hnUsb8lWWUr1lRbVN2PsSUSA` | `…/RA4BHII2…/Alpha-RBD-Variant` | `…/RAngbyT2iZe…/Alpha-RBD-Variant` | pending |
| Alpha knowlet pin-action | `RAzEolNOqr8I1aiZpafpUxJfqBOQRdTapceYWjXCoEYAE` | (references query above) | new query Trusty | pending (cascade) |
| Alpha knowlet wrapper | `RA_zvbVo3VX6Cy3lYOI6LNHJICb1copbCmJHayjpzCeJ0` | (references query above) | new query Trusty | pending (cascade) |
| Alpha knowlet view-display | `RA-QuZXXV9ni6b2YW0cM4ADyzYi-Uo4FQDR0p2pdR9tUk` | (references query above) | new query Trusty | pending (cascade) |
