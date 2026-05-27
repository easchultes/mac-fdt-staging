# Type 6 — Computational Prediction — AgMata — publication record

## Trusty URI

`https://w3id.org/np/RAuCu_OnyqK_dlaJ9l1EDdbtu_Wbpdw2pTlcTimQ9mqV0`

## Publish window

| Stage | Timestamp (UTC) |
|---|---|
| Local sign + np check | 2026-05-27T20:28Z (`1 trusty with signature`) |
| Publish start | 2026-05-27T20:28:26Z |
| Publish end   | 2026-05-27T20:28:29Z |

`nanopub publish`: `1 nanopub published at https://registry.petapico.org/`.

## Verification

- Registry HEAD via `w3id.org` → 307 → `registry.knowledgepixels.com` → **200 OK**.
- Signature roundtrip (local vs. fetched `npx:hasSignature`): **MATCH** (`JyQmDlAPFMFemnERvMYb3a1n79VQPE9J9QTXg4Bl…`).
- `npx:signedBy`: `https://orcid.org/0000-0001-8888-635X`.
- NanoDash explore (`/explore?id=…`): **200 OK**, body markers:
  - `AssertionTemplate` ×5
  - `use this template` ×1
  - `ExternalUriPlaceholder` ×15 (4 type-specific external-URI placeholders)
  - `AgMata` ×30
  - `hasAgMataScore` ×8

## SPS v1.3 conformance

- `includes_fair2 = False` (Types 3–6 omit fixed FAIR² pair).
- `dct:source` mandatory + repeatable (`st_src`).
- `cito:citesAsAuthority` optional + repeatable (`st_oc`).
- `mac:isObservationOf` → Type 1 Spike RBD Variant FDO (mandatory).
- `mac:hasPredictionMethod` → Bio2Byte AgMata Type 9 method FDO (mandatory; method-fixed at instance time).
- `mac:hasAgMataScore` → decimal value placeholder, unitless (mandatory).
- One FDO per variant (sequence-derived; not per (variant × method) like Types 3–5).
- Self-materialization block byte-identical to Type 1 v4.

## Generated from

- Config: `generator/configs/type6_config.py`
- Source: `drafts/template_type6_computational_prediction_agmata_v1.trig`
- Signed: `drafts/signed/template_type6_computational_prediction_agmata_v1.trig`
- Branch: `stage2-templates-type6`
