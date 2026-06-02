# v0.5 → v0.6_pre_consolidation §5 Trusty URI Substitution — Verification Report

**Date:** 2026-06-02 (UTC)
**Branch:** `cleanup-upstream-v2`
**Commit reproduced against:** `84d21fb0f331503c0a718383890ab4e9b113e2b8`
**Authoritative source mapping:** `docs/v2-cleanup/supersession_registry.md` (Stage 3 v1 → v2 mapping section)

## Inputs

- Source: `paper/FDT_paper_consolidated_draft_v0_5.md` (108597 bytes)
- Target: `paper/FDT_paper_consolidated_draft_v0_6_pre_consolidation.md` (newly created)
- Line range confined to per spec: **line 276** + **lines 290–339**
- Distinct placeholders in §5: **38** (matches spec count)

## Placeholder → v2 referent chain

The placeholder-to-v1 mapping was reconstructed from the placeholder naming convention (no pre-existing artifact found in repo). The chain placeholder → v1 local name → v2 referent was built using `docs/v2-cleanup/supersession_registry.md` (authoritative since PROMPT 3 commit `9e47c33`).

| Placeholder | v1 local name | v2 referent URI |
|---|---|---|
| `<TURI-A-Alpha>` | `Alpha-RBD-Variant` | `https://w3id.org/np/RAngbyT2iZe4xYUcPnTnDFKDaiL5-tSmoUYzF9RK3LHdE/Alpha-RBD-Variant` |
| `<TURI-A-Epsilon>` | `Epsilon-RBD-Variant` | `https://w3id.org/np/RADWPV5jeyK-7pxen6hMrxjP4hPNLk3EJTibcxJCInv30/Epsilon-RBD-Variant` |
| `<TURI-A-Eta>` | `Eta-RBD-Variant` | `https://w3id.org/np/RA8yS9sU1tq87fXelVb4Q7uwjpoDXOsoelXM5--tfu6IQ/Eta-RBD-Variant` |
| `<TURI-M-AF>` | `AlphaFold2-Method` | `https://w3id.org/np/RAPz4KzBYjUUaURNGn4pR7PpJ5VAvv43v5dYK7gyG1DXk/AlphaFold2-Method` |
| `<TURI-M-Bio2Byte>` | `AgMata-Method` | `https://w3id.org/np/RAfY9JAThg7kIl7-63YT2KdVN7y8INAyqpnow339n3tpU/AgMata-Method` |
| `<TURI-M-Bloom>` | `BloomLab-DMS-Method` | `https://w3id.org/np/RAWQDkXVW2tB6LEgirShh03PKJOznYQFVLx8-YXhWfnew/BloomLab-DMS-Method` |
| `<TURI-M-ESM>` | `ESM2-Method` | `https://w3id.org/np/RAV_9iAUAyUyNLhVQxpTaE54ko_liTnBpIarZBnkBcbgw/ESM2-Method` |
| `<TURI-M-GISAID>` | `GISAID-Method` | `https://w3id.org/np/RAdSYycNtllf-CCXJ5HMMUaF-arNhDj0oGdiZyCBC08o0/GISAID-Method` |
| `<TURI-O-Alpha-AgMata>` | `type6_alpha` | `https://w3id.org/np/RAZtTGo_ObQHC1hN7XIdW1JYbbRCuZqUofeUM-jsWJjds/Alpha-AgMata` |
| `<TURI-O-Alpha-DMS>` | `type7_alpha` | `https://w3id.org/np/RAgsEHPr-WCHfLH2RNMFCVw4BHgqP3GvnGPfV5SqEkPRY/Alpha-DMS` |
| `<TURI-O-Alpha-RMSD-AF>` | `Alpha-RMSD-AlphaFold2` | `https://w3id.org/np/RAaZJ0IuCVz8QaGyDWn10j8TBlpIifMDxqi7HzglNuz80/Alpha-RMSD-AlphaFold2` |
| `<TURI-O-Alpha-RMSD-ESM>` | `Alpha-RMSD-ESM2` | `https://w3id.org/np/RAf8cMF_qJFg1LAVkriSe7X1yoIz4Kg6GVaO0qrMYoaLg/Alpha-RMSD-ESM2` |
| `<TURI-O-Alpha-RWO>` | `type2_alpha` | `https://w3id.org/np/RAHiypVLAG5QdV2Dl09EAuvXJAsaTiOIS9JwNEGSFVPSg/Alpha-Occurrence` |
| `<TURI-O-Alpha-SASA-AF>` | `Alpha-SASA-AlphaFold2` | `https://w3id.org/np/RA2aycCXga1Q6CU9uN28ZLQqAVDXUuIgPsP8QW07LD5ws/Alpha-SASA-AlphaFold2` |
| `<TURI-O-Alpha-SASA-ESM>` | `Alpha-SASA-ESM2` | `https://w3id.org/np/RATDFrbGzT9BSFCTLpQDf4HZWNpd4ReXlzvuJJ5oaTKrQ/Alpha-SASA-ESM2` |
| `<TURI-O-Alpha-WHO>` | `type8_alpha` | `https://w3id.org/np/RAnX2nF3Xep8CEn5GGZbRrjPQHVORHx_0tHM4cagWFVJ8/Alpha-WHO` |
| `<TURI-O-Alpha-pLDDT-AF>` | `Alpha-pLDDT-AlphaFold2` | `https://w3id.org/np/RArrrQfjNxWFA6C4F3-QB5qJEsQOkTeivRX7_PmWWO_hQ/Alpha-pLDDT-AlphaFold2` |
| `<TURI-O-Alpha-pLDDT-ESM>` | `Alpha-pLDDT-ESM2` | `https://w3id.org/np/RAZc567NsX-8k7XJrKAnoBcwFI92miXJcdWrcD6U7rPPE/Alpha-pLDDT-ESM2` |
| `<TURI-O-Epsilon-AgMata>` | `type6_epsilon` | `https://w3id.org/np/RAMKsiqGr-f_FCX0lIrqfyilnwgS0GGpoUS7-3kQvZFJA/Epsilon-AgMata` |
| `<TURI-O-Epsilon-DMS>` | `type7_epsilon` | `https://w3id.org/np/RAs9zpNLdQ2G1UQqQPktjJho7GLdsrHWAVORbxPyC_BRA/Epsilon-DMS` |
| `<TURI-O-Epsilon-RMSD-AF>` | `Epsilon-RMSD-AlphaFold2` | `https://w3id.org/np/RAN_Wf7LjMSofwyG0x4uhLNln8kgPnbKzl7ZHjXGKLOc4/Epsilon-RMSD-AlphaFold2` |
| `<TURI-O-Epsilon-RMSD-ESM>` | `Epsilon-RMSD-ESM2` | `https://w3id.org/np/RA7EJKrmgtLHuKzT8FBNPLo-8HMgCLzBvR2Mfxpl5iJrI/Epsilon-RMSD-ESM2` |
| `<TURI-O-Epsilon-RWO>` | `type2_epsilon` | `https://w3id.org/np/RAScF7yrx-LR-kvrvuW58TVoc-TEjqBIwG-CV9IlvmFUk/Epsilon-Occurrence` |
| `<TURI-O-Epsilon-SASA-AF>` | `Epsilon-SASA-AlphaFold2` | `https://w3id.org/np/RAE9pIZSm1uZcf3AzCBLnhC6jzl5q53sHdd6xt-z4Qglk/Epsilon-SASA-AlphaFold2` |
| `<TURI-O-Epsilon-SASA-ESM>` | `Epsilon-SASA-ESM2` | `https://w3id.org/np/RASLEpL6BamsPTgEH1FDfQ9whKu_V3-B7hHe3mVJOsuIQ/Epsilon-SASA-ESM2` |
| `<TURI-O-Epsilon-WHO>` | `type8_epsilon` | `https://w3id.org/np/RA-uT1JVPfe5gGFAo32mUvfynHAYLlBpqgt8rUy_qhrP4/Epsilon-WHO` |
| `<TURI-O-Epsilon-pLDDT-AF>` | `Epsilon-pLDDT-AlphaFold2` | `https://w3id.org/np/RAwjLl2XsUTPoaFrv45EmHr7K-HNlN--f3-pUTxmgDNnA/Epsilon-pLDDT-AlphaFold2` |
| `<TURI-O-Epsilon-pLDDT-ESM>` | `Epsilon-pLDDT-ESM2` | `https://w3id.org/np/RA7QLv-gPyZjD6BWOBekq7ZWKu4hVFMraGwwJOhArOeJU/Epsilon-pLDDT-ESM2` |
| `<TURI-O-Eta-AgMata>` | `type6_eta` | `https://w3id.org/np/RARHGQesSG3Bq1t5nkw_NwPxJj8pDTSQKwABa45dQ6Cw8/Eta-AgMata` |
| `<TURI-O-Eta-DMS>` | `type7_eta` | `https://w3id.org/np/RAymn8p9SjkROiji7aVPDRVdD3A33Ad5uuoYPTEkaMkrA/Eta-DMS` |
| `<TURI-O-Eta-RMSD-AF>` | `Eta-RMSD-AlphaFold2` | `https://w3id.org/np/RAVHbFaBJ4Ezq3LpEvHlQR2y6FbyOeA6Ltk3wk-hZZTyE/Eta-RMSD-AlphaFold2` |
| `<TURI-O-Eta-RMSD-ESM>` | `Eta-RMSD-ESM2` | `https://w3id.org/np/RAPh6zDXbnsMP304CGWT3OcY8ielo_GVifxC7oDsVB8HM/Eta-RMSD-ESM2` |
| `<TURI-O-Eta-RWO>` | `type2_eta` | `https://w3id.org/np/RAhhXSQQgmCfZau05NMwwYGae21iwK_qjgOs7GzDyHn9w/Eta-Occurrence` |
| `<TURI-O-Eta-SASA-AF>` | `Eta-SASA-AlphaFold2` | `https://w3id.org/np/RAjsJgM13kFOaExAskq-K-7KcEf1anAAbrBz_TROBWtP0/Eta-SASA-AlphaFold2` |
| `<TURI-O-Eta-SASA-ESM>` | `Eta-SASA-ESM2` | `https://w3id.org/np/RAeGQbuaKdL82xN1MBbkzLemD7twqcJYfxZdGVUWTX8G0/Eta-SASA-ESM2` |
| `<TURI-O-Eta-WHO>` | `type8_eta` | `https://w3id.org/np/RAQmYYtUl5ZE31-1yFhP9rda1KSq_TDQipwlfCZPouAHc/Eta-WHO` |
| `<TURI-O-Eta-pLDDT-AF>` | `Eta-pLDDT-AlphaFold2` | `https://w3id.org/np/RAyaXL_U120427BOikVY6A_eSSxWTtInmUqUHdB4W7EYk/Eta-pLDDT-AlphaFold2` |
| `<TURI-O-Eta-pLDDT-ESM>` | `Eta-pLDDT-ESM2` | `https://w3id.org/np/RAOevfPSd_NZh3bek1YA8M9ZWFwGFP_pTJZ4Txjw0UWz4/Eta-pLDDT-ESM2` |

