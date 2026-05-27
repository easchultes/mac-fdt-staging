# Type 11 — Observational Method — publication record

## Trusty URI

`https://w3id.org/np/RAW9DfO6hmmt2sz_H4pHWWAX72BzTsnYjb9hi5wVQIQdE`

## Publish window

| Stage | Timestamp (UTC) |
|---|---|
| Local sign + np check | 2026-05-27T20:46Z (`1 trusty with signature`) |
| Publish start | 2026-05-27T20:46:52Z |
| Publish end   | 2026-05-27T20:46:55Z |

`nanopub publish`: `1 nanopub published at https://registry.petapico.org/`.

## Verification

- Registry HEAD via `w3id.org` → 307 → `registry.knowledgepixels.com` → **200 OK**.
- Signature roundtrip (local vs. fetched `npx:hasSignature`): **MATCH** (`tRP0uZUWpNVLkG/e4F0YD4wTo7rlCB0G2eF/RokR…`).
- `npx:signedBy`: `https://orcid.org/0000-0001-8888-635X`.
- NanoDash explore (`/explore?id=…`): **200 OK**.
  - `AssertionTemplate` ×5, `use this template` ×1, `ExternalUriPlaceholder` ×9, `RepeatableStatement` ×9, `OptionalStatement` ×18.
- Signed-file confirmation: `sub:st_ci a nt:RepeatableStatement` (mandatory + repeatable); `sub:st_su a nt:OptionalStatement` (optional).

## Manifest cross-check

- `mac:ObservationalMethod` → `RALrwDOAWiIPVr1uNQyNf43gRhcSkgFKDFm0jhn2pB0F8`

## SPS v1.3 conformance

Same as Type 9 — see `PUBLISHED_type9.md` for shared notes. The class
differs (`mac:ObservationalMethod`) and the sub:url placeholder label
is "platform URL" rather than "software URL".

## Generated from

- Config: `generator/configs/type11_config.py`
- Source: `drafts/template_type11_observational_method_v1.trig`
- Signed: `drafts/signed/template_type11_observational_method_v1.trig`
- Branch: `stage2-templates-types-9-10-11`

## Stage 2 complete

All 11 MAC FDT templates now live on the NSN:

| Type | Class | Trusty URI |
|---|---|---|
| 1 | Spike RBD Variant | RADOnITa1gjGIQtuENvlB2I7hykzrASzake1bIjGLiAtM |
| 2 | Real-World Occurrence | RA_-AALlM1rIYcJRsFUrIfSb5KYSvjiHUZbQbN-cpeV6w |
| 3 | Computational Prediction — RMSD | RALJKysR8vqqqZYXPGHcsI_J0BvPFUmzwOnV9WCGvUjcY |
| 4 | Computational Prediction — SASA | RALSYeUQIciUad7GTfKjdNkfhP-505fesw6yYtdLoyW18 |
| 5 | Computational Prediction — pLDDT | RAm5j8EmzrS_ZDXEEOkvG2icT27GlbaGoNAS0sCDS72wc |
| 6 | Computational Prediction — AgMata | RAuCu_OnyqK_dlaJ9l1EDdbtu_Wbpdw2pTlcTimQ9mqV0 |
| 7 | DMS Experimental Observation | RAp-dZcpmyNxtFsh7G0G1CDzzP2vPqoXVZSnlYRVQ_5Yk |
| 8 | WHO Variant Classification | RAWyoHGVyB3Rh-fizZguS1zzf8Cim3q5ngWSoQNs2Sgcs |
| 9 | Computational Method | RA5f4FtcnAGRtdt-vDTCvwXT1yVX7oMoXmvv-B8nfMelc |
| 10 | Experimental Method | RALExfuvWjR8Lezp7I64cWCHgqyLb52js6-CTDIoINohs |
| 11 | Observational Method | RAW9DfO6hmmt2sz_H4pHWWAX72BzTsnYjb9hi5wVQIQdE |

Next: incubator-project4 supersession to pin all 11 templates and add the standing SPARQL views.
