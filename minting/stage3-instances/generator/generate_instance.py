#!/usr/bin/env python3
"""Stage 3 instance generator — Type 1 (Spike RBD Variant).

Emits an instance nanopub conforming to the Type 1 template
(`https://w3id.org/np/RADOnITa1gjGIQtuENvlB2I7hykzrASzake1bIjGLiAtM`)
with concrete values substituted for placeholders. The instance:

  - Mints a local FDO referent URI `sub:<instance_id>` (e.g.
    sub:Alpha-RBD-Variant) — becomes
    `https://w3id.org/np/<TRUSTY>/<instance_id>` at sign time.
  - Carries all SPS v1.3 §"Type 1" mandatory statements with concrete
    literal / URI values.
  - Emits the 4-statement self-materialization block with `this:` as
    the subject (the nanopub itself materializes the FDO).
  - Declares institutional provenance via dct:isPartOf → the StayAhead
    Project FDO referent URI (mandatory per SPS v1.3).
  - Carries FAIR² cross-references (dct:references → article DOI,
    dct:source → package DOI) as fixed values per SPS v1.3.
  - Pubinfo carries nt:wasCreatedFromTemplate → live Type 1 template
    Trusty URI, plus the standard provenance/pubinfo template bundle.

Usage:
    python generate_instance.py instance_configs/type1_alpha.py > out.trig
    python generate_instance.py instance_configs/type1_alpha.py --out drafts/instance_type1_alpha_v1.trig
"""

import argparse
import importlib.util
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


# ============================================================
# Hardcoded values (per SPS v1.3 §"Type 1" + Stage 2 published assets)
# ============================================================

TYPE1_TEMPLATE_URI = "https://w3id.org/np/RADOnITa1gjGIQtuENvlB2I7hykzrASzake1bIjGLiAtM"
PROVENANCE_TEMPLATE_URI = "https://w3id.org/np/RA7lSq6MuK_TIC6JMSHvLtee3lpLoZDOqLJCLXevnrPoU"
PUBINFO_TEMPLATES = [
    "https://w3id.org/np/RA0J4vUn_dekg-U1kK3AOEt02p9mT2WO03uGxLDec1jLw",  # License
    "https://w3id.org/np/RAukAcWHRDlkqxk7H2XNSegc1WnHI569INvNr-xdptDGI",  # Creator
    "https://w3id.org/np/RAMEgudZsQ1bh1fZhfYnkthqH6YSXpghSE_DEN1I-6eAI",  # Hand-coded
    "https://w3id.org/np/RARW4MsFkHuwjycNElvEVtuMjpf4yWDL10-0C5l2MqqRQ",  # Derived
]

# Stage 3 Type 1 fixed values per SPS v1.3
PARENT_PROTEIN_URI = "https://www.uniprot.org/uniprot/P0DTC2"
STAYAHEAD_PROJECT_FDO = "https://w3id.org/np/RAFPOe4OIl_urs-U_7-FostjzcUo8ra6LasfSvGplOvto/StayAhead-Project"
FAIR2_ARTICLE_DOI = "https://doi.org/10.3389/fbinf.2025.1634111"
FAIR2_PACKAGE_DOI = "https://doi.org/10.71728/hw56-vj34"
CC_BY_4 = "https://creativecommons.org/licenses/by/4.0/"
TRIG_MEDIA_TYPE = "https://www.iana.org/assignments/media-types/application/trig"

# Validation patterns from SPS v1.3 Type 1 placeholders
MAC_SEQ_ID_REGEX = re.compile(r"^[ACDEFGHIKLMNPQRSTVWY]\d{1,3}[ACDEFGHIKLMNPQRSTVWY]$")
GISAID_ACCESSION_REGEX = re.compile(r"^EPI_ISL_\d+$")
RBD_SEQUENCE_LENGTH = 195
RBD_SEQUENCE_REGEX = re.compile(r"^[ACDEFGHIKLMNPQRSTVWY]+$")


# ============================================================
# Template strings
# ============================================================

