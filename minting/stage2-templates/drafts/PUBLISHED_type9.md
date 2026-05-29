# Type 9 — Computational Method — publication record

## Trusty URI

`https://w3id.org/np/RA5f4FtcnAGRtdt-vDTCvwXT1yVX7oMoXmvv-B8nfMelc`

## Publish window

| Stage | Timestamp (UTC) |
|---|---|
| Local sign + np check | 2026-05-27T20:46Z (`1 trusty with signature`) |
| Publish start | 2026-05-27T20:46:45Z |
| Publish end   | 2026-05-27T20:46:49Z |

`nanopub publish`: `1 nanopub published at https://registry.petapico.org/`.

## Verification

- Registry HEAD via `w3id.org` → 307 → `registry.knowledgepixels.com` → **200 OK**.
- Signature roundtrip (local vs. fetched `npx:hasSignature`): **MATCH** (`MUpuG4iqC4axOB1HV47noqoUNh7bZ8QDoZO3XtFx…`).
- `npx:signedBy`: `https://orcid.org/0000-0001-8888-635X`.
- NanoDash explore (`/explore?id=…`): **200 OK**.
  - `AssertionTemplate` ×5, `use this template` ×1, `ExternalUriPlaceholder` ×9, `RepeatableStatement` ×9, `OptionalStatement` ×18.
- Signed-file confirmation: `sub:st_ci a nt:RepeatableStatement` (mandatory + repeatable, no OptionalStatement); `sub:st_su a nt:OptionalStatement` (optional).

## Manifest cross-check

- `mac:ComputationalMethod` → `RAnxnqy2hDygtFwC0w7EtRCyh4mQtiCGIG31iS8QT8O5Q`

## SPS v1.3 conformance

- `includes_fair2 = False` — method FDOs do not carry the FAIR² pair.
- No `dct:source` (methods do not derive from FAIR² Data Package).
- No `mac:isObservationOf` (methods are not observations).
- `cito:citesAsAuthority` **mandatory + repeatable** (`st_ci`, `nt:RepeatableStatement` only) — distinct from Types 2-8 where the same predicate is optional + repeatable.
- `schema:url` optional (`st_su`, `nt:OptionalStatement`).
- Self-materialization block byte-identical to Type 1 v4.

`schema:` and `cito:` prefixes are not in the common scaffold @prefix header (would break Type 1 v4 round-trip), so both predicates appear as full URIs at instance-pattern time, and their rdfs:label entries are in `external_resource_labels`.

## Generated from

- Config: `generator/configs/type9_config.py`
- Source: `drafts/template_type9_computational_method_v1.trig`
- Signed: `drafts/signed/template_type9_computational_method_v1.trig`
- Branch: `stage2-templates-types-9-10-11`
