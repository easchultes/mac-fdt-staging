# MAC FAIR Digital Twin — Bosch Lab Extension
## v1.0 — Working Implementation Document

**Project:** StayAhead / MAC — Leiden University LACDR  
**Collaborator:** Dr. Berend Jan Bosch, Department of Biomolecular Health Sciences, Utrecht University  
**Status:** Ready for implementation after initial 3-variant FDT set is live on NSN  
**Relation to SPS v1.0:** Extends the 11-type framework by template reuse. Introduces 1 new predicate, 1 new observation class URI, and 1 new Type 10 method instance.

---

## Design principle

FDT observation FDOs record documented measurements and observations — events that occurred in the world under specified conditions using a specified method, with a result traceable to a source. They do not record interpretations, classifications, or conclusions derived from those measurements. This principle is applied strictly here: the predicted binding categories (Low/Neutral/High Binder) that motivated the Bosch experiment are interpretations of the computational predictions and are excluded from the FDOs. The APC+ve percentage is a measurement. The absence of expression is an assay outcome. Both are observations; both are recorded.

---

## Template reuse — the analogy is exact

| Element | Bloom Lab (DMS) | Bosch Lab (cell sorting) |
|---|---|---|
| Observation template | Type 7 | Type 7 (reused) |
| Observation class URI | `mac:ExperimentalDMSObservation` | `mac:ExperimentalCellSortingObservation` (new) |
| Method template | Type 10 | Type 10 (reused) |
| Method class URI | `mac:ExperimentalMethod` | `mac:ExperimentalMethod` (same — no new class) |
| Key metric predicate | bind, delta_bind, expr, delta_expr, confidence_bind, confidence_expr | `mac:hasAPCPositivePercentage` (1 new predicate) |

**New elements required:** 1 predicate, 1 class URI, 1 Type 10 instance.

---

## The assay and its measurements

An APC-labeled cell sorting binding assay was performed by the Bosch lab. Cells expressing the ACE2 receptor were incubated with APC-labeled RBD variants; the percentage of APC-positive cells in the flow cytometry gate (FL9-A :: 660-10(638)-A, threshold 10^4) quantifies binding.

**Assay controls (recorded in the Type 10 method FDO):**

| Condition | APC+ve % |
|---|---|
| APC-TM only (negative control) | 10.3 |
| Wildtype RBD (positive control) | 48.0 |

**Experimental outcomes:**

| Variant | MAC seq_id | Expression | APC+ve % |
|---|---|---|---|
| V35F_F10I | V35F_F10I | Yes | 5.00 |
| Y33W_N38Q | Y33W_N38Q | Yes | 3.44 |
| Y33W_P175F | Y33W_P175F | Not detected | — |
| V35F_R122L | V35F_R122L | Not detected | — |
| Q161Y_C148K | Q161Y_C148K | Not detected | — |

For the three non-expressing variants, no `mac:hasAPCPositivePercentage` value is present in the FDO. The absence is machine-readable: a SPARQL query for APC+ve measurements returns no results for these variants, which is itself a precise record that the assay was performed and the measurement was unobtainable.

---

## New predicate

**`mac:hasAPCPositivePercentage`**  
rdfs:label: "has APC-positive cell percentage (%, flow cytometry gate FL9-A :: 660-10(638)-A)"  
Object range: decimal literal  
Used in: Type 7 instances where expression was detected

---

## Type 1 FDTs — five double-mutant variants

Class `mac:SpikeRBDVariant` is reused unchanged. Class description in SPS v1.0 already accommodates "one or more amino acid substitutions." WHO variant name, Pango lineage, and GISAID seq_id are not populated (these are computationally designed variants, not real-world isolates).

**Verified 195-aa sequences (all confirmed at 195 residues):**

