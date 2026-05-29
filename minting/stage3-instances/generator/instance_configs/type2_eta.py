"""Stage 3 Type 2 instance — Eta real-world occurrence."""

VARIANT_FDO = "https://w3id.org/np/RAikllrKWQoo81RYYvGJjWfzE0QiGrLquMMIwDD6xem2s/Eta-RBD-Variant"
GISAID_METHOD = "https://w3id.org/np/RA7XLn4SiwTU4L_5YFYW8KBefgKeYXRu5DSFvYtlZE-o4/GISAID-Method"
TYPE2_TEMPLATE = "https://w3id.org/np/RA_-AALlM1rIYcJRsFUrIfSb5KYSvjiHUZbQbN-cpeV6w"

CONFIG = {
    "kind": "occurrence",
    "instance_id": "Eta-Occurrence",
    "template_uri": TYPE2_TEMPLATE,

    "instance_label": "Eta real-world occurrence — Nigeria (2020-12-15)",
    "instance_description": (
        "Real-world detection of SARS-CoV-2 Spike variant Eta "
        "(B.1.525) in Nigeria on 2020-12-15, as reported in GISAID "
        "(accession EPI_ISL_941290)."
    ),

    "variant_fdo": VARIANT_FDO,
    "method_fdo": GISAID_METHOD,
    "occurrence_date": "2020-12-15",
    "location_uri": "https://sws.geonames.org/2328926/",
    "gisaid_accession": "EPI_ISL_941290",

    "creator_orcid": "0000-0001-8888-635X",
    "contact_email": "e.a.schultes@lacdr.leidenuniv.nl",
    "publisher_ror": "https://ror.org/027bh9e22",
}
