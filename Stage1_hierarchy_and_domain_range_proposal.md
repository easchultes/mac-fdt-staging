<!--
AUTHOR: Erik Schultes
SESSION: Making MAC FAIR/Article - FDT Paper
DATE: 2026-05-22
URL: https://claude.ai/chat/22a7668a-24ce-4533-82fa-7e5a6b6204e9
CREATED_AT: P25/R25
DESCRIPTION: Proposal for class hierarchy and predicate domain/range, in response to Tobias's PR #1 review (22 May 2026). For Erik's review then Tobias's confirmation before regenerating Stage 1 TriG drafts.
-->

# Stage 1 vocabulary — hierarchy and domain/range proposal

*Response to Tobias's PR #1 review (22 May 2026), items 2 and 3. Items 1 (`dct:partOf` over `rdfs:isDefinedBy`) and 4 (slash separator) are mechanical and will be applied at TriG regeneration time without further discussion.*

---

## 1. Class hierarchy

The current Stage 1 draft defines 14 classes as a flat list. Tobias is right that this misses the natural taxonomy. We propose **five new abstract superclasses** (none with instances of their own), giving the catalogue a 3-level hierarchy and bringing the total class count to **14 + 5 = 19**.

### Proposed hierarchy

```
mac:SpikeRBDVariant                                  (the anchor type — no parent)

mac:Observation                              [NEW]   abstract
├── mac:RealWorldOccurrence
├── mac:ComputationalPrediction              [NEW]   abstract
│   ├── mac:ComputationalPredictionRMSD
│   ├── mac:ComputationalPredictionSASA
│   ├── mac:ComputationalPredictionPLDDT
│   └── mac:ComputationalPredictionAgMata
├── mac:ExperimentalObservation              [NEW]   abstract
│   └── mac:ExperimentalDMSObservation
└── mac:WHOVariantClassification

mac:Method                                   [NEW]   abstract
├── mac:ComputationalMethod
├── mac:ExperimentalMethod
└── mac:ObservationalMethod

mac:WHODesignation                           [NEW]   abstract
├── mac:VOC
├── mac:VOI
└── mac:VUM
```

### Rationale for each new abstract class

| New class | Justification |
|---|---|
| `mac:Observation` | Common parent for all observation-layer FDOs. Makes `mac:isObservationOf` typeable with a single domain (`mac:Observation`) rather than a disjunction. Also aligns with the §4.1 architectural layer terminology in the FDT paper. |
| `mac:ComputationalPrediction` | Groups the four metric-specific prediction classes. Lets `mac:hasPredictionMethod` have a single domain rather than enumerating four. Anticipates future computational prediction types (e.g., binding-affinity prediction by Boltz-2) that will add as siblings without further restructuring. |
| `mac:ExperimentalObservation` | Currently has only one child (DMS), but the Bosch extension introduces `mac:ExperimentalCellSortingObservation` as a sibling. Pre-emptively introducing the abstract parent now avoids a Stage 1 vocabulary patch when Bosch is minted. |
| `mac:Method` | Common parent for the three method classes. Lets a generic citation-to-method predicate, if needed in future, target a single domain. |
| `mac:WHODesignation` | Common parent for the three WHO controlled values. Lets `mac:hasWHOClassification` have a single class range rather than enumerating `{VOC, VOI, VUM}`. |

### Worth flagging

* **`mac:WHOVariantClassification` is kept under `mac:Observation`.** It is structurally an observation in the sense that it records the WHO's authoritative assignment of a designation to a variant at a point in time. If Tobias prefers it as a sibling of `mac:Observation` rather than a child, that's a one-line change. Our current preference is to keep it as a child to preserve the architectural symmetry — every member of an FDT cluster, including the classification, links back to the anchor via `mac:isObservationOf`.
* **`mac:SpikeRBDVariant` has no MAC-namespace parent.** It could in principle subclass from a UniProt/PR protein-variant class or from a generic `dcat:Resource`, but neither adds expressive value at this stage. Leaving it parentless is the conservative choice.
* **No `owl:disjointWith` axioms** in this proposal. The current flat-typing carries no disjointness either, and adding it now would require deciding whether siblings (e.g., the four `ComputationalPrediction*` classes) are mutually exclusive in some formal sense. Defer this question — it can be added later without breaking instances.

---

## 2. Predicate domain and range

