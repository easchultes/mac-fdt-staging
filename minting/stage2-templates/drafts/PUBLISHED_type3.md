# Type 3 — Computational Prediction — RMSD — publication record

## Trusty URI

`https://w3id.org/np/RALJKysR8vqqqZYXPGHcsI_J0BvPFUmzwOnV9WCGvUjcY`

## Publish window

| Stage | Timestamp (UTC) |
|---|---|
| Local sign + np check | 2026-05-27T20:22Z (`1 trusty with signature`) |
| Publish start | 2026-05-27T20:23:01Z |
| Publish end   | 2026-05-27T20:23:05Z |

`nanopub publish`: `1 nanopub published at https://registry.petapico.org/`.

## Verification

- Registry HEAD via `w3id.org` → 307 → `registry.knowledgepixels.com` → **200 OK**.
- Signature roundtrip (local vs. fetched `npx:hasSignature`): **MATCH** (`LWrdB7LO8wTHGkU41106n1uqoAqvX2/GJPvYOT1V…`).
- `npx:signedBy`: `https://orcid.org/0000-0001-8888-635X`.
- NanoDash explore (`/explore?id=…`): **200 OK**, body markers:
  - `AssertionTemplate` ×5
  - `use this template` ×1
  - `ExternalUriPlaceholder` ×15 (4 type-specific external-URI placeholders)
  - `RMSD` ×28

## SPS v1.3 conformance

- `includes_fair2 = False` (Types 3–6 omit fixed FAIR² pair).
- `dct:source` mandatory + repeatable (`st_src`, `nt:RepeatableStatement` only).
- `cito:citesAsAuthority` optional + repeatable (`st_oc`).
- `mac:isObservationOf` → Type 1 Spike RBD Variant FDO (mandatory).
- `mac:hasPredictionMethod` → Type 9 Computational Method FDO (mandatory).
- `mac:hasRMSD` → decimal value placeholder, units Angstroms (mandatory).
- Self-materialization block byte-identical to Type 1 v4.

## Generated from

- Config: `generator/configs/type3_config.py`
- Source: `drafts/template_type3_computational_prediction_rmsd_v1.trig`
- Signed: `drafts/signed/template_type3_computational_prediction_rmsd_v1.trig`
- Branch: `stage2-templates-types-3-4-5`
