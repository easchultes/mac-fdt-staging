# Type 2 — Real-World Occurrence — publication record

## Trusty URI

`https://w3id.org/np/RA_-AALlM1rIYcJRsFUrIfSb5KYSvjiHUZbQbN-cpeV6w`

## Publish window

| Stage | Timestamp (UTC) |
|---|---|
| Local sign + np check | 2026-05-27T20:09:00Z (approx; `np check` → `1 trusty with signature`) |
| Publish start | 2026-05-27T20:10:54Z |
| Publish end   | 2026-05-27T20:10:57Z |
| Registry HEAD verified | 2026-05-27T20:11:10Z |

`nanopub publish` reported: `1 nanopub published at https://registry.petapico.org/`.

## Signature roundtrip

Local signed bytes vs. live-registry fetch:

- Local `npx:hasSignature`:
  `sH51YjFu9Txkfirzd1r/H+U+EiaSm3vbo64X56K652s98NAuOzrVfaRjTG2CnzyN4TX/BBufTTENfJHxh7kOTwt4cFgOZSKPgVdw7cisfrrTlbPIx03SFIzu9Jk+PenGlsQLb/mgEF07WfZf4IH90AZetQINh6Ust6lZWJA6EKY=`
- Fetched `npx:hasSignature`: identical.
- `npx:signedBy`: `https://orcid.org/0000-0001-8888-635X`
- `npx:hasAlgorithm`: RSA

## Registry resolution

`HEAD https://w3id.org/np/RA_-AALlM1rIYcJRsFUrIfSb5KYSvjiHUZbQbN-cpeV6w`
→ `307 Temporary Redirect`
→ `https://registry.knowledgepixels.com/np/RA_-AALlM1rIYcJRsFUrIfSb5KYSvjiHUZbQbN-cpeV6w`
→ `200 OK`, `Nanopub-Registry-Version: 1.10.0`, `Nanopub-Registry-Status: ready`,
TriG content (10,147 bytes) retrievable with `Accept: application/trig`.

## NanoDash render

| View | URL | Status |
|---|---|---|
| Explore | `https://nanodash.knowledgepixels.com/explore?id=https://w3id.org/np/RA_-AALlM1rIYcJRsFUrIfSb5KYSvjiHUZbQbN-cpeV6w` | 200 OK; recognized as **AssertionTemplate**, **"use this template"** link present, label-pattern + class label + `ExternalUriPlaceholder` markers all rendered in the served HTML |
| Publish form | `https://nanodash.knowledgepixels.com/publish?template=https://w3id.org/np/RA_-AALlM1rIYcJRsFUrIfSb5KYSvjiHUZbQbN-cpeV6w` | 200 OK to ORCID OAuth challenge (expected production gating — full form rendering requires logged-in NanoDash session) |

Explore-view body markers (curl, no JS): `AssertionTemplate` ×5,
`use this template` ×1, `Real-World Occurrence` ×4, `Real-world occurrence` ×1
(label pattern), `isObservationOf` ×9, `ExternalUriPlaceholder` ×15,
`occurrenceDate` ×13.

## Generated from

- Config:   `minting/stage2-templates/generator/configs/type2_config.py`
- Source:   `minting/stage2-templates/drafts/template_type2_real_world_occurrence_v2.trig`
- Signed:   `minting/stage2-templates/drafts/signed/template_type2_real_world_occurrence_v2.trig`
- Branch:   `stage2-templates-type2`

## SPS v1.3 conformance

- Mandatory `dct:isPartOf → sub:project` (guided-choice from project catalogue): present via common scaffold `st_pp`.
- Optional + repeatable `cito:citesAsAuthority`: present as `st_oc`
  with placeholder `sub:authority`.
- No fixed FAIR² citation pair (`includes_fair2 = False`), per §"FAIR² citation policy" for Types 2–8.
- Self-materialization block (`st5`, `st5b`, `st5c`, `st5d`): byte-identical to Type 1 v4.

## Notes

- `Trusty URI artifact code starts with `RA_-` (leading underscore in
  base64url) — unusual but valid; resolution and signature verification
  unaffected.
- Incubator-project4 space-definition supersession deferred: all 11
  templates publish first, then a single supersession adds them as
  pinned templates.