PREFIXES_AND_HEAD = """\
@prefix this: <http://purl.org/nanopub/temp/np001/> .
@prefix sub: <http://purl.org/nanopub/temp/np001/> .
@prefix np: <http://www.nanopub.org/nschema#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix nt: <https://w3id.org/np/o/ntemplate/> .
@prefix npx: <http://purl.org/nanopub/x/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix orcid: <https://orcid.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix mac: <https://w3id.org/spaces/mac/r/ontology/> .

sub:Head {
  this: a np:Nanopublication ;
    np:hasAssertion sub:assertion ;
    np:hasProvenance sub:provenance ;
    np:hasPublicationInfo sub:pubinfo .
}
"""

# `fdof:` and `dcat:` are not declared in the header (matching the Type 1
# template scaffold); their predicates appear as full URIs below.
ASSERTION = """\

sub:assertion {{
  sub:{instance_id} a <https://w3id.org/fdof/ontology#FAIRDigitalObject>, mac:SpikeRBDVariant ;
    <https://w3id.org/fdof/ontology#hasMetadata> this: ;
    rdfs:label "{instance_label}" ;
    rdfs:comment "{instance_description}" ;
    dct:creator orcid:{creator_orcid} ;
    <https://www.w3.org/ns/dcat#contactPoint> "{contact_email}" ;
    dct:publisher <{publisher_ror}> ;
    dct:isPartOf <{project_fdo}> ;
    mac:hasWHOVariantName "{who_variant_name}" ;
    mac:hasPangoLineage "{pango_lineage}" ;
    mac:hasGISAIDSeqId "{gisaid_seq_id}" ;
    mac:hasMACSeqId "{mac_seq_id}" ;
    mac:hasParentProtein <{parent_protein}> ;
    mac:hasRBDSequence "{rbd_sequence}" ;
    mac:hasGISAIDAccession "{gisaid_accession}" ;
    dct:references <{fair2_article}> ;
    dct:source <{fair2_package}> .

  this: <https://w3id.org/fdof/ontology#materializes> sub:{instance_id} ;
    <https://w3id.org/fdof/ontology#hasEncodingFormat> <{trig_media_type}> ;
    dct:license <{license}> ;
    <https://www.w3.org/ns/dcat#accessURL> this: .
}}
"""

PROVENANCE = """\

sub:provenance {{
  sub:assertion prov:wasAttributedTo orcid:{creator_orcid} .
}}
"""

PUBINFO = """\

sub:pubinfo {{
  this: dct:created "{created}"^^xsd:dateTime ;
    dct:creator orcid:{creator_orcid} ;
    dct:license <{license}> ;
    rdfs:label "{instance_label}" ;
    npx:introduces sub:{instance_id} ;
    nt:wasCreatedFromTemplate <{template_uri}> ;
    nt:wasCreatedFromProvenanceTemplate <{provenance_template_uri}> ;
    nt:wasCreatedFromPubinfoTemplate
      <{pubinfo_template_1}>,
      <{pubinfo_template_2}>,
      <{pubinfo_template_3}>,
      <{pubinfo_template_4}> .
}}
"""


# ============================================================
# Validation
# ============================================================

MANDATORY_PREDICATES = [
    # FDO-statement predicates
    "rdf:type fdof:FAIRDigitalObject",
    "rdf:type mac:SpikeRBDVariant",
    "fdof:hasMetadata",
    "rdfs:label",
    "dct:creator",
    "dcat:contactPoint",
    "dct:publisher",
    "dct:isPartOf",
    "mac:hasWHOVariantName",
    "mac:hasPangoLineage",
    "mac:hasGISAIDSeqId",
    "mac:hasMACSeqId",
    "mac:hasParentProtein",
    "mac:hasRBDSequence",
    "dct:references",
    "dct:source",
    # Self-materialization block (4 statements; this: as subject)
    "fdof:materializes",
    "fdof:hasEncodingFormat",
    "dct:license",
    "dcat:accessURL",
]


