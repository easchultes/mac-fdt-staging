<!--
AUTHOR: Erik Schultes
SESSION: Making MAC FAIR/Article - FDT Paper
DATE: 2026-05-22
URL: https://claude.ai/chat/22a7668a-24ce-4533-82fa-7e5a6b6204e9
CREATED_AT: P25/R25
DESCRIPTION: Vocabulary specification v1.2 — class hierarchy added (5 new abstract classes; total 19), predicate domain/range declared, `dct:partOf` replaces `rdfs:isDefinedBy`. Reflects Tobias Kuhn's PR #1 review (22 May 2026), accepted via `Stage1_hierarchy_and_domain_range_proposal.md`. Supersedes v1.1.
-->

# MAC FAIR Digital Twin — Vocabulary Specification

## Working Document v1.2 — class hierarchy, domain/range, and `dct:partOf`

**Project:** StayAhead / MAC — Leiden University LACDR
**Date:** 22 May 2026
**Status:** Ready for nanopub minting. All vocabulary-affecting open items resolved with Tobias Kuhn; Stage 1 PR review items 1–4 applied.
**Companion spec:** `MAC_FDT_SPS_v1_2.md` (the 11-type FDT specification; updated in parallel to reference this vocabulary version).
**Supersedes:** `MAC_FDT_Vocabulary_v1_1.md` (21 May 2026).

---

## Changes since v1.1

This revision applies the four items from Tobias Kuhn's review of Stage 1 PR #1 (22 May 2026), as enumerated and justified in `../Stage1_hierarchy_and_domain_range_proposal.md`:

1. **`dct:partOf` replaces `rdfs:isDefinedBy`** as the predicate linking each vocabulary term to the MAC ontology anchor. The semantic intent (membership in the ontology) is more precisely conveyed by `dct:partOf`; `rdfs:isDefinedBy` is more often used for "the document that defines this term," which here would point to this specification file rather than to the ontology resource itself.
2. **Class hierarchy introduced.** Five new abstract classes (`mac:Observation`, `mac:ComputationalPrediction`, `mac:ExperimentalObservation`, `mac:Method`, `mac:WHODesignation`) bring the 14 concrete classes of v1.1 into a 3-level taxonomy. The class total rises to 19 (14 concrete + 5 abstract). `rdfs:subClassOf` triples are added per the hierarchy in §"Class hierarchy".
3. **Predicate `rdfs:domain` and `rdfs:range` declared.** Each of the 26 MAC-namespace predicates carries domain and range as specified in §"Predicate domain and range". Predicates whose range is an `xsd:*` datatype are declared `owl:DatatypeProperty`; predicates whose range is a class (or whose range is omitted) remain `owl:ObjectProperty`. Five edge cases per the proposal's §3 are resolved per the recommended option 1 (omit the constraint): `mac:hasGISAIDAccession` omits domain (dual-use); `mac:hasParentProtein`, `mac:hasCollectionLocation`, and `mac:hasWHOClassificationReference` omit range (foreign or generic URIs); `mac:hasOccurrenceDate` uses `xsd:string` to admit imprecision.
4. **Slash separator confirmed** for the `mac:` namespace expansion. Per Item 1's resolution, the term URI separator is assigned by NanoDash; the slash form `https://w3id.org/spaces/mac/r/ontology/MAC-Ontology/{local}` has been adopted in the draft TriGs and is retained in v1.2.

Predicate count is unchanged at 26. Class count rises from 14 to 19 (14 concrete + 5 abstract).

---

## Changes since v1.0 (carried forward from v1.1)

v1.1 applied the resolutions reached with Tobias Kuhn on 21 May 2026 for the five open items affecting vocabulary minting. The resolutions are recorded in §"Resolutions" below; the affected predicate and class definitions are updated accordingly throughout Parts A and B. Item 6 (class-count reconciliation) is resolved by inspection: in v1.1 the class inventory totalled 14, including the three WHO controlled values; the SPS v1.0 header value of "16" was a counting error and is corrected in SPS v1.1. In v1.2 the class inventory rises to 19 with the addition of 5 abstract classes (see §"Class hierarchy"). Item 7 (minting order) is procedural and is captured in `../minting/README_for_Claude_Code_v1_1.md`.

---

## Purpose and scope

This document supplies `rdfs:comment` definitions (and, where appropriate, accompanying notes) for every MAC-namespace predicate and class enumerated in `MAC_FDT_SPS_v1_2.md`. The definitions, the class hierarchy, and the predicate domain/range declarations are the **source of truth** from which the nanopublished vocabulary terms are generated in the Claude Code minting session.

Each predicate or class will be published as a nanopublication in the MAC NanoDash ontology space, following the FAIR Funder Framework (FFF) precedent established in `MAC_FAIR_v2.0`: the vocabulary itself is composed of np-FDOs, making it machine-actionable, persistently identified, and openly available under the same substrate as the FDOs that use it.

