#!/usr/bin/env python3
"""CSV-driven driver — emits Stage 3 Types 3/4/5 prediction instances.

Reads FDT4Claude_small_v1_2.csv and, for each (variant × method) row,
emits three observation FDOs (RMSD / SASA / pLDDT). Total: 3 variants
× 2 methods × 3 metrics = 18 instances.

Maps:
  CSV variant string  →  Type 1 anchor referent URI (published P122)
  CSV method string   →  Type 9 method referent URI (published P123) +
                         the 3 dct:source values for that method.

CSV metric values are emitted verbatim (no rounding).

Mandatory statements per SPS v1.3 §"Types 3-6":
  - rdf:type fdof:FAIRDigitalObject + rdf:type <metric class>
  - fdof:hasMetadata, dct:isPartOf, rdfs:label, dct:creator,
    dcat:contactPoint, dct:publisher
  - mac:isObservationOf, mac:hasPredictionMethod
  - <metric predicate> (decimal literal)
  - dct:source (mandatory + repeatable: Dataset FDO + FAIR² Package + per-method resource URL)
  - st5/5b/5c/5d (self-materialization block)
Forbidden: cito:citesAsAuthority, dct:references.
"""

import argparse
import csv
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# Allow importing generate_instance.py from this directory
sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_instance import (
    generate_prediction_instance,
    validate_prediction_config,
    check_mandatory_prediction_statements,
)


# ============================================================
# Maps
# ============================================================

VARIANT_ANCHORS = {
    "Alpha":   ("Alpha-RBD-Variant",   "https://w3id.org/np/RA4BHII2Bz7HfpUkaSJqNmhjF8F7hyWpCJnvXYkA4EP_M/Alpha-RBD-Variant"),
    "Epsilon": ("Epsilon-RBD-Variant", "https://w3id.org/np/RAbyuWWdW-j1rYt7Eqnva6aBvMyTkM9_Ka2FbA9dJHR7s/Epsilon-RBD-Variant"),
    "Eta":     ("Eta-RBD-Variant",     "https://w3id.org/np/RAikllrKWQoo81RYYvGJjWfzE0QiGrLquMMIwDD6xem2s/Eta-RBD-Variant"),
}

# Three dct:source values per method per SPS v1.3 §"Source URLs (Types 3-6)":
# the dataset FDO Trusty URI, the FAIR² Package DOI, and the FAIR² resource URL.
FAIR2_PACKAGE = "https://doi.org/10.71728/hw56-vj34"
ESM_DATASET_FDO = "https://w3id.org/np/RA9YxiABPRNy3rrJm20p1oanJchBcI22IPpSu36zj2MLs"
ESM_RESOURCE_URL = "https://sen.science/doi/10.71728/hw56-vj34/resources/esm_wuhan_1step_v1"
AF_DATASET_FDO = "https://w3id.org/np/RAv6JJe-lvoadhNwml8pzSLs5aOtbU1xbHT5qgFtgwQ-s"
AF_RESOURCE_URL = "https://sen.science/doi/10.71728/hw56-vj34/resources/af_wuhan_1step_v1"

METHODS = {
    # CSV string → (short id used in instance_id, label-friendly name, method FDO referent URI, dct:source list)
    "ESM": (
        "ESM2",
        "ESM2",
        "https://w3id.org/np/RADJxd-U-p7VpA01uXlsp3nkUo3oXFMSOam04-fcF0ZyM/ESM2-Method",
        [ESM_DATASET_FDO, FAIR2_PACKAGE, ESM_RESOURCE_URL],
    ),
    "AlphaFold II": (
        "AlphaFold2",
        "AlphaFold 2",
        "https://w3id.org/np/RA3zXmeaYZxYSPXzH7CK8-m5T31NWr9nvUCeyKz2mbvNI/AlphaFold2-Method",
        [AF_DATASET_FDO, FAIR2_PACKAGE, AF_RESOURCE_URL],
    ),
}

METRICS = [
    # (instance_id-suffix, CSV column index 0-based, class curie, metric predicate, units-suffix-for-label, units-in-comment)
    ("RMSD",  12, "mac:ComputationalPredictionRMSD",  "mac:hasRMSD",  "Å",          "Angstroms"),
    ("SASA",  13, "mac:ComputationalPredictionSASA",  "mac:hasSASA",  "Å²",         "square Angstroms"),
    ("pLDDT", 14, "mac:ComputationalPredictionPLDDT", "mac:haspLDDT", "(unitless)", "unitless, 0-100"),
]

TYPE_TEMPLATE_URI = {
    "mac:ComputationalPredictionRMSD":  "https://w3id.org/np/RALJKysR8vqqqZYXPGHcsI_J0BvPFUmzwOnV9WCGvUjcY",
    "mac:ComputationalPredictionSASA":  "https://w3id.org/np/RALSYeUQIciUad7GTfKjdNkfhP-505fesw6yYtdLoyW18",
    "mac:ComputationalPredictionPLDDT": "https://w3id.org/np/RAm5j8EmzrS_ZDXEEOkvG2icT27GlbaGoNAS0sCDS72wc",
}

