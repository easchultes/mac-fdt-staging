"""Stage 3 Type 8 instance — WHO classification for Epsilon (VOI)."""

VARIANT_FDO = "https://w3id.org/np/RAbyuWWdW-j1rYt7Eqnva6aBvMyTkM9_Ka2FbA9dJHR7s/Epsilon-RBD-Variant"
TYPE8_TEMPLATE = "https://w3id.org/np/RAWyoHGVyB3Rh-fizZguS1zzf8Cim3q5ngWSoQNs2Sgcs"

CONFIG = {
    "kind": "who",
    "instance_id": "Epsilon-WHO",
    "template_uri": TYPE8_TEMPLATE,

    "instance_label": "Epsilon — WHO Variant of Interest (2021-03-05)",
    "instance_description": (
        "WHO classification of SARS-CoV-2 Spike variant Epsilon "
        "(B.1.427 + B.1.429) as a Variant of Interest (VOI) on "
        "2021-03-05."
    ),

    "variant_fdo": VARIANT_FDO,
    "classification_curie": "mac:VOI",
    "classification_date": "2021-03-05",

    "creator_orcid": "0000-0001-8888-635X",
    "contact_email": "e.a.schultes@lacdr.leidenuniv.nl",
    "publisher_ror": "https://ror.org/027bh9e22",
}