Domain and range proposals for all 26 MAC-namespace predicates. The domain identifies the subject class; the range identifies the object class or datatype. Where range is `xsd:*`, the predicate is declared `owl:DatatypeProperty`; where range is a class, it remains `owl:ObjectProperty`.

### Type 1 — identity predicates (subject: `mac:SpikeRBDVariant`)

| Predicate | Domain | Range | Notes |
|---|---|---|---|
| `mac:hasWHOVariantName` | `mac:SpikeRBDVariant` | `xsd:string` | datatype |
| `mac:hasPangoLineage` | `mac:SpikeRBDVariant` | `xsd:string` | datatype |
| `mac:hasGISAIDSeqId` | `mac:SpikeRBDVariant` | `xsd:string` | datatype |
| `mac:hasMACSeqId` | `mac:SpikeRBDVariant` | `xsd:string` | datatype |
| `mac:hasParentProtein` | `mac:SpikeRBDVariant` | *(omit — foreign URI)* | UniProt URI; see §"Edge cases" below |
| `mac:hasRBDSequence` | `mac:SpikeRBDVariant` | `xsd:string` | datatype; 195-char one-letter code |
| `mac:hasGISAIDAccession` | *(omit — dual use)* | `xsd:string` | datatype; subject is either `mac:SpikeRBDVariant` or `mac:RealWorldOccurrence`; see §"Edge cases" |

### Cross-type predicate

| Predicate | Domain | Range | Notes |
|---|---|---|---|
| `mac:isObservationOf` | `mac:Observation` | `mac:SpikeRBDVariant` | the load-bearing cross-link |

### Type 2 — real-world occurrence predicates

| Predicate | Domain | Range | Notes |
|---|---|---|---|
| `mac:hasSurveillanceMethod` | `mac:RealWorldOccurrence` | `mac:ObservationalMethod` | object property |
| `mac:hasOccurrenceDate` | `mac:RealWorldOccurrence` | `xsd:string` | datatype; loose to admit imprecision ("late 2020–2021") |
| `mac:hasCollectionLocation` | `mac:RealWorldOccurrence` | *(omit — foreign URI)* | GeoNames URI; see §"Edge cases" |

### Types 3–6 — computational prediction predicates

| Predicate | Domain | Range | Notes |
|---|---|---|---|
| `mac:hasPredictionMethod` | `mac:ComputationalPrediction` | `mac:ComputationalMethod` | abstract parent on both sides where applicable |
| `mac:hasRMSD` | `mac:ComputationalPredictionRMSD` | `xsd:decimal` | datatype; units Å |
| `mac:hasSASA` | `mac:ComputationalPredictionSASA` | `xsd:decimal` | datatype; units Å² |
| `mac:haspLDDT` | `mac:ComputationalPredictionPLDDT` | `xsd:decimal` | datatype; unitless, 0–100 |
| `mac:hasAgMataScore` | `mac:ComputationalPredictionAgMata` | `xsd:decimal` | datatype; unitless |

### Type 7 — experimental DMS predicates

| Predicate | Domain | Range | Notes |
|---|---|---|---|
| `mac:hasExperimentalMethod` | `mac:ExperimentalObservation` | `mac:ExperimentalMethod` | abstract parent (Bosch will reuse) |
| `mac:hasBind` | `mac:ExperimentalDMSObservation` | `xsd:decimal` | datatype; log K_D, unitless |
| `mac:hasDeltaBind` | `mac:ExperimentalDMSObservation` | `xsd:decimal` | datatype |
| `mac:hasExpr` | `mac:ExperimentalDMSObservation` | `xsd:decimal` | datatype; log MFI |
| `mac:hasDeltaExpr` | `mac:ExperimentalDMSObservation` | `xsd:decimal` | datatype |
| `mac:hasConfidenceBind` | `mac:ExperimentalDMSObservation` | `xsd:decimal` | datatype |
| `mac:hasConfidenceExpr` | `mac:ExperimentalDMSObservation` | `xsd:decimal` | datatype |

### Type 8 — WHO classification predicates

| Predicate | Domain | Range | Notes |
|---|---|---|---|
| `mac:hasWHOClassification` | `mac:WHOVariantClassification` | `mac:WHODesignation` | object property; range is the abstract parent of VOC/VOI/VUM |
| `mac:hasClassificationDate` | `mac:WHOVariantClassification` | `xsd:date` | datatype; ISO 8601 |
| `mac:hasWHOClassificationReference` | `mac:WHOVariantClassification` | *(omit — generic URL)* | object property to an external URL; see §"Edge cases" |

