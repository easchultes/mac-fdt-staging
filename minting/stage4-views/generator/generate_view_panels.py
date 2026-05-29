#!/usr/bin/env python3
"""Stage 4 embedded panels — gen:View wrappers + gen:ViewDisplay actions.

Two artifact kinds emitted by this script:

  1. **Wrapper nanopub** — a `gen:ResourceView, gen:TabularView` that
     wraps one of our grlc-query nanopubs with display metadata
     (title, structural position, applies-to-instances, query target
     field). Created from template `RARLsTlqbTesu1b0WJZ-zL1z96xumOiqbK3l_vV6iZoww`
     ("Declaring a resource view").

  2. **ViewDisplay nanopub** — a `gen:ActivatedViewDisplay,
     gen:ViewDisplay` that anchors the wrapper to the project4 Space
     page. `gen:isDisplayOfView` points at the wrapper's referent URI
     (`<wrapper-trusty>/<view-local-name>`), so this CLI command needs
     the wrapper's signed Trusty URI as input. Created from template
     `RAsc8FMsGih955oFSFG0YcB9sDKA62VLbp3VIw86IxMvk` ("Displaying a view
     for a Space").

Usage:
    python generate_view_panels.py emit-wrappers --out-dir drafts/
    python generate_view_panels.py emit-viewdisplay <view-key> <wrapper-trusty> --out-dir drafts/
"""

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path


VIEW_TEMPLATE_URI         = "https://w3id.org/np/RARLsTlqbTesu1b0WJZ-zL1z96xumOiqbK3l_vV6iZoww"
VIEWDISPLAY_TEMPLATE_URI  = "https://w3id.org/np/RAsc8FMsGih955oFSFG0YcB9sDKA62VLbp3VIw86IxMvk"
PROVENANCE_TEMPLATE_URI   = "https://w3id.org/np/RA7lSq6MuK_TIC6JMSHvLtee3lpLoZDOqLJCLXevnrPoU"
PUBINFO_TEMPLATES = [
    "https://w3id.org/np/RA0J4vUn_dekg-U1kK3AOEt02p9mT2WO03uGxLDec1jLw",  # License
    "https://w3id.org/np/RAukAcWHRDlkqxk7H2XNSegc1WnHI569INvNr-xdptDGI",  # Creator
    "https://w3id.org/np/RAMEgudZsQ1bh1fZhfYnkthqH6YSXpghSE_DEN1I-6eAI",  # Hand-coded
    "https://w3id.org/np/RARW4MsFkHuwjycNElvEVtuMjpf4yWDL10-0C5l2MqqRQ",  # Derived
]

SPACE_URI       = "https://w3id.org/spaces/knowledgepixels/incubator/project4"
CREATOR_ORCID   = "0000-0001-8888-635X"
CC_BY_4         = "https://creativecommons.org/licenses/by/4.0/"


# ============================================================
# View specs (per Phase 1 review)
# ============================================================

VIEWS = [
    {
        "key": "catalogue-summary",
        "view_local": "fdt-catalogue-summary-view",
        "viewkind_local": "fdt-catalogue-summary-view-kind",
        "query_uri": "https://w3id.org/np/RAGlsCUDZrgFmlRQ8RNIpaWHaKAnRX7SGjEqOCGoWsM8A",
        "title": "MAC FDT — catalogue summary by type",
        "label": "MAC FDT — catalogue summary by type view",
        "structural_position": "5.1.fdt-catalogue-summary",
    },
    {
        "key": "variants-by-who",
        "view_local": "fdt-variants-by-who-view",
        "viewkind_local": "fdt-variants-by-who-view-kind",
        "query_uri": "https://w3id.org/np/RAlD3u-iOS5P95TlvydUePQCOqKyVsPLebBNTnu4lw7po",
        "title": "MAC FDT — variants by WHO classification",
        "label": "MAC FDT — variants by WHO classification view",
        "structural_position": "5.2.fdt-variants-by-who",
    },
    {
        "key": "observations-per-method",
        "view_local": "fdt-observations-per-method-view",
        "viewkind_local": "fdt-observations-per-method-view-kind",
        "query_uri": "https://w3id.org/np/RAIKnskDgF8ZX-hOIC1UKLSxDapH1K1FjkNKi5Or-A3ws",
        "title": "MAC FDT — observations per method",
        "label": "MAC FDT — observations per method view",
        "structural_position": "5.3.fdt-observations-per-method",
    },
    {
        "key": "alpha-knowlet",
        "view_local": "fdt-alpha-knowlet-view",
        "viewkind_local": "fdt-alpha-knowlet-view-kind",
        "query_uri": "https://w3id.org/np/RAecvUbvUWiIOKP7ZEQk7hnUsb8lWWUr1lRbVN2PsSUSA",
        "title": "MAC FDT — Alpha variant digital twin",
        "label": "MAC FDT — Alpha variant digital twin view",
        "structural_position": "5.4.fdt-alpha-knowlet",
    },
]


