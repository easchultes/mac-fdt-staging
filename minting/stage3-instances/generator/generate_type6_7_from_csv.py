#!/usr/bin/env python3
"""CSV-driven driver — emits Stage 3 Type 6 (AgMata) and Type 7 (DMS)
per-variant instances.

Both observation types are per-variant (not per-method, unlike Types
3-5). The driver reads FDT4Claude_small_v1_2.csv and, for each unique
variant, picks the ESM row (AgMata sits on that row per SPS v1.3;
DMS values are repeated on both ESM and AlphaFold rows for each
variant, so either row works). It emits two instances per variant:
one Type 6 (AgMata) and one Type 7 (DMS) — 6 instances total.

dct:source policy:
  - Type 6 (AgMata): mandatory + repeatable; emit [ESM dataset FDO,
    FAIR² Package DOI, FAIR² ESM resource URL] per SPS v1.3 §"Source
    URLs (Types 3-6)".
  - Type 7 (DMS): optional + repeatable per Stage 2 Type 7 template;
    omitted in demonstration posture (no canonical Bloom dataset FDO
    on the NSN).
"""

import argparse
import csv
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_instance import (
    generate_prediction_instance,
    validate_prediction_config,
    check_mandatory_prediction_statements,
    generate_dms_instance,
    validate_dms_config,
    check_mandatory_dms_statements,
)

# ============================================================
# Maps
# ============================================================

VARIANT_ANCHORS = {
    "Alpha":   "https://w3id.org/np/RA4BHII2Bz7HfpUkaSJqNmhjF8F7hyWpCJnvXYkA4EP_M/Alpha-RBD-Variant",
    "Epsilon": "https://w3id.org/np/RAbyuWWdW-j1rYt7Eqnva6aBvMyTkM9_Ka2FbA9dJHR7s/Epsilon-RBD-Variant",
    "Eta":     "https://w3id.org/np/RAikllrKWQoo81RYYvGJjWfzE0QiGrLquMMIwDD6xem2s/Eta-RBD-Variant",
}

# Methods (Stage 3 method instances, published P123)
AGMATA_METHOD = "https://w3id.org/np/RA3JGJN1R1uTyj1puobq1cEwHT52LNmM_67dzb0oRAz2U/AgMata-Method"
BLOOM_METHOD  = "https://w3id.org/np/RA0Bz7doV8fCSO9lEmpbtNTOnMu5lB3jVudjo-tD0T_Q0/BloomLab-DMS-Method"

# Templates
TYPE6_TEMPLATE = "https://w3id.org/np/RAuCu_OnyqK_dlaJ9l1EDdbtu_Wbpdw2pTlcTimQ9mqV0"
TYPE7_TEMPLATE = "https://w3id.org/np/RAp-dZcpmyNxtFsh7G0G1CDzzP2vPqoXVZSnlYRVQ_5Yk"

# dct:source values (AgMata is carried on the ESM row of the source CSV per SPS v1.3)
FAIR2_PACKAGE = "https://doi.org/10.71728/hw56-vj34"
ESM_DATASET_FDO = "https://w3id.org/np/RA9YxiABPRNy3rrJm20p1oanJchBcI22IPpSu36zj2MLs"
ESM_RESOURCE_URL = "https://sen.science/doi/10.71728/hw56-vj34/resources/esm_wuhan_1step_v1"
AGMATA_SOURCES = [ESM_DATASET_FDO, FAIR2_PACKAGE, ESM_RESOURCE_URL]

# CSV column indices (0-based)
COL_METHOD          = 0
COL_VARIANT         = 5
COL_PANGO           = 6
COL_MAC_SEQ         = 11
COL_AGMATA          = 15
COL_DMS_BIND        = 16
COL_DMS_DELTA_BIND  = 17
COL_DMS_EXPR        = 18
COL_DMS_DELTA_EXPR  = 19
COL_DMS_CONF_BIND   = 20
COL_DMS_CONF_EXPR   = 21

SHARED = {
    "creator_orcid": "0000-0001-8888-635X",
    "contact_email": "e.a.schultes@lacdr.leidenuniv.nl",
    "publisher_ror": "https://ror.org/027bh9e22",
}

DECIMAL_RE = re.compile(r"^-?\d+\.\d+$")


# ============================================================
# Driver
# ============================================================

def pick_esm_rows(csv_path: Path) -> dict:
    """Return {variant_name: row_list} — one ESM row per variant."""
    by_variant = {}
    with csv_path.open(newline="") as fh:
        reader = csv.reader(fh, delimiter=";")
        next(reader)  # skip header
        for row in reader:
            if not row or not row[COL_METHOD].strip():
                continue
            if row[COL_METHOD].strip() != "ESM":
                continue
            variant = row[COL_VARIANT].strip()
            if variant not in VARIANT_ANCHORS:
                raise SystemExit(f"Unknown variant in CSV: {variant!r}")
            by_variant[variant] = row
    return by_variant


