"""Stage 3 Type 2 instance — Epsilon real-world occurrence.

Location: GeoNames 6252001 (United States, country) — broader than
SPS v1.3's California candidate; flag per Post_demonstration_cleanup.md.
"""

VARIANT_FDO = "https://w3id.org/np/RAbyuWWdW-j1rYt7Eqnva6aBvMyTkM9_Ka2FbA9dJHR7s/Epsilon-RBD-Variant"
GISAID_METHOD = "https://w3id.org/np/RA7XLn4SiwTU4L_5YFYW8KBefgKeYXRu5DSFvYtlZE-o4/GISAID-Method"
TYPE2_TEMPLATE = "https://w3id.org/np/RA_-AALlM1rIYcJRsFUrIfSb5KYSvjiHUZbQbN-cpeV6w"

CONFIG = {
    "kind": "occurrence",
    "instance_id": "Epsilon-Occurrence",
    "template_uri": TYPE2_TEMPLATE,

    "instance_label": "Epsilon real-world occurrence — United States (2021-01-13)",
    "instance_description": (
        "Real-world detection of SARS-CoV-2 Spike variant Epsilon "
        "(B.1.427 + B.1.429) in the United States on 2021-01-13, as "
        "reported in GISAID (accession EPI_ISL_2295356)."
    ),

    "variant_fdo": VARIANT_FDO,
    "method_fdo": GISAID_METHOD,
    "occurrence_date": "2021-01-13",
    "location_uri": "https://sws.geonames.org/6252001/",
    "gisaid_accession": "EPI_ISL_2295356",

    "creator_orcid": "0000-0001-8888-635X",
    "contact_email": "e.a.schultes@lacdr.leidenuniv.nl",
    "publisher_ror": "https://ror.org/027bh9e22",
}
