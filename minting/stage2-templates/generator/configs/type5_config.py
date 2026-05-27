"""Type 5 — Computational Prediction — pLDDT.

Per SPS v1.3 §"Types 3-6": prediction of the per-residue confidence
score (pLDDT, unitless, 0-100) of a SARS-CoV-2 Spike RBD variant
structure, produced by a named computational method (typically
AlphaFold II). One FDO per (variant × method) pair.

Structurally identical to Type 3 and Type 4; differs only in class URI,
metric predicate (mac:haspLDDT — note lowercase 'p'), units (unitless),
and label pattern. See type3_config.py for SPS v1.3 conformance commentary.
"""

CONFIG = {
    "type_id": "type5",
    "type_label_short": "Type 5",
    "class_curie": "mac:ComputationalPredictionPLDDT",
    "includes_fair2": False,

    "template_label": "Declaring a Computational Prediction — pLDDT (MAC FDT Type 5)",
    "template_description": (
        "Computational prediction of the per-residue confidence score "
        "(pLDDT, unitless, 0-100) of a SARS-CoV-2 Spike RBD variant "
        "structure, produced by a named computational method "
        "(typically AlphaFold II). Links via mac:isObservationOf to "
        "the variant FDO it observes and via mac:hasPredictionMethod "
        "to the Type 9 method FDO. The nanopublication "
        "self-materializes (assertion graph is the FDO)."
    ),
    "label_pattern": "pLDDT = ${value} (${predictionMethod})",

    "fdo_label_text": "full URI or short suffix for this pLDDT observation FDO",
    "label_placeholder_text": 'label for this observation (e.g. \\"Alpha pLDDT - AlphaFold II\\")',
    "description_placeholder_text": "free-text description of this pLDDT observation",

    "external_resource_labels": [
        ("http://purl.org/spar/cito/citesAsAuthority", "cites as authority"),
    ],

    "mac_term_labels": [
        ("mac:ComputationalPredictionPLDDT", "Computational Prediction — pLDDT"),
        ("mac:isObservationOf",              "is observation of"),
        ("mac:hasPredictionMethod",          "has prediction method"),
        ("mac:haspLDDT",                     "has pLDDT score (0-100, unitless)"),
    ],

    "type_specific_statement_ids": [
        "sub:st_obs", "sub:st_pm", "sub:st_oc",
        "sub:st_val", "sub:st_src",
    ],

    "placeholders": [
        {"id": "sub:variant", "types": ["nt:ExternalUriPlaceholder"],
         "label": "Spike RBD Variant FDO referent URI"},
        {"id": "sub:predictionMethod", "types": ["nt:ExternalUriPlaceholder"],
         "label": "Computational Method FDO referent URI (Type 9)"},
        {"id": "sub:authority", "types": ["nt:ExternalUriPlaceholder"],
         "label": "observation-specific authority (DOI or URL)"},
        {"id": "sub:source", "types": ["nt:ExternalUriPlaceholder"],
         "label": "FAIR² Package DOI or FAIR² resource URL or OSF URL"},
        {"id": "sub:value", "types": ["nt:LiteralPlaceholder"],
         "label": "pLDDT score (0-100, unitless)"},
    ],

    "statements": [
        {"id": "sub:st_obs", "subject": "sub:fdo",
         "predicate": "mac:isObservationOf", "object": "sub:variant"},
        {"id": "sub:st_pm", "subject": "sub:fdo",
         "predicate": "mac:hasPredictionMethod", "object": "sub:predictionMethod"},
        {"id": "sub:st_oc", "subject": "sub:fdo",
         "predicate": "<http://purl.org/spar/cito/citesAsAuthority>",
         "object": "sub:authority",
         "st_types": ["nt:OptionalStatement", "nt:RepeatableStatement"]},
        {"id": "sub:st_val", "subject": "sub:fdo",
         "predicate": "mac:haspLDDT", "object": "sub:value"},
        {"id": "sub:st_src", "subject": "sub:fdo",
         "predicate": "dct:source", "object": "sub:source",
         "st_types": ["nt:RepeatableStatement"]},
    ],
}
