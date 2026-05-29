"""Type 3 — Computational Prediction — RMSD.

Per SPS v1.3 §"Types 3-6": prediction of the Root Mean Square Deviation
(RMSD, in Angstroms) of a SARS-CoV-2 Spike RBD variant relative to the
wild-type structure, produced by a named computational method
(e.g. ESM, AlphaFold II). One FDO per (variant × method) pair.

Anchors via mac:isObservationOf to the Type 1 Spike RBD Variant FDO and
via mac:hasPredictionMethod to the Type 9 Computational Method FDO.

Per SPS v1.3 §"FAIR² citation policy", Type 3 omits the fixed FAIR²
pair (includes_fair2=False) and emits dct:source per-observation
(mandatory + repeatable) — the source can be the FAIR² Package DOI,
the FAIR² resource URL, or an OSF URL — plus the optional + repeatable
cito:citesAsAuthority for one-hop attribution.
"""

CONFIG = {
    "type_id": "type3",
    "type_label_short": "Type 3",
    "class_curie": "mac:ComputationalPredictionRMSD",
    "includes_fair2": False,

    "template_label": "Declaring a Computational Prediction — RMSD (MAC FDT Type 3)",
    "template_description": (
        "Computational prediction of the Root Mean Square Deviation "
        "(RMSD, in Angstroms) of a SARS-CoV-2 Spike RBD variant "
        "relative to the wild-type structure, produced by a named "
        "computational method (e.g., ESM, AlphaFold II). Links via "
        "mac:isObservationOf to the variant FDO it observes and via "
        "mac:hasPredictionMethod to the Type 9 method FDO. The "
        "nanopublication self-materializes (assertion graph is the FDO)."
    ),
    "label_pattern": "RMSD = ${value} A (${predictionMethod})",

    "fdo_label_text": "full URI or short suffix for this RMSD observation FDO",
    "label_placeholder_text": 'label for this observation (e.g. \\"Alpha RMSD - AlphaFold II\\")',
    "description_placeholder_text": "free-text description of this RMSD observation",

    # cito: not in common @prefix; emit as full URI external-resource label.
    "external_resource_labels": [
        ("http://purl.org/spar/cito/citesAsAuthority", "cites as authority"),
    ],

    "mac_term_labels": [
        ("mac:ComputationalPredictionRMSD", "Computational Prediction — RMSD"),
        ("mac:isObservationOf",             "is observation of"),
        ("mac:hasPredictionMethod",         "has prediction method"),
        ("mac:hasRMSD",                     "has RMSD (Root Mean Square Deviation)"),
    ],

    "type_specific_statement_ids": [
        "sub:st_obs", "sub:st_pm", "sub:st_oc",
        "sub:st_val", "sub:st_src",
    ],

    "placeholders": [
        # Spike RBD Variant FDO (Type 1). Guided-choice deferred until
        # a SpikeRBDVariant lookup API exists.
        {"id": "sub:variant", "types": ["nt:ExternalUriPlaceholder"],
         "label": "Spike RBD Variant FDO referent URI"},
        # Type 9 Computational Method FDO. Guided-choice deferred until
        # the Type 9 catalogue is populated.
        {"id": "sub:predictionMethod", "types": ["nt:ExternalUriPlaceholder"],
         "label": "Computational Method FDO referent URI (Type 9)"},
        # SPS v1.3 observation-specific authority (optional + repeatable).
        {"id": "sub:authority", "types": ["nt:ExternalUriPlaceholder"],
         "label": "observation-specific authority (DOI or URL)"},
        # SPS v1.3 §"Source URLs for dct:source": FAIR² Package DOI,
        # FAIR² resource URL, or OSF URL. Mandatory + repeatable.
        {"id": "sub:source", "types": ["nt:ExternalUriPlaceholder"],
         "label": "FAIR² Package DOI or FAIR² resource URL or OSF URL"},
        # Decimal literal; no regex (NanoDash validates, or accept free-form).
        {"id": "sub:value", "types": ["nt:LiteralPlaceholder"],
         "label": "RMSD value (Angstroms)"},
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
         "predicate": "mac:hasRMSD", "object": "sub:value"},
        # Mandatory + repeatable (no nt:OptionalStatement). Generator
        # supports this combination; cf. st6 (creator) in the standard
        # descriptive block.
        {"id": "sub:st_src", "subject": "sub:fdo",
         "predicate": "dct:source", "object": "sub:source",
         "st_types": ["nt:RepeatableStatement"]},
    ],
}
