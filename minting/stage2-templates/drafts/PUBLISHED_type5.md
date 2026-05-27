# Type 5 — Computational Prediction — pLDDT — publication record

## Trusty URI

`https://w3id.org/np/RAm5j8EmzrS_ZDXEEOkvG2icT27GlbaGoNAS0sCDS72wc`

## Publish window

| Stage | Timestamp (UTC) |
|---|---|
| Local sign + np check | 2026-05-27T20:22Z (`1 trusty with signature`) |
| Publish start | 2026-05-27T20:23:08Z |
| Publish end   | 2026-05-27T20:23:11Z |

`nanopub publish`: `1 nanopub published at https://registry.petapico.org/`.

## Verification

- Registry HEAD via `w3id.org` → 307 → `registry.knowledgepixels.com` → **200 OK**.
- Signature roundtrip (local vs. fetched `npx:hasSignature`): **MATCH** (`NGKvteWkPm9HkQCG4uOIhwXXOSWsparzI3Sx6Gl0…`).
- `npx:signedBy`: `https://orcid.org/0000-0001-8888-635X`.
- NanoDash explore (`/explore?id=…`): **200 OK**, body markers:
  - `AssertionTemplate` ×5
  - `use this template` ×1
  - `ExternalUriPlaceholder` ×15 (4 type-specific external-URI placeholders)
  - `pLDDT` ×20

## Manifest cross-check

Stage 1 v2 vocabulary confirms the lowercase-'p' predicate form:

- `predicate,haspLDDT,…,https://w3id.org/np/RASdcWGO4FpX60LwauN-7KhSxWJgw8Na908HvhMqzqDzQ`
- `class,ComputationalPredictionPLDDT,…,https://w3id.org/np/RA-PiBGB7iMOT16-M3gpGUajoKFi6kWSXfRy2hrvWp5Sk`

SPS v1.3's `mac:haspLDDT` (lowercase 'p') matches the published vocabulary.

## SPS v1.3 conformance

- `includes_fair2 = False` (Types 3–6 omit fixed FAIR² pair).
- `dct:source` mandatory + repeatable (`st_src`).
- `cito:citesAsAuthority` optional + repeatable (`st_oc`).
- `mac:isObservationOf` → Type 1 Spike RBD Variant FDO (mandatory).
- `mac:hasPredictionMethod` → Type 9 Computational Method FDO (mandatory).
- `mac:haspLDDT` → decimal value placeholder, unitless 0–100 (mandatory).
- Self-materialization block byte-identical to Type 1 v4.

## Generated from

- Config: `generator/configs/type5_config.py`
- Source: `drafts/template_type5_computational_prediction_plddt_v1.trig`
- Signed: `drafts/signed/template_type5_computational_prediction_plddt_v1.trig`
- Branch: `stage2-templates-types-3-4-5`
