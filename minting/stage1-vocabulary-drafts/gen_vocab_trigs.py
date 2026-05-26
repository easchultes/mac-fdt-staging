#!/usr/bin/env python3
"""Generate 45 draft TriG nanopub files (26 predicates + 19 classes)
for Stage 1 vocabulary review. Definitions taken verbatim from
specs/MAC_FDT_Vocabulary_v1_2.md.

v1.2 changes vs v1.1 (per Stage1_hierarchy_and_domain_range_proposal.md,
accepted by Tobias Kuhn on 2026-05-22):

  1. rdfs:isDefinedBy → dct:partOf (item 1 of Tobias's review)
  2. Five new abstract classes (Observation, ComputationalPrediction,
     ExperimentalObservation, Method, WHODesignation), bringing the
     class total to 19.
  3. rdfs:subClassOf triples on all classes per §1 hierarchy.
  4. rdfs:domain and rdfs:range triples on predicates per §2.
  5. Predicates with xsd:* range are emitted as owl:DatatypeProperty;
     predicates with class range or omitted range remain owl:ObjectProperty.
  6. Edge cases per proposal §3, all option 1 (omit):
     (a) hasGISAIDAccession: domain omitted (dual use).
     (b) hasParentProtein: range omitted (foreign UniProt URI).
     (c) hasCollectionLocation: range omitted (foreign GeoNames URI).
     (d) hasWHOClassificationReference: range omitted (generic URL).
     (e) hasOccurrenceDate: range is xsd:string (loose, admits imprecision).
  7. Slash separator in the mac: prefix expansion (item 4).

v1.2 namespace correction (2026-05-26, after first test-publish):
  The mac: prefix expands to https://w3id.org/spaces/mac/r/ontology/
  (slash-terminated). Terms are siblings of the MAC-Ontology resource
  in that namespace, NOT children — i.e. mac:hasWHOVariantName resolves
  to https://w3id.org/spaces/mac/r/ontology/hasWHOVariantName, and
  dct:partOf still targets https://w3id.org/spaces/mac/r/ontology/MAC-Ontology
  (renders as mac:MAC-Ontology after signing). The earlier draft that
  used …/MAC-Ontology/{local} was one path level too deep and was
  re-signed/re-published on 2026-05-26.

v2 (2026-05-26, after Tobias's review of the published v1 nanopubs):
  Two new pubinfo triples per nanopub, per Tobias's review:

    this: npx:introduces <term_uri> ;
          npx:supersedes <original_v1_Trusty_URI> .

  - `npx:introduces` names the class/property defined in this nanopub's
    assertion graph (the URI mac: expands to that local-name).
  - `npx:supersedes` links back to the v1 Trusty URI, loaded from
    minting/stage1-vocabulary-drafts/manifest_live.csv.

  v1's unsigned drafts and signed/ folder remain in place at
  stage1-vocabulary-drafts/. v2's unsigned drafts go to v2/ and
  signed v2 will go to v2/signed/, keeping the audit trail clean.
"""
import csv
import os
from datetime import datetime, timezone

TODAY = "2026-05-22"
# Pubinfo publication timestamp — current UTC at generation time, per
# nanopub-skill SKILL.md line 465: "Always get the current UTC time …
# for dct:created timestamps. … When updating a nanopub before
# publishing (e.g. after revisions), always refresh the timestamp."
PUB_TIMESTAMP = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
ORCID = "https://orcid.org/0000-0001-8888-635X"
ONTOLOGY_URI = "https://w3id.org/spaces/mac/r/ontology/MAC-Ontology"
STAGE1_DIR = "/Users/erikschultes/Desktop/mac-fdt-staging/minting/stage1-vocabulary-drafts"
# v2 outputs go to v2/ subfolder so v1 stays intact
OUT_DIR = f"{STAGE1_DIR}/v2"
# v1 manifest provides the originals that v2 supersedes
V1_MANIFEST_PATH = f"{STAGE1_DIR}/manifest_live.csv"

