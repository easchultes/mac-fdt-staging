"""Type 6 — Computational Prediction — AgMata.

Per SPS v1.3 §"Type 6": sequence-derived prediction of the AgMata
aggregation propensity score (unitless) of a SARS-CoV-2 Spike RBD
variant, produced by the Bio2Byte AgMata predictor. One FDO per
variant (NOT per method — AgMata is method-fixed, unlike Types 3-5
which mint one FDO per (variant × method) pair).

Structurally identical to Types 3-5: differs only on class URI,
metric predicate (mac:hasAgMataScore), units (unitless), and
source-URL semantics (per SPS v1.3 Type 6 row, FAIR² ESM resource
URL is mandatory; AgMata is carried on the ESM row of the source CSV).

See type3_config.py for SPS v1.3 conformance commentary.
"""

CONFIG = {
    "type_id": "type6",
    "type_label_short": "Type 6",
    "class_curie": "mac:ComputationalPredictionAgMata",
    "includes_fair2": False,

    "template_label": "Declaring a Computational Prediction — AgMata (MAC FDT Type 6)",
    "template_description": (
        "Computational prediction of the AgMata aggregation propensity "
        "score (unitless) of a SARS-CoV-2 Spike RBD variant, produced "
        "by the Bio2Byte AgMata predictor. Sequence-derived: one FDO "
        "per variant. Links via mac:isObservationOf to the variant FDO "
        "it observes and via mac:hasPredictionMethod to the Bio2Byte "
        "Computational Method FDO (Type 9). The nanopublication "
        "self-materializes (assertion graph is the FDO)."
    ),
    "label_pattern": "AgMata = ${value}",

    "fdo_label_text": "full URI or short suffix for this AgMata observation FDO",
    "label_placeholder_text": 'label for this observation (e.g. \\"Alpha AgMata\\")',
    "description_placeholder_text": "free-text description of this AgMata observation",

    "external_resource_labels": [
        ("http://purl.org/spar/cito/citesAsAuthority", "cites as authority"),
    ],

    "mac_term_labels": [
        ("mac:ComputationalPredictionAgMata", "Computational Prediction — AgMata"),
        ("mac:isObservationOf",               "is observation of"),
        ("mac:hasPredictionMethod",           "has prediction method"),
        ("mac:hasAgMataScore",                "has AgMata score (aggregation propensity)"),
    ],

    "type_specific_statement_ids": [
        "sub:st_obs", "sub:st_pm", "sub:st_oc",
        "sub:st_val", "sub:st_src",
    ],

    "placeholders": [
        {"id": "sub:variant", "types": ["nt:ExternalUriPlaceholder"],
         "label": "Spike RBD Variant FDO referent URI"},
        # Method-fixed at instance time (Bio2Byte AgMata Type 9 FDO); the
        # placeholder is still external-URI because it points to a Type 9 FDO.
        {"id": "sub:predictionMethod", "types": ["nt:ExternalUriPlaceholder"],
         "label": "Computational Method FDO referent URI (Bio2Byte AgMata, Type 9)"},
        {"id": "sub:authority", "types": ["nt:ExternalUriPlaceholder"],
         "label": "observation-specific authority (DOI or URL)"},
        # SPS v1.3 §"Type 6" source URLs: FAIR² Package DOI (mandatory),
        # FAIR² ESM resource URL (mandatory — AgMata sits on the ESM row of
        # the source CSV), OSF URL (optional). Single placeholder reused for
        # all three at instance time via st_src's repeatability.
        {"id": "sub:source", "types": ["nt:ExternalUriPlaceholder"],
         "label": "FAIR² Package DOI or FAIR² ESM resource URL or OSF URL"},
        {"id": "sub:value", "types": ["nt:LiteralPlaceholder"],
         "label": "AgMata score (unitless)"},
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
         "predicate": "mac:hasAgMataScore", "object": "sub:value"},
        {"id": "sub:st_src", "subject": "sub:fdo",
         "predicate": "dct:source", "object": "sub:source",
         "st_types": ["nt:RepeatableStatement"]},
    ],
}
