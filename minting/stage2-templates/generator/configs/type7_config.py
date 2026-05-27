"""Type 7 — Experimental Measurement — Deep Mutational Scanning.

Per SPS v1.3 §"Type 7": experimental binding affinity and expression
level measurements for a SARS-CoV-2 Spike RBD variant determined by
deep mutational scanning (Bloom Lab). One FDO per variant.

Six measured DMS values (bind, delta_bind, expr, delta_expr) plus two
confidence scores (confidence_bind, confidence_expr), all unitless;
each emitted as a mandatory statement.

Anchors via mac:isObservationOf to the Type 1 Spike RBD Variant FDO
and via mac:hasExperimentalMethod to the Bloom Lab DMS Method FDO
(Type 10).

Per SPS v1.3 §"Type 7", dct:source is [opt] repeatable — distinct
from Types 3-6 where dct:source is mandatory. Optional + repeatable
cito:citesAsAuthority for one-hop attribution remains.

includes_fair2 = False per SPS v1.3 §"FAIR² citation policy" for
Types 2-8.
"""

CONFIG = {
    "type_id": "type7",
    "type_label_short": "Type 7",
    "class_curie": "mac:ExperimentalDMSObservation",
    "includes_fair2": False,

    "template_label": "Declaring a Deep Mutational Scanning Observation (MAC FDT Type 7)",
    "template_description": (
        "Experimental binding affinity and expression level "
        "measurements for a SARS-CoV-2 Spike RBD variant determined "
        "by deep mutational scanning (Bloom Lab). One FDO per variant. "
        "Carries six measured values: bind (log KD, unitless), "
        "delta_bind (vs. wild-type), expr (log MFI, unitless), "
        "delta_expr, and confidence scores for bind and expr. Links "
        "via mac:isObservationOf to the variant FDO it observes and "
        "via mac:hasExperimentalMethod to the Bloom Lab DMS Method "
        "FDO (Type 10). The nanopublication self-materializes "
        "(assertion graph is the FDO)."
    ),
    "label_pattern": "DMS observation (bind=${bind}, expr=${expr})",

    "fdo_label_text": "full URI or short suffix for this DMS observation FDO",
    "label_placeholder_text": 'label for this observation (e.g. \\"Alpha DMS - Bloom Lab\\")',
    "description_placeholder_text": "free-text description of this DMS observation",

    "external_resource_labels": [
        ("http://purl.org/spar/cito/citesAsAuthority", "cites as authority"),
    ],

    "mac_term_labels": [
        ("mac:ExperimentalDMSObservation", "Experimental DMS Observation"),
        ("mac:isObservationOf",            "is observation of"),
        ("mac:hasExperimentalMethod",      "has experimental method"),
        ("mac:hasBind",                    "has bind (binding affinity, log KD, unitless)"),
        ("mac:hasDeltaBind",               "has delta_bind (vs. wild-type, unitless)"),
        ("mac:hasExpr",                    "has expr (expression level, log MFI, unitless)"),
        ("mac:hasDeltaExpr",               "has delta_expr (vs. wild-type, unitless)"),
        ("mac:hasConfidenceBind",          "has confidence_bind (unitless)"),
        ("mac:hasConfidenceExpr",          "has confidence_expr (unitless)"),
    ],

    "type_specific_statement_ids": [
        "sub:st_obs", "sub:st_em", "sub:st_oc",
        "sub:st_bi", "sub:st_db", "sub:st_ex", "sub:st_de",
        "sub:st_cb", "sub:st_ce",
        "sub:st_src",
    ],

    "placeholders": [
        {"id": "sub:variant", "types": ["nt:ExternalUriPlaceholder"],
         "label": "Spike RBD Variant FDO referent URI"},
        {"id": "sub:experimentalMethod", "types": ["nt:ExternalUriPlaceholder"],
         "label": "Experimental Method FDO referent URI (Type 10)"},
        {"id": "sub:authority", "types": ["nt:ExternalUriPlaceholder"],
         "label": "observation-specific authority (DOI or URL)"},
        {"id": "sub:source", "types": ["nt:ExternalUriPlaceholder"],
         "label": "FAIR² Package DOI, FAIR² resource URL, or OSF URL"},
        {"id": "sub:bind", "types": ["nt:LiteralPlaceholder"],
         "label": "bind (binding affinity, log KD, unitless)"},
        {"id": "sub:deltaBind", "types": ["nt:LiteralPlaceholder"],
         "label": "delta_bind (change vs. wild-type, unitless)"},
        {"id": "sub:expr", "types": ["nt:LiteralPlaceholder"],
         "label": "expr (expression level, log MFI, unitless)"},
        {"id": "sub:deltaExpr", "types": ["nt:LiteralPlaceholder"],
         "label": "delta_expr (change vs. wild-type, unitless)"},
        {"id": "sub:confidenceBind", "types": ["nt:LiteralPlaceholder"],
         "label": "confidence_bind (unitless)"},
        {"id": "sub:confidenceExpr", "types": ["nt:LiteralPlaceholder"],
         "label": "confidence_expr (unitless)"},
    ],

    "statements": [
        {"id": "sub:st_obs", "subject": "sub:fdo",
         "predicate": "mac:isObservationOf", "object": "sub:variant"},
        {"id": "sub:st_em", "subject": "sub:fdo",
         "predicate": "mac:hasExperimentalMethod", "object": "sub:experimentalMethod"},
        {"id": "sub:st_oc", "subject": "sub:fdo",
         "predicate": "<http://purl.org/spar/cito/citesAsAuthority>",
         "object": "sub:authority",
         "st_types": ["nt:OptionalStatement", "nt:RepeatableStatement"]},
        {"id": "sub:st_bi", "subject": "sub:fdo",
         "predicate": "mac:hasBind", "object": "sub:bind"},
        {"id": "sub:st_db", "subject": "sub:fdo",
         "predicate": "mac:hasDeltaBind", "object": "sub:deltaBind"},
        {"id": "sub:st_ex", "subject": "sub:fdo",
         "predicate": "mac:hasExpr", "object": "sub:expr"},
        {"id": "sub:st_de", "subject": "sub:fdo",
         "predicate": "mac:hasDeltaExpr", "object": "sub:deltaExpr"},
        {"id": "sub:st_cb", "subject": "sub:fdo",
         "predicate": "mac:hasConfidenceBind", "object": "sub:confidenceBind"},
        {"id": "sub:st_ce", "subject": "sub:fdo",
         "predicate": "mac:hasConfidenceExpr", "object": "sub:confidenceExpr"},
        # Distinct from Types 3-6: dct:source is OPTIONAL + repeatable per
        # SPS v1.3 §"Type 7".
        {"id": "sub:st_src", "subject": "sub:fdo",
         "predicate": "dct:source", "object": "sub:source",
         "st_types": ["nt:OptionalStatement", "nt:RepeatableStatement"]},
    ],
}
