"""Stage 3 method instance — AlphaFold 2 (Type 9, Computational Method).

DeepMind's AlphaFold 2 protein structure prediction system. Referenced
by Type 3-5 computational-prediction observation FDOs via
mac:hasPredictionMethod for the AlphaFold-based predictions.
"""

CONFIG = {
    "kind": "method",
    "instance_id": "AlphaFold2-Method",
    "class_curie": "mac:ComputationalMethod",
    "template_uri": "https://w3id.org/np/RA5f4FtcnAGRtdt-vDTCvwXT1yVX7oMoXmvv-B8nfMelc",

    "instance_label": "AlphaFold 2 — DeepMind structure predictor",
    "instance_description": (
        "AlphaFold 2 (DeepMind) protein structure prediction system."
    ),

    "authorities": [
        "https://doi.org/10.1038/s41586-021-03819-2",
    ],
    "url": "https://github.com/google-deepmind/alphafold",

    "creator_orcid": "0000-0001-8888-635X",
    "contact_email": "e.a.schultes@lacdr.leidenuniv.nl",
    "publisher_ror": "https://ror.org/027bh9e22",
}
