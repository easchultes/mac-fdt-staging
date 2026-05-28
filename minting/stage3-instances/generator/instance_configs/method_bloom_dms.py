"""Stage 3 method instance — Bloom Lab DMS (Type 10, Experimental Method).

Deep mutational scanning of SARS-CoV-2 RBD for binding affinity and
expression level (Bloom Lab). Referenced by Type 7 DMS observation
FDOs via mac:hasExperimentalMethod.
"""

CONFIG = {
    "kind": "method",
    "instance_id": "BloomLab-DMS-Method",
    "class_curie": "mac:ExperimentalMethod",
    "template_uri": "https://w3id.org/np/RALExfuvWjR8Lezp7I64cWCHgqyLb52js6-CTDIoINohs",

    "instance_label": "Deep mutational scanning — Bloom Lab SARS-CoV-2 RBD",
    "instance_description": (
        "Deep mutational scanning of SARS-CoV-2 RBD binding and "
        "expression, Bloom Lab."
    ),

    "authorities": [
        "https://doi.org/10.1016/j.cell.2020.08.012",
    ],
    "url": "https://github.com/jbloomlab/SARS-CoV-2-RBD_DMS",

    "creator_orcid": "0000-0001-8888-635X",
    "contact_email": "e.a.schultes@lacdr.leidenuniv.nl",
    "publisher_ror": "https://ror.org/027bh9e22",
}