This is the *human-readable* specification. The nanopublished form encodes each term as an FDO with at minimum:

* `rdf:type` →
    * `owl:ObjectProperty` for predicates whose range is a class (or omitted); or
    * `owl:DatatypeProperty` for predicates whose range is an `xsd:*` datatype; or
    * `owl:Class` for classes.
* `rdfs:label` → human-readable label (from SPS)
* `rdfs:comment` → the definition below
* `rdfs:domain`, `rdfs:range` → domain and range as declared in §"Predicate domain and range" (predicates only; omitted where the proposal's §3 edge cases apply)
* `rdfs:subClassOf` → immediate parent class per §"Class hierarchy" (classes only; omitted for hierarchy roots `mac:SpikeRBDVariant`, `mac:Observation`, `mac:Method`, `mac:WHODesignation`)
* `dct:partOf` → MAC FDT ontology anchor URI (replaces `rdfs:isDefinedBy` in v1.1)
* `dct:creator`, `dct:created`, `dct:license` → standard provenance

---

## Resolutions of v1.0 open items (with Tobias Kuhn, 21 May 2026)

### Item 1 — MAC namespace URI: resolved

The MAC ontology resides in the NanoDash ontology space at the IRI

```
https://w3id.org/spaces/mac/r/ontology/MAC-Ontology
```

(viewable via NanoDash at `https://nanodash.petapico.org/resource?5&id=https://w3id.org/spaces/mac/r/ontology/MAC-Ontology`).

The `mac:` prefix used throughout this document and in SPS v1.2 expands to the term-URI pattern within this space. The exact slash-or-hash separator and the per-term URI suffix are assigned by NanoDash at the time of minting; the shorthand `mac:TermName` in this document refers unambiguously to the term published in the MAC ontology space with `rdfs:label = "TermName"` (or, in lower-camel cased label form, the corresponding predicate label).

### Item 2 — `mac:isObservationOf` resolution target: resolved

The URI object of `mac:isObservationOf` resolves to the **referent URI** (`sub:fdo` of the anchor nanopublication), not to the Trusty URI of the anchor nanopublication itself. This is the canonical FDO-as-subject semantics: an observation is asserted to be of the entity that the anchor declares, not of the publication act that declares it. SPARQL traversal patterns in §5.3 of the FDT paper, in tutorial materials, and in any subsequent agentic-consumption code use the referent URI accordingly.

### Item 3 — `mac:hasCollectionLocation` encoding: resolved

The object of `mac:hasCollectionLocation` is a **URI from the GeoNames gazetteer** (`https://www.geonames.org`), in the form

```
https://sws.geonames.org/{geonameId}/
```

Free-text literals are not used; ISO 3166-1 alpha-2 country codes are not the primary encoding (they may be carried as additional optional annotations via `dct:spatial` or `geonames:countryCode` when present in the GeoNames record). The GeoNames identifier scheme covers countries, administrative subdivisions, populated places, and other feature classes uniformly, which is the property the StayAhead use case requires (the granularity of "collection location" varies between national-level surveillance summaries and city-level reports).

### Item 4 — citation predicate for Types 9–11: resolved

The predicate used in Types 9, 10, and 11 to link a method FDO to its authoritative published description is

```
cito:citesAsAuthority
```

(from the SPAR Citation Typing Ontology, namespace `http://purl.org/spar/cito/`), replacing the `schema:citation` predicate proposed in v1.0. CiTO is purpose-built for citation typing in scholarly publication and provides the most precise available semantics for the relationship being asserted (the cited paper is the authoritative description of the method that the method FDO declares). The replacement is purely a predicate choice; the value range (URI of the citation target, typically a DOI) is unchanged.

Where a method has multiple authoritative descriptions (for example, an original method paper and a major revision), the predicate is repeatable.

### Item 5 — `mac:hasGISAIDAccession` dual use: resolved

The single predicate `mac:hasGISAIDAccession` is retained, used at both Type 1 (canonical exemplar accession of the variant) and Type 2 (specific surveilled accession of the real-world occurrence). The object range is **literal (string)** of the form `EPI_ISL_XXXXXXX`, consistent with GISAID's accession-numbering convention.

GISAID accessions are not currently dereferenceable as URIs (GISAID requires authentication), so URI-typed predicates such as `owl:sameAs` or `skos:closeMatch` are not used at present. Should GISAID introduce a public URI form for accessions in the future, the predicate semantics admit a straightforward migration: at Type 1 (where the variant is identified *as* the same entity as the canonical GISAID record), `owl:sameAs` becomes appropriate; at Type 2 (where the observation *concerns* a related but distinct surveilled instance), `dct:relation` or `skos:closeMatch` is more accurate. This migration is recorded as a forward-looking item but is not implemented in v1.1.

---

## Conventions

* All predicates and classes use the namespace prefix `mac:`, expanding within the MAC NanoDash ontology space at `https://w3id.org/spaces/mac/r/ontology/MAC-Ontology` (Item 1, resolved).
* "Object range" describes the expected RDF object: `literal` (with optional datatype), `URI` (with optional class constraint), or `controlled URI` (from an enumerated set).
* "Units" are given where the value is a measurement; "unitless" is explicit where applicable.

Standard-vocabulary predicates adopted without minting are namespaced as follows:

| Prefix | Namespace |
|---|---|
| `rdf:` | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` |
| `rdfs:` | `http://www.w3.org/2000/01/rdf-schema#` |
| `owl:` | `http://www.w3.org/2002/07/owl#` |
| `dct:` | `http://purl.org/dc/terms/` |
| `dcat:` | `http://www.w3.org/ns/dcat#` |
| `schema:` | `http://schema.org/` |
| `fdof:` | `https://w3id.org/fdof/ontology#` |
| `nt:` | `http://www.nanopub.org/nschema#` |
| `fair:` | `https://w3id.org/fair/principles/terms/` |
| **`cito:`** (new in v1.1) | `http://purl.org/spar/cito/` |

---

## Class hierarchy

The 19 classes of v1.2 form a three-level taxonomy. Five abstract parents (no direct instances) group the 14 concrete classes; the anchor type `mac:SpikeRBDVariant` is parentless.

```
mac:SpikeRBDVariant                                  (anchor type — no parent)

mac:Observation                              [abstract]
├── mac:RealWorldOccurrence
├── mac:ComputationalPrediction              [abstract]
│   ├── mac:ComputationalPredictionRMSD
│   ├── mac:ComputationalPredictionSASA
│   ├── mac:ComputationalPredictionPLDDT
│   └── mac:ComputationalPredictionAgMata
├── mac:ExperimentalObservation              [abstract]
│   └── mac:ExperimentalDMSObservation
└── mac:WHOVariantClassification

mac:Method                                   [abstract]
├── mac:ComputationalMethod
├── mac:ExperimentalMethod
└── mac:ObservationalMethod

mac:WHODesignation                           [abstract]
├── mac:VOC
├── mac:VOI
└── mac:VUM
```

**Abstractness convention.** The five abstract classes carry no `owl:disjointWith` axioms, no `owl:deprecated`, and no further OWL-DL machinery distinguishing them from concrete classes. Their abstract status is asserted in prose only — each `rdfs:comment` includes the sentence: *"This class is abstract: it carries no direct instances; all instances belong to one of its concrete subclasses."* This convention is consistent with the RDFS-level vocabulary the rest of v1.2 uses; a formal abstractness signal can be added in v2 without breaking instances.

**`mac:WHOVariantClassification` is kept under `mac:Observation`.** It is structurally an observation: it records the WHO's authoritative assignment of a designation to a variant at a point in time, and is linked to the variant anchor by `mac:isObservationOf` just as every other observation type is.

**`mac:SpikeRBDVariant` has no MAC-namespace parent.** It could in principle subclass a foreign protein-variant class (e.g., from UniProt/PR), but no such constraint adds expressive value at this stage. Leaving it parentless is the conservative choice.

**Anticipated extensions.** The Bosch extension (future cycle) adds `mac:ExperimentalCellSortingObservation` under `mac:ExperimentalObservation` and a new predicate `mac:hasAPCPositivePercentage`. The hierarchy in v1.2 accommodates this insertion without restructuring.

---

## Predicate domain and range

Each of the 26 MAC-namespace predicates is declared with `rdfs:domain` and `rdfs:range` per the table below. Predicates whose range is an `xsd:*` datatype are declared `owl:DatatypeProperty`; predicates with a class range or with range omitted remain `owl:ObjectProperty`. Per the proposal's §3, five predicates omit either domain or range, with the rationale recorded in the "Notes" column.

### Type 1 — identity predicates (subject: `mac:SpikeRBDVariant`)

| Predicate | Property type | Domain | Range | Notes |
|---|---|---|---|---|
| `mac:hasWHOVariantName` | DatatypeProperty | `mac:SpikeRBDVariant` | `xsd:string` | |
| `mac:hasPangoLineage` | DatatypeProperty | `mac:SpikeRBDVariant` | `xsd:string` | |
| `mac:hasGISAIDSeqId` | DatatypeProperty | `mac:SpikeRBDVariant` | `xsd:string` | |
| `mac:hasMACSeqId` | DatatypeProperty | `mac:SpikeRBDVariant` | `xsd:string` | |
| `mac:hasParentProtein` | ObjectProperty | `mac:SpikeRBDVariant` | *(omitted)* | Foreign UniProt URI; no MAC class applies. Range omitted per proposal §3(b). |
| `mac:hasRBDSequence` | DatatypeProperty | `mac:SpikeRBDVariant` | `xsd:string` | 195-char one-letter code |
| `mac:hasGISAIDAccession` | DatatypeProperty | *(omitted)* | `xsd:string` | Dual use at Type 1 and Type 2; domain omitted per proposal §3(a). |

### Cross-type predicate

| Predicate | Property type | Domain | Range | Notes |
|---|---|---|---|---|
| `mac:isObservationOf` | ObjectProperty | `mac:Observation` | `mac:SpikeRBDVariant` | The load-bearing FDT cross-link. |

### Type 2 — real-world occurrence predicates

| Predicate | Property type | Domain | Range | Notes |
|---|---|---|---|---|
| `mac:hasSurveillanceMethod` | ObjectProperty | `mac:RealWorldOccurrence` | `mac:ObservationalMethod` | |
| `mac:hasOccurrenceDate` | DatatypeProperty | `mac:RealWorldOccurrence` | `xsd:string` | Loose to admit imprecision ("late 2020–2021"); per proposal §3(e). |
| `mac:hasCollectionLocation` | ObjectProperty | `mac:RealWorldOccurrence` | *(omitted)* | Foreign GeoNames URI; range omitted per proposal §3(c). |

### Types 3–6 — computational prediction predicates

| Predicate | Property type | Domain | Range | Notes |
|---|---|---|---|---|
| `mac:hasPredictionMethod` | ObjectProperty | `mac:ComputationalPrediction` | `mac:ComputationalMethod` | Abstract parent on both sides. |
| `mac:hasRMSD` | DatatypeProperty | `mac:ComputationalPredictionRMSD` | `xsd:decimal` | Units Å. |
| `mac:hasSASA` | DatatypeProperty | `mac:ComputationalPredictionSASA` | `xsd:decimal` | Units Å². |
| `mac:haspLDDT` | DatatypeProperty | `mac:ComputationalPredictionPLDDT` | `xsd:decimal` | Unitless, 0–100. |
| `mac:hasAgMataScore` | DatatypeProperty | `mac:ComputationalPredictionAgMata` | `xsd:decimal` | Unitless. |

### Type 7 — experimental DMS predicates

| Predicate | Property type | Domain | Range | Notes |
|---|---|---|---|---|
| `mac:hasExperimentalMethod` | ObjectProperty | `mac:ExperimentalObservation` | `mac:ExperimentalMethod` | Abstract parents (Bosch will reuse). |
| `mac:hasBind` | DatatypeProperty | `mac:ExperimentalDMSObservation` | `xsd:decimal` | log K_D, unitless. |
| `mac:hasDeltaBind` | DatatypeProperty | `mac:ExperimentalDMSObservation` | `xsd:decimal` | |
| `mac:hasExpr` | DatatypeProperty | `mac:ExperimentalDMSObservation` | `xsd:decimal` | log MFI. |
| `mac:hasDeltaExpr` | DatatypeProperty | `mac:ExperimentalDMSObservation` | `xsd:decimal` | |
| `mac:hasConfidenceBind` | DatatypeProperty | `mac:ExperimentalDMSObservation` | `xsd:decimal` | |
| `mac:hasConfidenceExpr` | DatatypeProperty | `mac:ExperimentalDMSObservation` | `xsd:decimal` | |

### Type 8 — WHO classification predicates

| Predicate | Property type | Domain | Range | Notes |
|---|---|---|---|---|
| `mac:hasWHOClassification` | ObjectProperty | `mac:WHOVariantClassification` | `mac:WHODesignation` | Range is the abstract parent of `{VOC, VOI, VUM}`. |
| `mac:hasClassificationDate` | DatatypeProperty | `mac:WHOVariantClassification` | `xsd:date` | ISO 8601. |
| `mac:hasWHOClassificationReference` | ObjectProperty | `mac:WHOVariantClassification` | *(omitted)* | Generic web URL; range omitted per proposal §3(d). |

---

## Part A — Predicate definitions (26 total)

### A.1 Identity predicates (Type 1: Spike RBD Variant)

#### `mac:hasWHOVariantName`
* **Label:** has WHO variant name
* **Definition:** Asserts the World Health Organization-assigned label for the SARS-CoV-2 lineage to which this RBD variant belongs. The WHO scheme uses Greek-letter labels (Alpha, Beta, …, Omicron) for lineages designated as Variant of Concern, Variant of Interest, or Variant Under Monitoring.
* **Object range:** literal (string).
* **Reference:** WHO SARS-CoV-2 variant tracking pages (https://www.who.int/activities/tracking-SARS-CoV-2-variants).

#### `mac:hasPangoLineage`
* **Label:** has Pango lineage
* **Definition:** Asserts the Pango lineage designation for the SARS-CoV-2 lineage to which this RBD variant belongs. The Pango nomenclature provides a hierarchical lineage classification independent of WHO labelling.
* **Object range:** literal (string; e.g., `"B.1.1.7"`).
* **Reference:** Rambaut et al. 2020, *Nature Microbiology* 5:1403–1407; https://cov-lineages.org.

#### `mac:hasGISAIDSeqId`
* **Label:** has GISAID seq_id (full Spike mutation notation)
* **Definition:** Asserts the canonical amino-acid substitution notation, referenced to the full-length SARS-CoV-2 Spike protein numbering, that identifies the defining mutation of this variant as catalogued in GISAID surveillance records.
* **Object range:** literal (string in single-letter amino-acid notation; e.g., `"N501Y"`).

#### `mac:hasMACSeqId`
* **Label:** has MAC seq_id (RBD mutation notation)
* **Definition:** Asserts the amino-acid substitution notation, referenced to the 195-residue Spike Receptor Binding Domain (RBD; UniProt P0DTC2 positions 331–525), that identifies the defining mutation of this variant in the MAC StayAhead RBD-focused pipelines. Differs from `mac:hasGISAIDSeqId` only in the residue numbering reference frame.
* **Object range:** literal (string in single-letter amino-acid notation; e.g., `"N169Y"`).

#### `mac:hasParentProtein`
* **Label:** has parent protein
* **Definition:** Asserts the wild-type parent protein from which this RBD variant is derived by amino-acid substitution. In the present catalogue the value is hardcoded to the UniProt record for the Wuhan reference SARS-CoV-2 Spike glycoprotein.
* **Object range:** URI (fixed: `https://www.uniprot.org/uniprot/P0DTC2`).

#### `mac:hasRBDSequence`
* **Label:** has RBD amino acid sequence (195 residues, one-letter code)
* **Definition:** Asserts the complete amino-acid sequence of this RBD variant in one-letter code, 195 residues, corresponding to UniProt P0DTC2 positions 331–525 with the variant-defining substitution(s) applied.
* **Object range:** literal (string of length 195 over the standard amino-acid alphabet).

#### `mac:hasGISAIDAccession`
* **Label:** has GISAID accession number
* **Definition:** Asserts a GISAID EpiCoV accession identifier (format `EPI_ISL_XXXXXXX`) of a genome sequence relevant to this FDO. At the Type 1 (variant) level the value is the canonical exemplar sequence chosen to represent the variant; at the Type 2 (real-world occurrence) level the value is the specific surveilled sequence whose collection date and location are recorded by the observation.
* **Object range:** literal (string).
* **Resolution (Item 5):** Single-predicate dual use confirmed; literal range retained. URI-typed re-encoding deferred pending public GISAID URI scheme.

### A.2 Cross-type predicate (Types 2–8)

#### `mac:isObservationOf`
* **Label:** is observation of
* **Definition:** Asserts that this observation FDO records a measured, predicted, or recorded property of the referent identified by the object URI. Used by Types 2–8 to link each observation to the central anchor FDO of the FAIR Digital Twin, making the anchor the hub of the knowlet topology. The object URI is the referent URI (i.e., the `sub:fdo` identifier declared by the anchor nanopublication), not the Trusty URI of the anchor itself.
* **Object range:** URI (the referent URI declared by the anchor).
* **Resolution (Item 2):** Object resolves to the referent URI (FDO-as-subject semantics).

### A.3 Real-world occurrence predicates (Type 2)

#### `mac:hasSurveillanceMethod`
* **Label:** has surveillance method
* **Definition:** Asserts the surveillance system or observational platform through which this real-world occurrence was documented (e.g., the GISAID EpiCoV platform).
* **Object range:** URI (Type 11 Observational Method FDO).

#### `mac:hasOccurrenceDate`
* **Label:** has occurrence date (GISAID reported collection date)
* **Definition:** Asserts the GISAID-reported collection date of the sample exemplifying this real-world occurrence. Where only a date range or month is known, the literal carries that imprecision explicitly.
* **Object range:** literal (date or date-range string; ISO 8601 preferred where precision permits).

#### `mac:hasCollectionLocation`
* **Label:** has collection location
* **Definition:** Asserts the geographic location at which the sample exemplifying this real-world occurrence was collected. The value is a URI identifying a feature in the GeoNames gazetteer (https://www.geonames.org), of the form `https://sws.geonames.org/{geonameId}/`. The granularity (country, administrative subdivision, populated place) follows the granularity of the source surveillance record.
* **Object range:** URI (GeoNames feature URI).
* **Resolution (Item 3):** GeoNames URI encoding confirmed; free-text literals not used.

### A.4 Computational prediction predicates (Types 3–6)

#### `mac:hasPredictionMethod`
* **Label:** has prediction method
* **Definition:** Asserts the computational method, tool, or algorithm that produced this prediction.
* **Object range:** URI (Type 9 Computational Method FDO).

#### `mac:hasRMSD`
* **Label:** has RMSD (Root Mean Square Deviation)
* **Definition:** Asserts the Root Mean Square Deviation between the predicted structure of this variant's RBD and a reference structure, measured as the average distance between corresponding atoms after optimal superposition.
* **Object range:** decimal literal.
* **Units:** Angstroms (Å).

#### `mac:hasSASA`
* **Label:** has SASA (Solvent Accessible Surface Area)
* **Definition:** Asserts the Solvent Accessible Surface Area of the predicted structure of this variant's RBD, computed as the surface area accessible to a standard solvent probe.
* **Object range:** decimal literal.
* **Units:** square Angstroms (Å²).

#### `mac:haspLDDT`
* **Label:** has pLDDT score
* **Definition:** Asserts the predicted Local Distance Difference Test (pLDDT) score, a per-residue or aggregated confidence measure for the predicted protein structure, ranging from 0 (lowest confidence) to 100 (highest confidence). The aggregation convention (e.g., mean over residues) is specified by the predicting method's documentation.
* **Object range:** decimal literal (range 0–100).
* **Units:** unitless.

#### `mac:hasAgMataScore`
* **Label:** has AgMata score (aggregation propensity)
* **Definition:** Asserts the AgMata aggregation propensity score computed for this variant's sequence by the Bio2Byte toolkit, indicating predicted tendency to form protein aggregates.
* **Object range:** decimal literal.
* **Units:** unitless.

### A.5 Experimental DMS predicates (Type 7)

#### `mac:hasExperimentalMethod`
* **Label:** has experimental method
* **Definition:** Asserts the experimental method through which the measurements reported in this observation were obtained.
* **Object range:** URI (Type 10 Experimental Method FDO).

#### `mac:hasBind`
* **Label:** has bind (binding affinity)
* **Definition:** Asserts the binding affinity measurement for this variant's RBD interaction with its receptor (typically ACE2), reported on a logarithmic scale as −log(K_D). Higher values indicate stronger binding.
* **Object range:** decimal literal.
* **Units:** unitless (log K_D).

#### `mac:hasDeltaBind`
* **Label:** has delta_bind (change in binding affinity)
* **Definition:** Asserts the change in binding affinity for this variant relative to the wild-type reference, computed as Δ(−log K_D). Positive values indicate stronger binding than wild-type.
* **Object range:** decimal literal.
* **Units:** unitless.

#### `mac:hasExpr`
* **Label:** has expr (expression level)
* **Definition:** Asserts the protein expression level measurement for this variant, reported as the logarithm of the mean fluorescence intensity (log MFI) from the deep mutational scanning assay.
* **Object range:** decimal literal.
* **Units:** unitless (log MFI).

#### `mac:hasDeltaExpr`
* **Label:** has delta_expr (change in expression level)
* **Definition:** Asserts the change in expression level for this variant relative to the wild-type reference, computed as Δ(log MFI).
* **Object range:** decimal literal.
* **Units:** unitless.

#### `mac:hasConfidenceBind`
* **Label:** has confidence_bind (binding confidence score)
* **Definition:** Asserts the confidence score associated with the binding affinity measurement, as reported by the deep mutational scanning analysis pipeline. Higher values indicate higher reliability of the binding measurement.
* **Object range:** decimal literal.
* **Units:** unitless.

#### `mac:hasConfidenceExpr`
* **Label:** has confidence_expr (expression confidence score)
* **Definition:** Asserts the confidence score associated with the expression level measurement, as reported by the deep mutational scanning analysis pipeline.
* **Object range:** decimal literal.
* **Units:** unitless.

### A.6 WHO classification predicates (Type 8)

#### `mac:hasWHOClassification`
* **Label:** has WHO variant classification
* **Definition:** Asserts the World Health Organization risk classification assigned to this variant at a given point in time: Variant of Concern (VOC), Variant of Interest (VOI), or Variant Under Monitoring (VUM). Time-stamped because designation status changes over time.
* **Object range:** controlled URI from `{mac:VOC, mac:VOI, mac:VUM}`.

#### `mac:hasClassificationDate`
* **Label:** has WHO classification date
* **Definition:** Asserts the date on which the WHO assigned this classification to the variant.
* **Object range:** literal (date; ISO 8601 preferred).

#### `mac:hasWHOClassificationReference`
* **Label:** has WHO classification reference URL
* **Definition:** Asserts the URL of the WHO publication or tracking page that documents this classification.
* **Object range:** URI.

---

## Part B — Class definitions (19 total: 14 concrete + 5 abstract)

### B.0 Abstract parent classes (5, new in v1.2)

These classes carry no direct instances. Their role is to group their concrete subclasses for the purpose of typing predicate domains and ranges (see §"Predicate domain and range") and to make future extensions (e.g., the Bosch extension) accommodate additional siblings without restructuring.

#### `mac:Observation`
An abstract parent class for all observation-layer FDOs in a MAC FAIR Digital Twin. Concrete subclasses include `mac:RealWorldOccurrence` (Type 2), `mac:ComputationalPrediction` and its sub-hierarchy (Types 3–6), `mac:ExperimentalObservation` and its sub-hierarchy (Type 7), and `mac:WHOVariantClassification` (Type 8). Every member links to the FDT's anchor (a `mac:SpikeRBDVariant`) via `mac:isObservationOf`. This class is abstract: it carries no direct instances; all instances belong to one of its concrete subclasses.

#### `mac:ComputationalPrediction`
An abstract parent class for computational predictions about a Spike RBD variant, produced by a named computational method. Concrete subclasses cover specific predicted quantities (`mac:ComputationalPredictionRMSD`, `…SASA`, `…PLDDT`, `…AgMata`). Anticipates additional computational prediction types as siblings without restructuring the hierarchy. This class is abstract: all instances belong to one of its concrete subclasses.

#### `mac:ExperimentalObservation`
An abstract parent class for empirical observations produced by laboratory assays on a Spike RBD variant. Currently has one concrete child (`mac:ExperimentalDMSObservation`, deep mutational scanning); the forthcoming Bosch extension adds `mac:ExperimentalCellSortingObservation` as a sibling. This class is abstract: all instances belong to one of its concrete subclasses.

#### `mac:Method`
An abstract parent class for methods, tools, assays, or surveillance platforms that produce observations within the MAC FAIR Digital Twin substrate. Concrete subclasses distinguish computational methods (`mac:ComputationalMethod`), experimental methods (`mac:ExperimentalMethod`), and observational/surveillance methods (`mac:ObservationalMethod`). Instances of any concrete subclass carry one or more `cito:citesAsAuthority` URIs identifying the published descriptions of the method. This class is abstract: all instances belong to one of its concrete subclasses.

#### `mac:WHODesignation`
An abstract parent class for the World Health Organization's controlled-vocabulary risk designations applied to SARS-CoV-2 variants: Variant of Concern (`mac:VOC`), Variant of Interest (`mac:VOI`), and Variant Under Monitoring (`mac:VUM`). Used as the range of `mac:hasWHOClassification`. This class is abstract: all instances belong to one of its concrete subclasses.

### B.1 FDT and observation classes (8)

#### `mac:SpikeRBDVariant`
A variant of the SARS-CoV-2 Spike receptor-binding domain (RBD, 195 residues) produced by one or more amino-acid substitutions from the wild-type Wuhan isolate (UniProt P0DTC2). This class is the type of the anchor FDO ($A_r$) of a FAIR Digital Twin; all observation FDOs link to it via `mac:isObservationOf` and collectively constitute the FDT.
*Subclass of:* — (no MAC-namespace parent).

#### `mac:RealWorldOccurrence`
A documented detection of a SARS-CoV-2 Spike variant in the real world, as reported in a surveillance database (typically GISAID). The occurrence is anchored to a specific collection date and to a GeoNames-identified location.
*Subclass of:* `mac:Observation`.

#### `mac:ComputationalPredictionRMSD`
A computed prediction of the Root Mean Square Deviation between a predicted structure of a Spike RBD variant and a reference structure, produced by a named computational structure-prediction method.
*Subclass of:* `mac:ComputationalPrediction`.

#### `mac:ComputationalPredictionSASA`
A computed prediction of the Solvent Accessible Surface Area of a Spike RBD variant's predicted structure, produced by a named computational structure-prediction method.
*Subclass of:* `mac:ComputationalPrediction`.

#### `mac:ComputationalPredictionPLDDT`
A computed prediction confidence score (predicted Local Distance Difference Test) for the structural prediction of a Spike RBD variant, produced by a named computational structure-prediction method.
*Subclass of:* `mac:ComputationalPrediction`.

#### `mac:ComputationalPredictionAgMata`
A computed prediction of the aggregation propensity of a Spike RBD variant, produced by the Bio2Byte AgMata method. The score is sequence-derived and is therefore predicted once per variant rather than once per structural-prediction method.
*Subclass of:* `mac:ComputationalPrediction`.

#### `mac:ExperimentalDMSObservation`
An experimental observation of binding affinity and expression level measurements for a Spike RBD variant, determined by deep mutational scanning (Bloom Lab protocol). One FDO records all six DMS metrics (`bind`, `delta_bind`, `expr`, `delta_expr`, `confidence_bind`, `confidence_expr`) for a single variant.
*Subclass of:* `mac:ExperimentalObservation`.

#### `mac:WHOVariantClassification`
A classification of a SARS-CoV-2 lineage according to the WHO risk framework (VOC / VOI / VUM), with a specified assignment date and reference URL. Time-stamped because designation status changes over time.
*Subclass of:* `mac:Observation`.

### B.2 Method classes (3)

#### `mac:ComputationalMethod`
A computational method, tool, or algorithm that produces predictions or scores from biological sequence or structure data. Referenced by observation FDOs of Types 3–6 via `mac:hasPredictionMethod`. Instances carry one or more `cito:citesAsAuthority` URIs identifying the published descriptions of the method.
*Subclass of:* `mac:Method`.

#### `mac:ExperimentalMethod`
An experimental assay or measurement protocol that produces empirical observations about biological entities. Referenced by Type 7 observation FDOs via `mac:hasExperimentalMethod`. Instances carry one or more `cito:citesAsAuthority` URIs identifying the published descriptions of the assay.
*Subclass of:* `mac:Method`.

#### `mac:ObservationalMethod`
An epidemiological surveillance system or data-collection platform through which real-world occurrences of biological entities are documented. Referenced by Type 2 observation FDOs via `mac:hasSurveillanceMethod`. Instances carry one or more `cito:citesAsAuthority` URIs identifying the published descriptions of the surveillance platform.
*Subclass of:* `mac:Method`.

### B.3 WHO classification controlled values (3)

#### `mac:VOC` — Variant of Concern
A SARS-CoV-2 variant designated by the WHO as carrying evidence of increased transmissibility, increased disease severity, or significant reduction in vaccine or therapeutic effectiveness.
*Subclass of:* `mac:WHODesignation`.

#### `mac:VOI` — Variant of Interest
A SARS-CoV-2 variant designated by the WHO as carrying genetic markers associated with phenotypic changes and demonstrated epidemiological impact warranting enhanced monitoring.
*Subclass of:* `mac:WHODesignation`.

#### `mac:VUM` — Variant Under Monitoring
A SARS-CoV-2 variant for which the WHO has identified evidence of growth advantage or immune escape and that is being monitored precautionarily pending further characterisation.
*Subclass of:* `mac:WHODesignation`.

---

## Class inventory

| Category | Count | Members |
|---|---:|---|
| Abstract parent classes (new in v1.2) | 5 | `Observation`, `ComputationalPrediction`, `ExperimentalObservation`, `Method`, `WHODesignation` |
| FDT + observation classes (concrete) | 8 | `SpikeRBDVariant`, `RealWorldOccurrence`, `ComputationalPredictionRMSD`, `ComputationalPredictionSASA`, `ComputationalPredictionPLDDT`, `ComputationalPredictionAgMata`, `ExperimentalDMSObservation`, `WHOVariantClassification` |
| Method classes (concrete) | 3 | `ComputationalMethod`, `ExperimentalMethod`, `ObservationalMethod` |
| WHO classification controlled values (concrete) | 3 | `VOC`, `VOI`, `VUM` |
| **Total** | **19** | 14 concrete + 5 abstract. SPS v1.0 header value of "16" was a miscount for the concrete inventory; corrected to 14 in SPS v1.1. v1.2 adds the 5 abstract parents. |

## Predicate inventory

| Category | Count |
|---|---:|
| Type 1 identity | 7 |
| Cross-type | 1 |
| Type 2 real-world | 3 |
| Types 3–6 computational | 5 (1 shared + 4 metric-specific) |
| Type 7 experimental | 7 (1 method + 6 measurement) |
| Type 8 WHO | 3 |
| **Total MAC-namespace predicates** | **26** |

Standard-vocabulary predicates adopted without minting: `rdf:type`, `rdfs:label`, `rdfs:comment`, `dct:creator`, `dct:created`, `dct:license`, `dct:source`, `dct:references`, `schema:url`, `fdof:hasMetadata`, `fair:implements`, `dcat:contactPoint`, `dct:publisher`, `dct:subject`, and (new in v1.1) **`cito:citesAsAuthority`** in place of `schema:citation` for Types 9–11.

---

## Notes for the Tobias session

1. The vocabulary nanopubs are minted **before** the templates that reference them; the templates **before** the instances. Each layer's Trusty URIs feed the next.
2. With Items 1–5 now resolved, no further pre-minting confirmation is required from Tobias on the vocabulary itself. Any remaining adjustments emerging during minting (e.g., choice of `cito:citesAsAuthority` vs. `cito:citesAsSourceDocument` at term-creation time) are within-scope and do not require revision of this document.
3. The FFF precedent (from MAC_FAIR_v2.0) demonstrates that the vocabulary nanopubs can themselves be FDOs of a vocabulary-term type. Recommended: adopt the same pattern for the MAC FDT vocabulary so that the vocabulary is self-describing and SPARQL-queryable on the same NSN substrate as the FDT instances.

---

## Version history

| Version | Date | Notes |
|---|---|---|
| v1.0 | 20 May 2026 | Initial draft prepared for review by Tobias Kuhn. Seven open items recorded. |
| v1.1 | 21 May 2026 | Items 1–5 resolved. Item 6 corrected (concrete class count = 14). Item 7 captured in `README_for_Claude_Code_v1.1.md`. |
| v1.2 | 22 May 2026 | PR #1 review items applied (this document): `dct:partOf` replaces `rdfs:isDefinedBy`; class hierarchy introduced with 5 new abstract parents (total 19 classes); `rdfs:domain` and `rdfs:range` declared on all 26 predicates with 5 edge cases resolved per the proposal. Companion: `Stage1_hierarchy_and_domain_range_proposal.md`. |