def build_type6_config(variant: str, row: list) -> dict:
    """Build a Type 6 AgMata config (uses prediction kind)."""
    value = row[COL_AGMATA].strip()
    if not DECIMAL_RE.match(value):
        raise SystemExit(f"Non-decimal AgMata value at {variant}: {value!r}")
    mac_seq = row[COL_MAC_SEQ].strip()
    return {
        "kind": "prediction",
        "instance_id": f"{variant}-AgMata",
        "instance_label": f"{variant} AgMata = {value} — Bio2Byte",
        "instance_description": (
            f"Computational prediction of AgMata aggregation propensity "
            f"score ({value}, unitless) for SARS-CoV-2 Spike RBD variant "
            f"{variant} ({mac_seq}) using the Bio2Byte AgMata predictor. "
            f"Sequence-derived: one FDO per variant."
        ),
        "class_curie": "mac:ComputationalPredictionAgMata",
        "template_uri": TYPE6_TEMPLATE,
        "variant_fdo": VARIANT_ANCHORS[variant],
        "method_fdo": AGMATA_METHOD,
        "metric_predicate": "mac:hasAgMataScore",
        "metric_value": value,
        "sources": AGMATA_SOURCES,
        **SHARED,
    }


def build_type7_config(variant: str, row: list) -> dict:
    """Build a Type 7 DMS config."""
    bind        = row[COL_DMS_BIND].strip()
    delta_bind  = row[COL_DMS_DELTA_BIND].strip()
    expr        = row[COL_DMS_EXPR].strip()
    delta_expr  = row[COL_DMS_DELTA_EXPR].strip()
    conf_bind   = row[COL_DMS_CONF_BIND].strip()
    conf_expr   = row[COL_DMS_CONF_EXPR].strip()
    for label, v in [("bind", bind), ("delta_bind", delta_bind),
                     ("expr", expr), ("delta_expr", delta_expr),
                     ("confidence_bind", conf_bind), ("confidence_expr", conf_expr)]:
        if not DECIMAL_RE.match(v):
            raise SystemExit(f"Non-decimal DMS {label} value at {variant}: {v!r}")
    mac_seq = row[COL_MAC_SEQ].strip()
    return {
        "kind": "dms",
        "instance_id": f"{variant}-DMS",
        "instance_label": f"{variant} DMS observation — Bloom Lab (bind={bind}, expr={expr})",
        "instance_description": (
            f"Deep mutational scanning measurements (Bloom Lab) for "
            f"SARS-CoV-2 Spike RBD variant {variant} ({mac_seq}). Six "
            f"values: bind={bind}, delta_bind={delta_bind}, expr={expr}, "
            f"delta_expr={delta_expr}, confidence_bind={conf_bind}, "
            f"confidence_expr={conf_expr}. All unitless."
        ),
        "template_uri": TYPE7_TEMPLATE,
        "variant_fdo": VARIANT_ANCHORS[variant],
        "method_fdo": BLOOM_METHOD,
        "bind": bind,
        "delta_bind": delta_bind,
        "expr": expr,
        "delta_expr": delta_expr,
        "confidence_bind": conf_bind,
        "confidence_expr": conf_expr,
        **SHARED,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", type=Path)
    ap.add_argument("--out-dir", type=Path, required=True)
    ap.add_argument("--created", default=None)
    args = ap.parse_args()

    rows_by_variant = pick_esm_rows(args.csv)
    if len(rows_by_variant) != 3:
        sys.stderr.write(f"WARNING: expected 3 ESM rows, found {len(rows_by_variant)}\n")
    created = args.created or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    args.out_dir.mkdir(parents=True, exist_ok=True)

    print(f"{'variant':<8} {'type':<10} {'instance_id':<20} {'key value(s)'}")
    print(f"{'-'*92}")
    errs = 0

    for variant in ("Alpha", "Epsilon", "Eta"):
        row = rows_by_variant[variant]
        # Type 6
        cfg6 = build_type6_config(variant, row)
        errors = validate_prediction_config(cfg6)
        if errors:
            sys.stderr.write(f"  Type 6 {variant} config errors: {errors}\n")
            errs += 1
        else:
            out = generate_prediction_instance(cfg6, created)
            chk = check_mandatory_prediction_statements(out, cfg6["class_curie"], cfg6["metric_predicate"])
            if chk["missing"] or chk["forbidden_present"]:
                sys.stderr.write(f"  Type 6 {variant} check failed: {chk}\n")
                errs += 1
            else:
                path = args.out_dir / f"instance_type6_{variant.lower()}_v1.trig"
                path.write_text(out)
                print(f"{variant:<8} {'Type 6':<10} {cfg6['instance_id']:<20} AgMata={cfg6['metric_value']}")
        # Type 7
        cfg7 = build_type7_config(variant, row)
        errors = validate_dms_config(cfg7)
        if errors:
            sys.stderr.write(f"  Type 7 {variant} config errors: {errors}\n")
            errs += 1
        else:
            out = generate_dms_instance(cfg7, created)
            chk = check_mandatory_dms_statements(out)
            if chk["missing"] or chk["forbidden_present"]:
                sys.stderr.write(f"  Type 7 {variant} check failed: {chk}\n")
                errs += 1
            else:
                path = args.out_dir / f"instance_type7_{variant.lower()}_v1.trig"
                path.write_text(out)
                print(f"{variant:<8} {'Type 7':<10} {cfg7['instance_id']:<20} bind={cfg7['bind']} expr={cfg7['expr']}")

    if errs:
        sys.stderr.write(f"FAILED: {errs} instances had errors\n")
        return 1
    sys.stderr.write(f"OK: wrote 6 instances (3 Type 6 + 3 Type 7) to {args.out_dir}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