def validate_config(config: dict) -> list:
    """Return a list of validation errors (empty = clean)."""
    errors = []

    # RBD sequence: exactly 195 chars, one-letter amino acid alphabet
    seq = config.get("rbd_sequence", "")
    if len(seq) != RBD_SEQUENCE_LENGTH:
        errors.append(f"rbd_sequence length is {len(seq)}, expected {RBD_SEQUENCE_LENGTH}")
    if not RBD_SEQUENCE_REGEX.match(seq):
        errors.append("rbd_sequence contains non-amino-acid characters")

    # MAC seq_id regex
    mac_id = config.get("mac_seq_id", "")
    if not MAC_SEQ_ID_REGEX.match(mac_id):
        errors.append(f"mac_seq_id {mac_id!r} does not match {MAC_SEQ_ID_REGEX.pattern}")

    # GISAID accession regex (if present)
    if "gisaid_accession" in config:
        acc = config["gisaid_accession"]
        if not GISAID_ACCESSION_REGEX.match(acc):
            errors.append(f"gisaid_accession {acc!r} does not match {GISAID_ACCESSION_REGEX.pattern}")

    # Required keys
    required = [
        "instance_id", "instance_label", "instance_description",
        "who_variant_name", "pango_lineage", "gisaid_seq_id", "mac_seq_id",
        "rbd_sequence", "gisaid_accession",
        "creator_orcid", "contact_email", "publisher_ror",
    ]
    for key in required:
        if key not in config or config[key] in (None, ""):
            errors.append(f"missing required config key: {key}")

    return errors


def check_mandatory_statements(trig_text: str) -> list:
    """Return list of missing mandatory-statement markers."""
    missing = []
    markers = {
        "rdf:type fdof:FAIRDigitalObject": r"<https://w3id\.org/fdof/ontology#FAIRDigitalObject>",
        "rdf:type mac:SpikeRBDVariant":   r"mac:SpikeRBDVariant",
        "fdof:hasMetadata":               r"<https://w3id\.org/fdof/ontology#hasMetadata>",
        "rdfs:label":                     r"rdfs:label",
        "rdfs:comment":                   r"rdfs:comment",
        "dct:creator":                    r"dct:creator",
        "dcat:contactPoint":              r"<https://www\.w3\.org/ns/dcat#contactPoint>",
        "dct:publisher":                  r"dct:publisher",
        "dct:isPartOf":                   r"dct:isPartOf",
        "mac:hasWHOVariantName":          r"mac:hasWHOVariantName",
        "mac:hasPangoLineage":            r"mac:hasPangoLineage",
        "mac:hasGISAIDSeqId":             r"mac:hasGISAIDSeqId",
        "mac:hasMACSeqId":                r"mac:hasMACSeqId",
        "mac:hasParentProtein":           r"mac:hasParentProtein",
        "mac:hasRBDSequence":             r"mac:hasRBDSequence",
        "mac:hasGISAIDAccession":         r"mac:hasGISAIDAccession",  # opt but expected
        "dct:references":                 r"dct:references",
        "dct:source":                     r"dct:source",
        "fdof:materializes":              r"<https://w3id\.org/fdof/ontology#materializes>",
        "fdof:hasEncodingFormat":         r"<https://w3id\.org/fdof/ontology#hasEncodingFormat>",
        "dct:license":                    r"dct:license",
        "dcat:accessURL":                 r"<https://www\.w3\.org/ns/dcat#accessURL>",
    }
    for name, pattern in markers.items():
        if not re.search(pattern, trig_text):
            missing.append(name)
    return missing


# ============================================================
# Method-instance template (Types 9 / 10 / 11)
# ============================================================

