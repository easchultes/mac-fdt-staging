"""Stage 3 Type 1 instance — Epsilon (Spike RBD Variant FDO anchor).

Values from SPS v1.3 §"Type 1 Instance values" + §"RBD sequences" +
FDT4Claude_small_v1_2.csv (GISAID accession).

GISAID seq_id CORRECTION (2026-05-28):
L452R is Epsilon's canonical defining Spike mutation (lineages
B.1.427 / B.1.429). SPS v1.3 and FDT4Claude_small_v1_2.csv carry
L124R, an upstream data-entry error to be corrected in the
coordinated revision pass (see Post_demonstration_cleanup.md). Demo
nanopub publishes the correct value.

Pango lineage carries the composite designation B.1.427 + B.1.429
exactly as in SPS v1.3.
"""

CONFIG = {
    "instance_id": "Epsilon-RBD-Variant",
    "instance_label": "Spike RBD Variant Epsilon (L120R)",
    "instance_description": (
        "SARS-CoV-2 Spike RBD variant Epsilon, carrying the L120R "
        "substitution (corresponding to L452R in the full Spike "
        "numbering — Epsilon's canonical defining mutation). Pango "
        "lineage B.1.427 + B.1.429 (composite). RBD anchor FDO for "
        "the MAC FAIR Digital Twin observation cluster — all Type "
        "2-8 observation FDOs of this variant link back here via "
        "mac:isObservationOf."
    ),

    "who_variant_name":  "Epsilon",
    "pango_lineage":     "B.1.427 + B.1.429",
    "gisaid_seq_id":     "L452R",
    "mac_seq_id":        "L120R",
    "rbd_sequence":      "TNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYRYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGP",
    "gisaid_accession":  "EPI_ISL_2295356",

    "creator_orcid":     "0000-0001-8888-635X",
    "contact_email":     "e.a.schultes@lacdr.leidenuniv.nl",
    "publisher_ror":     "https://ror.org/027bh9e22",
}
