# Type 8 — WHO Variant Classification — publication record

## Trusty URI

`https://w3id.org/np/RAWyoHGVyB3Rh-fizZguS1zzf8Cim3q5ngWSoQNs2Sgcs`

## Publish window

| Stage | Timestamp (UTC) |
|---|---|
| Local sign + np check | 2026-05-27T20:39Z (`1 trusty with signature`) |
| Publish start | 2026-05-27T20:39:51Z |
| Publish end   | 2026-05-27T20:39:55Z |

`nanopub publish`: `1 nanopub published at https://registry.petapico.org/`.

## Verification

- Registry HEAD via `w3id.org` → 307 → `registry.knowledgepixels.com` → **200 OK**.
- Signature roundtrip (local vs. fetched `npx:hasSignature`): **MATCH** (`XUTiKqriNux1AlAbCiVBU31mlBBFr0BMp3nVnjkk…`).
- `npx:signedBy`: `https://orcid.org/0000-0001-8888-635X`.
- NanoDash explore (`/explore?id=…`): **200 OK**, body markers:
  - `AssertionTemplate` ×5
  - `use this template` ×1
  - `RestrictedChoicePlaceholder` ×6
  - `possibleValue` ×18
  - `WHO` ×40
  - `VOC` ×6, `VOI` ×5, `VUM` ×5 (all three enumerated values rendered in the form's classification picker)

## Manifest cross-check

Stage 1 v2 vocabulary confirms all required terms:

| Term | Type | Trusty URI |
|---|---|---|
| `mac:WHOVariantClassification` | class | `RAKAogouhVXFZUSbqSZ_AUAIeUnz24jzGQ3u8FKRVf0Ks` |
| `mac:VOC` | class | `RAYOlJ43EmeoJ8lLRjS9cv5pn1PKNy0udeS36KfWSRCPk` |
| `mac:VOI` | class | `RAiwK1L9NkB_qPZpdFoaIGISRB7-kO3xB3J3m3z_AkXR4` |
| `mac:VUM` | class | `RAwWafsvm-XuaeWXIfIkmY7-25TeGmLAxyb8baj0aUDGA` |
| `mac:hasWHOClassification` | predicate | `RA6-nM2tvv5wyi311wr_dumhdxsZOS3AMnLJWU8GtE3vM` |
| `mac:hasClassificationDate` | predicate | `RAtbKj58yNhJdAUthlTKf0iVzCAtN1w-U0rZxW7WvgXW4` |
| `mac:hasWHOClassificationReference` | predicate | `RAP7Qeec0TLDPZVvjYVKTATP-EMPJiCfqH4L8HbyAInOU` |

## SPS v1.3 conformance

- `includes_fair2 = False` (Types 2-8 omit fixed FAIR² pair).
- No `dct:source` statement (Type 8 lacks a published source per SPS v1.3 §"Type 8" — WHO designations are authoritative, not derivative).
- `cito:citesAsAuthority` optional + repeatable (`st_oc`) for per-observation citation.
- `mac:isObservationOf` → Type 1 Spike RBD Variant FDO (mandatory).
- `mac:hasWHOClassification` → `nt:RestrictedChoicePlaceholder` over {`mac:VOC`, `mac:VOI`, `mac:VUM`} (mandatory).
- `mac:hasClassificationDate` (optional) — time-stamps the designation, which changes over time.
- `mac:hasWHOClassificationReference` (optional) — reference URL to the WHO designation page.
- Self-materialization block byte-identical to Type 1 v4.

## Generator support

`nt:RestrictedChoicePlaceholder` with inline enumeration is supported by the existing `render_placeholder` function: the three values are passed as a single `extras` entry `("nt:possibleValue", "mac:VOC, mac:VOI, mac:VUM")`, which renders as a Turtle predicate-object-list. No generator extension was needed.

Generated output for the classification placeholder:
```turtle
sub:classification a nt:RestrictedChoicePlaceholder ;
  rdfs:label "WHO variant classification" ;
  nt:possibleValue mac:VOC, mac:VOI, mac:VUM .
```

## Generated from

- Config: `generator/configs/type8_config.py`
- Source: `drafts/template_type8_who_variant_classification_v1.trig`
- Signed: `drafts/signed/template_type8_who_variant_classification_v1.trig`
- Branch: `stage2-templates-type8`

## Note on hasStatement ID count

Task spec said `Total nt:hasStatement IDs: 20 (no st_f2a/st_f2p)`, but the math is 16 common base IDs (st0, st1, st2, st3, st4, st5, st5b, st5c, st5d, st6, st7, st8, st91, st92, st95, st_pp) + 5 type-specific (st_obs, st_oc, st_wc, st_cd, st_cr) = **21**. The "20" appears to be an off-by-one in the count (likely forgetting st_pp); the explicit statement list is internally consistent and renders correctly. Same pattern as Type 7's placeholder-count discrepancy.