# `cito:` and `schema:` prefixes are NOT declared in PREFIXES_AND_HEAD
# (matching the Stage 2 method-template scaffold convention). Both
# predicates appear as full URIs below. Multiple cito:citesAsAuthority
# values are emitted as a Turtle comma-separated object list.
METHOD_ASSERTION = """\

sub:assertion {{
  sub:{instance_id} a <https://w3id.org/fdof/ontology#FAIRDigitalObject>, {class_curie} ;
    <https://w3id.org/fdof/ontology#hasMetadata> this: ;
    rdfs:label "{instance_label}" ;
    rdfs:comment "{instance_description}" ;
    dct:creator orcid:{creator_orcid} ;
    <https://www.w3.org/ns/dcat#contactPoint> "{contact_email}" ;
    dct:publisher <{publisher_ror}> ;
    dct:isPartOf <{project_fdo}> ;
    <http://purl.org/spar/cito/citesAsAuthority> {authorities} ;
    <http://schema.org/url> <{url}> .

  this: <https://w3id.org/fdof/ontology#materializes> sub:{instance_id} ;
    <https://w3id.org/fdof/ontology#hasEncodingFormat> <{trig_media_type}> ;
    dct:license <{license}> ;
    <https://www.w3.org/ns/dcat#accessURL> this: .
}}
"""


def validate_method_config(config: dict) -> list:
    errors = []
    required = [
        "instance_id", "instance_label", "instance_description",
        "class_curie", "template_uri", "authorities", "url",
        "creator_orcid", "contact_email", "publisher_ror",
    ]
    for key in required:
        if key not in config or config[key] in (None, "", []):
            errors.append(f"missing required config key: {key}")
    if "authorities" in config:
        if not isinstance(config["authorities"], list) or len(config["authorities"]) < 1:
            errors.append("authorities must be a non-empty list (mandatory + repeatable cito:citesAsAuthority)")
    if "class_curie" in config:
        if not config["class_curie"].startswith("mac:"):
            errors.append(f"class_curie should be a mac:* curie, got {config['class_curie']!r}")
    return errors


def check_mandatory_method_statements(trig_text: str, class_curie: str) -> dict:
    """Return {'missing': [...], 'forbidden_present': [...]}."""
    missing = []
    required = {
        "rdf:type fdof:FAIRDigitalObject": r"<https://w3id\.org/fdof/ontology#FAIRDigitalObject>",
        f"rdf:type {class_curie}":          re.escape(class_curie),
        "fdof:hasMetadata":                  r"<https://w3id\.org/fdof/ontology#hasMetadata>",
        "rdfs:label":                        r"rdfs:label",
        "dct:creator":                       r"dct:creator",
        "dcat:contactPoint":                 r"<https://www\.w3\.org/ns/dcat#contactPoint>",
        "dct:publisher":                     r"dct:publisher",
        "dct:isPartOf":                      r"dct:isPartOf",
        "cito:citesAsAuthority":             r"<http://purl\.org/spar/cito/citesAsAuthority>",
        "fdof:materializes":                 r"<https://w3id\.org/fdof/ontology#materializes>",
        "fdof:hasEncodingFormat":            r"<https://w3id\.org/fdof/ontology#hasEncodingFormat>",
        "dct:license":                       r"dct:license",
        "dcat:accessURL":                    r"<https://www\.w3\.org/ns/dcat#accessURL>",
    }
    for name, pattern in required.items():
        if not re.search(pattern, trig_text):
            missing.append(name)

    forbidden = {
        "mac:isObservationOf": r"mac:isObservationOf",
        "dct:source":           r"dct:source",
        "dct:references":       r"dct:references",
    }
    forbidden_present = [name for name, pattern in forbidden.items()
                         if re.search(pattern, trig_text)]
    return {"missing": missing, "forbidden_present": forbidden_present}


