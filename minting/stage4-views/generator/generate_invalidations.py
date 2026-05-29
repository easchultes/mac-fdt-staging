#!/usr/bin/env python3
"""Author Stage 4 fix — invalidation nanopubs.

Emits invalidation nanopubs of the form:
    sub:assertion {
      this: npx:invalidates <target> ;
        rdfs:comment "<reason>" .
    }

This matches the pattern the get-all-datasets exemplar's SPARQL filter
recognises:
    filter not exists {
      ?np2 npx:invalidates ?n1 ;
           npa:hasValidSignatureForPublicKey ?pubkey .
    }

Hand-authored (no template), signed by Erik. Standard pubinfo bundle.
"""

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path


CREATOR_ORCID = "0000-0001-8888-635X"
CC_BY_4 = "https://creativecommons.org/licenses/by/4.0/"

PROVENANCE_TEMPLATE_URI = "https://w3id.org/np/RA7lSq6MuK_TIC6JMSHvLtee3lpLoZDOqLJCLXevnrPoU"
PUBINFO_TEMPLATES = [
    "https://w3id.org/np/RA0J4vUn_dekg-U1kK3AOEt02p9mT2WO03uGxLDec1jLw",  # License
    "https://w3id.org/np/RAukAcWHRDlkqxk7H2XNSegc1WnHI569INvNr-xdptDGI",  # Creator
    "https://w3id.org/np/RAMEgudZsQ1bh1fZhfYnkthqH6YSXpghSE_DEN1I-6eAI",  # Hand-coded
    "https://w3id.org/np/RARW4MsFkHuwjycNElvEVtuMjpf4yWDL10-0C5l2MqqRQ",  # Derived
]


TRIG = """\
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
  this: npx:invalidates <{target}> ;
    rdfs:comment "{reason}" .
}}

sub:provenance {{
  sub:assertion prov:wasAttributedTo orcid:{creator_orcid} .
}}

sub:pubinfo {{
  this: dct:created "{created}"^^xsd:dateTime ;
    dct:creator orcid:{creator_orcid} ;
    dct:license <{cc_by_4}> ;
    rdfs:label "{label}" ;
    nt:wasCreatedFromProvenanceTemplate <{provenance_template_uri}> ;
    nt:wasCreatedFromPubinfoTemplate
      <{pubinfo_1}>,
      <{pubinfo_2}>,
      <{pubinfo_3}>,
      <{pubinfo_4}> .
}}
"""


TARGETS = [
    {
        "key": "catalogue-summary",
        "target": "https://w3id.org/np/RAq9o-TF0vcyIvK7Rn79IBIj1ePoZI1mAcErhVQjUb4vA",
        "label": "Invalidating ViewDisplay RAq9o-TF0vcy (catalogue-summary, 2026-05-28 11:14Z)",
        "reason": (
            "Invalidating: ViewDisplay nanopub conflates two pinning mechanisms - "
            "gen:isDisplayOfView requires a gen:View wrapper, not a bare grlc-query. "
            "The P135 pin-action (gen:hasPinnedQuery on the bare query "
            "RAGlsCUDZrgFmlRQ8RNIpaWHaKAnRX7SGjEqOCGoWsM8A) remains correct and operates "
            "the project4 Queries sidebar pinning."
        ),
    },
    {
        "key": "alpha-knowlet",
        "target": "https://w3id.org/np/RAD5G7Z3kY14tsHLtunCJ26xpimAJ2-q1Thpf-4B8be84",
        "label": "Invalidating ViewDisplay RAD5G7Z3kY14 (alpha-knowlet, 2026-05-28 17:56Z)",
        "reason": (
            "Invalidating: ViewDisplay nanopub conflates two pinning mechanisms - "
            "gen:isDisplayOfView requires a gen:View wrapper, not a bare grlc-query. "
            "The P135 pin-action (gen:hasPinnedQuery on the bare query "
            "RAecvUbvUWiIOKP7ZEQk7hnUsb8lWWUr1lRbVN2PsSUSA) remains correct and operates "
            "the project4 Queries sidebar pinning."
        ),
    },
]


def emit(target, label, reason, created):
    return TRIG.format(
        target=target,
        reason=reason,
        label=label,
        creator_orcid=CREATOR_ORCID,
        created=created,
        cc_by_4=CC_BY_4,
        provenance_template_uri=PROVENANCE_TEMPLATE_URI,
        pubinfo_1=PUBINFO_TEMPLATES[0],
        pubinfo_2=PUBINFO_TEMPLATES[1],
        pubinfo_3=PUBINFO_TEMPLATES[2],
        pubinfo_4=PUBINFO_TEMPLATES[3],
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", type=Path, required=True)
    ap.add_argument("--created", default=None)
    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    created = args.created or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for t in TARGETS:
        out = emit(t["target"], t["label"], t["reason"], created)
        path = args.out_dir / f"invalidate_{t['key']}_viewdisplay_v1.trig"
        path.write_text(out)
        print(f"  wrote {path} ({len(out)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
