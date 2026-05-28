"""Stage 3 Type 1 instance — Eta (Spike RBD Variant FDO anchor).

Values from SPS v1.3 §"Type 1 Instance values" + §"RBD sequences" +
FDT4Claude_small_v1_2.csv (GISAID accession).
"""

CONFIG = {
    "instance_id": "Eta-RBD-Variant",
    "instance_label": "Spike RBD Variant Eta (E152K)",
    "instance_description": (
        "SARS-CoV-2 Spike RBD variant Eta, carrying the E152K "
        "substitution (corresponding to E484K in the full Spike "
        "numbering). Pango lineage B.1.525. Designated a Variant of "
        "Interest (VOI) by the WHO. RBD anchor FDO for the MAC FAIR "
        "Digital Twin observation cluster — all Type 2-8 observation "
        "FDOs of this variant link back here via mac:isObservationOf."
    ),

    "who_variant_name":  "Eta",
    "pango_lineage":     "B.1.525",
    "gisaid_seq_id":     "E484K",
    "mac_seq_id":        "E152K",
    "rbd_sequence":      "TNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVKGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGP",
    "gisaid_accession":  "EPI_ISL_941290",

    "creator_orcid":     "0000-0001-8888-635X",
    "contact_email":     "e.a.schultes@lacdr.leidenuniv.nl",
    "publisher_ror":     "https://ror.org/027bh9e22",
}
