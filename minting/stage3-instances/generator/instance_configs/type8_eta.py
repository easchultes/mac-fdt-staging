"""Stage 3 Type 8 instance — WHO classification for Eta (VOI)."""

VARIANT_FDO = "https://w3id.org/np/RAikllrKWQoo81RYYvGJjWfzE0QiGrLquMMIwDD6xem2s/Eta-RBD-Variant"
TYPE8_TEMPLATE = "https://w3id.org/np/RAWyoHGVyB3Rh-fizZguS1zzf8Cim3q5ngWSoQNs2Sgcs"

CONFIG = {
    "kind": "who",
    "instance_id": "Eta-WHO",
    "template_uri": TYPE8_TEMPLATE,

    "instance_label": "Eta — WHO Variant of Interest (2021-03-05)",
    "instance_description": (
        "WHO classification of SARS-CoV-2 Spike variant Eta "
        "(B.1.525) as a Variant of Interest (VOI) on 2021-03-05."
    ),

    "variant_fdo": VARIANT_FDO,
    "classification_curie": "mac:VOI",
    "classification_date": "2021-03-05",

    "creator_orcid": "0000-0001-8888-635X",
    "contact_email": "e.a.schultes@lacdr.leidenuniv.nl",
    "publisher_ror": "https://ror.org/027bh9e22",
}