---

## 3. Edge cases worth Tobias's input

Five predicates have non-trivial range decisions. Recommended treatment for each:

**(a) `mac:hasGISAIDAccession` — dual-use domain.** Used at both Type 1 (canonical variant accession) and Type 2 (specific surveilled accession). Three options:

1. **Omit the domain entirely** (recommended). The predicate floats freely; instances declare their subject's type independently. Simplest.
2. Use `owl:unionOf (mac:SpikeRBDVariant mac:RealWorldOccurrence)` — formally correct but introduces OWL-DL complexity into an otherwise RDFS-level vocabulary.
3. Split into two predicates (`mac:hasCanonicalGISAIDAccession`, `mac:hasObservedGISAIDAccession`). Cleanest formally but adds a predicate and changes the SPS.

Our preference: option 1 for v1.1; revisit at v2 if a use case forces the split.

**(b) `mac:hasParentProtein` — foreign-URI range (UniProt).** The value is a UniProt URI (specifically `https://www.uniprot.org/uniprot/P0DTC2`). Options:

1. **Omit the range** (recommended). The value is an IRI by virtue of being an ObjectProperty; no further constraint is added.
2. Declare a generic range like `owl:Thing` — no information gain.
3. Adopt a foreign class as range (e.g., `up:Protein` from the UniProt ontology). Adds an external dependency.

Our preference: option 1.

**(c) `mac:hasCollectionLocation` — foreign-URI range (GeoNames).** Same shape as (b). Recommend omitting the range. Alternatively, `gn:Feature` from the GeoNames ontology if Tobias wants the range typed.

**(d) `mac:hasWHOClassificationReference` — generic URL range.** The value is an arbitrary web URL (a WHO tracking page). Recommend omitting the range; the predicate is `owl:ObjectProperty` and the value is implicitly an IRI.

**(e) `mac:hasOccurrenceDate` — date-or-date-range range.** Some values in our catalogue are imprecise ("late 2020–2021"). `xsd:date` would reject these. Three options:

1. **Use `xsd:string`** (recommended). Lossy on machine-actionability but accommodates the surveillance reality.
2. Use `xsd:gYear`, `xsd:gYearMonth`, or `xsd:date` polymorphically — formally clean but instance-by-instance type variation is awkward.
3. Adopt EDTF (Extended Date/Time Format, ISO 8601-2) — most expressive but adds a parsing dependency for consumers.

Our preference: option 1 with a controlled-string-format note in the vocabulary comment. Revisit when surveillance dates routinely arrive in ISO 8601 form.

---

## 4. Implementation steps once approved

When Erik and Tobias agree on this proposal:

1. Update `specs/MAC_FDT_Vocabulary_v1_1.md` → `v1_2.md` with the hierarchy (5 new abstract classes) and the domain/range declarations.
2. Update the generator script `/tmp/gen_vocab_trigs.py` to:
   - Switch `rdfs:isDefinedBy` → `dct:partOf` (item 1)
   - Add `rdfs:subClassOf` triples per the hierarchy in §1
   - Add `rdfs:domain` and `rdfs:range` triples per §2
   - Emit 5 additional TriG files for the new abstract classes
   - Confirm slash separator (item 4) — already in use
3. Regenerate 19 class + 26 predicate = **45 TriG files** (replaces the current 40).
4. Re-run `nanopub check` (Java 21 + jar 1.88.0) — expect 45/45 PASS.
5. Amend the PR commit on `stage1-vocabulary-draft` so the branch carries one clean commit reflecting all four review items.

No structural changes to other documents are required at this stage. The FDT paper draft (v0.5) does not enumerate the predicate or class hierarchy; it cites the vocabulary spec by reference. SPS v1.2 references class names which remain unchanged for the 14 concrete classes.

---

## 5. Summary of class-count progression

| Stage | Concrete | Abstract | Total |
|---|---|---|---|
| v1.0 (initial) | 14 (with miscount as "16") | 0 | 14 |
| v1.1 (current) | 14 | 0 | 14 |
| v1.2 (this proposal) | 14 | 5 | **19** |
| Bosch extension (future) | 15 (adds `mac:ExperimentalCellSortingObservation`) | 5 | 20 |

Predicate count is unchanged at 26 in v1.2; the Bosch extension adds 1 (`mac:hasAPCPositivePercentage`) for a future total of 27.
