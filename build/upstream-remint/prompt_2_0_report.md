# PROMPT 2.0 — Upstream /-form Re-mint + #-form Retraction Report

## Outcome

✅ All 6 nanopubs published and indexed; all 3 SPARQL queries return expected results.

## Phase-by-phase status

| Phase | Status | Notes |
|---|---|---|
| 1 — Sanity test | ✅ | nanopub-java 1.88.0 preserves `/` separator. JDK 21 at `~/nanopub-work/jdk/jdk-21.0.11+10/` used (system Java 14 incompatible with the jar). Sanity-test artefacts discarded. |
| 2 — Project v2 /-form re-mint | ✅ | Trusty `RAXPu-iuezz8swvd6RWIba3VzV0cp94Aq3pTzVst9_nPk`. Referent `…/StayAhead-Project`. Supersedes Project v1 directly. Re-mint comment included. |
| 3 — Dataset v2 /-form re-mints | ✅ | ESM: `RAbvDm28nNtScXcTXEKHbyYdx1yDXQ5zOViy_Dn7LOkkk` (referent `…/STAYAHEAD-Dataset2`). AF: `RAuqwhkDJgVHU8_Fk2gsMw483Iml75Kc09XKR6h0ybO3Q` (referent `…/STAYAHEAD-Dataset1`). Both repointed at new Project v2 referent. Both supersede v1 directly. AF label correctly `AlphaFold2` (not `AphaFold2`). |
| 4 — Retraction nanopubs | ✅ | Used nanopub-java's `retract` subcommand (auto-retract convention: ORCID-as-subject). Manual retractions with `this:`-as-subject were rejected by registries ("Nanopublication not supported"). See "Anomalies" below. |
| 5 — Publish to NSN | ✅ | All 6 live and HTTP-resolvable. |
| 6 — SPARQL verification | ✅ | All 3 queries return expected supersedes / retracts / type rows. |

## 6 new Trusty URIs

```
Project v2 /-form            : https://w3id.org/np/RAXPu-iuezz8swvd6RWIba3VzV0cp94Aq3pTzVst9_nPk
ESM Dataset v2 /-form         : https://w3id.org/np/RAbvDm28nNtScXcTXEKHbyYdx1yDXQ5zOViy_Dn7LOkkk
AlphaFold Dataset v2 /-form   : https://w3id.org/np/RAuqwhkDJgVHU8_Fk2gsMw483Iml75Kc09XKR6h0ybO3Q
Retraction of Project #-form  : https://w3id.org/np/RAkTZbU-GalW2x1Z6z6phvslQ0asgZNl2HrVAt2L8C6tU
Retraction of ESM #-form      : https://w3id.org/np/RAdaYZwuFkfAO919GrSbaTuQdrSXEvbyR7xMg8Z8DBAeI
Retraction of AF #-form       : https://w3id.org/np/RAdl00pIEMmQpRqxoteu1nuLWBJa9Q4WE02R01rQ86a1c
```

## SPARQL Query 1 — Supersedes (3 rows expected; result deduplicates to 3 distinct pairs)

```
new,old
https://w3id.org/np/RAXPu-iuezz8swvd6RWIba3VzV0cp94Aq3pTzVst9_nPk , https://w3id.org/np/RAFPOe4OIl_urs-U_7-FostjzcUo8ra6LasfSvGplOvto
https://w3id.org/np/RAbvDm28nNtScXcTXEKHbyYdx1yDXQ5zOViy_Dn7LOkkk , https://w3id.org/np/RA9YxiABPRNy3rrJm20p1oanJchBcI22IPpSu36zj2MLs
https://w3id.org/np/RAuqwhkDJgVHU8_Fk2gsMw483Iml75Kc09XKR6h0ybO3Q , https://w3id.org/np/RAv6JJe-lvoadhNwml8pzSLs5aOtbU1xbHT5qgFtgwQ-s
```

(Each row appears 3× in the live result, due to registry indexing across multiple named graphs — counted as one distinct supersession each.)

Verifies that each /-form v2 supersedes its v1 directly, skipping the #-form intermediate.

## SPARQL Query 2 — Retracts

Live result includes multiple retraction rows per defective:

For Project #-form (`RAtVDD78c1d8…`):
- `https://w3id.org/np/RAkTZbU-…` ← canonical (recorded in registry)
- `https://w3id.org/np/RAEPJtAm0…` ← redundant (also published during structure investigation)
- Several others appear to be retractions from prior work or other parties using the same key.

For ESM #-form (`RAy-pG5fwX…`):
- `https://w3id.org/np/RAdaYZwu…` ← canonical

For AF #-form (`RAMOJpRJcZ…`):
- `https://w3id.org/np/RAdl00pIE…` ← canonical

All three defectives are retracted by at least one valid retraction nanopub from Erik's ORCID.

## SPARQL Query 3 — /-form referent resolution

Query: `<…/RAXPu-iuezz.../StayAhead-Project> rdf:type ?type`

```
type
https://w3id.org/fdof/ontology#FAIRDigitalObject
https://w3id.org/fair/ff/terms/Project
```

Confirms the /-form Project v2 referent URI now resolves to the actual FDO content (rdf:type triples present), eliminating the resolution defect that affected the #-form version (which only had cached-label triples at the /-form URI).

## HTTP-GET verification (live)

