# Stage 3 final observations (Types 2, 6, 7, 8) — publication record

12 observation FDOs published to the live NSN on 2026-05-28:
- Type 2 (Real-World Occurrence) × 3 — GISAID surveillance + GeoNames location
- Type 6 (AgMata) × 3 — sequence-derived aggregation propensity
- Type 7 (DMS) × 3 — Bloom Lab deep mutational scanning (6 values each)
- Type 8 (WHO Classification) × 3 — VOC / VOI designations

Completes the 38-instance Stage 3 demonstration catalogue:
**3 variant anchors + 5 method FDOs + 18 prediction observations +
12 final observations = 38 / 38**.

## Trusty URIs (12, by instance_id)

| instance_id | Trusty URI |
|---|---|
| type2_alpha       | `https://w3id.org/np/RAyjkMnXEnRF09TI4R531mYM4LKEm3HL5seHnVgQcqHN0` |
| type2_epsilon     | `https://w3id.org/np/RATGfqd-Sy27F_M9NXKkbL-GzIO9IYXJguGTXBb2VEyQA` |
| type2_eta         | `https://w3id.org/np/RAnwHIpm48gC4xB4d6ZxG1cDonBDEWGM-RyMf56_a5bk0` |
| type6_alpha       | `https://w3id.org/np/RArJqTu2lE7v02BrY-UmChPKJEwR004azwXfZhZ3d5ZjQ` |
| type6_epsilon     | `https://w3id.org/np/RAmPs3MytCSM__DOeyHDJQP9mwYJU6UXKKU8WGhrw5_KY` |
| type6_eta         | `https://w3id.org/np/RAcm_5ysAXUPBHcvhNVo_Xnu6OGO0SBEGvzqb4wGfVm-g` |
| type7_alpha       | `https://w3id.org/np/RARb0NfCsCVn6tTY3m1sXor6mEbZzIZ6WzBSEjtmftLgs` |
| type7_epsilon     | `https://w3id.org/np/RAfI_EQBRQvVh3LRb0WLQFvXra2gINrvxaOZQprZ0KngE` |
| type7_eta         | `https://w3id.org/np/RAmrs8u-EM7ejf5shyxo9OVXf2fgAcmB_HB4F-smPQJL0` |
| type8_alpha       | `https://w3id.org/np/RApoAkERvI9mPGcz-ExkSSDvXbNAYZygNFW2IAZpaRsGk` |
| type8_epsilon     | `https://w3id.org/np/RAn5yBad0gMJPsVE5rIiJvWP1GemI-2Wmi91KcCOSFQSg` |
| type8_eta         | `https://w3id.org/np/RAJRZGtEnHkqBERKZg34r8iX7sbEemtqOURYyRgB0MSa4` |

## Publish window

| instance_id | start (UTC) | end (UTC) |
|---|---|---|
| type2_alpha    | 08:24:50 | 08:24:54 |
| type2_epsilon  | 08:24:54 | 08:24:57 |
| type2_eta      | 08:24:57 | 08:25:00 |
| type6_alpha    | 08:25:00 | 08:25:03 |
| type6_epsilon  | 08:25:03 | 08:25:06 |
| type6_eta      | 08:25:06 | 08:25:10 |
| type7_alpha    | 08:25:10 | 08:25:13 |
| type7_epsilon  | 08:25:13 | 08:25:16 |
| type7_eta      | 08:25:16 | 08:25:19 |
| type8_alpha    | 08:25:19 | 08:25:23 |
| type8_epsilon  | 08:25:23 | 08:25:26 |
| type8_eta      | 08:25:26 | 08:25:29 |

All 12 published sequentially within 39 seconds (2026-05-28T08:24:50Z → 08:25:29Z). `1 nanopub published at https://registry.petapico.org/` for each.

## Verification

- All 12: registry HEAD `307→200`, signature roundtrip MATCH — **12/12 OK**.
- NanoDash explore spot-checks (the two new shapes):