## Verification Check 1 — No `<TURI-…>` markers remain in body text of substituted draft

✅ **PASS** — 0 markers remain in the substituted range (line 276 + lines 290–339).

Out-of-range `<TURI-…>` mentions preserved verbatim (per spec, the rest of the draft remains untouched at this stage):

  - line 28: ✅ preserved
  - line 400: ✅ preserved
  - line 689: ✅ preserved

## Verification Check 2 — Each v2 URI matches its supersession_registry entry

✅ **PASS** — all 38 v2 URIs found in `docs/v2-cleanup/supersession_registry.md` (line-by-line comparison via backticked string lookup).

## Verification Check 3 — HTTP GET each v2 URI on the NSN

Each v2 referent URI's bare Trusty (`<...>/<local-name>` stripped to `<...>`) HTTP-GET'd with `Accept: application/trig` against `w3id.org/np/<Trusty>` (redirects to a registry mirror). A response is considered successful if the body starts with `@prefix this: <expected-Trusty>` (raw TriG content, not the HTML 404 page).

Result: **38/38** v2 nanopubs returned live TriG content.

| Placeholder | v2 Trusty URI | HTTP code | Live TriG | First line of body |
|---|---|---|---|---|
| `<TURI-A-Alpha>` | `https://w3id.org/np/RAngbyT2iZe4xYUcPnTnDFKDaiL5-tSmoUYzF9RK3LHdE` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAngbyT2iZe4xYUcPnTnDFKDa…` |
| `<TURI-A-Epsilon>` | `https://w3id.org/np/RADWPV5jeyK-7pxen6hMrxjP4hPNLk3EJTibcxJCInv30` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RADWPV5jeyK-7pxen6hMrxjP4…` |
| `<TURI-A-Eta>` | `https://w3id.org/np/RA8yS9sU1tq87fXelVb4Q7uwjpoDXOsoelXM5--tfu6IQ` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RA8yS9sU1tq87fXelVb4Q7uwj…` |
| `<TURI-M-AF>` | `https://w3id.org/np/RAPz4KzBYjUUaURNGn4pR7PpJ5VAvv43v5dYK7gyG1DXk` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAPz4KzBYjUUaURNGn4pR7PpJ…` |
| `<TURI-M-Bio2Byte>` | `https://w3id.org/np/RAfY9JAThg7kIl7-63YT2KdVN7y8INAyqpnow339n3tpU` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAfY9JAThg7kIl7-63YT2KdVN…` |
| `<TURI-M-Bloom>` | `https://w3id.org/np/RAWQDkXVW2tB6LEgirShh03PKJOznYQFVLx8-YXhWfnew` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAWQDkXVW2tB6LEgirShh03PK…` |
| `<TURI-M-ESM>` | `https://w3id.org/np/RAV_9iAUAyUyNLhVQxpTaE54ko_liTnBpIarZBnkBcbgw` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAV_9iAUAyUyNLhVQxpTaE54k…` |
| `<TURI-M-GISAID>` | `https://w3id.org/np/RAdSYycNtllf-CCXJ5HMMUaF-arNhDj0oGdiZyCBC08o0` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAdSYycNtllf-CCXJ5HMMUaF-…` |
| `<TURI-O-Alpha-AgMata>` | `https://w3id.org/np/RAZtTGo_ObQHC1hN7XIdW1JYbbRCuZqUofeUM-jsWJjds` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAZtTGo_ObQHC1hN7XIdW1JYb…` |
| `<TURI-O-Alpha-DMS>` | `https://w3id.org/np/RAgsEHPr-WCHfLH2RNMFCVw4BHgqP3GvnGPfV5SqEkPRY` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAgsEHPr-WCHfLH2RNMFCVw4B…` |
| `<TURI-O-Alpha-RMSD-AF>` | `https://w3id.org/np/RAaZJ0IuCVz8QaGyDWn10j8TBlpIifMDxqi7HzglNuz80` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAaZJ0IuCVz8QaGyDWn10j8TB…` |
| `<TURI-O-Alpha-RMSD-ESM>` | `https://w3id.org/np/RAf8cMF_qJFg1LAVkriSe7X1yoIz4Kg6GVaO0qrMYoaLg` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAf8cMF_qJFg1LAVkriSe7X1y…` |
| `<TURI-O-Alpha-RWO>` | `https://w3id.org/np/RAHiypVLAG5QdV2Dl09EAuvXJAsaTiOIS9JwNEGSFVPSg` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAHiypVLAG5QdV2Dl09EAuvXJ…` |
| `<TURI-O-Alpha-SASA-AF>` | `https://w3id.org/np/RA2aycCXga1Q6CU9uN28ZLQqAVDXUuIgPsP8QW07LD5ws` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RA2aycCXga1Q6CU9uN28ZLQqA…` |
| `<TURI-O-Alpha-SASA-ESM>` | `https://w3id.org/np/RATDFrbGzT9BSFCTLpQDf4HZWNpd4ReXlzvuJJ5oaTKrQ` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RATDFrbGzT9BSFCTLpQDf4HZW…` |
| `<TURI-O-Alpha-WHO>` | `https://w3id.org/np/RAnX2nF3Xep8CEn5GGZbRrjPQHVORHx_0tHM4cagWFVJ8` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAnX2nF3Xep8CEn5GGZbRrjPQ…` |
| `<TURI-O-Alpha-pLDDT-AF>` | `https://w3id.org/np/RArrrQfjNxWFA6C4F3-QB5qJEsQOkTeivRX7_PmWWO_hQ` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RArrrQfjNxWFA6C4F3-QB5qJE…` |
| `<TURI-O-Alpha-pLDDT-ESM>` | `https://w3id.org/np/RAZc567NsX-8k7XJrKAnoBcwFI92miXJcdWrcD6U7rPPE` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAZc567NsX-8k7XJrKAnoBcwF…` |
| `<TURI-O-Epsilon-AgMata>` | `https://w3id.org/np/RAMKsiqGr-f_FCX0lIrqfyilnwgS0GGpoUS7-3kQvZFJA` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAMKsiqGr-f_FCX0lIrqfyiln…` |
| `<TURI-O-Epsilon-DMS>` | `https://w3id.org/np/RAs9zpNLdQ2G1UQqQPktjJho7GLdsrHWAVORbxPyC_BRA` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAs9zpNLdQ2G1UQqQPktjJho7…` |
| `<TURI-O-Epsilon-RMSD-AF>` | `https://w3id.org/np/RAN_Wf7LjMSofwyG0x4uhLNln8kgPnbKzl7ZHjXGKLOc4` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAN_Wf7LjMSofwyG0x4uhLNln…` |
| `<TURI-O-Epsilon-RMSD-ESM>` | `https://w3id.org/np/RA7EJKrmgtLHuKzT8FBNPLo-8HMgCLzBvR2Mfxpl5iJrI` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RA7EJKrmgtLHuKzT8FBNPLo-8…` |
| `<TURI-O-Epsilon-RWO>` | `https://w3id.org/np/RAScF7yrx-LR-kvrvuW58TVoc-TEjqBIwG-CV9IlvmFUk` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAScF7yrx-LR-kvrvuW58TVoc…` |
| `<TURI-O-Epsilon-SASA-AF>` | `https://w3id.org/np/RAE9pIZSm1uZcf3AzCBLnhC6jzl5q53sHdd6xt-z4Qglk` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAE9pIZSm1uZcf3AzCBLnhC6j…` |
| `<TURI-O-Epsilon-SASA-ESM>` | `https://w3id.org/np/RASLEpL6BamsPTgEH1FDfQ9whKu_V3-B7hHe3mVJOsuIQ` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RASLEpL6BamsPTgEH1FDfQ9wh…` |
| `<TURI-O-Epsilon-WHO>` | `https://w3id.org/np/RA-uT1JVPfe5gGFAo32mUvfynHAYLlBpqgt8rUy_qhrP4` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RA-uT1JVPfe5gGFAo32mUvfyn…` |
| `<TURI-O-Epsilon-pLDDT-AF>` | `https://w3id.org/np/RAwjLl2XsUTPoaFrv45EmHr7K-HNlN--f3-pUTxmgDNnA` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAwjLl2XsUTPoaFrv45EmHr7K…` |
| `<TURI-O-Epsilon-pLDDT-ESM>` | `https://w3id.org/np/RA7QLv-gPyZjD6BWOBekq7ZWKu4hVFMraGwwJOhArOeJU` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RA7QLv-gPyZjD6BWOBekq7ZWK…` |
| `<TURI-O-Eta-AgMata>` | `https://w3id.org/np/RARHGQesSG3Bq1t5nkw_NwPxJj8pDTSQKwABa45dQ6Cw8` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RARHGQesSG3Bq1t5nkw_NwPxJ…` |
| `<TURI-O-Eta-DMS>` | `https://w3id.org/np/RAymn8p9SjkROiji7aVPDRVdD3A33Ad5uuoYPTEkaMkrA` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAymn8p9SjkROiji7aVPDRVdD…` |
| `<TURI-O-Eta-RMSD-AF>` | `https://w3id.org/np/RAVHbFaBJ4Ezq3LpEvHlQR2y6FbyOeA6Ltk3wk-hZZTyE` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAVHbFaBJ4Ezq3LpEvHlQR2y6…` |
| `<TURI-O-Eta-RMSD-ESM>` | `https://w3id.org/np/RAPh6zDXbnsMP304CGWT3OcY8ielo_GVifxC7oDsVB8HM` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAPh6zDXbnsMP304CGWT3OcY8…` |
| `<TURI-O-Eta-RWO>` | `https://w3id.org/np/RAhhXSQQgmCfZau05NMwwYGae21iwK_qjgOs7GzDyHn9w` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAhhXSQQgmCfZau05NMwwYGae…` |
| `<TURI-O-Eta-SASA-AF>` | `https://w3id.org/np/RAjsJgM13kFOaExAskq-K-7KcEf1anAAbrBz_TROBWtP0` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAjsJgM13kFOaExAskq-K-7Kc…` |
| `<TURI-O-Eta-SASA-ESM>` | `https://w3id.org/np/RAeGQbuaKdL82xN1MBbkzLemD7twqcJYfxZdGVUWTX8G0` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAeGQbuaKdL82xN1MBbkzLemD…` |
| `<TURI-O-Eta-WHO>` | `https://w3id.org/np/RAQmYYtUl5ZE31-1yFhP9rda1KSq_TDQipwlfCZPouAHc` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAQmYYtUl5ZE31-1yFhP9rda1…` |
| `<TURI-O-Eta-pLDDT-AF>` | `https://w3id.org/np/RAyaXL_U120427BOikVY6A_eSSxWTtInmUqUHdB4W7EYk` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAyaXL_U120427BOikVY6A_eS…` |
| `<TURI-O-Eta-pLDDT-ESM>` | `https://w3id.org/np/RAOevfPSd_NZh3bek1YA8M9ZWFwGFP_pTJZ4Txjw0UWz4` | 200 | ✅ | `@prefix this: <https://w3id.org/np/RAOevfPSd_NZh3bek1YA8M9ZW…` |

