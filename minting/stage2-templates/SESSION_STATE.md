# Stage 2 — Session state snapshot (Stage 2 complete)

Snapshot captured 2026-05-27. Stage 2 work lives on un-merged branches
(retained for audit, listed below); this file on `main` is the single
tracking document.

## Stage 1 — vocabulary (DONE)

- 45 vocabulary nanopubs (26 predicates + 19 classes) published to live NSN as v2.
- Manifest: `minting/stage1-vocabulary-drafts/manifest_live_v2.csv` (45 v2 Trusty URIs + their v1 supersede targets).
- Merged into `main` via **PR #2** (merge commit `c53d90e`).
- v1 nanopubs remain on production as the `npx:supersedes` chain anchor (PR #1 closed with comment).
- Pubinfo per skill convention: `npx:introduces <term_uri>` + `npx:supersedes <v1_trusty_uri>` + `dct:created <UTC>`.
- Namespace: `mac:` expands to `https://w3id.org/spaces/mac/r/ontology/` (terms are siblings of `MAC-Ontology`, not under it).

## SPS (Stakeholder Participation Sheets)

- **v1.3** merged into `main` via **PR #3** (merge commit `8471c63`); merged ahead of Tobias's review per Erik's decision. PR description's review items (a) and (b) remain open for asynchronous comment.
- v1.3 introduces: mandatory `dct:isPartOf → Project FDO referent URI` on all 11 templates; optional `cito:citesAsAuthority` on Types 2–8 for observation-specific publications.
- **v1.4** merged 2026-05-27 via **PR #4** (merge commit `b141a71`). Locks SPS to Stage 2 implementation. Adds: self-materialization commitment, per-type provenance-obligation table, implementation-notes appendix (regex, label patterns, naming, prefix handling, space membership, derived analytics).

## Stage 2 — templates (COMPLETE)

**11 of 11 MAC FDT templates signed and published to live NSN on 2026-05-27.**
All 11 pinned manually to KP incubator/project4 via NanoDash UI (`gen:hasPinnedTemplate`).
Self-materialization 4-statement block is byte-identical across all 11 templates
(regression-verified at every Type generation).

### Trusty URI roster

| Type | Class | Trusty URI |
|---|---|---|
| 1  | Spike RBD Variant            | `https://w3id.org/np/RADOnITa1gjGIQtuENvlB2I7hykzrASzake1bIjGLiAtM` |
| 2  | Real-World Occurrence        | `https://w3id.org/np/RA_-AALlM1rIYcJRsFUrIfSb5KYSvjiHUZbQbN-cpeV6w` |
| 3  | Computational Prediction — RMSD   | `https://w3id.org/np/RALJKysR8vqqqZYXPGHcsI_J0BvPFUmzwOnV9WCGvUjcY` |
| 4  | Computational Prediction — SASA   | `https://w3id.org/np/RALSYeUQIciUad7GTfKjdNkfhP-505fesw6yYtdLoyW18` |
| 5  | Computational Prediction — pLDDT  | `https://w3id.org/np/RAm5j8EmzrS_ZDXEEOkvG2icT27GlbaGoNAS0sCDS72wc` |
| 6  | Computational Prediction — AgMata | `https://w3id.org/np/RAuCu_OnyqK_dlaJ9l1EDdbtu_Wbpdw2pTlcTimQ9mqV0` |
| 7  | DMS Experimental Observation | `https://w3id.org/np/RAp-dZcpmyNxtFsh7G0G1CDzzP2vPqoXVZSnlYRVQ_5Yk` |
| 8  | WHO Variant Classification   | `https://w3id.org/np/RAWyoHGVyB3Rh-fizZguS1zzf8Cim3q5ngWSoQNs2Sgcs` |
| 9  | Computational Method         | `https://w3id.org/np/RA5f4FtcnAGRtdt-vDTCvwXT1yVX7oMoXmvv-B8nfMelc` |
| 10 | Experimental Method          | `https://w3id.org/np/RALExfuvWjR8Lezp7I64cWCHgqyLb52js6-CTDIoINohs` |
| 11 | Observational Method         | `https://w3id.org/np/RAW9DfO6hmmt2sz_H4pHWWAX72BzTsnYjb9hi5wVQIQdE` |

### Branches (un-merged, retained for audit)

| Branch | HEAD | Contents |
|---|---|---|
| `stage2-generator`              | `de4e62e` | Generator (`generate_template.py`) + Type 1 config + FAIR² config-driven refactor |
| `stage2-templates-type1`        | `06d3b6b` | Type 1 v4 publication record (branched off pre-generator work) |
| `stage2-templates-type2`        | `90c680e` | Type 2 config, drafts (v1/v2), signed, PUBLISHED record |
| `stage2-templates-types-3-4-5`  | `3b43284` | Types 3/4/5 configs, drafts, signed, PUBLISHED records |
| `stage2-templates-type6`        | `c32c916` | Type 6 (AgMata) — config, draft, signed, PUBLISHED record |
| `stage2-templates-type7`        | `215a979` | Type 7 (DMS) — config, draft, signed, PUBLISHED record |
| `stage2-templates-type8`        | `b27a87f` | Type 8 (WHO) — config, draft, signed, PUBLISHED record |
| `stage2-templates-types-9-10-11`| `33a8ef7` | Types 9/10/11 (Method FDOs) — configs, drafts, signed, PUBLISHED records |

Optional follow-up: merge all 7 branches into `main` as a single batched PR for audit consolidation. No functional dependency on this — the live NSN nanopubs are authoritative; branches are repo provenance.

### Generator

- `minting/stage2-templates/generator/generate_template.py` (on `stage2-generator` and downstream)
- 11 configs at `minting/stage2-templates/generator/configs/type{1-11}_config.py`
- All 11 types round-trip byte-for-byte through the generator (modulo `dct:created` timestamp); regression-verified at every Type generation.
- One generator extension across Stage 2: auto-aligned `rdfs:label` column for `mac:*` curie blocks (introduced when Type 2's longest curie exceeded Type 1's). Type 1 round-trip preserved by a baseline column of 26.

### Self-materialization 4-statement block (byte-identical across all 11 templates)

```turtle
sub:st5  rdf:subject nt:NANOPUB ;
    rdf:predicate <https://w3id.org/fdof/ontology#materializes> ;
    rdf:object sub:fdo .

sub:st5b rdf:subject nt:NANOPUB ;
    rdf:predicate <https://w3id.org/fdof/ontology#hasEncodingFormat> ;
    rdf:object <https://www.iana.org/assignments/media-types/application/trig> .

sub:st5c rdf:subject nt:NANOPUB ;
    rdf:predicate dct:license ;
    rdf:object <https://creativecommons.org/licenses/by/4.0/> .

sub:st5d rdf:subject nt:NANOPUB ;
    rdf:predicate <https://www.w3.org/ns/dcat#accessURL> ;
    rdf:object nt:NANOPUB .
```

`st5d`'s NANOPUB-as-both-subject-and-object pattern (novel — not attested in the
446-template corpus prior to Type 1 v4) is preserved on production and across all
11 published Types.

