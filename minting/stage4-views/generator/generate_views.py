#!/usr/bin/env python3
"""Stage 4 view generator.

Emits two kinds of nanopubs for pinning standing SPARQL views on
incubator/project4:

  1. grlc-query nanopubs — created from template
     RAEFAt-QcFK0ZhqfvlsmS10BnzGJA0xwOICZXkO-ai87k. One nanopub per
     view, carrying rdfs:label, dct:description, dct:license (Apache),
     <grlc/endpoint>, and <grlc/sparql> (verbatim).
  2. pin-query action nanopubs — created from template
     RAuLESdeRUlk1GcTwvzVXShiBMI0ntJs2DL2Bm5DzW_ZQ. One nanopub per
     view, asserting <project4-space> gen:hasPinnedQuery <query> and
     <query> gen:hasPinGroupTag "<tag>".

Usage:
    python generate_views.py emit-queries --out-dir drafts/
    python generate_views.py emit-pins <view> <query-trusty-uri> --out-dir drafts/
"""

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path


# ============================================================
# Hardcoded refs
# ============================================================

QUERY_TEMPLATE_URI    = "https://w3id.org/np/RAEFAt-QcFK0ZhqfvlsmS10BnzGJA0xwOICZXkO-ai87k"
PIN_QUERY_TEMPLATE_URI = "https://w3id.org/np/RAuLESdeRUlk1GcTwvzVXShiBMI0ntJs2DL2Bm5DzW_ZQ"
PROVENANCE_TEMPLATE_URI = "https://w3id.org/np/RA7lSq6MuK_TIC6JMSHvLtee3lpLoZDOqLJCLXevnrPoU"
PUBINFO_TEMPLATES = [
    "https://w3id.org/np/RA0J4vUn_dekg-U1kK3AOEt02p9mT2WO03uGxLDec1jLw",  # License
    "https://w3id.org/np/RAukAcWHRDlkqxk7H2XNSegc1WnHI569INvNr-xdptDGI",  # Creator
    "https://w3id.org/np/RAMEgudZsQ1bh1fZhfYnkthqH6YSXpghSE_DEN1I-6eAI",  # Hand-coded
    "https://w3id.org/np/RARW4MsFkHuwjycNElvEVtuMjpf4yWDL10-0C5l2MqqRQ",  # Derived
]

SPARQL_ENDPOINT = "https://w3id.org/np/l/nanopub-query-1.1/repo/full"
SPACE_URI       = "https://w3id.org/spaces/knowledgepixels/incubator/project4"
APACHE_LICENSE  = "https://www.apache.org/licenses/LICENSE-2.0"
CC_BY_4         = "https://creativecommons.org/licenses/by/4.0/"

CREATOR_ORCID = "0000-0001-8888-635X"


# ============================================================
# View specs — verbatim Phase-1 SPARQL
# ============================================================

SHARED_PREFIXES = """PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX np:   <http://www.nanopub.org/nschema#>
PREFIX npa:  <http://purl.org/nanopub/admin/>
PREFIX npx:  <http://purl.org/nanopub/x/>
PREFIX dct:  <http://purl.org/dc/terms/>
PREFIX fdof: <https://w3id.org/fdof/ontology#>
PREFIX mac:  <https://w3id.org/spaces/mac/r/ontology/>"""

SIG_BLOCK = """  GRAPH npa:graph {
    ?n1 npa:hasValidSignatureForPublicKey ?pubkey .
    filter not exists {
      ?np2 npx:invalidates ?n1 ;
           npa:hasValidSignatureForPublicKey ?pubkey .
    }
    ?n1 np:hasAssertion ?a .
  }"""

