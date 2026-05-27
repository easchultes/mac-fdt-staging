"""Type 11 — Observational Method (MAC FDT method FDO).

Per SPS v1.3 §"Types 9-11": an epidemiological surveillance system or
data collection platform through which real-world occurrences of
biological entities are documented. Referenced by real-world
observation FDOs (Type 2) via mac:hasSurveillanceMethod.

Structurally identical to Types 9 and 10; differs only on class URI,
the placeholder/template wording, and the optional URL placeholder
label. See type9_config.py for SPS v1.3 conformance commentary.
"""

CONFIG = {
    "type_id": "type11",
    "type_label_short": "Type 11",
    "class_curie": "mac:ObservationalMethod",
    "includes_fair2": False,

    "template_label": "Declaring an Observational Method (MAC FDT Type 11)",
    "template_description": (
        "An epidemiological surveillance system or data collection "
        "platform through which real-world occurrences of biological "
        "entities are documented. Referenced by real-world observation "
        "FDOs (Type 2) via mac:hasSurveillanceMethod. Carries one or "
        "more cito:citesAsAuthority URIs identifying the published "
        "descriptions of the system, and an optional schema:url for "
        "the platform. The nanopublication self-materializes "
        "(assertion graph is the FDO)."
    ),
    "label_pattern": "Observational method (${label})",

    "fdo_label_text": "full URI or short suffix for this observational method FDO",
    "label_placeholder_text": 'label for this method (e.g. \\"GISAID — Global Initiative on Sharing All Influenza Data\\")',
    "description_placeholder_text": "free-text description of this method",

    "external_resource_labels": [
        ("http://purl.org/spar/cito/citesAsAuthority", "cites as authority"),
        ("http://schema.org/url",                      "has URL"),
    ],

    "mac_term_labels": [
        ("mac:ObservationalMethod", "Observational Method"),
    ],

    "type_specific_statement_ids": [
        "sub:st_ci", "sub:st_su",
    ],

    "placeholders": [
        {"id": "sub:authority", "types": ["nt:ExternalUriPlaceholder"],
         "label": "published method authority (DOI or URL)"},
        {"id": "sub:url", "types": ["nt:ExternalUriPlaceholder"],
         "label": "platform URL"},
    ],

    "statements": [
        {"id": "sub:st_ci", "subject": "sub:fdo",
         "predicate": "<http://purl.org/spar/cito/citesAsAuthority>",
         "object": "sub:authority",
         "st_types": ["nt:RepeatableStatement"]},
        {"id": "sub:st_su", "subject": "sub:fdo",
         "predicate": "<http://schema.org/url>",
         "object": "sub:url",
         "st_types": ["nt:OptionalStatement"]},
    ],
}
