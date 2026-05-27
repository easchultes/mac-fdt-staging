# Stage 2 — Session state snapshot (before /compact)

Snapshot captured 2026-05-27. Use this as the source of truth when resuming after context compaction.

## Stage 1 — vocabulary (DONE)

- 45 vocabulary nanopubs (26 predicates + 19 classes) published to live NSN as v2.
- Manifest: `minting/stage1-vocabulary-drafts/manifest_live_v2.csv` (45 v2 Trusty URIs + their v1 supersede targets).
- Merged into `main` via **PR #2** (merge commit `c53d90e`).
- v1 nanopubs remain on production as the `npx:supersedes` chain anchor (PR #1 closed with comment).
- Pubinfo per skill convention: `npx:introduces <term_uri>` + `npx:supersedes <v1_trusty_uri>` + `dct:created <UTC>`.
- Namespace: `mac:` expands to `https://w3id.org/spaces/mac/r/ontology/` (terms are siblings of `MAC-Ontology`, not under it).

## SPS (Stakeholder Participation Sheets)

- **v1.3** merged into `main` via **PR #3** (merge commit `8471c63`); merged ahead of Tobias's review per Erik's decision. PR description's review items (a) and (b) remain open for asynchronous comment; subsequent revisions land as v1.4.
- v1.3 introduces: mandatory `dct:isPartOf → Project FDO referent URI` on all 11 templates; optional `cito:citesAsAuthority` on Types 2–8 for observation-specific publications.
- **v1.4 update log**: user-side outputs (not yet uploaded); will land in repo when v1.4 drafts. Trigger to draft v1.4: after all 11 FDT templates validated.

## Stage 2 — Type 1 template (DONE — first of 11)

- **Branch**: `stage2-templates-type1` (HEAD `06d3b6b`)
- **v4 signed + published to live NSN**:
  - Trusty URI: `https://w3id.org/np/RADOnITa1gjGIQtuENvlB2I7hykzrASzake1bIjGLiAtM`
  - Publish window: 2026-05-27T13:15:27Z → 2026-05-27T13:15:31Z
  - Verification: HEAD via `w3id.org` returns 307 → `registry.knowledgepixels.com` → 200 OK; signature roundtrip matches signed bytes.
  - NanoDash render: HTTP 200, recognized as "AssertionTemplate" with "use this template" link present.
  - Publication record: `minting/stage2-templates/drafts/PUBLISHED_v4.md`.
- **Draft history** (all on disk in `minting/stage2-templates/drafts/`):
  - `template_type1_spike_rbd_variant.trig` (initial draft, snake_case placeholders)
  - `template_type1_spike_rbd_variant_v3.trig` (self-materialization block introduced)
  - `template_type1_spike_rbd_variant_v4.trig` (camelCase placeholders, regex validation, guided-choice project picker, refreshed label pattern)
  - `signed/template_type1_spike_rbd_variant_v4.trig` (signed bytes — published)

## Reference templates (audit trail)

`minting/stage2-templates/reference/` — 9 files fetched from production and committed:

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

## Self-materialization block (validated)

Four-statement constant block, identical across all 11 MAC FDT templates. Validated end-to-end: signed → published → fetched → rendered.

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

`st5d`'s NANOPUB-as-both-subject-and-object pattern (novel — not attested in the 446-template corpus prior to v4) **preserved on production** in the fetched TriG. NanoDash renders the page without errors.

## Open architectural decisions

| Topic | Decision |
|---|---|
| **FDT validation space** | KP incubator project4 — `https://w3id.org/spaces/knowledgepixels/incubator/project4` |
| **Permanent FDT space** | Deferred; likely MAC-namespace eventually |
| **Pinning rights** | Erik is admin on incubator/project4 — can pin directly (no prerequisite gate) |
| **Mutation analytics** | External script over `mac:hasRBDSequence` (P60) — not in vocabulary |
| **Tiered analytics architecture** | Paper material only (P61) |

## Pending tasks (next session)

1. **Stage 2 Types 2–11** — generator-based; scaffold from Type 1. 10 more templates to draft, sign, publish.
2. **Stage 3** — 38 instance nanopubs; pre-minting checklist exists.
3. **Incubator space-definition supersession** — pin all 11 templates + standing SPARQL views once all are published. Defer until Types 2–11 are on the live NSN.
4. **SPS v1.4 draft** — after all 11 templates validated. v1.4 update log will arrive user-side.

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
| Stage 2 reference dir | `minting/stage2-templates/reference/` |
| Stage 2 drafts dir | `minting/stage2-templates/drafts/` |
| Stage 2 signed dir | `minting/stage2-templates/drafts/signed/` |

## Key Trusty URIs

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
| Type 1 template (Spike RBD Variant) — published | `https://w3id.org/np/RADOnITa1gjGIQtuENvlB2I7hykzrASzake1bIjGLiAtM` |
| MAC-FDO project definition | `https://w3id.org/np/RA5ID1TGERiCerY1uO270r16jqYKQjvA1emomce3l89Jo` |
| Erik's key introduction | `https://w3id.org/np/RAV0JEgLu0mUsZiQBJds4JbV-nVR_bGvFsjo0p-hdRB28` |

## Branch state at snapshot

| Branch | HEAD | Origin synced? |
|---|---|---|
| `main` | `8471c63` (Merge PR #3 — SPS v1.3) | ✅ |
| `stage2-templates-type1` | `06d3b6b` (v4 published-to-live record) | ✅ |
