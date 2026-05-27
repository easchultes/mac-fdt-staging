# Type 7 — Experimental Measurement — DMS — publication record

## Trusty URI

`https://w3id.org/np/RAp-dZcpmyNxtFsh7G0G1CDzzP2vPqoXVZSnlYRVQ_5Yk`

## Publish window

| Stage | Timestamp (UTC) |
|---|---|
| Local sign + np check | 2026-05-27T20:34Z (`1 trusty with signature`) |
| Publish start | 2026-05-27T20:34:18Z |
| Publish end   | 2026-05-27T20:34:21Z |

`nanopub publish`: `1 nanopub published at https://registry.petapico.org/`.

## Verification

- Registry HEAD via `w3id.org` → 307 → `registry.knowledgepixels.com` → **200 OK**.
- Signature roundtrip (local vs. fetched `npx:hasSignature`): **MATCH** (`Wbmm2QWzPYa9m0Fnp/OpS/gKfXRurjtXY9dkzDvh…`).
- `npx:signedBy`: `https://orcid.org/0000-0001-8888-635X`.
- NanoDash explore (`/explore?id=…`): **200 OK**, body markers:
  - `AssertionTemplate` ×5
  - `use this template` ×1
  - `ExternalUriPlaceholder` ×15 (4 type-specific external-URI placeholders: variant, experimentalMethod, authority, source)
  - `LiteralPlaceholder` ×27 (6 mandatory metric values + 2 confidences + 1 standard literal placeholder; remaining counts from class declarations)
  - `DMS` ×14
  - `hasBind`, `hasExpr`, `hasConfidenceBind` each ×8

## Manifest cross-check

Stage 1 v2 vocabulary confirms all required terms:

- class `ExperimentalDMSObservation` → `RA4W7BTjZqyFF7yHyNBPXKwqfoFFBlC1-OLYw-U6jy1S4`
- predicate `hasExperimentalMethod` → `RA7nK11diUZ6vdCL0_EPljblhbXYnNNvDaj-ZFMoBPTmA`
- predicate `hasBind` → `RAt9ZUC4T6urQ_tgkEEsg6vtZy7v9CD7WeGqeT9Zax3qY`
- predicate `hasDeltaBind` → `RASbvkLZcQLl8jACJL7a2ebSLN-b9u6xVC-Dr-wDiDVJU`
- predicate `hasExpr` → `RAlUEgjqST9CBROWFUTqK1ccF2J97REjRtZClPEqLlUQg`
- predicate `hasDeltaExpr` → `RAWvjyY6rAIBNhr7_y-aqU1JRBoorX3vkN9JNmqLAu8ug`
- predicate `hasConfidenceBind` → `RAvp1VY59E_8UACyopJWQDgISZoAvHYFph8np_TubNhLE`
- predicate `hasConfidenceExpr` → `RALp4b32qCoszmkcc2o-yp_MOOSudty7gOdS26AYYGeMs`

## SPS v1.3 conformance

- `includes_fair2 = False` (Types 2-8 omit fixed FAIR² pair).
- `dct:source` **optional + repeatable** (`st_src`, `nt:OptionalStatement, nt:RepeatableStatement`) — Type 7 differs from Types 3-6 where `dct:source` is mandatory.
- `cito:citesAsAuthority` optional + repeatable (`st_oc`).
- `mac:isObservationOf` → Type 1 Spike RBD Variant FDO (mandatory).
- `mac:hasExperimentalMethod` → Bloom Lab DMS Type 10 method FDO (mandatory).
- Six mandatory DMS metric statements (`mac:hasBind`, `mac:hasDeltaBind`, `mac:hasExpr`, `mac:hasDeltaExpr`, `mac:hasConfidenceBind`, `mac:hasConfidenceExpr`) — all mandatory (no optional/repeatable flags).
- Self-materialization block byte-identical to Type 1 v4.

## Generated from

- Config: `generator/configs/type7_config.py`
- Source: `drafts/template_type7_experimental_dms_observation_v1.trig`
- Signed: `drafts/signed/template_type7_experimental_dms_observation_v1.trig`
- Branch: `stage2-templates-type7`

## Note on placeholder count

Task spec header said `Placeholders (19 total: 10 std + 9 type-specific)` but the explicit list itemized 10 type-specific entries (variant, experimentalMethod, authority, source, bind, deltaBind, expr, deltaExpr, confidenceBind, confidenceExpr), each referenced by one of the 10 type-specific statements. Generated template has 20 total placeholders (10 std + 10 type-specific) per the explicit list — the "9 / 19" figure in the spec header was an off-by-one in the count; the list itself is internally consistent.