def generate_method_instance(config: dict, created: str) -> str:
    authorities_turtle = ", ".join(f"<{a}>" for a in config["authorities"])
    return (
        PREFIXES_AND_HEAD
        + METHOD_ASSERTION.format(
            instance_id=config["instance_id"],
            class_curie=config["class_curie"],
            instance_label=config["instance_label"],
            instance_description=config["instance_description"],
            creator_orcid=config["creator_orcid"],
            contact_email=config["contact_email"],
            publisher_ror=config["publisher_ror"],
            project_fdo=STAYAHEAD_PROJECT_FDO,
            authorities=authorities_turtle,
            url=config["url"],
            trig_media_type=TRIG_MEDIA_TYPE,
            license=CC_BY_4,
        )
        + PROVENANCE.format(creator_orcid=config["creator_orcid"])
        + PUBINFO.format(
            created=created,
            creator_orcid=config["creator_orcid"],
            license=CC_BY_4,
            instance_label=config["instance_label"],
            instance_id=config["instance_id"],
            template_uri=config["template_uri"],
            provenance_template_uri=PROVENANCE_TEMPLATE_URI,
            pubinfo_template_1=PUBINFO_TEMPLATES[0],
            pubinfo_template_2=PUBINFO_TEMPLATES[1],
            pubinfo_template_3=PUBINFO_TEMPLATES[2],
            pubinfo_template_4=PUBINFO_TEMPLATES[3],
        )
    )


# ============================================================
# Prediction-instance template (Types 3 / 4 / 5)
# ============================================================

# Like the method-instance template, `cito:` and `schema:` predicates
# do not appear here (the user's spec for this batch says no
# cito:citesAsAuthority, deferred to a later round). dct:source is
# emitted as a Turtle comma-separated object list (mandatory +
# repeatable; SPS v1.3 §"Source URLs" for Types 3-6).
PREDICTION_ASSERTION = """\

sub:assertion {{
  sub:{instance_id} a <https://w3id.org/fdof/ontology#FAIRDigitalObject>, {class_curie} ;
    <https://w3id.org/fdof/ontology#hasMetadata> this: ;
    rdfs:label "{instance_label}" ;
    rdfs:comment "{instance_description}" ;
    dct:creator orcid:{creator_orcid} ;
    <https://www.w3.org/ns/dcat#contactPoint> "{contact_email}" ;
    dct:publisher <{publisher_ror}> ;
    dct:isPartOf <{project_fdo}> ;
    mac:isObservationOf <{variant_fdo}> ;
    mac:hasPredictionMethod <{method_fdo}> ;
    {metric_predicate} {metric_value} ;
    dct:source {sources} .

  this: <https://w3id.org/fdof/ontology#materializes> sub:{instance_id} ;
    <https://w3id.org/fdof/ontology#hasEncodingFormat> <{trig_media_type}> ;
    dct:license <{license}> ;
    <https://www.w3.org/ns/dcat#accessURL> this: .
}}
"""


def validate_prediction_config(config: dict) -> list:
    errors = []
    required = [
        "instance_id", "instance_label", "instance_description",
        "class_curie", "template_uri",
        "variant_fdo", "method_fdo",
        "metric_predicate", "metric_value",
        "sources",
        "creator_orcid", "contact_email", "publisher_ror",
    ]
    for key in required:
        if key not in config or config[key] in (None, "", []):
            errors.append(f"missing required config key: {key}")
    if "sources" in config and isinstance(config["sources"], list):
        if len(config["sources"]) < 1:
            errors.append("sources must contain at least one URI (mandatory + repeatable dct:source)")
    if "class_curie" in config and not config["class_curie"].startswith("mac:"):
        errors.append(f"class_curie should be a mac:* curie, got {config['class_curie']!r}")
    if "metric_predicate" in config and not config["metric_predicate"].startswith("mac:"):
        errors.append(f"metric_predicate should be a mac:* curie, got {config['metric_predicate']!r}")
    return errors


