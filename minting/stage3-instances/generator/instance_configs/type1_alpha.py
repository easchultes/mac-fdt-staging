"""Stage 3 Type 1 instance — Alpha (Spike RBD Variant FDO anchor).

Values from SPS v1.3 §"Type 1 Instance values" + §"RBD sequences" +
FDT4Claude_small_v1_2.csv (GISAID accession).
"""

CONFIG = {
    "instance_id": "Alpha-RBD-Variant",
    "instance_label": "Spike RBD Variant Alpha (N169Y)",
    "instance_description": (
        "SARS-CoV-2 Spike RBD variant Alpha, carrying the N169Y "
        "substitution (corresponding to N501Y in the full Spike "
        "numbering). Pango lineage B.1.1.7. Designated a Variant of "
        "Concern (VOC) by the WHO. RBD anchor FDO for the MAC FAIR "
        "Digital Twin observation cluster — all Type 2-8 observation "
        "FDOs of this variant link back here via mac:isObservationOf."
    ),

    "who_variant_name":  "Alpha",
    "pango_lineage":     "B.1.1.7",
    "gisaid_seq_id":     "N501Y",
    "mac_seq_id":        "N169Y",
    "rbd_sequence":      "TNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTYGVGYQPYRVVVLSFELLHAPATVCGP",
    "gisaid_accession":  "EPI_ISL_601443",

    "creator_orcid":     "0000-0001-8888-635X",
    "contact_email":     "e.a.schultes@lacdr.leidenuniv.nl",
    "publisher_ror":     "https://ror.org/027bh9e22",  # Leiden University
}