**Type 2 — Alpha-Occurrence** (`RAyjkMnX…`):
- `FAIRDigitalObject` ×5, `RealWorldOccurrence` ×5, `isObservationOf` ×3, **`hasSurveillanceMethod` ×3**, `hasOccurrenceDate` ×3, **`hasCollectionLocation` ×3**, `hasGISAIDAccession` ×3, GeoNames id `6269131` ×4, `GISAID` ×9.

**Type 8 — Alpha-WHO** (`RApoAkER…`):
- `FAIRDigitalObject` ×5, `WHOVariantClassification` ×5, `isObservationOf` ×3, `hasWHOClassification` ×3, `hasClassificationDate` ×3, `VOC` ×5 (the assigned classification), `VOI` ×0, `VUM` ×0 (correctly absent — only the chosen value renders).

Both spot-checks confirm: AssertionTemplate-derived instance, mac:isObservationOf linkage to Type 1 anchor present, type-specific predicates render correctly.

## Stage 3 catalogue (38 / 38 live)

| Group | Count | Live | Trusty URIs (record) |
|---|---|---|---|
| Type 1 anchors (Alpha/Epsilon/Eta) | 3 | ✓ | `PUBLISHED_type1_instances.md` |
| Method FDOs (ESM2/AlphaFold2/AgMata/Bloom/GISAID) | 5 | ✓ | `PUBLISHED_methods.md` |
| Prediction observations (3 var × 2 method × 3 metric) | 18 | ✓ | `PUBLISHED_predictions.md` |
| Final observations (Type 2 × 3 + Type 6 × 3 + Type 7 × 3 + Type 8 × 3) | 12 | ✓ | this file |
| **Total** | **38** | **38 / 38** | |

## SPS v1.3 / v1.4 conformance

- All 12: `dct:isPartOf → draft StayAhead Project FDO` (per demonstration posture; cleanup logged in `Post_demonstration_cleanup.md`).
- All 12: self-materialization 4-statement block byte-identical to Type 1 Alpha instance.
- All 12: `cito:citesAsAuthority` absent (two-hop method attribution).
- Type 2: `dct:source` absent (occurrences cite no published data source; surveillance method link covers attribution).
- Type 6: `dct:source` mandatory + repeatable with 3 values [ESM Dataset FDO + FAIR² Package + FAIR² ESM resource URL] per SPS v1.3 §"Source URLs (Types 3-6)".
- Type 7: `dct:source` absent per demonstration posture (template makes it optional + repeatable; no canonical Bloom dataset FDO on the NSN).
- Type 8: `dct:source` absent (WHO designations are authoritative, not derivative); `mac:hasWHOClassification` uses curie form (`mac:VOC` / `mac:VOI`) matching the template's `nt:possibleValue` declaration.

## Generated from

- Generator: `minting/stage3-instances/generator/generate_instance.py` (extended with `kind: "occurrence"`, `"dms"`, `"who"`)
- CSV driver: `minting/stage3-instances/generator/generate_type6_7_from_csv.py` (per-variant; reuses prediction path for Type 6)
- Per-instance configs: `instance_configs/type2_{alpha,epsilon,eta}.py`, `type8_{alpha,epsilon,eta}.py`
- Source data: `data/FDT4Claude_small_v1_2.csv` (Type 6 + Type 7)
- Sources: `drafts/instance_type{2,6,7,8}_{alpha,epsilon,eta}_v1.trig`
- Signed:  `drafts/signed/instance_type{2,6,7,8}_{alpha,epsilon,eta}_v1.trig`
- Branch:  `stage3-instances-types-2-6-7-8`

## Post-demonstration items (deferred per Post_demonstration_cleanup.md)

- StayAhead Project FDO and the 2 Dataset FDOs (ESM + AlphaFold) are
  `npx:DraftNanopub` — all 38 Stage 3 instances reference at least one
  via `dct:isPartOf` (Project) or `dct:source` (Datasets). Promotion to
  non-draft happens in the coordinated revision pass.
- Per-observation `cito:citesAsAuthority` deferred for Types 2-8.
- Epsilon location: `GeoNames 6252001` (United States) — broader than
  v1.3's California candidate (`5332921`). Already published as-is per
  CSV review confirmation.
