# mac-fdt-staging

Staging materials for the 38 nanopublication-based FAIR Digital Twins of SARS-CoV-2 Spike RBD variants (Alpha N169Y, Epsilon L120R, Eta E152K), developed at the Metabolomics and Analytics Center (MAC), Leiden Academic Center for Drug Research (LACDR), Leiden University, under the STAYAHEAD programme.

**Status (21 May 2026).** All five vocabulary-affecting open items resolved with Tobias Kuhn. FAIR² citation policy committed (SPS v1.2). GISAID accessions now populated for all three variants (Alpha EPI_ISL_601443, Epsilon EPI_ISL_2295356, Eta EPI_ISL_941290; Epsilon collection date and location aligned to the accession: 2021-01-13, United States). Awaiting Stage 1–3 minting session (`nanopub-skill` cloned to `~/nanopub-work/`).

## Contents

| Folder | Files | Role |
|---|---|---|
| `specs/` | `MAC_FDT_SPS_v1_2.md`, `MAC_FDT_Vocabulary_v1_1.md` | Authoritative specifications: 11 FDO types, 26 predicates, 14 classes, FAIR² citation policy. |
| `data/` | `FDT4Claude_small_v1_2.csv`, `af_wuhan_1step_v1.csv`, `esm_wuhan_1step_v1.csv` | Source data: three-variant working CSV (v1.2, GISAID accessions populated for all three variants) plus full FAIR² ESM/AlphaFold datasets. |
| `minting/` | `README_for_Claude_Code_v1_1.md` | Orientation for the Claude Code nanopub-minting session. Three-stage plan: 40 vocabulary + 11 templates + 38 instances = 89 nanopubs. |
| `extensions/` | `MAC_FDT_Bosch_Extension_v1.0.md` | Post-Stage-3 extension: Bosch lab APC cell-sorting binding assay on five double-mutant variants. |
| `paper/` | `FDT_paper_consolidated_draft_v0_5.md` | Manuscript draft for *Frontiers in Big Data*: "FAIR Digital Twins for SARS-CoV-2 Spike Variants — A nanopublication-based realisation of the Knowlet concept." |

## Companion materials (not in this repo)

- `nanopub-skill` (https://github.com/knowledgepixels/nanopub-skill) — minting tooling.
- `MAC_FAIR_v2.0` — substrate paper (companion to the FDT manuscript in `paper/`).

## Funding

This collaboration project (LSHM22038) is co-funded by the PPP Allowance awarded by Health~Holland, Top Sector Life Sciences and Health (LSH), under the project "Staying Ahead of the Virus: Rapid CoV detection and variant characterization using mass spectrometry (MS) coupled to ML/AI predictions of variants of high risk" (Project STAYAHEAD), to stimulate public-private partnerships.

## License

CC BY 4.0.

## Author

Erik Schultes (ORCID: 0000-0001-8888-635X) — MAC / LACDR / Leiden University, GO FAIR Foundation.
