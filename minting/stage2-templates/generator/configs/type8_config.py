"""Type 8 — WHO SARS-CoV-2 Variant Classification.

Per SPS v1.3 §"Type 8": classification of a SARS-CoV-2 lineage under
the WHO risk framework — Variant of Concern (VOC), Variant of
Interest (VOI), or Variant Under Monitoring (VUM) — based on
public-health risk and virological characteristics. Time-stamped
because designation status changes over time.

Anchors via mac:isObservationOf to the Type 1 Spike RBD Variant FDO.
No method link (the WHO designation is the method-output by
authoritative committee, not by a programmatic predictor).

Per SPS v1.3 §"FAIR² citation policy" for Types 2-8, includes_fair2
is False. Per-observation citations use the optional + repeatable
cito:citesAsAuthority (st_oc).
"""

CONFIG = {
    "type_id": "type8",
    "type_label_short": "Type 8",
    "class_curie": "mac:WHOVariantClassification",
    "includes_fair2": False,

    "template_label": "Declaring a WHO Variant Classification (MAC FDT Type 8)",
    "template_description": (
        "Classification of a SARS-CoV-2 lineage according to the WHO "
        "risk framework — Variant of Concern (VOC), Variant of "
        "Interest (VOI), or Variant Under Monitoring (VUM) — based "
        "on assessed public-health risk and virological characteristics. "
        "Time-stamped because designation status changes over time. "
        "Links via mac:isObservationOf to the Spike RBD Variant FDO "
        "it observes. The nanopublication self-materializes (assertion "
        "graph is the FDO)."
    ),
    "label_pattern": "WHO classification: ${classification} (${classificationDate})",

    "fdo_label_text": "full URI or short suffix for this WHO classification FDO",
    "label_placeholder_text": 'label for this classification (e.g. \\"Alpha WHO classification: VOC\\")',
    "description_placeholder_text": "free-text description of this WHO classification",

    "external_resource_labels": [
        ("http://purl.org/spar/cito/citesAsAuthority", "cites as authority"),
    ],

    "mac_term_labels": [
        ("mac:WHOVariantClassification",      "WHO Variant Classification"),
        ("mac:isObservationOf",               "is observation of"),
        ("mac:hasWHOClassification",          "has WHO variant classification"),
        ("mac:hasClassificationDate",         "has WHO classification date"),
        ("mac:hasWHOClassificationReference", "has WHO classification reference URL"),
    ],

    "type_specific_statement_ids": [
        "sub:st_obs", "sub:st_oc",
        "sub:st_wc", "sub:st_cd", "sub:st_cr",
    ],

    "placeholders": [
        {"id": "sub:variant", "types": ["nt:ExternalUriPlaceholder"],
         "label": "Spike RBD Variant FDO referent URI"},
        {"id": "sub:authority", "types": ["nt:ExternalUriPlaceholder"],
         "label": "observation-specific authority (DOI or URL)"},
        # RestrictedChoicePlaceholder with inline enumeration. The three
        # class URIs (mac:VOC, mac:VOI, mac:VUM) were minted in Stage 1 v2:
        #   mac:VOC → RAYOlJ43EmeoJ8lLRjS9cv5pn1PKNy0udeS36KfWSRCPk
        #   mac:VOI → RAiwK1L9NkB_qPZpdFoaIGISRB7-kO3xB3J3m3z_AkXR4
        #   mac:VUM → RAwWafsvm-XuaeWXIfIkmY7-25TeGmLAxyb8baj0aUDGA
        # Generator emits the three values as a single Turtle
        # predicate-object-list via `nt:possibleValue mac:VOC, mac:VOI, mac:VUM .`
        {"id": "sub:classification", "types": ["nt:RestrictedChoicePlaceholder"],
         "label": "WHO variant classification",
         "extras": [
             ("nt:possibleValue", "mac:VOC, mac:VOI, mac:VUM"),
         ]},
        # No regex — instance supplies a date string; NanoDash validates.
        {"id": "sub:classificationDate", "types": ["nt:LiteralPlaceholder"],
         "label": "WHO classification date (date)"},
        {"id": "sub:classificationRef", "types": ["nt:ExternalUriPlaceholder"],
         "label": "WHO classification reference URL"},
    ],

    "statements": [
        {"id": "sub:st_obs", "subject": "sub:fdo",
         "predicate": "mac:isObservationOf", "object": "sub:variant"},
        {"id": "sub:st_oc", "subject": "sub:fdo",
         "predicate": "<http://purl.org/spar/cito/citesAsAuthority>",
         "object": "sub:authority",
         "st_types": ["nt:OptionalStatement", "nt:RepeatableStatement"]},
        {"id": "sub:st_wc", "subject": "sub:fdo",
         "predicate": "mac:hasWHOClassification", "object": "sub:classification"},
        {"id": "sub:st_cd", "subject": "sub:fdo",
         "predicate": "mac:hasClassificationDate", "object": "sub:classificationDate",
         "st_types": ["nt:OptionalStatement"]},
        {"id": "sub:st_cr", "subject": "sub:fdo",
         "predicate": "mac:hasWHOClassificationReference", "object": "sub:classificationRef",
         "st_types": ["nt:OptionalStatement"]},
    ],
}
