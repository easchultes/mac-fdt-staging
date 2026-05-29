"""Type 10 — Experimental Method (MAC FDT method FDO).

Per SPS v1.3 §"Types 9-11": an experimental assay or measurement
protocol producing empirical observations about biological entities.
Referenced by experimental observation FDOs (Type 7) via
mac:hasExperimentalMethod.

Structurally identical to Types 9 and 11; differs only on class URI,
the placeholder/template wording, and the optional URL placeholder
label. See type9_config.py for SPS v1.3 conformance commentary.
"""

CONFIG = {
    "type_id": "type10",
    "type_label_short": "Type 10",
    "class_curie": "mac:ExperimentalMethod",
    "includes_fair2": False,

    "template_label": "Declaring an Experimental Method (MAC FDT Type 10)",
    "template_description": (
        "An experimental assay or measurement protocol producing "
        "empirical observations about biological entities. Referenced "
        "by experimental observation FDOs (Type 7) via "
        "mac:hasExperimentalMethod. Carries one or more "
        "cito:citesAsAuthority URIs identifying the published assay "
        "descriptions, and an optional schema:url for the data "
        "resource. The nanopublication self-materializes (assertion "
        "graph is the FDO)."
    ),
    "label_pattern": "Experimental method (${label})",

    "fdo_label_text": "full URI or short suffix for this experimental method FDO",
    "label_placeholder_text": 'label for this method (e.g. \\"Deep mutational scanning — Bloom Lab SARS-CoV-2 RBD\\")',
    "description_placeholder_text": "free-text description of this method",

    "external_resource_labels": [
        ("http://purl.org/spar/cito/citesAsAuthority", "cites as authority"),
        ("http://schema.org/url",                      "has URL"),
    ],

    "mac_term_labels": [
        ("mac:ExperimentalMethod", "Experimental Method"),
    ],

    "type_specific_statement_ids": [
        "sub:st_ci", "sub:st_su",
    ],

    "placeholders": [
        {"id": "sub:authority", "types": ["nt:ExternalUriPlaceholder"],
         "label": "published method authority (DOI or URL)"},
        {"id": "sub:url", "types": ["nt:ExternalUriPlaceholder"],
         "label": "data resource URL"},
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