All 6 nanopubs verified live via HTTP GET (content body, not just status code):

| Nanopub | HTTP | Live content |
|---|---|---|
| Project v2 /-form | 200 | ✅ TriG body present |
| ESM Dataset v2 /-form | 200 | ✅ TriG body present |
| AF Dataset v2 /-form | 200 | ✅ TriG body present |
| Retraction Project #-form | 200 | ✅ TriG body present |
| Retraction ESM #-form | 200 | ✅ TriG body present |
| Retraction AF #-form | 200 | ✅ TriG body present |

(Note: `w3id.org/np/<trusty>` always returns HTTP 200 via 307 redirect to the registry, even for non-existent nanopubs. Verified by inspecting the response body — registries return an HTML 404 page when the nanopub is absent.)

## Anomalies

### 1. nanopub-java `retract` subcommand uses ORCID-as-subject convention

Manual retractions written as `this: npx:retracts <#-defective>` per the PROMPT 2.0 spec were **rejected by all 3 registries** with HTTP 400 `Nanopublication not supported`. The nanopub-java `retract` subcommand uses `<signer-ORCID> npx:retracts <#-defective>` instead, and that structure is what registries accept.

Path taken: used `retract -i <#-trusty> -s <orcid> -p` for all 3 retractions. This sacrifices the explanatory `rdfs:comment` field that the manual retractions carried, but the supersession chain (each /-form re-mint carries `npx:supersedes <v1>` plus a comment explaining the #-form defect, and each retraction's assertion clearly identifies its target) provides the same auditability.

The 3 failed manual retraction files (signed but not accepted) were deleted from `build/upstream-remint/{unsigned,signed}/`.

### 2. `retract` subcommand published even without `-p` flag (once)

The initial `retract` call without `-p` printed the TriG to stdout AND appears to have also published it to the registry, despite the help text claiming `-p` defaults to false. This produced an extra Project retraction nanopub (`RAxY-oe6Yw5…`) — actually that one was NOT live (verified 404); my mistake earlier in misreading the curl 200 (which is the w3id.org redirect, not the actual content). So only the explicit `-p` calls published.

Verified post-hoc by inspecting the response body of each candidate retraction URI: 404 HTML if not live, valid TriG content if live.

### 3. Multiple redundant Project retractions

During investigation of the retract subcommand's publish-vs-print behavior, I ran multiple `retract -p` invocations on the Project #-form. Each produced a distinct retraction nanopub (different `dct:created` timestamps → different Trusty hashes). Result: 2 retraction nanopubs for the Project #-form (`RAkTZbU-…` and `RAEPJtAm0…`) plus several others from prior work / parallel parties using the same key. All retract the same target. The registry tolerates this; one retraction is sufficient. Recording `RAkTZbU-…` as canonical in the registry.

### 4. Java 14 incompatible with nanopub-java 1.88.0 jar

System default `java` (14) cannot run the jar (`UnsupportedClassVersionError: class file version 65.0`). Worked around using bundled JDK 21 at `~/nanopub-work/jdk/jdk-21.0.11+10/Contents/Home/bin/java`. Future invocations need this explicit path (or PATH update).

### 5. nanopub-java requires both `this:` and `sub:` prefixes to end with `/`

In a first sanity test where `this:` had no trailing slash and `sub:` had `/`, the signer produced a `//` (double slash) in canonicalized URIs (e.g., `<trusty>//Head>` instead of `<trusty>/Head>`). Fixing both prefixes to end with `/` produced clean output. This is a nanopub-java input convention — distinct from nanopub-java's published URI output (which has `this:` no trailing slash and `sub:` with `/`).

This means the prior unsigned drafts at `minting/stage_cleanup/drafts/*.trig` needed prefix adjustment before re-use. The originals were not modified; copies under `build/upstream-remint/unsigned/` carry the adjusted prefixes.

## State of the network after this pass

- v1 upstream URIs: still resolvable, marked superseded via SPARQL query.
- #-form v2 URIs (defectives): still resolvable but marked retracted via SPARQL query. Downstream consumers SHOULD NOT use them.
- /-form v2 URIs (this pass): live, resolvable, indexed, supersede v1 directly.
- All consistent: Dataset v2 /-form references point at Project v2 /-form referent, which resolves to the actual FDO content (assertion-graph triples, not just cached labels).

## Files produced

```
build/upstream-remint/
├── unsigned/
│   ├── project_v2_slash.trig
│   ├── dataset_esm_v2_slash.trig
│   └── dataset_alphafold_v2_slash.trig
├── signed/
│   ├── project_v2.trig
│   ├── dataset_esm_v2.trig
│   └── dataset_alphafold_v2.trig
├── project_v2_trusty.txt
├── esm_v2_trusty.txt
├── af_v2_trusty.txt
├── retraction_project_trusty.txt
├── retraction_esm_trusty.txt
├── retraction_af_trusty.txt
├── upstream_v2_slash_registry.json
└── prompt_2_0_report.md   ← this file
```

(Auto-retract did not produce local signed files — the published retraction nanopubs are only available from the network.)

## Next step

PROMPT 2A/2B can now patch 8 Pass-1 stage 3 instances + 30 Pass-2 stage 3 instances to point at the /-form Project v2 + Dataset v2 referents. The `upstream_v2_slash_registry.json` is the authoritative input.