def check_mandatory_prediction_statements(trig_text: str, class_curie: str, metric_predicate: str) -> dict:
    missing = []
    required = {
        "rdf:type fdof:FAIRDigitalObject": r"<https://w3id\.org/fdof/ontology#FAIRDigitalObject>",
        f"rdf:type {class_curie}":          re.escape(class_curie),
        "fdof:hasMetadata":                  r"<https://w3id\.org/fdof/ontology#hasMetadata>",
        "rdfs:label":                        r"rdfs:label",
        "dct:creator":                       r"dct:creator",
        "dcat:contactPoint":                 r"<https://www\.w3\.org/ns/dcat#contactPoint>",
        "dct:publisher":                     r"dct:publisher",
        "dct:isPartOf":                      r"dct:isPartOf",
        "mac:isObservationOf":               r"mac:isObservationOf",
        "mac:hasPredictionMethod":           r"mac:hasPredictionMethod",
        f"metric predicate {metric_predicate}": re.escape(metric_predicate),
        "dct:source":                        r"dct:source",
        "fdof:materializes":                 r"<https://w3id\.org/fdof/ontology#materializes>",
        "fdof:hasEncodingFormat":            r"<https://w3id\.org/fdof/ontology#hasEncodingFormat>",
        "dct:license":                       r"dct:license",
        "dcat:accessURL":                    r"<https://www\.w3\.org/ns/dcat#accessURL>",
    }
    for name, pattern in required.items():
        if not re.search(pattern, trig_text):
            missing.append(name)
    forbidden = {
        "cito:citesAsAuthority":  r"citesAsAuthority",
        "dct:references":          r"dct:references",
    }
    forbidden_present = [name for name, pattern in forbidden.items()
                         if re.search(pattern, trig_text)]
    return {"missing": missing, "forbidden_present": forbidden_present}


def generate_prediction_instance(config: dict, created: str) -> str:
    sources_turtle = ", ".join(f"<{s}>" for s in config["sources"])
    return (
        PREFIXES_AND_HEAD
        + PREDICTION_ASSERTION.format(
            instance_id=config["instance_id"],
            class_curie=config["class_curie"],
            instance_label=config["instance_label"],
            instance_description=config["instance_description"],
            creator_orcid=config["creator_orcid"],
            contact_email=config["contact_email"],
            publisher_ror=config["publisher_ror"],
            project_fdo=STAYAHEAD_PROJECT_FDO,
            variant_fdo=config["variant_fdo"],
            method_fdo=config["method_fdo"],
            metric_predicate=config["metric_predicate"],
            metric_value=config["metric_value"],
            sources=sources_turtle,
            trig_media_type=TRIG_MEDIA_TYPE,
            license=CC_BY_4,
        )
        + PROVENANCE.format(creator_orcid=config["creator_orcid"])
        + PUBINFO.format(
            created=created,
            creator_orcid=config["creator_orcid"],
            license=CC_BY_4,
            instance_label=config["instance_label"],
            instance_id=config["instance_id"],
            template_uri=config["template_uri"],
            provenance_template_uri=PROVENANCE_TEMPLATE_URI,
            pubinfo_template_1=PUBINFO_TEMPLATES[0],
            pubinfo_template_2=PUBINFO_TEMPLATES[1],
            pubinfo_template_3=PUBINFO_TEMPLATES[2],
            pubinfo_template_4=PUBINFO_TEMPLATES[3],
        )
    )


# ============================================================
# Generation (Type 1)
# ============================================================

def generate(config: dict, created: str) -> str:
    return (
        PREFIXES_AND_HEAD
        + ASSERTION.format(
            instance_id=config["instance_id"],
            instance_label=config["instance_label"],
            instance_description=config["instance_description"],
            creator_orcid=config["creator_orcid"],
            contact_email=config["contact_email"],
            publisher_ror=config["publisher_ror"],
            project_fdo=STAYAHEAD_PROJECT_FDO,
            who_variant_name=config["who_variant_name"],
            pango_lineage=config["pango_lineage"],
            gisaid_seq_id=config["gisaid_seq_id"],
            mac_seq_id=config["mac_seq_id"],
            parent_protein=PARENT_PROTEIN_URI,
            rbd_sequence=config["rbd_sequence"],
            gisaid_accession=config["gisaid_accession"],
            fair2_article=FAIR2_ARTICLE_DOI,
            fair2_package=FAIR2_PACKAGE_DOI,
            trig_media_type=TRIG_MEDIA_TYPE,
            license=CC_BY_4,
        )
        + PROVENANCE.format(creator_orcid=config["creator_orcid"])
        + PUBINFO.format(
            created=created,
            creator_orcid=config["creator_orcid"],
            license=CC_BY_4,
            instance_label=config["instance_label"],
            instance_id=config["instance_id"],
            template_uri=TYPE1_TEMPLATE_URI,
            provenance_template_uri=PROVENANCE_TEMPLATE_URI,
            pubinfo_template_1=PUBINFO_TEMPLATES[0],
            pubinfo_template_2=PUBINFO_TEMPLATES[1],
            pubinfo_template_3=PUBINFO_TEMPLATES[2],
            pubinfo_template_4=PUBINFO_TEMPLATES[3],
        )
    )