VIEWS = [
    {
        "key": "catalogue-summary",
        "local_name": "catalogue-summary-by-type",
        "label": "MAC FDT — catalogue summary by type",
        "description": (
            "Counts of MAC FDT FDOs grouped by their specific type "
            "(variants, observations, methods). Bounded summary view "
            "of the full catalogue."
        ),
        "group_tag": "Catalogue overview",
        "sparql": (
            SHARED_PREFIXES + "\n\n"
            "SELECT ?type (COUNT(?thing) AS ?count) WHERE {\n"
            + SIG_BLOCK + "\n"
            "  graph ?a {\n"
            "    ?thing a fdof:FAIRDigitalObject .\n"
            "    ?thing a ?type .\n"
            "    FILTER(?type != fdof:FAIRDigitalObject)\n"
            "    FILTER(STRSTARTS(STR(?type), \"https://w3id.org/spaces/mac/r/ontology/\"))\n"
            "  }\n"
            "} GROUP BY ?type ORDER BY DESC(?count)"
        ),
    },
    {
        "key": "variants-by-who",
        "local_name": "variants-by-who-classification",
        "label": "MAC FDT — variants by WHO classification",
        "description": (
            "Counts of Spike RBD variants grouped by WHO risk "
            "designation (VOC / VOI / VUM), via their WHO classification "
            "observation FDOs."
        ),
        "group_tag": "Situational dashboards",
        "sparql": (
            SHARED_PREFIXES + "\n\n"
            "SELECT ?whoClass (COUNT(?variant) AS ?count) WHERE {\n"
            + SIG_BLOCK + "\n"
            "  graph ?a {\n"
            "    ?obs a mac:WHOVariantClassification .\n"
            "    ?obs mac:hasWHOClassification ?whoClass .\n"
            "    ?obs mac:isObservationOf ?variant .\n"
            "  }\n"
            "} GROUP BY ?whoClass ORDER BY DESC(?count)"
        ),
    },
    {
        "key": "observations-per-method",
        "local_name": "observations-per-method",
        "label": "MAC FDT — observations per method",
        "description": (
            "Counts of observation FDOs grouped by the method "
            "(computational, experimental, or surveillance) that "
            "produced them — demonstrating multi-source decentralized "
            "attribution."
        ),
        "group_tag": "Situational dashboards",
        "sparql": (
            SHARED_PREFIXES + "\n\n"
            "SELECT ?method (COUNT(?obs) AS ?count) WHERE {\n"
            + SIG_BLOCK + "\n"
            "  graph ?a {\n"
            "    ?obs ?methodPred ?method .\n"
            "    VALUES ?methodPred { mac:hasPredictionMethod mac:hasExperimentalMethod mac:hasSurveillanceMethod }\n"
            "  }\n"
            "} GROUP BY ?method ORDER BY DESC(?count)"
        ),
    },
    {
        "key": "alpha-knowlet",
        "local_name": "alpha-knowlet",
        "label": "MAC FDT — Alpha variant digital twin (knowlet)",
        "description": (
            "All observation FDOs about the Alpha Spike RBD variant — "
            "real-world occurrence, computational predictions, "
            "experimental DMS, and WHO classification — forming the "
            "FAIR Digital Twin knowlet for Alpha. Worked example of a "
            "single FDT."
        ),
        "group_tag": "Digital twin (worked example)",
        "sparql": (
            SHARED_PREFIXES + "\n\n"
            "SELECT ?obs ?type ?label WHERE {\n"
            + SIG_BLOCK + "\n"
            "  graph ?a {\n"
            "    ?obs mac:isObservationOf <https://w3id.org/np/RA4BHII2Bz7HfpUkaSJqNmhjF8F7hyWpCJnvXYkA4EP_M/Alpha-RBD-Variant> .\n"
            "    ?obs a ?type .\n"
            "    FILTER(?type != fdof:FAIRDigitalObject)\n"
            "    OPTIONAL { ?obs rdfs:label ?label . }\n"
            "  }\n"
            "} ORDER BY ?type"
        ),
    },
]


def get_view(key):
    for v in VIEWS:
        if v["key"] == key:
            return v
    raise SystemExit(f"Unknown view key: {key}")


# ============================================================
# Templates
# ============================================================

QUERY_TRIG = """\
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
  sub:{local_name} a <https://w3id.org/kpxl/grlc/grlc-query> ;
    rdfs:label "{label}" ;
    dct:description "{description}" ;
    dct:license <{apache_license}> ;
    <https://w3id.org/kpxl/grlc/endpoint> <{sparql_endpoint}> ;
    <https://w3id.org/kpxl/grlc/sparql> \"\"\"{sparql}\"\"\" .
}}

sub:provenance {{
  sub:assertion prov:wasAttributedTo orcid:{creator_orcid} .
}}

sub:pubinfo {{
  this: dct:created "{created}"^^xsd:dateTime ;
    dct:creator orcid:{creator_orcid} ;
    dct:license <{cc_by_4}> ;
    rdfs:label "{label}" ;
    npx:introduces sub:{local_name} ;
    nt:wasCreatedFromTemplate <{query_template_uri}> ;
    nt:wasCreatedFromProvenanceTemplate <{provenance_template_uri}> ;
    nt:wasCreatedFromPubinfoTemplate
      <{pubinfo_1}>,
      <{pubinfo_2}>,
      <{pubinfo_3}>,
      <{pubinfo_4}> .
}}
"""

