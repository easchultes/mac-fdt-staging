"""Type 2 — Real-World Occurrence (MAC FDT observation type).

Per SPS v1.3 §"Type 2": real-world detection of a SARS-CoV-2 Spike
variant as reported in GISAID. Anchors via mac:isObservationOf to a
Type 1 (Spike RBD Variant) FDO, and optionally to a Type 11
surveillance-method FDO via mac:hasSurveillanceMethod.

Per SPS v1.3 §"FAIR² citation policy", Type 2 carries no fixed FAIR²
pair at the scaffold level; observation-specific authorities use the
optional+repeatable cito:citesAsAuthority statement (st_oc).
"""

CONFIG = {
    "type_id": "type2",
    "type_label_short": "Type 2",
    "class_curie": "mac:RealWorldOccurrence",

    # SPS v1.3: Types 2-8 omit the Type 1 FAIR² citation pair; observation
    # citations are carried by per-instance cito:citesAsAuthority (st_oc).
    "includes_fair2": False,

    "template_label": "Declaring a Real-World Occurrence (MAC FDT Type 2)",
    "template_description": (
        "Real-world detection of a SARS-CoV-2 Spike variant, as reported "
        "in GISAID. Carries the occurrence date and the collection "
        "location (GeoNames URI), and optionally the canonical GISAID "
        "accession. Links via mac:isObservationOf to the Spike RBD "
        "Variant FDO it observes, and optionally via "
        "mac:hasSurveillanceMethod to the surveillance system (Type 11 "
        "FDO). The nanopublication self-materializes (assertion graph "
        "is the FDO)."
    ),
    "label_pattern": "Real-world occurrence (${occurrenceDate})",

    # Noun-phrase placeholder texts (slot into sub:fdo, sub:label,
    # sub:description). Example in sub:label is illustrative, not
    # normative — see report §(d).
    "fdo_label_text": "full URI (e.g. handle.net) or short suffix for this occurrence FDO",
    "label_placeholder_text": 'label or name for this occurrence (e.g. \\"Alpha first detected, UK Sept 2020\\")',
    "description_placeholder_text": "free-text description of this occurrence",

    # External-resource labels: cito:citesAsAuthority predicate has no
    # prefix in the common scaffold header, so emit its label as a full
    # URI. (Adding `cito:` to common @prefix would break Type 1 v4
    # round-trip; deferred until the prefix is needed across enough
    # types that scaffold change is worth the v5 supersession.)
    "external_resource_labels": [
        ("http://purl.org/spar/cito/citesAsAuthority", "cites as authority"),
    ],

    # mac:* class + predicates introduced for this type. Stage 1 v2
    # vocabulary entries — all present in manifest_live_v2.csv.
    "mac_term_labels": [
        ("mac:RealWorldOccurrence",    "Real-World Occurrence"),
        ("mac:isObservationOf",        "is observation of"),
        ("mac:hasSurveillanceMethod",  "has surveillance method"),
        ("mac:hasOccurrenceDate",      "has occurrence date"),
        ("mac:hasCollectionLocation",  "has collection location"),
        ("mac:hasGISAIDAccession",     "has GISAID accession number"),
    ],

    # Order matches SPS v1.3 §"Type 2" statement table.
    "type_specific_statement_ids": [
        "sub:st_obs", "sub:st_sm", "sub:st_oc",
        "sub:st_d", "sub:st_l", "sub:st_gi",
    ],

    "placeholders": [
        # SPS v1.3 prefers a guided-choice picker for the variant FDO,
        # deferred until a SpikeRBDVariant lookup API exists.
        {
            "id": "sub:variant",
            "types": ["nt:ExternalUriPlaceholder"],
            "label": "Spike RBD Variant FDO referent URI",
        },
        # SPS v1.3 prefers guided-choice from a Type 11 surveillance-method
        # catalogue, deferred until that catalogue is populated.
        {
            "id": "sub:surveillanceMethod",
            "types": ["nt:ExternalUriPlaceholder"],
            "label": "surveillance method FDO referent URI",
        },
        # SPS v1.3 introduced optional+repeatable cito:citesAsAuthority for
        # observation-specific authorities (DOIs, URLs). One-hop
        # attribution; instance supplies the URI.
        {
            "id": "sub:authority",
            "types": ["nt:ExternalUriPlaceholder"],
            "label": "observation-specific authority (DOI or URL)",
        },
        # No regex: SPS v1.3 instance values use fuzzy strings like
        # "late 2020-2021".
        {
            "id": "sub:occurrenceDate",
            "types": ["nt:LiteralPlaceholder"],
            "label": "GISAID-reported collection date",
        },
        # GeoNames feature URI. Guided-choice deferred until a GeoNames
        # lookup API is wired up.
        {
            "id": "sub:location",
            "types": ["nt:ExternalUriPlaceholder"],
            "label": "GeoNames feature URI (e.g. https://sws.geonames.org/6269131/)",
        },
        {
            "id": "sub:gisaidAccession",
            "types": ["nt:LiteralPlaceholder"],
            "label": "canonical GISAID accession (EPI_ISL_XXXXXXX)",
            "extras": [
                ("nt:hasRegex", '"^EPI_ISL_\\\\d+$"'),
            ],
        },
    ],

    "statements": [
        # Mandatory anchor to a Type 1 Spike RBD Variant FDO.
        {"id": "sub:st_obs", "subject": "sub:fdo",
         "predicate": "mac:isObservationOf", "object": "sub:variant"},
        # Optional one-hop link to a Type 11 surveillance-method FDO.
        {"id": "sub:st_sm", "subject": "sub:fdo",
         "predicate": "mac:hasSurveillanceMethod", "object": "sub:surveillanceMethod",
         "st_types": ["nt:OptionalStatement"]},
        # SPS v1.3 observation-citation (optional + repeatable). Predicate
        # is full URI; cito: prefix not in common scaffold.
        {"id": "sub:st_oc", "subject": "sub:fdo",
         "predicate": "<http://purl.org/spar/cito/citesAsAuthority>",
         "object": "sub:authority",
         "st_types": ["nt:OptionalStatement", "nt:RepeatableStatement"]},
        # Mandatory occurrence date.
        {"id": "sub:st_d", "subject": "sub:fdo",
         "predicate": "mac:hasOccurrenceDate", "object": "sub:occurrenceDate"},
        # Mandatory collection location (GeoNames URI).
        {"id": "sub:st_l", "subject": "sub:fdo",
         "predicate": "mac:hasCollectionLocation", "object": "sub:location"},
        # Optional canonical GISAID accession.
        {"id": "sub:st_gi", "subject": "sub:fdo",
         "predicate": "mac:hasGISAIDAccession", "object": "sub:gisaidAccession",
         "st_types": ["nt:OptionalStatement"]},
    ],
}