## Stage 3 — instances (COMPLETE)

**38 / 38 MAC FDT instances signed and published to the live NSN on
2026-05-28.** Each instance materializes its TriG as the FDO substance
(per SPS v1.4 §"Self-materialization") and links to its template +
upstream FDOs (variant anchor → method → dataset → project) via the
SPS v1.3-mandated predicates.

### Catalogue (38 = 3 + 5 + 18 + 12)

| Group | Count | Branch HEAD | PUBLISHED record |
|---|---|---|---|
| **Type 1 anchors** (Alpha / Epsilon / Eta) | 3 | `26e29dc` (stage3-instances-type1) | `PUBLISHED_type1_instances.md` |
| **Method FDOs** (ESM2 / AlphaFold2 / AgMata / Bloom DMS / GISAID; Types 9-11) | 5 | `03e5e10` (stage3-instances-methods) | `PUBLISHED_methods.md` |
| **Prediction observations** (3 var × 2 method × 3 metric; Types 3-5) | 18 | `000ada0` (stage3-instances-types-3-4-5) | `PUBLISHED_predictions.md` |
| **Final observations** (Type 2 × 3 + Type 6 × 3 + Type 7 × 3 + Type 8 × 3) | 12 | `65308ee` (stage3-instances-types-2-6-7-8) | `PUBLISHED_observations_final.md` |
| **Total** | **38** | — | — |