## Anomalies

**None.** All three verification checks pass.

## Outputs

1. **Substituted draft:** `paper/FDT_paper_consolidated_draft_v0_6_pre_consolidation.md`
2. **Unified diff:** `/tmp/paper_unified_diff.patch` (will be moved to a more permanent location at commit time if Erik chooses)
3. **Verification report:** this file (`/tmp/paper_verification_report.md`; also movable at commit time)

## Reproducibility

To reproduce this substitution exactly:
1. Check out branch `cleanup-upstream-v2` at commit `84d21fb0f331503c0a718383890ab4e9b113e2b8`.
2. The substitution script + chain table are at `/tmp/substitute_paper.py` + `/tmp/paper_v2_chain.json`.
3. The placeholder → v1 local name convention is captured in the `PLACEHOLDER_TO_LOCAL` dict at the top of the script.
4. Run `python3 /tmp/substitute_paper.py` to produce the substituted draft + diff.
5. The substitution is idempotent for a given commit: same input file + same registry → same output file (no mint timestamps in the substitution; v2 URIs are stable per supersession_registry.md).

## Subsequent work

This substitution is **PRE-consolidation**. The §5 tables are now populated with v2 referent URIs; §6.4, §6.6, §6.7, and §6.8 revisions drafted in the chat session will be merged in a subsequent step to produce the canonical v0.6.