# Type 10 — Experimental Method — publication record

## Trusty URI

`https://w3id.org/np/RALExfuvWjR8Lezp7I64cWCHgqyLb52js6-CTDIoINohs`

## Publish window

| Stage | Timestamp (UTC) |
|---|---|
| Local sign + np check | 2026-05-27T20:46Z (`1 trusty with signature`) |
| Publish start | 2026-05-27T20:46:49Z |
| Publish end   | 2026-05-27T20:46:52Z |

`nanopub publish`: `1 nanopub published at https://registry.petapico.org/`.

## Verification

- Registry HEAD via `w3id.org` → 307 → `registry.knowledgepixels.com` → **200 OK**.
- Signature roundtrip (local vs. fetched `npx:hasSignature`): **MATCH** (`NvMKzcpuy7bQWYhEJ0+UE7x22uIYBWiuaUuVkLEo…`).
- `npx:signedBy`: `https://orcid.org/0000-0001-8888-635X`.
- NanoDash explore (`/explore?id=…`): **200 OK**.
  - `AssertionTemplate` ×5, `use this template` ×1, `ExternalUriPlaceholder` ×9, `RepeatableStatement` ×9, `OptionalStatement` ×18.
- Signed-file confirmation: `sub:st_ci a nt:RepeatableStatement` (mandatory + repeatable); `sub:st_su a nt:OptionalStatement` (optional).

## Manifest cross-check

- `mac:ExperimentalMethod` → `RAZ6oFtmR_aeSfjBD634RS-VhRP1k__3u_tWgziHbW1JU`

## SPS v1.3 conformance

Same as Type 9 — see `PUBLISHED_type9.md` for shared notes. The class
differs (`mac:ExperimentalMethod`) and the sub:url placeholder label
is "data resource URL" rather than "software URL".

## Generated from

- Config: `generator/configs/type10_config.py`
- Source: `drafts/template_type10_experimental_method_v1.trig`
- Signed: `drafts/signed/template_type10_experimental_method_v1.trig`
- Branch: `stage2-templates-types-9-10-11`