SHARED = {
    "creator_orcid": "0000-0001-8888-635X",
    "contact_email": "e.a.schultes@lacdr.leidenuniv.nl",
    "publisher_ror": "https://ror.org/027bh9e22",
}

DECIMAL_RE = re.compile(r"^-?\d+\.\d+$")


# ============================================================
# Driver
# ============================================================

def build_configs_from_csv(csv_path: Path) -> list:
    """Return a list of 18 prediction-instance config dicts."""
    configs = []
    with csv_path.open(newline="") as fh:
        reader = csv.reader(fh, delimiter=";")
        header = next(reader)
        for row in reader:
            if not row or not row[0].strip():
                continue
            csv_method = row[0].strip()
            csv_variant = row[5].strip()
            csv_mac_seq = row[11].strip()
            if csv_variant not in VARIANT_ANCHORS:
                raise SystemExit(f"Unknown variant in CSV: {csv_variant!r}")
            if csv_method not in METHODS:
                raise SystemExit(f"Unknown method in CSV: {csv_method!r}")
            _, variant_fdo = VARIANT_ANCHORS[csv_variant]
            method_short, method_label, method_fdo, sources = METHODS[csv_method]
            for metric_id, col_idx, class_curie, metric_pred, units_short, units_long in METRICS:
                if col_idx >= len(row):
                    raise SystemExit(f"CSV row too short for column {col_idx}: {row}")
                metric_value = row[col_idx].strip()
                if not DECIMAL_RE.match(metric_value):
                    raise SystemExit(f"Non-decimal metric value at row {csv_variant}/{csv_method}/{metric_id}: {metric_value!r}")
                instance_id = f"{csv_variant}-{metric_id}-{method_short}"
                if metric_id == "pLDDT":
                    label_units = ""
                else:
                    label_units = f" {units_short}"
                label = f"{csv_variant} {metric_id} = {metric_value}{label_units} — {method_label}"
                description = (
                    f"Computational prediction of {metric_id} ({metric_value} "
                    f"{units_long}) for SARS-CoV-2 Spike RBD variant "
                    f"{csv_variant} ({csv_mac_seq}) using {method_label}."
                )
                configs.append({
                    "kind": "prediction",
                    "instance_id": instance_id,
                    "instance_label": label,
                    "instance_description": description,
                    "class_curie": class_curie,
                    "template_uri": TYPE_TEMPLATE_URI[class_curie],
                    "variant_fdo": variant_fdo,
                    "method_fdo": method_fdo,
                    "metric_predicate": metric_pred,
                    "metric_value": metric_value,
                    "sources": sources,
                    **SHARED,
                })
    return configs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", type=Path)
    ap.add_argument("--out-dir", type=Path, required=True)
    ap.add_argument("--created", default=None, help="Override dct:created (default: now UTC).")
    args = ap.parse_args()

    configs = build_configs_from_csv(args.csv)
    if len(configs) != 18:
        sys.stderr.write(f"WARNING: expected 18 configs, got {len(configs)}\n")
    created = args.created or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    args.out_dir.mkdir(parents=True, exist_ok=True)

    print(f"variant   metric  method        value                    instance_id")
    print(f"{'-'*92}")
    errs = 0
    for cfg in configs:
        errors = validate_prediction_config(cfg)
        if errors:
            sys.stderr.write(f"  config errors for {cfg['instance_id']}:\n")
            for e in errors:
                sys.stderr.write(f"    - {e}\n")
            errs += 1
            continue
        output = generate_prediction_instance(cfg, created)
        result = check_mandatory_prediction_statements(
            output, cfg["class_curie"], cfg["metric_predicate"])
        if result["missing"]:
            sys.stderr.write(f"  missing markers in {cfg['instance_id']}: {result['missing']}\n")
            errs += 1
            continue
        if result["forbidden_present"]:
            sys.stderr.write(f"  forbidden markers in {cfg['instance_id']}: {result['forbidden_present']}\n")
            errs += 1
            continue
        out_path = args.out_dir / f"instance_prediction_{cfg['instance_id']}_v1.trig"
        out_path.write_text(output)
        # Decompose instance_id for the table
        bits = cfg["instance_id"].split("-")
        variant = bits[0]
        metric = bits[1]
        method = bits[2]
        print(f"{variant:<9} {metric:<7} {method:<13} {cfg['metric_value']:<24} {cfg['instance_id']}")
    if errs:
        sys.stderr.write(f"FAILED: {errs} instance(s) had errors\n")
        return 1
    sys.stderr.write(f"OK: wrote {len(configs)} prediction TriG files to {args.out_dir}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