# ----------------------------------------------------------------------
# Predicates: (local, label, comment, domain, range, kind)
#   domain, range: None means omit the triple. Class names are mac:<local>;
#                  xsd datatypes carry the "xsd:" prefix.
#   kind: "object" → owl:ObjectProperty; "datatype" → owl:DatatypeProperty.
# ----------------------------------------------------------------------
PREDICATES = [
    # --- Type 1 identity predicates (domain = SpikeRBDVariant) ---
    ("hasWHOVariantName", "has WHO variant name",
     "Asserts the World Health Organization-assigned label for the SARS-CoV-2 lineage to which this RBD variant belongs. The WHO scheme uses Greek-letter labels (Alpha, Beta, …, Omicron) for lineages designated as Variant of Concern, Variant of Interest, or Variant Under Monitoring.",
     "SpikeRBDVariant", "xsd:string", "datatype"),
    ("hasPangoLineage", "has Pango lineage",
     "Asserts the Pango lineage designation for the SARS-CoV-2 lineage to which this RBD variant belongs. The Pango nomenclature provides a hierarchical lineage classification independent of WHO labelling.",
     "SpikeRBDVariant", "xsd:string", "datatype"),
    ("hasGISAIDSeqId", "has GISAID seq_id (full Spike mutation notation)",
     "Asserts the canonical amino-acid substitution notation, referenced to the full-length SARS-CoV-2 Spike protein numbering, that identifies the defining mutation of this variant as catalogued in GISAID surveillance records.",
     "SpikeRBDVariant", "xsd:string", "datatype"),
    ("hasMACSeqId", "has MAC seq_id (RBD mutation notation)",
     "Asserts the amino-acid substitution notation, referenced to the 195-residue Spike Receptor Binding Domain (RBD; UniProt P0DTC2 positions 331–525), that identifies the defining mutation of this variant in the MAC StayAhead RBD-focused pipelines. Differs from `mac:hasGISAIDSeqId` only in the residue numbering reference frame.",
     "SpikeRBDVariant", "xsd:string", "datatype"),
    ("hasParentProtein", "has parent protein",
     "Asserts the wild-type parent protein from which this RBD variant is derived by amino-acid substitution. In the present catalogue the value is hardcoded to the UniProt record for the Wuhan reference SARS-CoV-2 Spike glycoprotein.",
     "SpikeRBDVariant", None, "object"),
    ("hasRBDSequence", "has RBD amino acid sequence (195 residues, one-letter code)",
     "Asserts the complete amino-acid sequence of this RBD variant in one-letter code, 195 residues, corresponding to UniProt P0DTC2 positions 331–525 with the variant-defining substitution(s) applied.",
     "SpikeRBDVariant", "xsd:string", "datatype"),
    ("hasGISAIDAccession", "has GISAID accession number",
     "Asserts a GISAID EpiCoV accession identifier (format `EPI_ISL_XXXXXXX`) of a genome sequence relevant to this FDO. At the Type 1 (variant) level the value is the canonical exemplar sequence chosen to represent the variant; at the Type 2 (real-world occurrence) level the value is the specific surveilled sequence whose collection date and location are recorded by the observation.",
     None, "xsd:string", "datatype"),
    # --- Cross-type predicate ---
    ("isObservationOf", "is observation of",
     "Asserts that this observation FDO records a measured, predicted, or recorded property of the referent identified by the object URI. Used by Types 2–8 to link each observation to the central anchor FDO of the FAIR Digital Twin, making the anchor the hub of the knowlet topology. The object URI is the referent URI (i.e., the `sub:fdo` identifier declared by the anchor nanopublication), not the Trusty URI of the anchor itself.",
     "Observation", "SpikeRBDVariant", "object"),
    # --- Type 2 real-world occurrence ---
    ("hasSurveillanceMethod", "has surveillance method",
     "Asserts the surveillance system or observational platform through which this real-world occurrence was documented (e.g., the GISAID EpiCoV platform).",
     "RealWorldOccurrence", "ObservationalMethod", "object"),
    ("hasOccurrenceDate", "has occurrence date (GISAID reported collection date)",
     "Asserts the GISAID-reported collection date of the sample exemplifying this real-world occurrence. Where only a date range or month is known, the literal carries that imprecision explicitly.",
     "RealWorldOccurrence", "xsd:string", "datatype"),
    ("hasCollectionLocation", "has collection location",
     "Asserts the geographic location at which the sample exemplifying this real-world occurrence was collected. The value is a URI identifying a feature in the GeoNames gazetteer (https://www.geonames.org), of the form `https://sws.geonames.org/{geonameId}/`. The granularity (country, administrative subdivision, populated place) follows the granularity of the source surveillance record.",
     "RealWorldOccurrence", None, "object"),
    # --- Types 3–6 computational ---
    ("hasPredictionMethod", "has prediction method",
     "Asserts the computational method, tool, or algorithm that produced this prediction.",
     "ComputationalPrediction", "ComputationalMethod", "object"),
    ("hasRMSD", "has RMSD (Root Mean Square Deviation)",
     "Asserts the Root Mean Square Deviation between the predicted structure of this variant's RBD and a reference structure, measured as the average distance between corresponding atoms after optimal superposition.",
     "ComputationalPredictionRMSD", "xsd:decimal", "datatype"),
    ("hasSASA", "has SASA (Solvent Accessible Surface Area)",
     "Asserts the Solvent Accessible Surface Area of the predicted structure of this variant's RBD, computed as the surface area accessible to a standard solvent probe.",
     "ComputationalPredictionSASA", "xsd:decimal", "datatype"),
    ("haspLDDT", "has pLDDT score",
     "Asserts the predicted Local Distance Difference Test (pLDDT) score, a per-residue or aggregated confidence measure for the predicted protein structure, ranging from 0 (lowest confidence) to 100 (highest confidence). The aggregation convention (e.g., mean over residues) is specified by the predicting method's documentation.",
     "ComputationalPredictionPLDDT", "xsd:decimal", "datatype"),
    ("hasAgMataScore", "has AgMata score (aggregation propensity)",
     "Asserts the AgMata aggregation propensity score computed for this variant's sequence by the Bio2Byte toolkit, indicating predicted tendency to form protein aggregates.",
     "ComputationalPredictionAgMata", "xsd:decimal", "datatype"),
    # --- Type 7 experimental ---
    ("hasExperimentalMethod", "has experimental method",
     "Asserts the experimental method through which the measurements reported in this observation were obtained.",
     "ExperimentalObservation", "ExperimentalMethod", "object"),
    ("hasBind", "has bind (binding affinity)",
     "Asserts the binding affinity measurement for this variant's RBD interaction with its receptor (typically ACE2), reported on a logarithmic scale as −log(K_D). Higher values indicate stronger binding.",
     "ExperimentalDMSObservation", "xsd:decimal", "datatype"),
    ("hasDeltaBind", "has delta_bind (change in binding affinity)",
     "Asserts the change in binding affinity for this variant relative to the wild-type reference, computed as Δ(−log K_D). Positive values indicate stronger binding than wild-type.",
     "ExperimentalDMSObservation", "xsd:decimal", "datatype"),
    ("hasExpr", "has expr (expression level)",
     "Asserts the protein expression level measurement for this variant, reported as the logarithm of the mean fluorescence intensity (log MFI) from the deep mutational scanning assay.",
     "ExperimentalDMSObservation", "xsd:decimal", "datatype"),
    ("hasDeltaExpr", "has delta_expr (change in expression level)",
     "Asserts the change in expression level for this variant relative to the wild-type reference, computed as Δ(log MFI).",
     "ExperimentalDMSObservation", "xsd:decimal", "datatype"),
    ("hasConfidenceBind", "has confidence_bind (binding confidence score)",
     "Asserts the confidence score associated with the binding affinity measurement, as reported by the deep mutational scanning analysis pipeline. Higher values indicate higher reliability of the binding measurement.",
     "ExperimentalDMSObservation", "xsd:decimal", "datatype"),
    ("hasConfidenceExpr", "has confidence_expr (expression confidence score)",
     "Asserts the confidence score associated with the expression level measurement, as reported by the deep mutational scanning analysis pipeline.",
     "ExperimentalDMSObservation", "xsd:decimal", "datatype"),
    # --- Type 8 WHO classification ---
    ("hasWHOClassification", "has WHO variant classification",
     "Asserts the World Health Organization risk classification assigned to this variant at a given point in time: Variant of Concern (VOC), Variant of Interest (VOI), or Variant Under Monitoring (VUM). Time-stamped because designation status changes over time.",
     "WHOVariantClassification", "WHODesignation", "object"),
    ("hasClassificationDate", "has WHO classification date",
     "Asserts the date on which the WHO assigned this classification to the variant.",
     "WHOVariantClassification", "xsd:date", "datatype"),
    ("hasWHOClassificationReference", "has WHO classification reference URL",
     "Asserts the URL of the WHO publication or tracking page that documents this classification.",
     "WHOVariantClassification", None, "object"),
]

