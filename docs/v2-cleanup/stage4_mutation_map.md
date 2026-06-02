# Stage 4 — Alpha Knowlet View-Set Mutation Map

Generated: 2026-06-01 (PROMPT 5 PHASE 2)
Source: ground-truth parse of v1 TriGs at `build/v2-stage4/v1-fetch/`.
Target referent: Alpha-RBD-Variant v2 (from supersession_registry):
`https://w3id.org/np/RAngbyT2iZe4xYUcPnTnDFKDaiL5-tSmoUYzF9RK3LHdE/Alpha-RBD-Variant`.

Gen namespace (locked): `https://w3id.org/kpxl/gen/terms/`
(Per `docs/v2-cleanup/stage4_gen_namespace.txt` — extracted from all 4 v1 TriGs; no @prefix gen: declared in v1, terms are emitted as full URIs.)

> **`gen:hasViewQuery` convention:** target is the bare nanopub Trusty URI (the query is accessed as an artifact). Contrast with `gen:isDisplayOfView`, which targets a `gen:View` referent URI. Different relationships, different URI forms. Useful annotation for the eventual Tobias second-PR addendum.

## Dependency chain (3 passes)

```
Pass 1 (independent)        Pass 2 (refs Pass 1)            Pass 3 (refs Pass 2)
─────────────────────       ─────────────────────────       ──────────────────────────
(1) Query nanopub  ◄────┬── (2) Pin-action               (4) View-display
                        │                                  │
                        └── (3) gen:View wrapper  ◄────────┘
```

## Nanopub (1) — Query (Pass 1)

- **v1 Trusty:** `https://w3id.org/np/RAecvUbvUWiIOKP7ZEQk7hnUsb8lWWUr1lRbVN2PsSUSA`
- **Local name (subj):** `sub:alpha-knowlet`
- **Classes:** `<https://w3id.org/kpxl/grlc/grlc-query>` (not gen: ; this is the `grlc` namespace)
- **Cross-references to mutate (1):**
  - **Alpha v1 referent inside SPARQL string literal** (the `gen:sparql` value).
    - Pattern: `?obs mac:isObservationOf <https://w3id.org/np/RA4BHII2Bz7HfpUkaSJqNmhjF8F7hyWpCJnvXYkA4EP_M/Alpha-RBD-Variant>`
    - Mutation: replace the v1 Alpha referent URI with the v2 Alpha referent URI **inside the multi-line `"""…"""` literal string**, byte-equal otherwise.
    - Note: this is a string-substitution within a literal, NOT a URI substitution in a triple object position.
- **Intra-view-set cross-refs:** 0 (does not reference any of the other 3 Stage 4 nanopubs).
- **Pass:** 1.

## Nanopub (2) — Pin-action (Pass 2)

- **v1 Trusty:** `https://w3id.org/np/RAzEolNOqr8I1aiZpafpUxJfqBOQRdTapceYWjXCoEYAE`
- **Assertion structure:** 2 triples (no `sub:` local subjects; both URIs are external):
  - `<query-trusty> gen:hasPinGroupTag "Digital twin (worked example)"`
  - `<spaces/knowledgepixels/incubator/project4> gen:hasPinnedQuery <query-trusty>`
- **Cross-references to mutate (2 occurrences of the same URI):**
  - **Bare Trusty URI of nanopub (1)** — both as subject of the first triple and object of the second.
  - Mutation: `<RAecvUbv… v1 query>` → `<v2 query Trusty>` (bare Trusty, no `/local-name` suffix).
