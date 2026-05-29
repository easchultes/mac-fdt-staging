"""Type 9 — Computational Method (MAC FDT method FDO).

Per SPS v1.3 §"Types 9-11": a computational method, tool, or algorithm
producing predictions or scores from biological sequence or structure
data. Referenced by computational-prediction observation FDOs (Types
3-6) via mac:hasPredictionMethod.

Simpler than observation FDOs:
- No mac:isObservationOf (methods are not observations).
- No dct:source (methods do not derive from a FAIR² Data Package).
- cito:citesAsAuthority is MANDATORY + repeatable (differs from
  Types 2-8 where it is optional+repeatable) per SPS v1.3 §"Method
  attribution" — the method's published-authority citation is
  load-bearing.
- schema:url is optional — software/data/platform URL.

`schema:` and `cito:` prefixes are not in the common scaffold @prefix
header (would break Type 1 v4 round-trip), so both predicates are
emitted as full URIs at instance-pattern time and their rdfs:label
entries go in external_resource_labels.
"""

CONFIG = {
    "type_id": "type9",
    "type_label_short": "Type 9",
    "class_curie": "mac:ComputationalMethod",
    "includes_fair2": False,

    "template_label": "Declaring a Computational Method (MAC FDT Type 9)",
    "template_description": (
        "A computational method, tool, or algorithm producing "
        "predictions or scores from biological sequence or structure "
        "data. Referenced by computational-prediction observation "
        "FDOs (Types 3-6) via mac:hasPredictionMethod. Carries one or "
        "more cito:citesAsAuthority URIs identifying the published "
        "method descriptions, and an optional schema:url for the "
        "software resource. The nanopublication self-materializes "
        "(assertion graph is the FDO)."
    ),
    "label_pattern": "Computational method (${label})",

    "fdo_label_text": "full URI or short suffix for this computational method FDO",
    "label_placeholder_text": 'label for this method (e.g. \\"ESM2 — Meta AI protein language model\\")',
    "description_placeholder_text": "free-text description of this method",

    "external_resource_labels": [
        ("http://purl.org/spar/cito/citesAsAuthority", "cites as authority"),
        ("http://schema.org/url",                      "has URL"),
    ],

    "mac_term_labels": [
        ("mac:ComputationalMethod", "Computational Method"),
    ],

    "type_specific_statement_ids": [
        "sub:st_ci", "sub:st_su",
    ],

    "placeholders": [
        # Method's published-authority URI(s). Mandatory + repeatable
        # via st_ci's nt:RepeatableStatement (no OptionalStatement).
        {"id": "sub:authority", "types": ["nt:ExternalUriPlaceholder"],
         "label": "published method authority (DOI or URL)"},
        # Optional software/data/platform URL. Per-type label varies.
        {"id": "sub:url", "types": ["nt:ExternalUriPlaceholder"],
         "label": "software URL"},
    ],

    "statements": [
        # Method attribution: mandatory + repeatable (NOT optional —
        # differs from Types 2-8).
        {"id": "sub:st_ci", "subject": "sub:fdo",
         "predicate": "<http://purl.org/spar/cito/citesAsAuthority>",
         "object": "sub:authority",
         "st_types": ["nt:RepeatableStatement"]},
        # Optional software/resource URL.
        {"id": "sub:st_su", "subject": "sub:fdo",
         "predicate": "<http://schema.org/url>",
         "object": "sub:url",
         "st_types": ["nt:OptionalStatement"]},
    ],
}
