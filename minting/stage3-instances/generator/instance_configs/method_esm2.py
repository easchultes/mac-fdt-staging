"""Stage 3 method instance — ESM2 (Type 9, Computational Method).

Meta AI's ESM2 protein language model. Referenced by Type 3-5
computational-prediction observation FDOs via mac:hasPredictionMethod
for the ESM-based predictions.
"""

CONFIG = {
    "kind": "method",
    "instance_id": "ESM2-Method",
    "class_curie": "mac:ComputationalMethod",
    "template_uri": "https://w3id.org/np/RA5f4FtcnAGRtdt-vDTCvwXT1yVX7oMoXmvv-B8nfMelc",

    "instance_label": "ESM2 — Meta AI protein language model",
    "instance_description": (
        "ESM2 protein language model (Meta AI) for structure and "
        "property prediction from sequence."
    ),

    "authorities": [
        "https://doi.org/10.1126/science.ade2574",
    ],
    "url": "https://github.com/facebookresearch/esm",

    "creator_orcid": "0000-0001-8888-635X",
    "contact_email": "e.a.schultes@lacdr.leidenuniv.nl",
    "publisher_ror": "https://ror.org/027bh9e22",
}