| MAC seq_id | Mutations | 195-aa sequence |
|---|---|---|
| Y33W_P175F | pos. 33 Y→W, pos. 175 P→F | `TNLCPFGEVFNATRFASVYAWNRKRISNCVADWSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQFYRVVVLSFELLHAPATVCGP` |
| V35F_F10I | pos. 10 F→I, pos. 35 V→F | `TNLCPFGEVINATRFASVYAWNRKRISNCVADYSFLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGP` |
| V35F_R122L | pos. 35 V→F, pos. 122 R→L | `TNLCPFGEVFNATRFASVYAWNRKRISNCVADYSFLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYLLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGP` |
| Y33W_N38Q | pos. 33 Y→W, pos. 38 N→Q | `TNLCPFGEVFNATRFASVYAWNRKRISNCVADWSVLYQSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGP` |
| Q161Y_C148K | pos. 148 C→K, pos. 161 Q→Y | `TNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPKNGVEGFNCYFPLYSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGP` |

---

## Type 10 method instance — Bosch Lab

Reuses existing Type 10 (Experimental Method) template and `mac:ExperimentalMethod` class. No new class URI.

| Field | Value |
|---|---|
| `rdfs:label` | "APC-labeled cell sorting binding assay — Bosch Lab, Utrecht University" |
| `rdfs:comment` | "Cell sorting assay for detection of SARS-CoV-2 Spike RBD binding to ACE2-expressing cells. APC-labeled RBD variants are incubated with cells; the percentage of APC-positive cells in the FL9-A gate (threshold 10^4) is the primary measurement. Assay controls: APC-TM only (negative control) = 10.3% APC+ve; wildtype Wuhan RBD (positive control) = 48.0% APC+ve. Laboratory of Dr. Berend Jan Bosch, Biomolecular Health Sciences, Utrecht University." |
| `schema:citation` | [opt] to be added when method is published |
| `schema:url` | `https://www.uu.nl/staff/organizationalchart/dgk/200` |

---

## Type 7 FDO instances — Bosch lab observations

Class: `mac:ExperimentalCellSortingObservation`

**V35F_F10I and Y33W_N38Q (expression detected):**

| Field | V35F_F10I | Y33W_N38Q |
|---|---|---|
| `rdfs:label` | "V35F_F10I cell sorting — Bosch Lab" | "Y33W_N38Q cell sorting — Bosch Lab" |
| `rdfs:comment` | "Expression detected in cell sorting assay. APC+ve: 5.00%. Negative control: 10.3%. Positive control (wildtype RBD): 48.0%. No binding detected." | "Expression detected in cell sorting assay. APC+ve: 3.44%. Negative control: 10.3%. Positive control (wildtype RBD): 48.0%. No binding detected." |
| `mac:isObservationOf` | URI of V35F_F10I Type 1 FDT | URI of Y33W_N38Q Type 1 FDT |
| `mac:hasExperimentalMethod` | URI of Bosch Type 10 FDO | URI of Bosch Type 10 FDO |
| `mac:hasAPCPositivePercentage` | 5.00 | 3.44 |

**Y33W_P175F, V35F_R122L, Q161Y_C148K (expression not detected):**

| Field | Value (same structure for all three) |
|---|---|
| `rdfs:label` | e.g. "Y33W_P175F cell sorting — Bosch Lab (no expression)" |
| `rdfs:comment` | e.g. "Expression not detected in cell sorting assay. No APC+ve measurement obtained. Negative control: 10.3%. Positive control (wildtype RBD): 48.0%." |
| `mac:isObservationOf` | URI of corresponding Type 1 FDT |
| `mac:hasExperimentalMethod` | URI of Bosch Type 10 FDO |
| `mac:hasAPCPositivePercentage` | *(not present)* |

---

## Nanopub count

| Type | FDOs | Notes |
|---|---|---|
| 1 — Spike RBD Variant | 5 | One per double mutant |
| 7 — Cell Sorting Observation | 5 | 2 with APC+ve value, 3 without |
| 10 — Experimental Method (Bosch) | 1 | Shared library instance |
| 3–6 — Computational Predictions | 35 if available | Pending confirmation with StayAhead team |
| **Minimum (no comp. predictions)** | **11** | |
| **Maximum (with comp. predictions)** | **46** | |

---

## Open questions before implementation

| Question | Action |
|---|---|
| Computational predictions available for 5 double mutants? | Confirm with StayAhead team |
| Bosch method publication in preparation? | Confirm with Dr. Bosch |
| MAC seq_id notation for double mutants: Y33W_P175F or Y33W+P175F? | Confirm with MAC MFGG before minting |