# ----------------------------------------------------------------------
# Classes: (local, label, comment, parent_local | None)
#   parent_local None ⇒ no rdfs:subClassOf triple (top-level abstract or
#   parentless anchor type).
# ----------------------------------------------------------------------
CLASSES = [
    # --- Anchor type (no parent) ---
    ("SpikeRBDVariant", "Spike RBD Variant",
     "A variant of the SARS-CoV-2 Spike receptor-binding domain (RBD, 195 residues) produced by one or more amino-acid substitutions from the wild-type Wuhan isolate (UniProt P0DTC2). This class is the type of the anchor FDO (A_r) of a FAIR Digital Twin; all observation FDOs link to it via `mac:isObservationOf` and collectively constitute the FDT.",
     None),
    # --- Observation hierarchy ---
    ("Observation", "Observation",
     "An abstract parent class for all observation-layer FDOs in a MAC FAIR Digital Twin. Concrete subclasses include `mac:RealWorldOccurrence` (Type 2), `mac:ComputationalPrediction` and its sub-hierarchy (Types 3–6), `mac:ExperimentalObservation` and its sub-hierarchy (Type 7), and `mac:WHOVariantClassification` (Type 8). Every member links to the FDT's anchor (a `mac:SpikeRBDVariant`) via `mac:isObservationOf`. This class is abstract: it carries no direct instances; all instances belong to one of its concrete subclasses.",
     None),
    ("RealWorldOccurrence", "Real-World Occurrence",
     "A documented detection of a SARS-CoV-2 Spike variant in the real world, as reported in a surveillance database (typically GISAID). The occurrence is anchored to a specific collection date and to a GeoNames-identified location.",
     "Observation"),
    ("ComputationalPrediction", "Computational Prediction",
     "An abstract parent class for computational predictions about a Spike RBD variant, produced by a named computational method. Concrete subclasses cover specific predicted quantities (`mac:ComputationalPredictionRMSD`, `…SASA`, `…PLDDT`, `…AgMata`). Anticipates additional computational prediction types as siblings without restructuring the hierarchy. This class is abstract: all instances belong to one of its concrete subclasses.",
     "Observation"),
    ("ComputationalPredictionRMSD", "Computational Prediction RMSD",
     "A computed prediction of the Root Mean Square Deviation between a predicted structure of a Spike RBD variant and a reference structure, produced by a named computational structure-prediction method.",
     "ComputationalPrediction"),
    ("ComputationalPredictionSASA", "Computational Prediction SASA",
     "A computed prediction of the Solvent Accessible Surface Area of a Spike RBD variant's predicted structure, produced by a named computational structure-prediction method.",
     "ComputationalPrediction"),
    ("ComputationalPredictionPLDDT", "Computational Prediction pLDDT",
     "A computed prediction confidence score (predicted Local Distance Difference Test) for the structural prediction of a Spike RBD variant, produced by a named computational structure-prediction method.",
     "ComputationalPrediction"),
    ("ComputationalPredictionAgMata", "Computational Prediction AgMata",
     "A computed prediction of the aggregation propensity of a Spike RBD variant, produced by the Bio2Byte AgMata method. The score is sequence-derived and is therefore predicted once per variant rather than once per structural-prediction method.",
     "ComputationalPrediction"),
    ("ExperimentalObservation", "Experimental Observation",
     "An abstract parent class for empirical observations produced by laboratory assays on a Spike RBD variant. Currently has one concrete child (`mac:ExperimentalDMSObservation`, deep mutational scanning); the forthcoming Bosch extension adds `mac:ExperimentalCellSortingObservation` as a sibling. This class is abstract: all instances belong to one of its concrete subclasses.",
     "Observation"),
    ("ExperimentalDMSObservation", "Experimental DMS Observation",
     "An experimental observation of binding affinity and expression level measurements for a Spike RBD variant, determined by deep mutational scanning (Bloom Lab protocol). One FDO records all six DMS metrics (`bind`, `delta_bind`, `expr`, `delta_expr`, `confidence_bind`, `confidence_expr`) for a single variant.",
     "ExperimentalObservation"),
    ("WHOVariantClassification", "WHO Variant Classification",
     "A classification of a SARS-CoV-2 lineage according to the WHO risk framework (VOC / VOI / VUM), with a specified assignment date and reference URL. Time-stamped because designation status changes over time.",
     "Observation"),
    # --- Method hierarchy ---
    ("Method", "Method",
     "An abstract parent class for methods, tools, assays, or surveillance platforms that produce observations within the MAC FAIR Digital Twin substrate. Concrete subclasses distinguish computational methods (`mac:ComputationalMethod`), experimental methods (`mac:ExperimentalMethod`), and observational/surveillance methods (`mac:ObservationalMethod`). Instances of any concrete subclass carry one or more `cito:citesAsAuthority` URIs identifying the published descriptions of the method. This class is abstract: all instances belong to one of its concrete subclasses.",
     None),
    ("ComputationalMethod", "Computational Method",
     "A computational method, tool, or algorithm that produces predictions or scores from biological sequence or structure data. Referenced by observation FDOs of Types 3–6 via `mac:hasPredictionMethod`. Instances carry one or more `cito:citesAsAuthority` URIs identifying the published descriptions of the method.",
     "Method"),
    ("ExperimentalMethod", "Experimental Method",
     "An experimental assay or measurement protocol that produces empirical observations about biological entities. Referenced by Type 7 observation FDOs via `mac:hasExperimentalMethod`. Instances carry one or more `cito:citesAsAuthority` URIs identifying the published descriptions of the assay.",
     "Method"),
    ("ObservationalMethod", "Observational Method",
     "An epidemiological surveillance system or data-collection platform through which real-world occurrences of biological entities are documented. Referenced by Type 2 observation FDOs via `mac:hasSurveillanceMethod`. Instances carry one or more `cito:citesAsAuthority` URIs identifying the published descriptions of the surveillance platform.",
     "Method"),
    # --- WHO Designation hierarchy ---
    ("WHODesignation", "WHO Designation",
     "An abstract parent class for the World Health Organization's controlled-vocabulary risk designations applied to SARS-CoV-2 variants: Variant of Concern (`mac:VOC`), Variant of Interest (`mac:VOI`), and Variant Under Monitoring (`mac:VUM`). Used as the range of `mac:hasWHOClassification`. This class is abstract: all instances belong to one of its concrete subclasses.",
     None),
    ("VOC", "Variant of Concern",
     "A SARS-CoV-2 variant designated by the WHO as carrying evidence of increased transmissibility, increased disease severity, or significant reduction in vaccine or therapeutic effectiveness.",
     "WHODesignation"),
    ("VOI", "Variant of Interest",
     "A SARS-CoV-2 variant designated by the WHO as carrying genetic markers associated with phenotypic changes and demonstrated epidemiological impact warranting enhanced monitoring.",
     "WHODesignation"),
    ("VUM", "Variant Under Monitoring",
     "A SARS-CoV-2 variant for which the WHO has identified evidence of growth advantage or immune escape and that is being monitored precautionarily pending further characterisation.",
     "WHODesignation"),
]

