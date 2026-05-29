#!/usr/bin/env python3
"""Author retraction nanopubs using the canonical npx:retracts pattern
(NanoDash template `Retracting a nanopublication that I published`).

Per Tobias's guidance: `npx:retracts` is the publisher-facing predicate;
`npx:invalidates` is an internal query-repo generalization that the
admin layer derives from retractions (and other invalidating events).

Assertion shape (matches the standard retraction template):

    sub:assertion {
      orcid:<creator> npx:retracts <target> .
      sub:assertion rdfs:comment "<reason>" .
    }

Pubinfo carries `npx:hasNanopubType npx:retracts` and references the
retraction template via `nt:wasCreatedFromTemplate`.

Signed by Erik (who originally published every target — required for
npx:retracts to take effect).
"""

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path


CREATOR_ORCID = "0000-0001-8888-635X"
CC_BY_4 = "https://creativecommons.org/licenses/by/4.0/"

RETRACTION_TEMPLATE_URI  = "http://purl.org/np/RAQP3NJvnLA2Z-2DrYAN0nTC-RFp67td1t4-pQqQ_ZKmo"
PROVENANCE_TEMPLATE_URI  = "https://w3id.org/np/RA7lSq6MuK_TIC6JMSHvLtee3lpLoZDOqLJCLXevnrPoU"
PUBINFO_TEMPLATES = [
    "https://w3id.org/np/RA0J4vUn_dekg-U1kK3AOEt02p9mT2WO03uGxLDec1jLw",  # License
    "https://w3id.org/np/RAukAcWHRDlkqxk7H2XNSegc1WnHI569INvNr-xdptDGI",  # Creator
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
  orcid:{creator_orcid} npx:retracts <{target}> .
  sub:assertion rdfs:comment "{reason}" .
}}

sub:provenance {{
  sub:assertion prov:wasAttributedTo orcid:{creator_orcid} .
}}

sub:pubinfo {{
  this: dct:created "{created}"^^xsd:dateTime ;
    dct:creator orcid:{creator_orcid} ;
    dct:license <{cc_by_4}> ;
    npx:hasNanopubType npx:retracts ;
    rdfs:label "{label}" ;
    nt:wasCreatedFromTemplate <{retraction_template_uri}> ;
    nt:wasCreatedFromProvenanceTemplate <{provenance_template_uri}> ;
    nt:wasCreatedFromPubinfoTemplate
      <{pubinfo_1}>,
      <{pubinfo_2}> .
}}
"""


REASON_VIEWDISPLAY = (
    "Conflated mechanism: ViewDisplay (gen:isDisplayOfView) requires "
    "a gen:View wrapper, not a bare grlc-query."
)

REASON_BAD_INVALIDATION = (
    "Wrong mechanism: used npx:invalidates rather than the publisher-"
    "facing npx:retracts. Superseded by an npx:retracts-based "
    "retraction in the same fix branch."
)

TARGETS = [
    {
        "key": "viewdisplay-catalogue-summary",
        "target": "https://w3id.org/np/RAq9o-TF0vcyIvK7Rn79IBIj1ePoZI1mAcErhVQjUb4vA",
        "label": "Retraction of RAq9o-TF0vcy (broken ViewDisplay, catalogue-summary)",
        "reason": REASON_VIEWDISPLAY,
    },
    {
        "key": "viewdisplay-alpha-knowlet",
        "target": "https://w3id.org/np/RAD5G7Z3kY14tsHLtunCJ26xpimAJ2-q1Thpf-4B8be84",
        "label": "Retraction of RAD5G7Z3kY14 (broken ViewDisplay, alpha-knowlet)",
        "reason": REASON_VIEWDISPLAY,
    },
    {
        "key": "invalidation-catalogue-summary",
        "target": "https://w3id.org/np/RAUVFxrhms_YLANEQdoQjn8nNgDRW18ZcRx3m-mndVXRY",
        "label": "Retraction of RAUVFxrhms_ (mistaken npx:invalidates nanopub, catalogue-summary)",
        "reason": REASON_BAD_INVALIDATION,
    },
    {
        "key": "invalidation-alpha-knowlet",
        "target": "https://w3id.org/np/RA0aGsMc41L8xLWfJeXpTUMz-py1vMpBJSIy1P13xaxX8",
        "label": "Retraction of RA0aGsMc41L (mistaken npx:invalidates nanopub, alpha-knowlet)",
        "reason": REASON_BAD_INVALIDATION,
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
        retraction_template_uri=RETRACTION_TEMPLATE_URI,
        provenance_template_uri=PROVENANCE_TEMPLATE_URI,
        pubinfo_1=PUBINFO_TEMPLATES[0],
        pubinfo_2=PUBINFO_TEMPLATES[1],
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
        path = args.out_dir / f"retract_{t['key']}_v1.trig"
        path.write_text(out)
        print(f"  wrote {path} ({len(out)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
