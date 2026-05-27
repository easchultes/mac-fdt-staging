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
- **v1.4 update log**: now ready to draft — all Stage 2 learnings in hand. See "Pending tasks" below.

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
| **Standing SPARQL views (pinned queries)** | Not yet added. Optional; can be added via NanoDash UI when desired. |
| **Permanent FDT space** | Deferred; likely MAC-namespace eventually. |
| **`cito:` and `schema:` prefix handling** | Emitted as **full URIs** at predicate positions and as `external_resource_labels` entries — not in common scaffold @prefix header (would break Type 1 v4 round-trip). Worth documenting in SPS v1.4 so future contributors don't trip on it. |
| **Mutation analytics** | External script over `mac:hasRBDSequence` (P60) — not in vocabulary. |
| **Tiered analytics architecture** | Paper material only (P61). |

## Pending tasks

1. **SPS v1.4 draft** — now ready to start. All Stage 2 learnings in hand:
   - Document `cito:` / `schema:` prefix policy (emitted as full URIs).
   - Codify the 4-statement self-materialization block as a Stage-2 invariant.
   - Confirm Types 9-11 `cito:citesAsAuthority` as mandatory + repeatable (deviation from Types 2-8).
   - Confirm Types 3-6 `dct:source` mandatory + repeatable; Type 7 `dct:source` optional + repeatable; Type 8 omits `dct:source` entirely.
2. **Stage 3 pre-minting checklist** (`Stage3_pre_minting_notes.md` — user-side; not yet uploaded). Items to resolve before any Stage 3 minting:
   - StayAhead Project FDO Trusty URI verification (for `dct:isPartOf` on all instances).
   - GISAID accession numbers for Alpha / Epsilon / Eta.
   - GeoNames feature ID verification (Type 2 instances).
   - FAIR² resource URL verification (Types 3-6 `dct:source` instances).
   - StayAhead Dataset FDO Trusty URIs (for Types 3-6 `dct:source` instances).
   - Observation-specific authority instance values (Types 2-8 `cito:citesAsAuthority`).
3. **Stage 3 — 38 instance nanopubs** (3 variants + 30 observations + 5 method FDOs, approximate). Gated on (2).
4. **Optional: pinned SPARQL queries on incubator/project4** — via NanoDash UI.
5. **Optional: merge all 7 `stage2-templates-*` branches into `main`** as a single batched PR for repo audit consolidation. No functional dependency.

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
| SPS v1.3 (current) | `specs/MAC_FDT_SPS_v1_3.md` |
| SPS v1.4 update log | user-side (will be uploaded when v1.4 drafts) |
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