# ============================================================
# CLI
# ============================================================

def load_config(path: Path) -> dict:
    spec = importlib.util.spec_from_file_location("instance_config", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.CONFIG


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("config", type=Path)
    ap.add_argument("--out", type=Path, help="Write to this path instead of stdout.")
    ap.add_argument("--created", default=None, help="Override dct:created (default: now UTC).")
    args = ap.parse_args()

    config = load_config(args.config)
    kind = config.get("kind", "type1")

    created = args.created or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    if kind == "method":
        errors = validate_method_config(config)
        if errors:
            sys.stderr.write("Config validation errors:\n")
            for e in errors:
                sys.stderr.write(f"  - {e}\n")
            return 1
        output = generate_method_instance(config, created)
        result = check_mandatory_method_statements(output, config["class_curie"])
        if result["missing"]:
            sys.stderr.write("Mandatory method statements missing in generated TriG:\n")
            for m in result["missing"]:
                sys.stderr.write(f"  - {m}\n")
            return 1
        if result["forbidden_present"]:
            sys.stderr.write("Forbidden statements present (method instances must not carry these):\n")
            for f in result["forbidden_present"]:
                sys.stderr.write(f"  - {f}\n")
            return 1
        ok_note = (f"OK: wrote {args.out} ({len(output)} bytes, method instance "
                   f"({config['class_curie']}), {len(config['authorities'])} authority/-ies, "
                   f"mandatory statements all present, forbidden statements absent)\n")
    elif kind == "prediction":
        errors = validate_prediction_config(config)
        if errors:
            sys.stderr.write("Config validation errors:\n")
            for e in errors:
                sys.stderr.write(f"  - {e}\n")
            return 1
        output = generate_prediction_instance(config, created)
        result = check_mandatory_prediction_statements(
            output, config["class_curie"], config["metric_predicate"])
        if result["missing"]:
            sys.stderr.write("Mandatory prediction statements missing in generated TriG:\n")
            for m in result["missing"]:
                sys.stderr.write(f"  - {m}\n")
            return 1
        if result["forbidden_present"]:
            sys.stderr.write("Forbidden statements present (prediction instances must not carry these):\n")
            for f in result["forbidden_present"]:
                sys.stderr.write(f"  - {f}\n")
            return 1
        ok_note = (f"OK: wrote {args.out} ({len(output)} bytes, prediction instance "
                   f"({config['class_curie']}, {config['metric_predicate']}={config['metric_value']}), "
                   f"{len(config['sources'])} source(s), mandatory statements all present, "
                   f"forbidden statements absent)\n")
    else:
        errors = validate_config(config)
        if errors:
            sys.stderr.write("Config validation errors:\n")
            for e in errors:
                sys.stderr.write(f"  - {e}\n")
            return 1
        output = generate(config, created)
        missing = check_mandatory_statements(output)
        if missing:
            sys.stderr.write("Mandatory statements missing in generated TriG:\n")
            for m in missing:
                sys.stderr.write(f"  - {m}\n")
            return 1
        ok_note = (f"OK: wrote {args.out} ({len(output)} bytes, "
                   f"RBD seq len {len(config['rbd_sequence'])}, "
                   f"mandatory statements all present)\n")

    if args.out:
        args.out.write_text(output)
        sys.stderr.write(ok_note)
    else:
        sys.stdout.write(output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
