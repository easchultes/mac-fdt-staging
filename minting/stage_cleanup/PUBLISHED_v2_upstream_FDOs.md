<!--
AUTHOR: Erik Schultes
PROJECT: Making MAC FAIR
SESSION: Article - FDT Paper (2) — Stage cleanup
DATE: 2026-05-31 / 2026-06-01 (UTC / local)
DESCRIPTION: Publication record for the coordinated v2 supersession of the
StayAhead Project FDO and both Dataset FDOs (ESM, AlphaFold). Promotes all
three from npx:DraftNanopub to non-draft, repoints Dataset dct:isPartOf to
the Project v2 referent, fixes the AphaFold2 label typo, and adds FAIR²
cross-references on both Datasets. Downstream 38-instance re-mint deferred
to a follow-up session.
-->

# PUBLISHED — Upstream FDO v2 Cleanup Pass

Three v2 nanopubs published as a coordinated batch on 2026-05-31 UTC. All three
supersede their v1 drafts via `npx:supersedes`. None were previously published
in a non-draft form.

## Publication record

| # | Artifact | v2 Trusty URI | Publish timestamp (UTC) | HTTP HEAD (purl) | HTTP HEAD (w3id) |
|---|---|---|---|---|---|
| 1 | StayAhead Project FDO v2 | `http://purl.org/np/RAtVDD78c1d8ANCXc6B0Gz7EjRweOPfR1dTsMONS4MZrE` | 2026-05-31T22:45:38Z | 200 | 200 |
| 2 | ESM Dataset FDO v2 | `http://purl.org/np/RAy-pG5fwX53YEX_Wfmw-xUmpI9RsPTaw8l8Fn_j_CJIw` | 2026-05-31T22:46:05Z | 200 | 200 |
| 3 | AlphaFold Dataset FDO v2 | `http://purl.org/np/RAMOJpRJcZVEFqxJfdvLIF5Qjfi1db9FeROfosXL7XE58` | 2026-05-31T22:46:23Z | 200 | 200 |

All three resolved to `registry.knowledgepixels.com` immediately after publish.

## v2 Referent URIs (the `dct:isPartOf` / `dct:source` targets)

- StayAhead Project v2 referent: `http://purl.org/np/RAtVDD78c1d8ANCXc6B0Gz7EjRweOPfR1dTsMONS4MZrE/StayAhead-Project`
- ESM Dataset v2 referent: `http://purl.org/np/RAy-pG5fwX53YEX_Wfmw-xUmpI9RsPTaw8l8Fn_j_CJIw/STAYAHEAD-Dataset2`
- AlphaFold Dataset v2 referent: `http://purl.org/np/RAMOJpRJcZVEFqxJfdvLIF5Qjfi1db9FeROfosXL7XE58/STAYAHEAD-Dataset1`

Local-name asymmetry preserved from v1: ESM = `STAYAHEAD-Dataset2`, AlphaFold = `STAYAHEAD-Dataset1` (mint-order numbering from 2025-07-13).

## Supersession mapping (v1 → v2)

| v1 Trusty URI | v2 Trusty URI | Status |
|---|---|---|
| `https://w3id.org/np/RAFPOe4OIl_urs-U_7-FostjzcUo8ra6LasfSvGplOvto` (Project, draft) | `http://purl.org/np/RAtVDD78c1d8ANCXc6B0Gz7EjRweOPfR1dTsMONS4MZrE` (non-draft) | superseded |
| `https://w3id.org/np/RA9YxiABPRNy3rrJm20p1oanJchBcI22IPpSu36zj2MLs` (ESM Dataset, draft) | `http://purl.org/np/RAy-pG5fwX53YEX_Wfmw-xUmpI9RsPTaw8l8Fn_j_CJIw` (non-draft) | superseded |
| `https://w3id.org/np/RAv6JJe-lvoadhNwml8pzSLs5aOtbU1xbHT5qgFtgwQ-s` (AlphaFold Dataset, draft, label typo) | `http://purl.org/np/RAMOJpRJcZVEFqxJfdvLIF5Qjfi1db9FeROfosXL7XE58` (non-draft, typo fixed) | superseded |

## SPARQL verification

Verified against `https://query.knowledgepixels.com/repo/full` immediately
after publish. The supersession index returned all three expected rows with no
indexing lag:

