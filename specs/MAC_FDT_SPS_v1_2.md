<!--
AUTHOR: Erik Schultes
SESSION: Making MAC FAIR/Article - FDT Paper
DATE: 2026-05-21
URL: https://claude.ai/chat/22a7668a-24ce-4533-82fa-7e5a6b6204e9
CREATED_AT: P24/R24
DESCRIPTION: Stakeholder Participation Sheets v1.2 — FAIR² citation policy committed (mandatory data-article DOI on Type 1; mandatory Package DOI + portal URL on Types 3–6). Supersedes v1.1.
-->

# MAC FAIR Digital Twin — Stakeholder Participation Sheets
## Working Document v1.2
### 11 FDO types for Spike protein RBD variant knowlets

**Project:** StayAhead / MAC — Leiden University LACDR
**Date:** 21 May 2026
**Status:** Approved for NanoDash template implementation. FAIR² citation policy committed.
**Companion spec:** `MAC_FDT_Vocabulary_v1_2.md` (authoritative for predicate and class definitions; updated 22 May 2026 to add class hierarchy, predicate domain/range, and `dct:partOf` per Tobias Kuhn's PR #1 review).
**Supersedes:** `MAC_FDT_SPS_v1.1.md` (21 May 2026).

---

## Changes since v1.1

This revision commits the FAIR² citation policy that v1.1 left optional. The data article DOI (`10.3389/fbinf.2025.1634111`) is now **mandatory** on every Type 1 anchor via `dct:references`. The FAIR² Data Package DOI (`10.71728/hw56-vj34`) is now **mandatory** as a `dct:source` value on every Type 3–6 observation, alongside the per-resource FAIR² portal URL (`https://sen.science/doi/10.71728/hw56-vj34/resources/…`). A new §"FAIR² citation policy" records the rationale. No vocabulary changes; predicate and class inventories are unchanged from v1.1.

---

## Conventions and architecture

**Namespace prefix:** `mac:` expands within the MAC NanoDash ontology space at

```
https://w3id.org/spaces/mac/r/ontology/MAC-Ontology
```

(viewable via NanoDash at `https://nanodash.petapico.org/resource?5&id=https://w3id.org/spaces/mac/r/ontology/MAC-Ontology`). The exact term-URI separator is assigned by NanoDash at minting time; in this document the shorthand `mac:TermName` refers unambiguously to the term published in the MAC ontology space with the corresponding label.

**Three-layer architecture:**
- **Layer 1 — Identity:** Type 1 (FDT) is the central knowlet node; all observations link to it.
- **Layer 2 — Observations:** Types 2–8 are observation FDOs, each declaring one measured or recorded property of the variant. All link to the Type 1 anchor via `mac:isObservationOf`, whose object is the **referent URI** (the `sub:fdo` declared by the anchor), not the Trusty URI of the anchor nanopublication.
- **Layer 3 — Methods:** Types 9–11 are method FDOs, referenced by the observation types. They carry one or more `cito:citesAsAuthority` URIs (typically DOIs) identifying the published descriptions of the method, and a `schema:url` for the data/software/platform resource. No new template predicates are needed for new method types — only new class URIs and new instances.

**Method reference predicates (observation → method):**
- Types 3–6 (computational predictions): `mac:hasPredictionMethod` → Type 9 FDO
- Type 7 (experimental DMS): `mac:hasExperimentalMethod` → Type 10 FDO
- Type 2 (real-world occurrence): `mac:hasSurveillanceMethod` → Type 11 FDO

**Source data:** `dct:source` (repeatable, standard Dublin Core) is used for all source dataset references. Where a StayAhead dataset FDO Trusty URI exists, it is preferred over a raw file URL. Include up to three values for computational observations: FAIR² Data Package DOI, FAIR² resource URL, and MAC OSF URL.

**FAIR² references in Type 1:** `dct:references` → FAIR² data article DOI (`10.3389/fbinf.2025.1634111`) **mandatory**; `dct:source` → FAIR² Data Package DOI (`10.71728/hw56-vj34`) **mandatory**. See §"FAIR² citation policy" below.

**All fields mandatory unless marked [opt]. Standard vocabulary predicates require no minting.**

**Namespace declarations used in this document:**

```
@prefix mac:    <https://w3id.org/spaces/mac/r/ontology/MAC-Ontology[/|#]> .   # NanoDash-assigned separator
@prefix cito:   <http://purl.org/spar/cito/> .                                  # SPAR Citation Typing Ontology
@prefix dct:    <http://purl.org/dc/terms/> .
@prefix schema: <http://schema.org/> .
@prefix fdof:   <https://w3id.org/fdof/ontology#> .
@prefix nt:     <http://www.nanopub.org/nschema#> .
@prefix fair:   <https://w3id.org/fair/principles/terms/> .
@prefix dcat:   <http://www.w3.org/ns/dcat#> .
@prefix rdf:    <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:   <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl:    <http://www.w3.org/2002/07/owl#> .
```

---

## FAIR² citation policy

This catalogue commits to two mandatory cross-references on every FDO that derives from the FAIR² ESM/AlphaFold dataset:

1. **Data article DOI** — `https://doi.org/10.3389/fbinf.2025.1634111` — the *narrative description* of the dataset (peer-reviewed Frontiers in Bioinformatics article). Carried by every Type 1 anchor via `dct:references`. Captures the human-readable scientific context, methods summary, and authorship.

2. **FAIR² Data Package DOI** — `https://doi.org/10.71728/hw56-vj34` — the *resolvable access point* to the Data Package on the FAIR² portal (`https://sen.science/doi/10.71728/hw56-vj34`). Carried by every Type 1 anchor via `dct:source` (as the top-level reference) and by every Type 3–6 observation via `dct:source` (alongside the resource-specific FAIR² URL).

The two roles are distinct and complementary: `dct:references` points to the *paper about* the data, `dct:source` points to *the data itself*. Both are mandatory because every nanopublication in this catalogue inherits its scientific provenance from the FAIR² dataset, and the FAIR² infrastructure is the canonical access point for the underlying values. Making both mandatory eliminates a class of unattributed-reuse failure modes and ensures that a downstream consumer of any single observation FDO can recover both the dataset and its narrative description in two cross-link traversals.

This policy applies to the present three-variant catalogue and to all subsequent extensions that draw on the same FAIR² source (notably the 3705-mutation scale-up). Catalogues drawing on different source data substitute the corresponding article DOI and Package DOI but retain the two-mandatory-references structure.

---

Derived from wild-type Spike RBD of SARS-CoV-2 Wuhan isolate (UniProt P0DTC2) by single-residue substitution. All lengths confirmed at 195 residues.

| Variant | MAC seq_id | Mut. | Sequence |
|---|---|---|---|
| Wild-type | — | — | `TNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGP` |
| Alpha | N169Y | 169 N→Y | `TNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTYGVGYQPYRVVVLSFELLHAPATVCGP` |
| Epsilon | L120R | 120 L→R | `TNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYRYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGP` |
| Eta | E152K | 152 E→K | `TNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVKGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGP` |

Wild-type is accessible via `https://www.uniprot.org/uniprot/P0DTC2` and referenced in all Type 1 FDTs via `mac:hasParentProtein` (hardcoded).

---

## Type 1 — Spike RBD Variant (FAIR Digital Twin anchor)

**Template label:** Declaring a Spike RBD Variant
**Default class URI:** `mac:SpikeRBDVariant`
**Class description:** A variant of the SARS-CoV-2 Spike receptor-binding domain (RBD, 195 residues) produced by one or more amino acid substitutions from the wild-type Wuhan isolate (UniProt P0DTC2). This FDO is the central node (the *anchor*) of a FAIR Digital Twin knowlet; all observation FDOs linking to it via `mac:isObservationOf` collectively constitute the knowlet.

| Stmt | Predicate URI | rdfs:label | Object range | Notes |
|---|---|---|---|---|
| st0 | `rdf:type` | is a | `fdof:FAIRDigitalObject` | fixed |
| st3 | `rdf:type` | is a | `mac:SpikeRBDVariant` | fixed |
| st4 | `fdof:hasMetadata` | has its metadata in | `nt:NANOPUB` | fixed |
| st1 | `rdfs:label` | has the label | literal | e.g. "Alpha RBD variant (N169Y)" |
| st2 | `rdfs:comment` | has description | literal | [opt] |
| st6 | `dct:creator` | has creator | ORCID | repeatable |
| st8 | `dcat:contactPoint` | has contact point | literal (email) | |
| st92 | `dct:publisher` | has publisher | ROR URI | |
| st91 | `dct:subject` | has domain | controlled list | |
| st95 | `fair:implements` | implements | FIP nanopub URI | [opt] |
| st5 | materialization group | — | — | [opt] repeatable |
| **FDT-specific statements** | | | | |
| st_w | `mac:hasWHOVariantName` | has WHO variant name | literal | e.g. "Alpha" |
| st_p | `mac:hasPangoLineage` | has Pango lineage | literal | e.g. "B.1.1.7" |
| st_g | `mac:hasGISAIDSeqId` | has GISAID seq_id (full spike, amino acid change notation) | literal | e.g. "N501Y" |
| st_m | `mac:hasMACSeqId` | has MAC seq_id (RBD, amino acid change notation) | literal | e.g. "N169Y" |
| st_u | `mac:hasParentProtein` | has parent protein | URI — hardcoded: `https://www.uniprot.org/uniprot/P0DTC2` | fixed |
| st_s | `mac:hasRBDSequence` | has RBD amino acid sequence (one-letter code, 195 residues) | literal | variant-specific; see sequence appendix |
| st_a | `mac:hasGISAIDAccession` | has GISAID accession number | literal (`EPI_ISL_XXXXXXX`) | [opt] canonical exemplar at this Type |
| **FAIR² cross-references** | | | | |
| st_f2a | `dct:references` | references (FAIR² data article) | URI: `https://doi.org/10.3389/fbinf.2025.1634111` | **mandatory** (FAIR² citation policy) |
| st_f2p | `dct:source` | has source (FAIR² Data Package) | URI: `https://doi.org/10.71728/hw56-vj34` | **mandatory** (FAIR² citation policy) |

**Instance values:**

| Variant | WHO name | Pango | GISAID seq_id | MAC seq_id | RBD sequence |
|---|---|---|---|---|---|
| Alpha | Alpha | B.1.1.7 | N501Y | N169Y | *see appendix* |
| Epsilon | Epsilon | B.1.427 + B.1.429 | L124R | L120R | *see appendix* |
| Eta | Eta | B.1.525 | E484K | E152K | *see appendix* |

---

## Type 2 — Observation: Real-World Occurrence

**Template label:** Declaring a Real-World Occurrence of a Spike Variant
**Default class URI:** `mac:RealWorldOccurrence`
**Class description:** A documented detection of a SARS-CoV-2 Spike variant in the real world, as reported in GISAID. The occurrence date records the GISAID-reported collection date of the sample; the collection location is identified by a URI from the GeoNames gazetteer.

| Stmt | Predicate URI | rdfs:label | Object range | Notes |
|---|---|---|---|---|
| *(core 18 statements — same structure as Type 1)* | | | | |
| st1 | `rdfs:label` | has the label | literal | e.g. "Alpha real-world occurrence — England" |
| st_obs | `mac:isObservationOf` | is observation of | URI — **referent URI** (`sub:fdo` of Type 1 anchor) | guided choice from MAC FDT catalogue |
| st_sm | `mac:hasSurveillanceMethod` | has surveillance method | URI (Type 11 Method FDO) | [opt] guided choice from method catalogue |
| st_d | `mac:hasOccurrenceDate` | has occurrence date (GISAID reported collection date) | literal | e.g. "late 2020–2021" |
| st_l | `mac:hasCollectionLocation` | has collection location | URI — GeoNames feature (`https://sws.geonames.org/{id}/`) | resolved per Item 3 |
| st_gi | `mac:hasGISAIDAccession` | has GISAID accession number | literal (`EPI_ISL_XXXXXXX`) | [opt] specific surveilled accession at this Type |

**Instance values:**

| Variant | Date | Location (GeoNames URI) | GeoNames feature |
|---|---|---|---|
| Alpha | "late 2020–2021" | `https://sws.geonames.org/6269131/` | England |
| Epsilon | "March 2020" | `https://sws.geonames.org/5332921/` | California, US |
| Eta | "Dec 15, 2020" | `https://sws.geonames.org/2328926/` | Nigeria |

> GeoNames IDs above are working candidates from the GeoNames gazetteer. Verify at minting time by dereferencing each URI; substitute the precise feature ID returned by `https://www.geonames.org` search if any candidate resolves to a different feature than intended.

---

## Types 3–6 — Observation: Computational Prediction (RMSD, SASA, pLDDT, AgMata)

**Shared structure for Types 3–5.** One FDO per variant per method (ESM or AlphaFold II).

| Stmt | Predicate URI | rdfs:label | Object range | Notes |
|---|---|---|---|---|
| *(core 18 statements)* | | | | |
| st1 | `rdfs:label` | has the label | literal | e.g. "Alpha RMSD — AlphaFold II" |
| st_obs | `mac:isObservationOf` | is observation of | URI — **referent URI** (`sub:fdo` of Type 1 anchor) | |
| st_pm | `mac:hasPredictionMethod` | has prediction method | URI (Type 9 Computational Method FDO) | |
| st_val | *(type-specific predicate)* | *(see below)* | decimal literal | |
| st_src | `dct:source` | has source dataset | URI | **mandatory, repeatable**: must include FAIR² Package DOI **and** the per-resource FAIR² portal URL (per FAIR² citation policy); MAC OSF URL [opt] additional |

**Type-specific metric predicates:**

| Type | Class URI | Metric predicate | rdfs:label | Units |
|---|---|---|---|---|
| 3 | `mac:ComputationalPredictionRMSD` | `mac:hasRMSD` | has RMSD (Root Mean Square Deviation) | Angstroms (Å) |
| 4 | `mac:ComputationalPredictionSASA` | `mac:hasSASA` | has SASA (Solvent Accessible Surface Area) | square Angstroms (Å²) |
| 5 | `mac:ComputationalPredictionPLDDT` | `mac:haspLDDT` | has pLDDT score (unitless, 0–100) | unitless |

**Type 6 — AgMata.** One FDO per variant only (score is sequence-derived, method-independent). Method reference: Bio2Byte Type 9 instance.

| Type | Class URI | Metric predicate | rdfs:label | Units |
|---|---|---|---|---|
| 6 | `mac:ComputationalPredictionAgMata` | `mac:hasAgMataScore` | has AgMata score (aggregation propensity) | unitless |

**All instance values:**

| Variant | Method | RMSD | SASA | pLDDT | AgMata |
|---|---|---|---|---|---|
| Alpha | ESM | 13.378861773140596 | 16494.878394358453 | 23.673561732385306 | 0.7004717948717948 |
| Alpha | AlphaFold II | 2.277628683231952 | 10141.236988525969 | 93.74392833444035 | — |
| Epsilon | ESM | 12.801648143493145 | 17620.862527029858 | 23.73609314359643 | 0.7194974358974362 |
| Epsilon | AlphaFold II | 2.975776098053212 | 10181.968717666516 | 94.19297808764844 | — |
| Eta | ESM | 2.476768477258109 | 18026.596842240684 | 23.15035644847704 | 0.680579487179487 |
| Eta | AlphaFold II | 2.7195180252543003 | 10226.641288430395 | 94.05421698739244 | — |

*(AgMata is per-variant, not per-method. ESM row carries the value; AlphaFold row omitted.)*

**Source URLs for `dct:source` (Types 3–6):**

| dct:source value | Description | Status |
|---|---|---|
| `https://doi.org/10.71728/hw56-vj34` | FAIR² Data Package DOI — stable top-level reference | **mandatory** (all Types 3–6) |
| `https://sen.science/doi/10.71728/hw56-vj34/resources/esm_wuhan_1step_v1` | FAIR² ESM dataset resource | **mandatory** for ESM-method instances |
| `https://sen.science/doi/10.71728/hw56-vj34/resources/af_wuhan_1step_v1` | FAIR² AlphaFold dataset resource | **mandatory** for AlphaFold-method instances |
| `https://osf.io/r625a/files/emk49` | MAC OSF — ESM dataset | [opt] additional, ESM instances |
| `https://osf.io/r625a/files/9tj6b` | MAC OSF — AlphaFold dataset | [opt] additional, AlphaFold instances |

For Type 6 (AgMata): both mandatory values are the Package DOI and the ESM resource URL, since AgMata is carried on the ESM-row of the source CSV. The Bio2Byte AgMata predictor is referenced separately via `mac:hasPredictionMethod` → Type 9 FDO.

---

## Type 7 — Observation: Experimental Measurement — Deep Mutational Scanning

**Template label:** Declaring a Deep Mutational Scanning Observation for a Spike Variant
**Default class URI:** `mac:ExperimentalDMSObservation`
**Class description:** Experimental binding affinity and expression level measurements for a Spike RBD variant determined by deep mutational scanning (Bloom Lab). One FDO per variant.

| Stmt | Predicate URI | rdfs:label | Object range | Notes |
|---|---|---|---|---|
| *(core 18 statements)* | | | | |
| st1 | `rdfs:label` | has the label | literal | e.g. "Alpha DMS measurement — Bloom Lab" |
| st_obs | `mac:isObservationOf` | is observation of | URI — **referent URI** (`sub:fdo` of Type 1 anchor) | |
| st_em | `mac:hasExperimentalMethod` | has experimental method | URI (Type 10 Experimental Method FDO) | |
| st_bi | `mac:hasBind` | has bind (binding affinity, log KD, unitless) | decimal literal | |
| st_db | `mac:hasDeltaBind` | has delta_bind (change in binding affinity vs. WT, unitless) | decimal literal | |
| st_ex | `mac:hasExpr` | has expr (expression level, log MFI, unitless) | decimal literal | |
| st_de | `mac:hasDeltaExpr` | has delta_expr (change in expression level vs. WT, unitless) | decimal literal | |
| st_cb | `mac:hasConfidenceBind` | has confidence_bind (binding confidence score, unitless) | decimal literal | |
| st_ce | `mac:hasConfidenceExpr` | has confidence_expr (expression confidence score, unitless) | decimal literal | |
| st_src | `dct:source` | has source dataset | URI | [opt] repeatable |

**Instance values:**

| Variant | bind | delta_bind | expr | delta_expr | conf_bind | conf_expr |
|---|---|---|---|---|---|---|
| Alpha | 9.81374 | 1.04213 | 10.05266 | -0.13322 | 0.0732354593527125 | 0.0713853600674372 |
| Epsilon | 8.93862 | 0.16701 | 10.25356 | 0.06768 | 0.0729917177063099 | 0.0705230077448188 |
| Eta | 9.01256 | 0.24095 | 10.21898 | 0.03311 | 0.0722604927671021 | 0.0697838486111459 |

---

## Type 8 — WHO SARS-CoV-2 Variant Classification

**Template label:** Declaring a WHO SARS-CoV-2 Variant Classification
**Default class URI:** `mac:WHOVariantClassification`
**Class description:** A classification of a SARS-CoV-2 lineage according to the WHO risk framework — Variant of Concern (VOC), Variant of Interest (VOI), or Variant Under Monitoring (VUM) — based on assessed public-health risk and virological characteristics. Time-stamped because designation status changes over time.

| Stmt | Predicate URI | rdfs:label | Object range | Notes |
|---|---|---|---|---|
| *(core 18 statements)* | | | | |
| st1 | `rdfs:label` | has the label | literal | e.g. "Alpha WHO classification: VOC" |
| st2 | `rdfs:comment` | has description | literal | [opt] |
| st_obs | `mac:isObservationOf` | is observation of | URI — **referent URI** (`sub:fdo` of Type 1 anchor) | |
| st_wc | `mac:hasWHOClassification` | has WHO variant classification | controlled: `mac:VOC` / `mac:VOI` / `mac:VUM` | |
| st_cd | `mac:hasClassificationDate` | has WHO classification date | literal (date) | [opt] |
| st_cr | `mac:hasWHOClassificationReference` | has WHO classification reference URL | URI | [opt] |

**Controlled class instances to mint:**

| Class | rdfs:label | Definition |
|---|---|---|
| `mac:VOC` | Variant of Concern | Increased transmissibility, disease severity, or vaccine/therapeutic evasion |
| `mac:VOI` | Variant of Interest | Genetic markers with phenotypic changes and epidemiological impact warranting enhanced monitoring |
| `mac:VUM` | Variant Under Monitoring | Evidence of growth advantage or immune escape; monitored precautionarily |

**Instance values:** Alpha → `mac:VOC` (2020-12-18); Epsilon → `mac:VOI` (2021-03-05); Eta → `mac:VOI` (2021-03-05)

---

## Type 9 — Computational Method

**Template label:** Declaring a Computational Method
**Default class URI:** `mac:ComputationalMethod`
**Class description:** A computational method, tool, or algorithm producing predictions or scores from biological sequence or structure data. Types 3–6 reference this via `mac:hasPredictionMethod`.

| Stmt | Predicate URI | rdfs:label | Object range | Notes |
|---|---|---|---|---|
| *(core 18 statements)* | | | | |
| st1 | `rdfs:label` | has the label | literal | method name |
| st2 | `rdfs:comment` | has description | literal | [opt] |
| st_ci | `cito:citesAsAuthority` | cites as authority | URI | repeatable; per Item 4 (replaces `schema:citation`) |
| st_su | `schema:url` | has software URL | URI | [opt] |

**Instances to mint (shared library):**

| Label | `cito:citesAsAuthority` | `schema:url` |
|---|---|---|
| "ESM2 — Meta AI protein language model" | `https://doi.org/10.1126/science.ade2574` | `https://github.com/facebookresearch/esm` |
| "AlphaFold 2 — DeepMind structure predictor" | `https://doi.org/10.1038/s41586-021-03819-2` | `https://github.com/google-deepmind/alphafold` |
| "Bio2Byte toolkit — AgMata aggregation predictor" | `https://doi.org/10.1093/bioinformatics/btac149` | `https://bio2byte.be/b2btools/` |

---

## Type 10 — Experimental Method

**Template label:** Declaring an Experimental Method
**Default class URI:** `mac:ExperimentalMethod`
**Class description:** An experimental assay or measurement protocol producing empirical observations about biological entities. Type 7 references this via `mac:hasExperimentalMethod`. Structurally identical to Type 9; distinguished by class URI.

| Stmt | Predicate URI | rdfs:label | Object range | Notes |
|---|---|---|---|---|
| *(core 18 statements)* | | | | |
| st1 | `rdfs:label` | has the label | literal | assay name |
| st2 | `rdfs:comment` | has description | literal | [opt] |
| st_ci | `cito:citesAsAuthority` | cites as authority | URI | repeatable; per Item 4 (replaces `schema:citation`) |
| st_su | `schema:url` | has data resource URL | URI | [opt] |

**Instance to mint:**

| Label | `cito:citesAsAuthority` | `schema:url` |
|---|---|---|
| "Deep mutational scanning — Bloom Lab SARS-CoV-2 RBD" | `https://doi.org/10.1016/j.cell.2020.08.012` | `https://github.com/jbloomlab/SARS-CoV-2-RBD_DMS` |

---

## Type 11 — Observational Method (Surveillance)

**Template label:** Declaring a Surveillance or Observational Method
**Default class URI:** `mac:ObservationalMethod`
**Class description:** An epidemiological surveillance system or data collection platform through which real-world occurrences of biological entities are documented. Type 2 references this via `mac:hasSurveillanceMethod`. Structurally identical to Types 9 and 10; distinguished by class URI. No new predicates are required: any new surveillance method requires only a new class URI and a new instance.

| Stmt | Predicate URI | rdfs:label | Object range | Notes |
|---|---|---|---|---|
| *(core 18 statements)* | | | | |
| st1 | `rdfs:label` | has the label | literal | system name |
| st2 | `rdfs:comment` | has description | literal | [opt] |
| st_ci | `cito:citesAsAuthority` | cites as authority | URI | repeatable; per Item 4 (replaces `schema:citation`) |
| st_su | `schema:url` | has platform URL | URI | [opt] |

**Instance to mint:**

| Label | `cito:citesAsAuthority` | `schema:url` |
|---|---|---|
| "GISAID — Global Initiative on Sharing All Influenza Data (SARS-CoV-2 surveillance)" | `https://doi.org/10.2807/1560-7917.ES.2017.22.13.30494` (Shu & McCauley 2017) + `https://doi.org/10.46234/ccdcw2021.255` (Khare et al. 2021) | `https://www.gisaid.org/` |

---

## Summary: predicate and class inventory

### MAC-namespace predicates (26 total)

| Predicate | rdfs:label | Type(s) | Object range |
|---|---|---|---|
| `mac:hasWHOVariantName` | has WHO variant name | 1 | literal |
| `mac:hasPangoLineage` | has Pango lineage | 1 | literal |
| `mac:hasGISAIDSeqId` | has GISAID seq_id (full spike mutation notation) | 1 | literal |
| `mac:hasMACSeqId` | has MAC seq_id (RBD mutation notation) | 1 | literal |
| `mac:hasParentProtein` | has parent protein | 1 | URI (hardcoded P0DTC2) |
| `mac:hasRBDSequence` | has RBD amino acid sequence (195 residues, one-letter code) | 1 | literal |
| `mac:hasGISAIDAccession` | has GISAID accession number | 1, 2 | literal (single-predicate dual use, Item 5) |
| `mac:isObservationOf` | is observation of | 2,3,4,5,6,7,8 | URI — referent URI (Item 2) |
| `mac:hasSurveillanceMethod` | has surveillance method | 2 | URI (Type 11 FDO) |
| `mac:hasOccurrenceDate` | has occurrence date | 2 | literal |
| `mac:hasCollectionLocation` | has collection location | 2 | URI — GeoNames (Item 3) |
| `mac:hasPredictionMethod` | has prediction method | 3,4,5,6 | URI (Type 9 FDO) |
| `mac:hasRMSD` | has RMSD (Å) | 3 | decimal literal |
| `mac:hasSASA` | has SASA (Å²) | 4 | decimal literal |
| `mac:haspLDDT` | has pLDDT score (0–100, unitless) | 5 | decimal literal |
| `mac:hasAgMataScore` | has AgMata score (unitless) | 6 | decimal literal |
| `mac:hasExperimentalMethod` | has experimental method | 7 | URI (Type 10 FDO) |
| `mac:hasBind` | has bind (log KD, unitless) | 7 | decimal literal |
| `mac:hasDeltaBind` | has delta_bind (unitless) | 7 | decimal literal |
| `mac:hasExpr` | has expr (log MFI, unitless) | 7 | decimal literal |
| `mac:hasDeltaExpr` | has delta_expr (unitless) | 7 | decimal literal |
| `mac:hasConfidenceBind` | has confidence_bind (unitless) | 7 | decimal literal |
| `mac:hasConfidenceExpr` | has confidence_expr (unitless) | 7 | decimal literal |
| `mac:hasWHOClassification` | has WHO variant classification | 8 | URI (mac:VOC/VOI/VUM) |
| `mac:hasClassificationDate` | has WHO classification date | 8 | literal |
| `mac:hasWHOClassificationReference` | has WHO classification reference URL | 8 | URI |

### Standard vocabulary adopted (no minting required)

| Predicate | Type(s) | Purpose |
|---|---|---|
| `dct:source` | 1,3,4,5,6,7 | Source dataset reference — repeatable |
| `dct:references` | 1 | FAIR² data article citation |
| **`cito:citesAsAuthority`** | 9,10,11 | Method's authoritative published description — repeatable (Item 4; replaces `schema:citation`) |
| `schema:url` | 9,10,11 | Software, data resource, or platform URL |

### MAC-namespace classes to mint (19 total: 14 concrete + 5 abstract)

**Abstract parent classes (5, added in Vocabulary v1.2 per PR #1 item 2):** `mac:Observation`, `mac:ComputationalPrediction`, `mac:ExperimentalObservation`, `mac:Method`, `mac:WHODesignation`. These carry no direct instances and exist to type predicate domains/ranges and to accommodate future siblings (e.g., the Bosch extension's `mac:ExperimentalCellSortingObservation`).

**FDT and observation classes (8, concrete):** `mac:SpikeRBDVariant`, `mac:RealWorldOccurrence`, `mac:ComputationalPredictionRMSD`, `mac:ComputationalPredictionSASA`, `mac:ComputationalPredictionPLDDT`, `mac:ComputationalPredictionAgMata`, `mac:ExperimentalDMSObservation`, `mac:WHOVariantClassification`

**Method classes (3, concrete):** `mac:ComputationalMethod`, `mac:ExperimentalMethod`, `mac:ObservationalMethod`

**WHO classification controlled values (3, concrete):** `mac:VOC`, `mac:VOI`, `mac:VUM`

The Stage 3 instance count (38 nanopubs) is unchanged: instances type themselves with the concrete classes only. The class hierarchy and per-predicate `rdfs:domain` / `rdfs:range` declarations are encoded in the Stage 1 vocabulary nanopubs and are documented in `MAC_FDT_Vocabulary_v1_2.md` §"Class hierarchy" and §"Predicate domain and range".

> *Note (Item 6 resolution).* SPS v1.0 header text gave a class count of "16"; enumeration in v1.1 consistently yielded 14 (8 + 3 + 3) concrete classes. The "16" value was a counting error and was corrected in v1.1. The class total rises to 19 in v1.2 with the addition of 5 abstract parents.

### Nanopub count — 3-variant initial dataset

| Type | Per variant | Total (3 var.) | Notes |
|---|---|---|---|
| 1 — Spike RBD Variant | 1 | 3 | |
| 2 — Real-World Occurrence | 1 | 3 | |
| 3 — RMSD | 2 | 6 | ESM + AlphaFold |
| 4 — SASA | 2 | 6 | ESM + AlphaFold |
| 5 — pLDDT | 2 | 6 | ESM + AlphaFold |
| 6 — AgMata | 1 | 3 | Bio2Byte |
| 7 — DMS Experimental | 1 | 3 | Bloom Lab |
| 8 — WHO Classification | 1 | 3 | |
| 9 — Computational Method | — | 3 | Shared library |
| 10 — Experimental Method | — | 1 | Shared library |
| 11 — Observational Method | — | 1 | Shared library |
| **Total** | **11** | **33 + 5 = 38** | |

---

## Open items before minting (post-v1.1)

| Item | Status | Notes |
|---|---|---|
| MAC NanoDash ontology space URI | **Resolved** (Item 1) | `https://w3id.org/spaces/mac/r/ontology/MAC-Ontology` |
| `mac:isObservationOf` resolution target | **Resolved** (Item 2) | Referent URI (`sub:fdo` of anchor) |
| `mac:hasCollectionLocation` encoding | **Resolved** (Item 3) | GeoNames URIs |
| Method citation predicate | **Resolved** (Item 4) | `cito:citesAsAuthority` |
| `mac:hasGISAIDAccession` dual use | **Resolved** (Item 5) | Kept single predicate, literal range |
| GISAID accession numbers | Open | Supply EPI_ISL_XXXXXXX values for Alpha, Epsilon, Eta at minting time |
| FAIR² source dataset links | Open | Verify FAIR² resource URLs resolve correctly at minting time |
| StayAhead dataset FDO Trusty URIs | Open | Substitute for raw OSF URLs in `dct:source` of Types 3–6 once available |
| GeoNames feature IDs | Verify | Confirm working candidates resolve to intended features at minting time |

---

## Version history

| Version | Date | Notes |
|---|---|---|
| v1.0 | 20 May 2026 | Initial working document. Seven vocabulary-related open items. |
| v1.1 | 21 May 2026 | Items 1–5 resolved with Tobias Kuhn; Item 6 corrected (class count = 14). |
| v1.2 | 21–22 May 2026 | FAIR² citation policy committed: data article DOI mandatory on Type 1 via `dct:references`; FAIR² Package DOI + resource URL mandatory on Types 3–6 via `dct:source`. Companion vocabulary spec updated 22 May 2026 to `MAC_FDT_Vocabulary_v1_2.md`: class hierarchy (5 new abstract parents → 19 classes), predicate domain/range, and `dct:partOf` per Tobias Kuhn's PR #1 review. This document. |
