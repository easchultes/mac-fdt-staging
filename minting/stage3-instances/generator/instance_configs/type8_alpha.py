"""Stage 3 Type 8 instance — WHO classification for Alpha (VOC)."""

VARIANT_FDO = "https://w3id.org/np/RA4BHII2Bz7HfpUkaSJqNmhjF8F7hyWpCJnvXYkA4EP_M/Alpha-RBD-Variant"
TYPE8_TEMPLATE = "https://w3id.org/np/RAWyoHGVyB3Rh-fizZguS1zzf8Cim3q5ngWSoQNs2Sgcs"

CONFIG = {
    "kind": "who",
    "instance_id": "Alpha-WHO",
    "template_uri": TYPE8_TEMPLATE,

    "instance_label": "Alpha — WHO Variant of Concern (2020-12-18)",
    "instance_description": (
        "WHO classification of SARS-CoV-2 Spike variant Alpha "
        "(B.1.1.7) as a Variant of Concern (VOC) on 2020-12-18."
    ),

    "variant_fdo": VARIANT_FDO,
    "classification_curie": "mac:VOC",
    "classification_date": "2020-12-18",

    "creator_orcid": "0000-0001-8888-635X",
    "contact_email": "e.a.schultes@lacdr.leidenuniv.nl",
    "publisher_ror": "https://ror.org/027bh9e22",
}