PIN_TRIG = """\
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
  <{query_trusty}> <https://w3id.org/kpxl/gen/terms/hasPinGroupTag> "{group_tag}" .
  <{space_uri}> <https://w3id.org/kpxl/gen/terms/hasPinnedQuery> <{query_trusty}> .
}}

sub:provenance {{
  sub:assertion prov:wasAttributedTo orcid:{creator_orcid} .
}}

sub:pubinfo {{
  this: dct:created "{created}"^^xsd:dateTime ;
    dct:creator orcid:{creator_orcid} ;
    dct:license <{cc_by_4}> ;
    npx:hasNanopubType <https://w3id.org/kpxl/gen/terms/hasPinnedQuery> ;
    rdfs:label "Knowledge Pixels Incubator #4: FAIRification of mass spectrometry workflows using FDOs has pinned query: {label}" ;
    nt:wasCreatedFromTemplate <{pin_query_template_uri}> ;
    nt:wasCreatedFromProvenanceTemplate <{provenance_template_uri}> ;
    nt:wasCreatedFromPubinfoTemplate
      <{pubinfo_1}>,
      <{pubinfo_2}>,
      <{pubinfo_3}>,
      <{pubinfo_4}> .
}}
"""


# ============================================================
# Emit functions
# ============================================================

def emit_query(view, created):
    return QUERY_TRIG.format(
        local_name=view["local_name"],
        label=view["label"],
        description=view["description"],
        sparql=view["sparql"],
        apache_license=APACHE_LICENSE,
        sparql_endpoint=SPARQL_ENDPOINT,
        creator_orcid=CREATOR_ORCID,
        created=created,
        cc_by_4=CC_BY_4,
        query_template_uri=QUERY_TEMPLATE_URI,
        provenance_template_uri=PROVENANCE_TEMPLATE_URI,
        pubinfo_1=PUBINFO_TEMPLATES[0],
        pubinfo_2=PUBINFO_TEMPLATES[1],
        pubinfo_3=PUBINFO_TEMPLATES[2],
        pubinfo_4=PUBINFO_TEMPLATES[3],
    )


def emit_pin(view, query_trusty, created):
    return PIN_TRIG.format(
        query_trusty=query_trusty,
        group_tag=view["group_tag"],
        space_uri=SPACE_URI,
        label=view["label"],
        creator_orcid=CREATOR_ORCID,
        created=created,
        cc_by_4=CC_BY_4,
        pin_query_template_uri=PIN_QUERY_TEMPLATE_URI,
        provenance_template_uri=PROVENANCE_TEMPLATE_URI,
        pubinfo_1=PUBINFO_TEMPLATES[0],
        pubinfo_2=PUBINFO_TEMPLATES[1],
        pubinfo_3=PUBINFO_TEMPLATES[2],
        pubinfo_4=PUBINFO_TEMPLATES[3],
    )


# ============================================================
# CLI
# ============================================================

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_q = sub.add_parser("emit-queries", help="Emit all 4 query drafts")
    p_q.add_argument("--out-dir", type=Path, required=True)
    p_q.add_argument("--created", default=None)

    p_p = sub.add_parser("emit-pin", help="Emit one pin-query action draft")
    p_p.add_argument("view_key")
    p_p.add_argument("query_trusty")
    p_p.add_argument("--out-dir", type=Path, required=True)
    p_p.add_argument("--created", default=None)

    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    created = args.created or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    if args.cmd == "emit-queries":
        for v in VIEWS:
            out = emit_query(v, created)
            path = args.out_dir / f"query_{v['key']}_v1.trig"
            path.write_text(out)
            print(f"  wrote {path} ({len(out)} bytes)")
    elif args.cmd == "emit-pin":
        v = get_view(args.view_key)
        out = emit_pin(v, args.query_trusty, created)
        path = args.out_dir / f"pin_{v['key']}_v1.trig"
        path.write_text(out)
        print(f"  wrote {path} ({len(out)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
