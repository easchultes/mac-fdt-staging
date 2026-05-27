# Stage 2 Type 1 v4 — live NSN publication record

## Trusty URI
```
https://w3id.org/np/RADOnITa1gjGIQtuENvlB2I7hykzrASzake1bIjGLiAtM
```

## Publication

- **Registry**: https://registry.petapico.org/ (canonical w3id.org redirect goes to https://registry.knowledgepixels.com/)
- **Publish start**: 2026-05-27T13:15:27Z
- **Publish end**: 2026-05-27T13:15:31Z
- **Method**: `nanopub publish` (no `-u` flag — production)
- **Log**: `1 nanopub published at https://registry.petapico.org/`

## Verification

| Check | Result |
|---|---|
| HEAD on canonical w3id.org URI | 307 → `registry.knowledgepixels.com`, then 200 OK |
| Fetched signature matches signed file's `npx:hasSignature` | ✅ identical |
| Novel `st5d` self-reference (`<NANOPUB> dcat:accessURL <NANOPUB>`) preserved on production | ✅ present in fetched TriG (serializer reordered to object/predicate/subject; semantically identical) |
| `nanopub check` on signed bytes pre-publish | `Summary: 1 trusty with signature;` |

## NanoDash render

URL inspected: `https://nanodash.knowledgepixels.com/explore?id=https://w3id.org/np/RADOnITa1gjGIQtuENvlB2I7hykzrASzake1bIjGLiAtM`

- HTTP 200 (after session redirect)
- 338 KB rendered HTML
- "Template:" header and "Declaring a Spike RBD Variant" label present
- "AssertionTemplate" type recognized
- **"use this template" link present** — NanoDash recognizes v4 as a usable template
- Constructed publish URL: `https://nanodash.knowledgepixels.com/publish?template=https%3A%2F%2Fw3id.org%2Fnp%2FRADOnITa1gjGIQtuENvlB2I7hykzrASzake1bIjGLiAtM&template-version=latest`

**Render status: OK.** No error rendering the novel `st5d` self-reference clause.

## Project page integration (separate from this publication)

To make v4 appear on the MAC-FDO NanoDash project page (`https://w3id.org/kpxl/custom/project/terms/MAC-FDO`), the project definition nanopub (`https://w3id.org/np/RA5ID1TGERiCerY1uO270r16jqYKQjvA1emomce3l89Jo`) must be superseded by a new version that adds v4's Trusty URI to its `gen:hasPinnedTemplate` list. Erik is one of three `gen:hasOwner` ORCIDs on the project definition and can do this when ready.
