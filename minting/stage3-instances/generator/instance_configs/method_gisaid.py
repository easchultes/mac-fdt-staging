"""Stage 3 method instance — GISAID (Type 11, Observational Method).

GISAID SARS-CoV-2 genomic surveillance platform. Referenced by Type 2
real-world-occurrence observation FDOs via mac:hasSurveillanceMethod.
Carries two cito:citesAsAuthority entries (the GISAID 2017 reference
publication and the 2021 CCDC Weekly update).
"""

CONFIG = {
    "kind": "method",
    "instance_id": "GISAID-Method",
    "class_curie": "mac:ObservationalMethod",
    "template_uri": "https://w3id.org/np/RAW9DfO6hmmt2sz_H4pHWWAX72BzTsnYjb9hi5wVQIQdE",

    "instance_label": "GISAID — Global Initiative on Sharing All Influenza Data",
    "instance_description": (
        "GISAID SARS-CoV-2 genomic surveillance platform."
    ),

    "authorities": [
        "https://doi.org/10.2807/1560-7917.ES.2017.22.13.30494",
        "https://doi.org/10.46234/ccdcw2021.255",
    ],
    "url": "https://www.gisaid.org/",

    "creator_orcid": "0000-0001-8888-635X",
    "contact_email": "e.a.schultes@lacdr.leidenuniv.nl",
    "publisher_ror": "https://ror.org/027bh9e22",
}