```sparql
PREFIX npx: <http://purl.org/nanopub/x/>
PREFIX np:  <http://www.nanopub.org/nschema#>
PREFIX npa: <http://purl.org/nanopub/admin/>

SELECT ?v2 ?v1 WHERE {
  GRAPH npa:graph {
    ?v2 npx:supersedes ?v1 .
    VALUES ?v1 {
      <https://w3id.org/np/RAFPOe4OIl_urs-U_7-FostjzcUo8ra6LasfSvGplOvto>
      <https://w3id.org/np/RA9YxiABPRNy3rrJm20p1oanJchBcI22IPpSu36zj2MLs>
      <https://w3id.org/np/RAv6JJe-lvoadhNwml8pzSLs5aOtbU1xbHT5qgFtgwQ-s>
    }
  }
}
```

Result (3 rows, CSV):

```
v2,v1
http://purl.org/np/RAtVDD78c1d8ANCXc6B0Gz7EjRweOPfR1dTsMONS4MZrE,https://w3id.org/np/RAFPOe4OIl_urs-U_7-FostjzcUo8ra6LasfSvGplOvto
http://purl.org/np/RAy-pG5fwX53YEX_Wfmw-xUmpI9RsPTaw8l8Fn_j_CJIw,https://w3id.org/np/RA9YxiABPRNy3rrJm20p1oanJchBcI22IPpSu36zj2MLs
http://purl.org/np/RAMOJpRJcZVEFqxJfdvLIF5Qjfi1db9FeROfosXL7XE58,https://w3id.org/np/RAv6JJe-lvoadhNwml8pzSLs5aOtbU1xbHT5qgFtgwQ-s
```

## Defect-fix summary (what changed v1 → v2)

**Project v2** (`RAtVDD78c1d8…`):
- Removed `npx:DraftNanopub` flag from pubinfo.
- Added `npx:supersedes <v1>` in pubinfo.
- Refreshed `dct:created`.
- Assertion graph reproduced byte-for-byte from v1 (23 triples on `sub:StayAhead-Project` + 5 on `osf.io/js8gc` materialization). No assertion-level edits.

**ESM Dataset v2** (`RAy-pG5fwX53YEX_…`):
- Removed `npx:DraftNanopub`; added `npx:supersedes <v1>`.
- Repointed `dct:isPartOf` from stale predecessor `…/RAqpkNMBQyEWP_…/StayAhead-Project` to Project v2 referent `…/RAtVDD78c1d8…/StayAhead-Project`.
- Added FAIR² cross-references: `dct:references` → article DOI (10.3389/fbinf.2025.1634111); `dct:source` → Package DOI (10.71728/hw56-vj34) and per-resource URL (`sen.science/…/esm_wuhan_1step_v1`).
- Replaced stale-URI `nt:hasLabelFromApi` cache triple in pubinfo with a fresh cache triple pointing at the Project v2 referent.

**AlphaFold Dataset v2** (`RAMOJpRJcZVEFqxJfdvLIF5…`):
- All ESM-symmetric edits above, with `af_wuhan_1step_v1` as the per-resource URL.
- Fixed `rdfs:label` typo: `"AphaFold2 Dataset STAYAHEAD"` → `"AlphaFold2 Dataset STAYAHEAD"`.

## Signing key

All three v2s signed with the local CLI key in `~/.nanopub/id_rsa` (different
from the NanoDash-managed key that signed the v1 drafts; both bound to Erik's
ORCID 0000-0001-8888-635X via separate introduction nanopubs).

## What this cleanup pass does NOT touch

- The 38 Stage 3 FDT instance nanopubs still reference the v1 Project FDO referent
  (`…/RAFPOe4OIl_…/StayAhead-Project`) via `dct:isPartOf`, and the 21 ESM/AlphaFold-method
  instances + 3 Type 6 AgMata instances still reference v1 Dataset Trusty URIs via
  `dct:source`. These will be re-minted in a follow-up session to point at the v2
  referents.
- SPS / Vocabulary specs (`MAC_FDT_SPS_v1_4.md`, `MAC_FDT_Vocabulary_v1_2.md`) are
  unchanged; this cleanup is statement-value, not statement-schema.
- The PUBLISHED records for prior stages (`PUBLISHED_v4.md`, Stage 3 PUBLISHED_*.md)
  are unchanged; they record v1 URIs which remain valid (superseded but not retracted).

## Follow-ups (open)

1. Re-mint 38 FDT instances to point at Project v2 + Dataset v2 referents.
2. Refresh `Post_demonstration_cleanup.md` to note this pass is complete (items §1 steps 1–2 done; step 3 still pending — the 38-instance re-mint).
3. Update `Stage3_pre_minting_notes.md` if it references the stale Project URI discrepancy as open.