def get_view(key):
    for v in VIEWS:
        if v["key"] == key:
            return v
    raise SystemExit(f"Unknown view key: {key}")


# ============================================================
# Wrapper template
# ============================================================

WRAPPER_TRIG = """\
@prefix this: <http://purl.org/nanopub/temp/np001/> .
@prefix sub: <http://purl.org/nanopub/temp/np001/> .
@prefix np: <http://www.nanopub.org/nschema#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix nt: <https://w3id.org/np/o/ntemplate/> .
@prefix npx: <http://purl.org/nanopub/x/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix orcid: <https://orcid.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .

sub:Head {{
  this: a np:Nanopublication ;
    np:hasAssertion sub:assertion ;
    np:hasProvenance sub:provenance ;
    np:hasPublicationInfo sub:pubinfo .
}}

sub:assertion {{
  sub:{view_local} a <https://w3id.org/kpxl/gen/terms/ResourceView>, <https://w3id.org/kpxl/gen/terms/TabularView> ;
    dct:isVersionOf sub:{viewkind_local} ;
    dct:title "{title}" ;
    rdfs:label "{label}" ;
    <https://w3id.org/kpxl/gen/terms/appliesToInstancesOf> <https://w3id.org/kpxl/gen/terms/Space> ;
    <https://w3id.org/kpxl/gen/terms/hasStructuralPosition> "{structural_position}" ;
    <https://w3id.org/kpxl/gen/terms/hasViewQuery> <{query_uri}> ;
    <https://w3id.org/kpxl/gen/terms/hasViewQueryTargetField> "resource" .
}}

sub:provenance {{
  sub:assertion prov:wasAttributedTo orcid:{creator_orcid} .
}}

sub:pubinfo {{
  this: dct:created "{created}"^^xsd:dateTime ;
    dct:creator orcid:{creator_orcid} ;
    dct:license <{cc_by_4}> ;
    rdfs:label "{label}" ;
    npx:embeds sub:{view_local} ;
    npx:introduces sub:{viewkind_local} ;
    nt:wasCreatedFromTemplate <{view_template_uri}> ;
    nt:wasCreatedFromProvenanceTemplate <{provenance_template_uri}> ;
    nt:wasCreatedFromPubinfoTemplate
      <{pubinfo_1}>,
      <{pubinfo_2}>,
      <{pubinfo_3}>,
      <{pubinfo_4}> .
}}
"""


# ============================================================
# ViewDisplay template
# ============================================================

