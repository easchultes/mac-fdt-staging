# Stage 3 Type 1 instances — publication record

Three Spike RBD Variant anchor FDOs (Alpha / Epsilon / Eta) published
to the live NSN on 2026-05-28. Each instance materializes its TriG as
the FDO substance (per SPS v1.4 §"Self-materialization"), references
the Type 1 template (`RADOnITa1gjGIQtuENvlB2I7hykzrASzake1bIjGLiAtM`),
and anchors institutional provenance via `dct:isPartOf → StayAhead
Project FDO` (still a draft per Post_demonstration_cleanup.md; demo
instances reference it as-is).

## Trusty URIs

| Variant | Trusty URI |
|---|---|
| Alpha   | `https://w3id.org/np/RA4BHII2Bz7HfpUkaSJqNmhjF8F7hyWpCJnvXYkA4EP_M` |
| Epsilon | `https://w3id.org/np/RAbyuWWdW-j1rYt7Eqnva6aBvMyTkM9_Ka2FbA9dJHR7s` |
| Eta     | `https://w3id.org/np/RAikllrKWQoo81RYYvGJjWfzE0QiGrLquMMIwDD6xem2s` |

## Publish window

| Stage | Alpha | Epsilon | Eta |
|---|---|---|---|
| Publish start (UTC) | 2026-05-28T07:39:04Z | 2026-05-28T07:39:07Z | 2026-05-28T07:39:10Z |
| Publish end   (UTC) | 2026-05-28T07:39:07Z | 2026-05-28T07:39:10Z | 2026-05-28T07:39:13Z |

`nanopub publish`: `1 nanopub published at https://registry.petapico.org/` for each.

## Verification

| Variant | Registry HEAD | Signature roundtrip | NanoDash explore markers |
|---|---|---|---|
| Alpha   | 307 → 200 | MATCH (`w59QAJZNC1uUV0Do0HZo7VAy/CyLvw4fBLwtVxXH…`) | `FAIRDigitalObject` ×5, `SpikeRBDVariant` ×5, `hasRBDSequence` ×3, `hasMACSeqId` ×3, `Alpha` ×86 |
| Epsilon | 307 → 200 | MATCH (`VXGcBjbZALN4+0JRwT8CwXbpUYOrF1L1pUwGQso4…`) | `FAIRDigitalObject` ×5, `SpikeRBDVariant` ×5, `hasRBDSequence` ×3, `hasMACSeqId` ×3, `Epsilon` ×87 |
| Eta     | 307 → 200 | MATCH (`ZWZGZ/eq9TjlL1AL7s3MLLeBpdqjhWUZXE9P9CGK…`) | `FAIRDigitalObject` ×5, `SpikeRBDVariant` ×5, `hasRBDSequence` ×3, `hasMACSeqId` ×3, `Eta` ×86 |

All three: `npx:signedBy` = `https://orcid.org/0000-0001-8888-635X`.

## Epsilon GISAID seq_id correction

Epsilon's `mac:hasGISAIDSeqId` is published as **`L452R`** — Epsilon's
canonical defining Spike mutation (lineages B.1.427 / B.1.429). SPS v1.3
and `FDT4Claude_small_v1_2.csv` carry `L124R`, an upstream data-entry
error to be corrected in the coordinated revision pass (see
`Post_demonstration_cleanup.md`). The live nanopub publishes the correct
value; the upstream sources will be patched separately.

Alpha and Eta carry their CSV/SPS-supplied GISAID seq_ids unchanged
(`N501Y` and `E484K` respectively).

## Per-instance values summary

| Field | Alpha | Epsilon | Eta |
|---|---|---|---|
| WHO variant name | Alpha | Epsilon | Eta |
| Pango lineage | B.1.1.7 | B.1.427 + B.1.429 | B.1.525 |
| GISAID seq_id | N501Y | **L452R (corrected)** | E484K |
| MAC seq_id | N169Y | L120R | E152K |
| GISAID accession | EPI_ISL_601443 | EPI_ISL_2295356 | EPI_ISL_941290 |
| RBD sequence length | 195 | 195 | 195 |

## Generated from

- Generator: `minting/stage3-instances/generator/generate_instance.py`
- Configs: `minting/stage3-instances/generator/instance_configs/type1_{alpha,epsilon,eta}.py`
- Sources: `minting/stage3-instances/drafts/instance_type1_{alpha,epsilon,eta}_v1.trig`
- Signed:  `minting/stage3-instances/drafts/signed/instance_type1_{alpha,epsilon,eta}_v1.trig`
- Branch:  `stage3-instances-type1`