Branches chain linearly off each other (Type 1 → methods → predictions → finals), un-merged, retained for audit.

### Instance generator

`minting/stage3-instances/generator/`:

- `generate_instance.py` — multi-kind dispatcher (`type1`, `method`, `prediction`, `occurrence`, `dms`, `who`); each kind has its own template string, validator, and mandatory/forbidden-statement check. Self-materialization 4-statement block byte-identical across all kinds.
- `generate_predictions_from_csv.py` — CSV-driven driver for Types 3-5 (3 variants × 2 methods × 3 metrics = 18 instances).
- `generate_type6_7_from_csv.py` — CSV-driven driver for Types 6 + 7 (per-variant, 6 instances).
- `instance_configs/type1_{alpha,epsilon,eta}.py`, `method_*.py`, `type2_*.py`, `type8_*.py` — per-instance configs for the non-CSV-driven types.

The CSV-driven path is **the code path Tranche 2 (3705-mutation scale-up) will reuse**: drop new variants into `VARIANT_ANCHORS` (after their Type 1 anchors publish) and iterate.

### Notable corrections at minting time

- **Epsilon GISAID seq_id**: published as `L452R` (Epsilon's canonical defining Spike mutation). SPS v1.3 and `FDT4Claude_small_v1_2.csv` still carry `L124R`; to be patched in the coordinated cleanup pass (`Post_demonstration_cleanup.md`).

### Demonstration posture (cleanup deferred)

- All 38 instances reference the draft `StayAhead Project FDO` via `dct:isPartOf`. Prediction instances reference draft `Dataset FDOs` (ESM + AlphaFold) via `dct:source`. Draft → non-draft promotion in the coordinated cleanup pass.
- `cito:citesAsAuthority` is omitted on observation instances (two-hop attribution via the method FDO, which carries the published authority DOIs). Per-observation citation can be added in the cleanup pass where canonical observation-specific publications exist.

### Tranche 2 (future scale-up)

3705 1-step mutations × 2 methods (AlphaFold + ESM) × 3 metrics
(RMSD / SASA / pLDDT) — no real-world occurrence — to be generated by
the same `generate_predictions_from_csv.py` driver against the
Tranche 2 CSV. No new generator code expected; only `VARIANT_ANCHORS`
expansion after Type 1 anchors are minted for the new variants.

## Stage 4 — standing SPARQL views (COMPLETE)

**4 standing views pinned to incubator/project4 on 2026-05-28.**
Each view is a separate grlc-query nanopub plus a separate pin-query
action nanopub that asserts `<project4-space> gen:hasPinnedQuery
<query>` — the **federated per-action model**, the same pattern
project4 already uses for the 11 pinned Stage 2 templates. **No
space-definition supersession needed.**

### View nanopubs (4)

| View | Query Trusty URI | Pin-action Trusty URI | Group tag |
|---|---|---|---|
| Catalogue summary by type      | `https://w3id.org/np/RAGlsCUDZrgFmlRQ8RNIpaWHaKAnRX7SGjEqOCGoWsM8A` | `https://w3id.org/np/RAr2do6-Zm_F5tv9NP4iziOpRCX-mJUZzCqUfY-brnNRY` | Catalogue overview |
| Variants by WHO classification | `https://w3id.org/np/RAlD3u-iOS5P95TlvydUePQCOqKyVsPLebBNTnu4lw7po` | `https://w3id.org/np/RAkwEb52MHk6Xe4uzOruIAkmGZAq4URDyg5bPqx4SXY1Y` | Situational dashboards |
| Observations per method        | `https://w3id.org/np/RAIKnskDgF8ZX-hOIC1UKLSxDapH1K1FjkNKi5Or-A3ws` | `https://w3id.org/np/RAZge9g-AM2aYodnkKrlt6ag1s1QPYjTYBCJZaPezTZ6M` | Situational dashboards |
| Alpha digital-twin knowlet     | `https://w3id.org/np/RAecvUbvUWiIOKP7ZEQk7hnUsb8lWWUr1lRbVN2PsSUSA` | `https://w3id.org/np/RAzEolNOqr8I1aiZpafpUxJfqBOQRdTapceYWjXCoEYAE` | Digital twin (worked example) |

### Scale-correct forms

- A, B, C are **GROUP BY aggregates** (row count bounded by the cardinality of MAC types, WHO classes, and method FDOs respectively — independent of instance volume).
- D is a **fixed-referent knowlet** (all observations of `Alpha-RBD-Variant`) — bounded by Alpha's observation set, not the catalogue. Tranche 2 adds new variants, not new Alpha observations, so D stays constant.

All four queries target the signature-validated endpoint
`https://w3id.org/np/l/nanopub-query-1.1/repo/full` and use the same
SPARQL `npa:hasValidSignatureForPublicKey` + `npx:invalidates` filter
block as the MAC-FDO exemplar (`get-all-datasets`).

### Branch + record

| Branch | HEAD | Record |
|---|---|---|
| `stage4-views` | `4509ca2` (off main, un-merged) | `PUBLISHED_views.md` |

NanoDash space-view indexing may lag (minutes-hours); NSN data verified
via SPARQL immediately (`SELECT … WHERE { <project4> gen:hasPinnedQuery
?q ; ?q gen:hasPinGroupTag ?tag }` returns the 4 expected rows).

### Pin-query template + grlc-query template

| Role | Trusty URI |
|---|---|
| grlc-query template ("Defining a grlc query") | `https://w3id.org/np/RAEFAt-QcFK0ZhqfvlsmS10BnzGJA0xwOICZXkO-ai87k` |
| Pin-query template ("Declare a pinned query for a Space") | `https://w3id.org/np/RAuLESdeRUlk1GcTwvzVXShiBMI0ntJs2DL2Bm5DzW_ZQ` |

## Demonstration tally (all four stages)

| Stage | Output | Live |
|---|---|---|
| Stage 1 — vocabulary | 45 v2 vocab nanopubs (26 predicates + 19 classes) | ✓ |
| Stage 2 — templates | 11 MAC FDT type templates (Types 1-11) | ✓ |
| Stage 3 — instances | 38 instance FDOs (3 anchors + 5 methods + 18 predictions + 12 observations) | ✓ |
| Stage 4 — views | 4 standing SPARQL views pinned to project4 | ✓ |

**Full MAC FDT demonstration live on the NSN** — vocabulary, templates,
instance catalogue, and discovery surface all in place.

## Reference templates (audit trail)

`minting/stage2-templates/reference/` (on `stage2-templates-type1` and downstream)
— 9 files fetched from production and committed:

| File | Trusty URI prefix | Role |
|---|---|---|
| `MAC_v2_core_template.trig` | `RA5reLVX…` | **Meta-template** ("Defining an assertion template") — schema authority for `nt:*` vocabulary |
| `MAC_v2_dataset_template.trig` | `RAnSHAFu…` | Concrete MAC v2 FDO template (Dataset) — pattern source |
| `nanodash_provenance_template_RA7lSq.trig` | `RA7lSq6M…` | Provenance template |
| `nanodash_pubinfo_template_RA0J4v.trig` | `RA0J4vUn…` | Pubinfo: License |
| `nanodash_pubinfo_template_RAukAc.trig` | `RAukAcWH…` | Pubinfo: Creator |
| `nanodash_pubinfo_template_RAMEgu.trig` | `RAMEgudZ…` | Pubinfo: Hand-coded statements |
| `nanodash_pubinfo_template_RARW4M.trig` | `RARW4MsF…` | Pubinfo: Derived |
| `nanodash_pubinfo_template_RAoTD7.trig` | `RAoTD7ud…` | Pubinfo: Supersedes (for v5+ supersessions) |
| `nanodash_pubinfo_template_RAxuGR.trig` | `RAxuGRKI…` | Pubinfo: Draft marker |

## Open architectural decisions (updated)

| Topic | Decision |
|---|---|
| **FDT validation space** | KP incubator project4 — `https://w3id.org/spaces/knowledgepixels/incubator/project4`. **11 templates pinned manually by Erik (admin) via NanoDash UI on 2026-05-27.** |
| **Standing SPARQL views (pinned queries)** | 4 views pinned on 2026-05-28 via federated per-action nanopubs (no space-definition supersession). See "Stage 4 — standing SPARQL views" section above. |
| **Permanent FDT space** | Deferred; likely MAC-namespace eventually. |
| **`cito:` and `schema:` prefix handling** | Emitted as **full URIs** at predicate positions and as `external_resource_labels` entries — not in common scaffold @prefix header (would break Type 1 v4 round-trip). Documented in SPS v1.4 §"Implementation notes". |
| **Mutation analytics** | External script over `mac:hasRBDSequence` (P60) — not in vocabulary. |
| **Tiered analytics architecture** | Paper material only (P61). |

## Pending tasks

1. **Post-demonstration cleanup (deferred):** see [`Post_demonstration_cleanup.md`](Post_demonstration_cleanup.md). Coordinated MAC v2 + MAC FDT revision pass before paper submission — covers (a) promoting `StayAhead Project FDO` + the 2 `Dataset FDOs` (ESM + AlphaFold) from `npx:DraftNanopub` to non-draft (with `AphaFold2` → `AlphaFold2` typo fix); (b) per-observation `cito:citesAsAuthority` for Types 2-8 where canonical observation-specific publications exist; (c) SPS v1.3 + CSV patch for Epsilon GISAID seq_id (`L124R` → `L452R`, already correct in live nanopub). Stage 3 demonstration is already published against current drafts; cleanup is consolidated.
2. **FDT paper draft** — v0.5 → v0.6 (incorporates Stage 2 + Stage 3 + Stage 4 completion).
3. **Tranche 2 scale-up** — 3705 1-step mutations × 2 methods × 3 metrics. Gated on the Tranche 2 CSV + Type 1 anchor minting for the new variants. Reuses `generate_predictions_from_csv.py` directly.
4. **Optional: merge the 7 `stage2-templates-*` + 4 `stage3-instances-*` + 1 `stage4-views` branches into `main`** as one batched PR for repo audit consolidation. No functional dependency.

## Tobias-pending

None currently. P98 PR #3 review items (a) and (b) remain open for asynchronous
comment; no decisions gated on them.

## Reference paths

| Resource | Location |
|---|---|
| nanopub-skill | `~/nanopub-work/nanopub-skill/` |
| nanopub JAR | `~/nanopub-work/nanopub-1.88.0-jar-with-dependencies.jar` |
| Temurin JDK 21 | `~/nanopub-work/jdk/jdk-21.0.11+10/Contents/Home/bin/java` |
| Signing profile | `~/.nanopub/profile.yaml` (also mirrored in repo at `signing_profile.yaml`) |
| Signing key | `~/.nanopub/id_rsa` (mode 0600) |
| Key intro nanopub | `https://w3id.org/np/RAV0JEgLu0mUsZiQBJds4JbV-nVR_bGvFsjo0p-hdRB28` |
| SPS v1.4 (current) | `specs/MAC_FDT_SPS_v1_4.md` |
| SPS v1.3 (previous) | `specs/MAC_FDT_SPS_v1_3.md` |
| Vocabulary spec (current) | `specs/MAC_FDT_Vocabulary_v1_2.md` |
| Stage 1 generator | `minting/stage1-vocabulary-drafts/gen_vocab_trigs.py` |
| Stage 1 manifest (live) | `minting/stage1-vocabulary-drafts/manifest_live_v2.csv` |
| Stage 2 generator (on branches) | `minting/stage2-templates/generator/generate_template.py` |
| Stage 2 configs (on branches) | `minting/stage2-templates/generator/configs/type{1-11}_config.py` |
| Stage 2 reference dir (on branches) | `minting/stage2-templates/reference/` |
| Stage 2 drafts dir (on branches) | `minting/stage2-templates/drafts/` |
| Stage 2 signed dir (on branches) | `minting/stage2-templates/drafts/signed/` |
| Stage 2 PUBLISHED records (on branches) | `minting/stage2-templates/drafts/PUBLISHED_type{1-11}.md` |

## Key Trusty URIs

### Meta-templates and pubinfo bundle (used by all 11 Stage 2 templates)

| Role | Trusty URI |
|---|---|
| Meta-template (Defining an assertion template) | `https://w3id.org/np/RA5reLVXOCPQFWr2UiCJb19ES7NwOpQRmudb17e2iB0c4` |
| Provenance template (attributed to author) | `https://w3id.org/np/RA7lSq6MuK_TIC6JMSHvLtee3lpLoZDOqLJCLXevnrPoU` |
| Pubinfo: License | `https://w3id.org/np/RA0J4vUn_dekg-U1kK3AOEt02p9mT2WO03uGxLDec1jLw` |
| Pubinfo: Creator | `https://w3id.org/np/RAukAcWHRDlkqxk7H2XNSegc1WnHI569INvNr-xdptDGI` |
| Pubinfo: Hand-coded statements | `https://w3id.org/np/RAMEgudZsQ1bh1fZhfYnkthqH6YSXpghSE_DEN1I-6eAI` |
| Pubinfo: Derived | `https://w3id.org/np/RARW4MsFkHuwjycNElvEVtuMjpf4yWDL10-0C5l2MqqRQ` |
| Pubinfo: Supersedes (for v5+ supersessions) | `https://w3id.org/np/RAoTD7udB2KtUuOuAe74tJi1t3VzK0DyWS7rYVAq1GRvw` |
| Pubinfo: Draft marker | `https://w3id.org/np/RAxuGRKID6yNg63V5Mf0ot2NjncOnodh-mkN3qT_1txGI` |

### MAC FDT templates (Stage 2)

See "Trusty URI roster" table above — all 11 listed there.

### Project context

| Role | Trusty URI |
|---|---|
| MAC-FDO project definition | `https://w3id.org/np/RA5ID1TGERiCerY1uO270r16jqYKQjvA1emomce3l89Jo` |
| Erik's key introduction | `https://w3id.org/np/RAV0JEgLu0mUsZiQBJds4JbV-nVR_bGvFsjo0p-hdRB28` |

## Branch state at snapshot

| Branch | HEAD | Origin synced? |
|---|---|---|
| `main` | (this commit) | ✅ |
| `stage2-generator` | `de4e62e` | ✅ |
| `stage2-templates-type1` | `06d3b6b` | ✅ |
| `stage2-templates-type2` | `90c680e` | ✅ |
| `stage2-templates-types-3-4-5` | `3b43284` | ✅ |
| `stage2-templates-type6` | `c32c916` | ✅ |
| `stage2-templates-type7` | `215a979` | ✅ |
| `stage2-templates-type8` | `b27a87f` | ✅ |
| `stage2-templates-types-9-10-11` | `33a8ef7` | ✅ |