VIEWDISPLAY_TRIG = """\
@prefix this: <http://purl.org/nanopub/temp/np001/> .
@prefix sub: <http://purl.org/nanopub/temp/np001/> .
@prefix np: <http://www.nanopub.org/nschema#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix nt: <https://w3id.org/np/o/ntemplate/> .
@prefix npx: <http://purl.org/nanopub/x/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix orcid: <https://orcid.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .

sub:Head {{
  this: a np:Nanopublication ;
    np:hasAssertion sub:assertion ;
    np:hasProvenance sub:provenance ;
    np:hasPublicationInfo sub:pubinfo .
}}

sub:assertion {{
  sub:display a <https://w3id.org/kpxl/gen/terms/ActivatedViewDisplay>, <https://w3id.org/kpxl/gen/terms/ViewDisplay> ;
    <https://w3id.org/kpxl/gen/terms/appliesTo> <{space_uri}> ;
    <https://w3id.org/kpxl/gen/terms/isDisplayFor> <{space_uri}> ;
    <https://w3id.org/kpxl/gen/terms/isDisplayOfView> <{view_referent_uri}> .
}}

sub:provenance {{
  sub:assertion prov:wasAttributedTo orcid:{creator_orcid} .
}}

sub:pubinfo {{
  this: dct:created "{created}"^^xsd:dateTime ;
    dct:creator orcid:{creator_orcid} ;
    dct:license <{cc_by_4}> ;
    rdfs:label "Knowledge Pixels Incubator #4: FAIRification of mass spectrometry workflows using FDOs displays view: {view_local}" ;
    npx:embeds sub:display ;
    nt:wasCreatedFromTemplate <{viewdisplay_template_uri}> ;
    nt:wasCreatedFromProvenanceTemplate <{provenance_template_uri}> ;
    nt:wasCreatedFromPubinfoTemplate
      <{pubinfo_1}>,
      <{pubinfo_2}>,
      <{pubinfo_3}>,
      <{pubinfo_4}> .
}}
"""


# ============================================================
# Emit
# ============================================================

def emit_wrapper(view, created):
    return WRAPPER_TRIG.format(
        view_local=view["view_local"],
        viewkind_local=view["viewkind_local"],
        title=view["title"],
        label=view["label"],
        structural_position=view["structural_position"],
        query_uri=view["query_uri"],
        creator_orcid=CREATOR_ORCID,
        created=created,
        cc_by_4=CC_BY_4,
        view_template_uri=VIEW_TEMPLATE_URI,
        provenance_template_uri=PROVENANCE_TEMPLATE_URI,
        pubinfo_1=PUBINFO_TEMPLATES[0],
        pubinfo_2=PUBINFO_TEMPLATES[1],
        pubinfo_3=PUBINFO_TEMPLATES[2],
        pubinfo_4=PUBINFO_TEMPLATES[3],
    )


def emit_viewdisplay(view, wrapper_trusty, created):
    view_referent_uri = f"{wrapper_trusty}/{view['view_local']}"
    return VIEWDISPLAY_TRIG.format(
        space_uri=SPACE_URI,
        view_referent_uri=view_referent_uri,
        view_local=view["view_local"],
        creator_orcid=CREATOR_ORCID,
        created=created,
        cc_by_4=CC_BY_4,
        viewdisplay_template_uri=VIEWDISPLAY_TEMPLATE_URI,
        provenance_template_uri=PROVENANCE_TEMPLATE_URI,
        pubinfo_1=PUBINFO_TEMPLATES[0],
        pubinfo_2=PUBINFO_TEMPLATES[1],
        pubinfo_3=PUBINFO_TEMPLATES[2],
        pubinfo_4=PUBINFO_TEMPLATES[3],
    )


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_w = sub.add_parser("emit-wrappers", help="Emit all 4 wrapper drafts")
    p_w.add_argument("--out-dir", type=Path, required=True)
    p_w.add_argument("--created", default=None)

    p_v = sub.add_parser("emit-viewdisplay", help="Emit one ViewDisplay")
    p_v.add_argument("view_key")
    p_v.add_argument("wrapper_trusty")
    p_v.add_argument("--out-dir", type=Path, required=True)
    p_v.add_argument("--created", default=None)

    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    created = args.created or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    if args.cmd == "emit-wrappers":
        for v in VIEWS:
            out = emit_wrapper(v, created)
            path = args.out_dir / f"wrapper_{v['key']}_v1.trig"
            path.write_text(out)
            print(f"  wrote {path} ({len(out)} bytes)")
    elif args.cmd == "emit-viewdisplay":
        v = get_view(args.view_key)
        out = emit_viewdisplay(v, args.wrapper_trusty, created)
        path = args.out_dir / f"viewdisplay_{v['key']}_v1.trig"
        path.write_text(out)
        print(f"  wrote {path} ({len(out)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
