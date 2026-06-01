# v2 Dry-Run Full Report — Pass 1 + Pass 2 Consolidated

## Summary across both passes

- Pass 1 (upstream-dependent): 8 / 8 dry-run emitted ✅, all verifications pass ✅
- Pass 2 (downstream): 30 / 30 dry-run emitted, 30 / 30 verifications pass ✅
- Total: 38 / 38 dry-run emitted
- Signer: nanopub-java 1.88.0 via bundled JDK 21
- Local-name preservation: ✅ verified verbatim against pass1_local_names.txt + pass2_local_names.txt

## Pass 2 rewrite totals

- dct:isPartOf rewrites:  30 / 30 (✅)
- dct:source rewrites:    21 / 21 (✅)
- Cross-ref rewrites:     57 / 57 (✅)

## Pass-1 referent URI registry

- **Alpha-RBD-Variant**: `https://w3id.org/np/RAngbyT2iZe4xYUcPnTnDFKDaiL5-tSmoUYzF9RK3LHdE/Alpha-RBD-Variant`
- **Epsilon-RBD-Variant**: `https://w3id.org/np/RADWPV5jeyK-7pxen6hMrxjP4hPNLk3EJTibcxJCInv30/Epsilon-RBD-Variant`
- **Eta-RBD-Variant**: `https://w3id.org/np/RA8yS9sU1tq87fXelVb4Q7uwjpoDXOsoelXM5--tfu6IQ/Eta-RBD-Variant`
- **ESM2-Method**: `https://w3id.org/np/RAV_9iAUAyUyNLhVQxpTaE54ko_liTnBpIarZBnkBcbgw/ESM2-Method`
- **AlphaFold2-Method**: `https://w3id.org/np/RAPz4KzBYjUUaURNGn4pR7PpJ5VAvv43v5dYK7gyG1DXk/AlphaFold2-Method`
- **AgMata-Method**: `https://w3id.org/np/RAfY9JAThg7kIl7-63YT2KdVN7y8INAyqpnow339n3tpU/AgMata-Method`
- **BloomLab-DMS-Method**: `https://w3id.org/np/RAWQDkXVW2tB6LEgirShh03PKJOznYQFVLx8-YXhWfnew/BloomLab-DMS-Method`
- **GISAID-Method**: `https://w3id.org/np/RAdSYycNtllf-CCXJ5HMMUaF-arNhDj0oGdiZyCBC08o0/GISAID-Method`

## Upstream /-form referents (PROMPT 2.0)

- Project v2: `https://w3id.org/np/RAXPu-iuezz8swvd6RWIba3VzV0cp94Aq3pTzVst9_nPk/StayAhead-Project`
- ESM Dataset v2: `https://w3id.org/np/RAbvDm28nNtScXcTXEKHbyYdx1yDXQ5zOViy_Dn7LOkkk/STAYAHEAD-Dataset2`
- AlphaFold Dataset v2: `https://w3id.org/np/RAuqwhkDJgVHU8_Fk2gsMw483Iml75Kc09XKR6h0ybO3Q/STAYAHEAD-Dataset1`

## Failures

None.

## Files

```
build/v2-dryrun/
├── pass1/
│   ├── unsigned/   ← 8 /-form drafts
│   └── signed/     ← 8 signed nanopubs (NOT published)
├── pass2/
│   ├── unsigned/   ← 30 /-form drafts
│   └── signed/     ← 30 signed nanopubs (NOT published)
├── pass1_dryrun_report.md
├── pass2_dryrun_report.md
└── dryrun_full_report.md   ← this file

docs/v2-cleanup/
├── pass1_referent_map.json
├── pass2_referent_map.json
├── audit_data.json
└── mutation_table.md
```

## Next step

On Erik's confirmation, PROMPT 3 will publish all 38 signed nanopubs to the live NSN and run SPARQL verification of the full v1→v2 supersession chain.