PREFIXES = """@prefix this: <http://purl.org/nanopub/temp/np001/> .
@prefix sub: <http://purl.org/nanopub/temp/np001/> .
@prefix np: <http://www.nanopub.org/nschema#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix npx: <http://purl.org/nanopub/x/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix orcid: <https://orcid.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix mac: <https://w3id.org/spaces/mac/r/ontology/> .

"""


def turtle_long_literal(s):
    """Emit a Turtle triple-quoted literal. The vocab definitions do not
    contain triple-quote sequences or literal backslashes, so a passthrough
    is safe; we still escape backslashes defensively."""
    return '"""' + s.replace("\\", "\\\\") + '"""'


def _range_term(rng):
    """Render a range term: xsd:* tokens pass through; class local names
    get the mac: prefix."""
    return rng if rng.startswith("xsd:") else f"mac:{rng}"


def load_v1_manifest():
    """Return {term_local_name: v1_trusty_uri} from manifest_live.csv."""
    mapping = {}
    with open(V1_MANIFEST_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            mapping[row["term_local_name"]] = row["trusty_uri"]
    return mapping


V1_TRUSTY = load_v1_manifest()


def make_predicate_trig(local, label, comment, domain, rng, kind):
    type_decl = "owl:DatatypeProperty" if kind == "datatype" else "owl:ObjectProperty"
    np_label = f"Vocabulary term: mac:{local}"
    # Build the assertion body as a list of "predicate object" pairs so we
    # can join with ` ;\n    ` and end with ` .`.
    pairs = [
        f"a {type_decl}",
        f'rdfs:label "{label}"',
        f"rdfs:comment {turtle_long_literal(comment)}",
    ]
    if domain is not None:
        pairs.append(f"rdfs:domain mac:{domain}")
    if rng is not None:
        pairs.append(f"rdfs:range {_range_term(rng)}")
    pairs.append(f"dct:partOf <{ONTOLOGY_URI}>")
    assertion_body = f"  mac:{local} " + " ;\n    ".join(pairs) + " .\n"
    return _wrap(assertion_body, np_label, local)


def make_class_trig(local, label, comment, parent):
    np_label = f"Vocabulary term: mac:{local}"
    pairs = [
        "a owl:Class",
        f'rdfs:label "{label}"',
        f"rdfs:comment {turtle_long_literal(comment)}",
    ]
    if parent is not None:
        pairs.append(f"rdfs:subClassOf mac:{parent}")
    pairs.append(f"dct:partOf <{ONTOLOGY_URI}>")
    assertion_body = f"  mac:{local} " + " ;\n    ".join(pairs) + " .\n"
    return _wrap(assertion_body, np_label, local)


def _wrap(assertion_body, np_label, term_local):
    v1_uri = V1_TRUSTY[term_local]
    return (
        PREFIXES
        + "sub:Head {\n"
        + "  this: a np:Nanopublication ;\n"
        + "    np:hasAssertion sub:assertion ;\n"
        + "    np:hasProvenance sub:provenance ;\n"
        + "    np:hasPublicationInfo sub:pubinfo .\n"
        + "}\n\n"
        + "sub:assertion {\n"
        + assertion_body
        + "}\n\n"
        + "sub:provenance {\n"
        + f"  sub:assertion prov:wasAttributedTo <{ORCID}> ;\n"
        + f"    dct:created \"{TODAY}\"^^xsd:date .\n"
        + "}\n\n"
        + "sub:pubinfo {\n"
        + f"  this: dct:created \"{PUB_TIMESTAMP}\"^^xsd:dateTime ;\n"
        + f"    dct:creator <{ORCID}> ;\n"
        + "    dct:license <https://creativecommons.org/licenses/by/4.0/> ;\n"
        + f"    rdfs:label \"{np_label}\" ;\n"
        + f"    npx:introduces mac:{term_local} ;\n"
        + f"    npx:supersedes <{v1_uri}> .\n"
        + "}\n"
    )


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    written = []
    for local, label, comment, domain, rng, kind in PREDICATES:
        path = f"{OUT_DIR}/predicate_{local}.trig"
        with open(path, "w", encoding="utf-8") as f:
            f.write(make_predicate_trig(local, label, comment, domain, rng, kind))
        written.append(path)
    for local, label, comment, parent in CLASSES:
        path = f"{OUT_DIR}/class_{local}.trig"
        with open(path, "w", encoding="utf-8") as f:
            f.write(make_class_trig(local, label, comment, parent))
        written.append(path)
    print(f"Wrote {len(written)} TriG files to {OUT_DIR}")
    print(f"  predicates: {len(PREDICATES)}")
    print(f"  classes:    {len(CLASSES)}")


if __name__ == "__main__":
    main()
