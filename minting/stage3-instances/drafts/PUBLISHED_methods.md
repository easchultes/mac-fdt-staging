# Stage 3 method instances — publication record

Five shared method FDOs (Types 9, 10, 11) published to the live NSN on
2026-05-28. Each materializes its TriG as the FDO substance (per SPS
v1.4 §"Self-materialization") and is referenced by observation
instances (Types 2-8) via `mac:hasPredictionMethod`,
`mac:hasExperimentalMethod`, or `mac:hasSurveillanceMethod`.

## Trusty URIs — for observation-instance cross-references

These are the URIs Stage 3 Type 2-8 observation instances will use
when they fill in `sub:predictionMethod`, `sub:experimentalMethod`,
or `sub:surveillanceMethod`.

| Method | Used by observation type(s) | Trusty URI |
|---|---|---|
| **ESM2** | Type 3 RMSD, Type 4 SASA, Type 5 pLDDT (ESM rows) | `https://w3id.org/np/RADJxd-U-p7VpA01uXlsp3nkUo3oXFMSOam04-fcF0ZyM` |
| **AlphaFold 2** | Type 3 RMSD, Type 4 SASA, Type 5 pLDDT (AlphaFold rows) | `https://w3id.org/np/RA3zXmeaYZxYSPXzH7CK8-m5T31NWr9nvUCeyKz2mbvNI` |
| **Bio2Byte AgMata** | Type 6 AgMata | `https://w3id.org/np/RA3JGJN1R1uTyj1puobq1cEwHT52LNmM_67dzb0oRAz2U` |
| **Bloom Lab DMS** | Type 7 DMS | `https://w3id.org/np/RA0Bz7doV8fCSO9lEmpbtNTOnMu5lB3jVudjo-tD0T_Q0` |
| **GISAID** | Type 2 Real-World Occurrence (`hasSurveillanceMethod`) | `https://w3id.org/np/RA7XLn4SiwTU4L_5YFYW8KBefgKeYXRu5DSFvYtlZE-o4` |

The full referent URIs (what observation instances actually need for
`sub:fdo` cross-link) are the Trusty URI + `/<instance_id>`:

- `…/RADJxd…/ESM2-Method`
- `…/RA3zXm…/AlphaFold2-Method`
- `…/RA3JGJ…/AgMata-Method`
- `…/RA0Bz7…/BloomLab-DMS-Method`
- `…/RA7XLn…/GISAID-Method`

## Publish window

| Method | Start (UTC) | End (UTC) |
|---|---|---|
| ESM2       | 2026-05-28T07:47:16Z | 2026-05-28T07:47:19Z |
| AlphaFold2 | 2026-05-28T07:47:19Z | 2026-05-28T07:47:22Z |
| AgMata     | 2026-05-28T07:47:22Z | 2026-05-28T07:47:25Z |
| Bloom DMS  | 2026-05-28T07:47:25Z | 2026-05-28T07:47:28Z |
| GISAID     | 2026-05-28T07:47:28Z | 2026-05-28T07:47:31Z |

All five: `1 nanopub published at https://registry.petapico.org/`.

## Verification

| Method | Registry HEAD | Signature roundtrip | NanoDash explore markers |
|---|---|---|---|
| ESM2       | 307 → 200 | MATCH (`IESNZhNEoGgv9faJfuCWe2Mz4tbHsc8jzLBIEQDD…`) | `FAIRDigitalObject` ×5, `citesAsAuthority` ×3, `schema.org/url` ×2, no isObservationOf/dct:source |
| AlphaFold2 | 307 → 200 | MATCH (`9JUUgW6A8QWwdPVeVagORrtkCZEq5NTJxf+0PIhJ…`) | same shape |
| AgMata     | 307 → 200 | MATCH (`dvjaAXwZj/syiPN3hEsC/MCqCZLJ3IOqapp8+qJp…`) | same shape |
| Bloom DMS  | 307 → 200 | MATCH (`CyMQ/wj1VI2O0GTe32ipSHSa8YskTCOJyFDvdegf…`) | same shape |
| GISAID     | 307 → 200 | MATCH (`Qkwj+rmkGBSbGlyoMGow5oQsIZX/HEycEehdOOy0…`) | `citesAsAuthority` ×6 (2 DOIs), `schema.org/url` ×2 |

All five: `npx:signedBy` = `https://orcid.org/0000-0001-8888-635X`.

## Per-instance facts

| Method | Class | cito:citesAsAuthority | schema:url |
|---|---|---|---|
| ESM2 | `mac:ComputationalMethod` | https://doi.org/10.1126/science.ade2574 | https://github.com/facebookresearch/esm |
| AlphaFold 2 | `mac:ComputationalMethod` | https://doi.org/10.1038/s41586-021-03819-2 | https://github.com/google-deepmind/alphafold |
| Bio2Byte AgMata | `mac:ComputationalMethod` | https://doi.org/10.1093/bioinformatics/btac149 | https://bio2byte.be/b2btools/ |
| Bloom Lab DMS | `mac:ExperimentalMethod` | https://doi.org/10.1016/j.cell.2020.08.012 | https://github.com/jbloomlab/SARS-CoV-2-RBD_DMS |
| GISAID | `mac:ObservationalMethod` | https://doi.org/10.2807/1560-7917.ES.2017.22.13.30494, https://doi.org/10.46234/ccdcw2021.255 | https://www.gisaid.org/ |

## SPS v1.3/v1.4 conformance

- Self-materialization block (st5b/st5c/st5d + closing brace) **byte-identical** across all 5 method instances and matches Type 1 Alpha/Epsilon/Eta instances.
- `dct:isPartOf → StayAhead Project FDO` (mandatory) present on all 5.
- Forbidden statements absent on all 5: `mac:isObservationOf` ×0, `dct:source` ×0, `dct:references` ×0.
- `cito:citesAsAuthority` rendered as mandatory + repeatable; GISAID carries 2 authorities.
- `schema:url` optional but provided for all 5.
- `cito:` and `schema:` prefixes emitted as full URIs (not in scaffold @prefix header) — same convention as the Stage 2 method templates.
- Each instance's pubinfo carries `nt:wasCreatedFromTemplate` pointing at the matching Stage 2 Type 9/10/11 template Trusty URI.

## Generated from

- Generator: `minting/stage3-instances/generator/generate_instance.py` (extended with `kind: "method"` dispatch)
- Configs: `minting/stage3-instances/generator/instance_configs/method_{esm2,alphafold2,agmata,bloom_dms,gisaid}.py`
- Sources: `minting/stage3-instances/drafts/instance_method_{…}_v1.trig`
- Signed:  `minting/stage3-instances/drafts/signed/instance_method_{…}_v1.trig`
- Branch:  `stage3-instances-methods`
