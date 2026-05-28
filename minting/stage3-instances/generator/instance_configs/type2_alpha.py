"""Stage 3 Type 2 instance — Alpha real-world occurrence."""

VARIANT_FDO = "https://w3id.org/np/RA4BHII2Bz7HfpUkaSJqNmhjF8F7hyWpCJnvXYkA4EP_M/Alpha-RBD-Variant"
GISAID_METHOD = "https://w3id.org/np/RA7XLn4SiwTU4L_5YFYW8KBefgKeYXRu5DSFvYtlZE-o4/GISAID-Method"
TYPE2_TEMPLATE = "https://w3id.org/np/RA_-AALlM1rIYcJRsFUrIfSb5KYSvjiHUZbQbN-cpeV6w"

CONFIG = {
    "kind": "occurrence",
    "instance_id": "Alpha-Occurrence",
    "template_uri": TYPE2_TEMPLATE,

    "instance_label": "Alpha real-world occurrence — England (late 2020-2021)",
    "instance_description": (
        "Real-world detection of SARS-CoV-2 Spike variant Alpha "
        "(B.1.1.7) in England during late 2020-2021, as reported in "
        "GISAID (accession EPI_ISL_601443)."
    ),

    "variant_fdo": VARIANT_FDO,
    "method_fdo": GISAID_METHOD,
    "occurrence_date": "late 2020-2021",
    "location_uri": "https://sws.geonames.org/6269131/",
    "gisaid_accession": "EPI_ISL_601443",

    "creator_orcid": "0000-0001-8888-635X",
    "contact_email": "e.a.schultes@lacdr.leidenuniv.nl",
    "publisher_ror": "https://ror.org/027bh9e22",
}
