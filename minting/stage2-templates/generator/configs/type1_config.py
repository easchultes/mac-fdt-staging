"""Type 1 — Spike RBD Variant (MAC FDT anchor).

Round-trip target: drafts/template_type1_spike_rbd_variant_v4.trig
(modulo dct:created timestamp).
"""

CONFIG = {
    "type_id": "type1",
    "type_label_short": "Type 1",
    "class_curie": "mac:SpikeRBDVariant",

    # SPS v1.3: Type 1 (anchor FDO) carries the mandatory FAIR² citation
    # pair (st_f2a → article DOI, st_f2p → package DOI). Types 2–8 emit
    # dct:source as a per-observation statement instead; Types 9–11 omit
    # FAIR² references entirely.
    "includes_fair2": True,

    "template_label": "Declaring a Spike RBD Variant (MAC FDT Type 1)",
    "template_description": (
        "Template for the central anchor of a MAC FAIR Digital Twin: a "
        "SARS-CoV-2 Spike RBD variant. All observation FDOs (Types 2–8) "
        "link back to an instance of this template via mac:isObservationOf. "
        "Per SPS v1.3, every instance also declares its institutional "
        "context via dct:isPartOf → a Project FDO referent URI "
        "(mandatory; instance-supplied via guided-choice from the project "
        "catalogue). The nanopublication self-materializes: it is its own "
        "access mechanism, in TriG, under CC BY 4.0."
    ),
    "label_pattern": "Spike RBD Variant ${whoVariantName} (${macSeqId})",

    # Standard descriptive placeholder texts (carry the variant-noun
    # phrase that distinguishes one type from another).
    "fdo_label_text": "full URI (e.g. handle.net) or short suffix for this variant FDO",
    "label_placeholder_text": 'label or name for this variant (e.g. \\"Alpha RBD variant (N169Y)\\")',
    "description_placeholder_text": "free-text description of this variant",

    # External-resource URI labels, placed between the common FDO/dcat/FIP
    # block and the common FAIR²/format/license block. Type 1 anchors the
    # wild-type Spike (UniProt P0DTC2).
    "external_resource_labels": [
        ("https://www.uniprot.org/uniprot/P0DTC2", "wild-type SARS-CoV-2 Spike (UniProt P0DTC2)"),
    ],

    # Type-specific class + predicate labels (mac:* curies), placed at
    # the end of the external-term-labels block.
    "mac_term_labels": [
        ("mac:SpikeRBDVariant",    "Spike RBD Variant"),
        ("mac:hasWHOVariantName",  "has WHO variant name"),
        ("mac:hasPangoLineage",    "has Pango lineage"),
        ("mac:hasGISAIDSeqId",     "has GISAID seq_id (full Spike notation)"),
        ("mac:hasMACSeqId",        "has MAC seq_id (RBD notation)"),
        ("mac:hasParentProtein",   "has parent protein"),
        ("mac:hasRBDSequence",     "has RBD amino acid sequence (one-letter code, 195 residues)"),
        ("mac:hasGISAIDAccession", "has GISAID accession number"),
    ],

    # Statement IDs to splice into nt:hasStatement between st_pp and
    # the FAIR² entries (in source order).
    "type_specific_statement_ids": [
        "sub:st_w", "sub:st_p", "sub:st_g", "sub:st_m",
        "sub:st_u", "sub:st_s", "sub:st_a",
    ],

    # Type-specific placeholders.
    "placeholders": [
        {
            "id": "sub:whoVariantName",
            "types": ["nt:LiteralPlaceholder"],
            "label": 'WHO variant name (e.g. \\"Alpha\\", \\"Epsilon\\", \\"Eta\\")',
        },
        {
            "id": "sub:pangoLineage",
            "types": ["nt:LiteralPlaceholder"],
            "label": 'Pango lineage (e.g. \\"B.1.1.7\\", \\"B.1.427 + B.1.429\\")',
        },
        {
            "id": "sub:gisaidSeqId",
            "types": ["nt:LiteralPlaceholder"],
            "label": 'GISAID seq_id — full Spike amino-acid notation (e.g. \\"N501Y\\")',
            "extras": [
                ("nt:hasRegex", '"^[ACDEFGHIKLMNPQRSTVWY]\\\\d{1,3}[ACDEFGHIKLMNPQRSTVWY]$"'),
            ],
        },
        {
            "id": "sub:macSeqId",
            "types": ["nt:LiteralPlaceholder"],
            "label": 'MAC seq_id — RBD amino-acid notation (e.g. \\"N169Y\\")',
            "extras": [
                ("nt:hasRegex", '"^[ACDEFGHIKLMNPQRSTVWY]\\\\d{1,3}[ACDEFGHIKLMNPQRSTVWY]$"'),
            ],
        },
        {
            "id": "sub:rbdSequence",
            "types": ["nt:LongLiteralPlaceholder"],
            "label": "RBD amino-acid sequence (one-letter code, 195 residues)",
            "extras": [
                ("nt:hasRegex", '"^[ACDEFGHIKLMNPQRSTVWY]{195}$"'),
            ],
        },
        {
            "id": "sub:gisaidAccession",
            "types": ["nt:LiteralPlaceholder"],
            "label": 'canonical GISAID accession (e.g. \\"EPI_ISL_601443\\")',
            "extras": [
                ("nt:hasRegex", '"^EPI_ISL_\\\\d+$"'),
            ],
        },
    ],

    # Type-specific statement patterns (st_w, st_p, st_g, st_m, st_u, st_s, st_a).
    "statements": [
        {"id": "sub:st_w", "subject": "sub:fdo", "predicate": "mac:hasWHOVariantName", "object": "sub:whoVariantName"},
        {"id": "sub:st_p", "subject": "sub:fdo", "predicate": "mac:hasPangoLineage",   "object": "sub:pangoLineage"},
        {"id": "sub:st_g", "subject": "sub:fdo", "predicate": "mac:hasGISAIDSeqId",    "object": "sub:gisaidSeqId"},
        {"id": "sub:st_m", "subject": "sub:fdo", "predicate": "mac:hasMACSeqId",       "object": "sub:macSeqId"},
        {"id": "sub:st_u", "subject": "sub:fdo", "predicate": "mac:hasParentProtein",  "object": "<https://www.uniprot.org/uniprot/P0DTC2>"},
        {"id": "sub:st_s", "subject": "sub:fdo", "predicate": "mac:hasRBDSequence",    "object": "sub:rbdSequence"},
        {"id": "sub:st_a", "subject": "sub:fdo", "predicate": "mac:hasGISAIDAccession","object": "sub:gisaidAccession", "st_types": ["nt:OptionalStatement"]},
    ],
}