- **⚠️ Spec divergence — pin (2) → query (1) via BARE TRUSTY URI, NOT referent URI** (the spec's PHASE 4.1.a was correct: "v1 (1) Trusty → v2 (1) Trusty"). Pin uses bare-Trusty form.
- **Pass:** 2 (depends on Pass 1 v2 (1) Trusty URI).

## Nanopub (3) — Wrapper / gen:View (Pass 2)

- **v1 Trusty:** `https://w3id.org/np/RA_zvbVo3VX6Cy3lYOI6LNHJICb1copbCmJHayjpzCeJ0`
- **Local name (subj):** `sub:fdt-alpha-knowlet-view` (the wrapper's own referent local name)
- **Classes:** `gen:ResourceView`, `gen:TabularView`
- **Cross-references to mutate (1 occurrence):**
  - `gen:hasViewQuery <https://w3id.org/np/RAecvUbvUWiIOKP7ZEQk7hnUsb8lWWUr1lRbVN2PsSUSA>` — **BARE TRUSTY URI of nanopub (1)**, NOT a referent URI.
  - Mutation: `<v1 query Trusty>` → `<v2 query Trusty>` (bare-to-bare).
- **⚠️ Spec divergence — PHASE 4.1.a stated wrapper (3) → query (1) via "v1 (1) referent → v2 (1) referent" (referent form). Actual v1 ground truth uses BARE TRUSTY URI form for `gen:hasViewQuery`. Mutation must use bare-to-bare. The wrapper itself declares its own referent (`sub:fdt-alpha-knowlet-view`) which (4) uses, but the wrapper does NOT reference (1) via (1)'s referent.**
- **Pass:** 2 (depends on Pass 1 v2 (1) Trusty URI).

## Nanopub (4) — View-display (Pass 3)

- **v1 Trusty:** `https://w3id.org/np/RA-QuZXXV9ni6b2YW0cM4ADyzYi-Uo4FQDR0p2pdR9tUk`
- **Local name (subj):** `sub:display`
- **Classes:** `gen:ActivatedViewDisplay`, `gen:ViewDisplay`
- **Cross-references to mutate (1 occurrence):**
  - `gen:isDisplayOfView <https://w3id.org/np/RA_zvbVo3VX6Cy3lYOI6LNHJICb1copbCmJHayjpzCeJ0/fdt-alpha-knowlet-view>` — **REFERENT URI of nanopub (3)** wrapper (with `/fdt-alpha-knowlet-view` suffix).
  - Mutation: `<v1 wrapper-trusty>/fdt-alpha-knowlet-view` → `<v2 wrapper-trusty>/fdt-alpha-knowlet-view` (referent-to-referent).
- **Spec match — PHASE 5.1 correctly identified this as referent-to-referent.**
- **Pass:** 3 (depends on Pass 2 v2 (3) wrapper Trusty URI).

## Summary — mutations per nanopub

| # | v1 Trusty (short) | Pass | Mutations | Reference form | Spec-match? |
|---|---|---|---|---|---|
| 1 | RAecvUbv… | 1 | 1 (Alpha v1→v2 referent inside SPARQL literal) | string substitution inside literal | ✅ |
| 2 | RAzEolNO… | 2 | 2 occurrences of (1)'s v1 Trusty URI → v2 Trusty URI | **bare Trusty** | ✅ (PHASE 4 spec correct) |
| 3 | RA_zvbVo… | 2 | 1 occurrence of (1)'s v1 Trusty URI → v2 Trusty URI | **bare Trusty** (NOT referent) | ⚠️ **Spec PHASE 4.1.a said referent-to-referent; ground truth is bare-to-bare** |
| 4 | RA-QuZXX… | 3 | 1 occurrence of (3)'s v1 referent → v2 referent | **referent URI** | ✅ |

## Per-nanopub pubinfo template inventory (preserve verbatim across re-mints)

All 4 v1 nanopubs share **4 standard pubinfo templates** + 1 nanopub-specific assertion template:

| Template role | Trusty URI |
|---|---|
| `nt:wasCreatedFromProvenanceTemplate` (all 4) | `https://w3id.org/np/RA7lSq6MuK_TIC6JMSHvLtee3lpLoZDOqLJCLXevnrPoU` |
| `nt:wasCreatedFromPubinfoTemplate` (all 4, License) | `https://w3id.org/np/RA0J4vUn_dekg-U1kK3AOEt02p9mT2WO03uGxLDec1jLw` |
| `nt:wasCreatedFromPubinfoTemplate` (all 4, Hand-coded) | `https://w3id.org/np/RAMEgudZsQ1bh1fZhfYnkthqH6YSXpghSE_DEN1I-6eAI` |
| `nt:wasCreatedFromPubinfoTemplate` (all 4, Derived) | `https://w3id.org/np/RARW4MsFkHuwjycNElvEVtuMjpf4yWDL10-0C5l2MqqRQ` |
| `nt:wasCreatedFromPubinfoTemplate` (all 4, Creator) | `https://w3id.org/np/RAukAcWHRDlkqxk7H2XNSegc1WnHI569INvNr-xdptDGI` |
| `nt:wasCreatedFromTemplate` (1, grlc-query) | `https://w3id.org/np/RAEFAt-QcFK0ZhqfvlsmS10BnzGJA0xwOICZXkO-ai87k` |
| `nt:wasCreatedFromTemplate` (2, Pin-query) | `https://w3id.org/np/RAuLESdeRUlk1GcTwvzVXShiBMI0ntJs2DL2Bm5DzW_ZQ` |
| `nt:wasCreatedFromTemplate` (3, gen:View wrapper) | `https://w3id.org/np/RARLsTlqbTesu1b0WJZ-zL1z96xumOiqbK3l_vV6iZoww` |
| `nt:wasCreatedFromTemplate` (4, gen:ViewDisplay) | `https://w3id.org/np/RAsc8FMsGih955oFSFG0YcB9sDKA62VLbp3VIw86IxMvk` |

All 4 v1 templates are still on-network (no retraction/supersession noted). Will be preserved verbatim in v2 mints (same convention as PROMPT 2A/2B).

## Provenance attribution (preserve verbatim)

All 4 v1 nanopubs: `sub:assertion prov:wasAttributedTo orcid:0000-0001-8888-635X` (Erik). No variations. Same signing key as v2 work (PROMPT 2.0/2A/2B/3).

## Anomalies / notes for Erik

1. **Spec divergence on nanopub (3) cross-ref form.** The spec PHASE 4.1.a said wrapper (3) mutates "v1 (1) referent → v2 (1) referent". Ground truth: wrapper uses `gen:hasViewQuery <query-bare-Trusty>` (NOT referent). Mutation will use bare-to-bare. Net effect on the dependency chain is identical; the URI form is just different from what the spec assumed.

2. **Nanopub (1) mutation is a STRING SUBSTITUTION inside a triple-quoted literal**, not a URI-object substitution. The Alpha v1 referent appears in the SPARQL query body literal (the `gen:sparql` value). The substitution preserves the rest of the literal byte-equal.

3. **Nanopub (1)'s assertion has only one subject (`sub:alpha-knowlet`)**; it does NOT declare a `gen:View` or `fdof:FAIRDigitalObject` typing. The referent of the query is the introduced URI (`sub:alpha-knowlet`); nanopub (3) wrapper's job is to wrap this query into a view via `gen:hasViewQuery`. Both (2) and (3) reference (1) by bare Trusty URI, not by `sub:alpha-knowlet`.

4. **`gen:` namespace** locked at `https://w3id.org/kpxl/gen/terms/` per `docs/v2-cleanup/stage4_gen_namespace.txt`.

5. **Signing key** for all 4 v1 nanopubs is Erik's local CLI key (`MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQD3w/IU...`) — the same key used for the v2 cleanup pass. Key continuity preserved.
