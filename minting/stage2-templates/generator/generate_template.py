#!/usr/bin/env python3
"""Stage 2 template generator (MAC FDT).

Emits a nanopub-template TriG file for one of the 11 MAC FDT types. The
4-graph scaffold — prefixes, Head, external-term labels, standard
placeholders, FDO-typing statements, descriptive statements, the
self-materialization block, the SPS v1.3 institutional-provenance
statement, the FAIR² cross-references, provenance, and pubinfo bundle —
is identical across all 11 types and is hardcoded here. The per-type
config (e.g. configs/type1_config.py) supplies the class URI, label
pattern, description, type-specific external-term labels, placeholders,
and statements.

The Type 1 config must round-trip the v4 source byte-for-byte modulo the
dct:created timestamp in the pubinfo graph.

Usage:
    python generate_template.py configs/type1_config.py > out.trig
    python generate_template.py configs/type1_config.py --diff drafts/template_type1_spike_rbd_variant_v4.trig
"""

import argparse
import difflib
import importlib.util
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


# Column at which `rdfs:label` aligns inside the URI external-labels block.
# 2-space indent + URI + padding-to-col-53 + `rdfs:label`.
URI_LABEL_COL = 53
# Baseline column for `rdfs:label` inside the curie (mac:*) labels block.
# 2-space indent + curie + padding + `rdfs:label`. The actual column
# is auto-extended when the type's longest curie exceeds 22 chars, so
# each type's block is internally aligned to its widest curie with a
# 2-space minimum gap. Type 1 (max 22 chars) lands at 26; Type 2 (max
# 25 chars) at 29.
CURIE_LABEL_BASELINE_COL = 26
CURIE_LABEL_MIN_GAP = 2


# ============================================================
# Renderers for type-specific slots
# ============================================================

def render_uri_label(uri: str, label: str) -> str:
    """Emit one external-term label line for a full URI.

    Aligns `rdfs:label` to URI_LABEL_COL. If the URI is too wide,
    pushes `rdfs:label` onto the next line with leading whitespace
    that reaches URI_LABEL_COL.
    """
    bracketed = f"<{uri}>"
    prefix = "  " + bracketed
    if len(prefix) + 1 <= URI_LABEL_COL:
        padding = " " * (URI_LABEL_COL - len(prefix))
        return f'{prefix}{padding}rdfs:label "{label}" .'
    indent = " " * URI_LABEL_COL
    return f'{prefix}\n{indent}rdfs:label "{label}" .'


def render_curie_label(curie: str, label: str, align_col: int) -> str:
    """Emit one external-term label line for a prefixed name (e.g. mac:Foo)."""
    prefix = "  " + curie
    padding = " " * max(1, align_col - len(prefix))
    return f'{prefix}{padding}rdfs:label "{label}" .'


def render_external_resource_labels(config) -> str:
    """Type-specific external-resource URI labels (e.g. UniProt P0DTC2).

    Sits between the common scaffold's FDO/dcat/FIP labels and the
    common FAIR²/format/license labels. Empty string if the type
    declares no such resources.
    """
    items = config.get("external_resource_labels", [])
    if not items:
        return ""
    return "".join(render_uri_label(u, l) + "\n" for (u, l) in items)


def render_mac_term_labels(config) -> str:
    """Type-specific class+predicate labels (mac:* curies).

    Sits at the end of the external-term-labels block. Empty string
    if the type declares no mac:* terms.
    """
    items = config.get("mac_term_labels", [])
    if not items:
        return ""
    max_prefixed = 2 + max(len(curie) for curie, _ in items)
    align_col = max(CURIE_LABEL_BASELINE_COL, max_prefixed + CURIE_LABEL_MIN_GAP)
    body = "".join(render_curie_label(c, l, align_col) + "\n" for (c, l) in items)
    return "\n" + body  # preceded by a blank line separator


def render_statement_list(config) -> str:
    """Full nt:hasStatement value list (without the leading nt:hasStatement
    header line, without the trailing nt:hasTag line).

    Lines end with `,` except the final line which ends with ` ;`.
    Type-specific statements (if any) splice in after st_pp; FAIR²
    statements (st_f2a, st_f2p) splice in last when
    `config["includes_fair2"]` is True (default False).
    """
    common = [
        "      sub:st0, sub:st3, sub:st4,",
        "      sub:st1, sub:st2,",
        "      sub:st6, sub:st7, sub:st8,",
        "      sub:st91, sub:st92, sub:st95,",
        "      sub:st5, sub:st5b, sub:st5c, sub:st5d,",
        "      sub:st_pp,",
    ]
    lines = list(common)
    type_ids = config.get("type_specific_statement_ids", [])
    if type_ids:
        lines.append("      " + ", ".join(type_ids) + ",")
    if config.get("includes_fair2", False):
        lines.append("      sub:st_f2a, sub:st_f2p,")
    lines[-1] = lines[-1].rstrip(",") + " ;"
    return "\n".join(lines) + "\n"


def render_placeholder(ph: dict) -> str:
    """Emit one placeholder block.

    Schema:
        id:    sub:foo
        types: list[str] of placeholder rdf:types (e.g. ["nt:LiteralPlaceholder"])
        label: rdfs:label literal
        extras: optional list[(predicate, object_literal_or_curie)] for
                nt:hasRegex, nt:hasDefaultValue, nt:possibleValuesFrom*,
                etc. Object string is emitted verbatim.
    """
    types_str = ", ".join(ph["types"])
    lines = [f'  {ph["id"]} a {types_str} ;']
    extras = ph.get("extras", [])
    label_terminator = ";" if extras else "."
    lines.append(f'    rdfs:label "{ph["label"]}" {label_terminator}')
    for i, (pred, obj) in enumerate(extras):
        terminator = "." if i == len(extras) - 1 else ";"
        lines.append(f'    {pred} {obj} {terminator}')
    return "\n".join(lines)


def render_type_specific_placeholders(config) -> str:
    blocks = [render_placeholder(p) for p in config.get("placeholders", [])]
    return "\n\n".join(blocks)


def render_statement(st: dict) -> str:
    """Emit one statement pattern block.

    Schema:
        id:        sub:stX
        st_types:  optional list[str] (e.g. ["nt:OptionalStatement"])
        subject:   string (curie or <URI> or local sub:name)
        predicate: string
        object:    string
    """
    lines = []
    st_types = st.get("st_types", [])
    if st_types:
        types_str = ", ".join(st_types)
        lines.append(f'  {st["id"]} a {types_str} ;')
        lines.append(f'    rdf:object {st["object"]} ;')
    else:
        lines.append(f'  {st["id"]} rdf:object {st["object"]} ;')
    lines.append(f'    rdf:predicate {st["predicate"]} ;')
    lines.append(f'    rdf:subject {st["subject"]} .')
    return "\n".join(lines)


def render_type_specific_statements(config) -> str:
    blocks = [render_statement(s) for s in config.get("statements", [])]
    return "\n\n".join(blocks)


# ============================================================
# Common scaffold — identical across all 11 MAC FDT types
# ============================================================

PREFIXES_AND_HEAD = """\
@prefix this: <http://purl.org/nanopub/temp/np001/> .
@prefix sub: <http://purl.org/nanopub/temp/np001/> .
@prefix np: <http://www.nanopub.org/nschema#> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix nt: <https://w3id.org/np/o/ntemplate/> .
@prefix npx: <http://purl.org/nanopub/x/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix orcid: <https://orcid.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix mac: <https://w3id.org/spaces/mac/r/ontology/> .

sub:Head {
  this: a np:Nanopublication ;
    np:hasAssertion sub:assertion ;
    np:hasProvenance sub:provenance ;
    np:hasPublicationInfo sub:pubinfo .
}
"""

# External-term labels: common block 1 (FDO + dcat + FIP), used by the
# scaffold's standard statements.
EXTERNAL_LABELS_COMMON_1 = """\

sub:assertion {

  # ---- External-term labels (for NanoDash UI rendering) ----

  <https://w3id.org/fdof/ontology#FAIRDigitalObject> rdfs:label "FAIR Digital Object (FDO)" .
  <https://w3id.org/fdof/ontology#hasMetadata>       rdfs:label "has its metadata in" .
  <https://w3id.org/fdof/ontology#materializes>      rdfs:label "is a concrete materialization of" .
  <https://w3id.org/fdof/ontology#hasEncodingFormat> rdfs:label "has format" .
  <https://www.w3.org/ns/dcat#accessURL>             rdfs:label "has access URL" .
  <https://www.w3.org/ns/dcat#contactPoint>          rdfs:label "has contact point" .
  <https://w3id.org/fair/fip/terms/implements>       rdfs:label "implements" .
"""

# External-term labels: common block 2 (FAIR² DOIs + TriG + CC BY) used
# by SPS v1.3 cross-references and the self-materialization block.
EXTERNAL_LABELS_COMMON_2 = """\
  <https://doi.org/10.3389/fbinf.2025.1634111>       rdfs:label "FAIR² data article (Frontiers in Bioinformatics)" .
  <https://doi.org/10.71728/hw56-vj34>               rdfs:label "FAIR² Data Package DOI" .
  <https://www.iana.org/assignments/media-types/application/trig>
                                                     rdfs:label "TriG (RDF named-graph serialization)" .
  <https://creativecommons.org/licenses/by/4.0/>     rdfs:label "Attribution 4.0 International (CC BY 4.0)" .
"""

# External-term labels: common block 3 (dct + rdf labels for predicates
# emitted by the scaffold and by SPS v1.3 / FAIR² statements).
EXTERNAL_LABELS_COMMON_3 = """\

  dct:creator      rdfs:label "has creator" .
  dct:contributor  rdfs:label "has contributor" .
  dct:license      rdfs:label "data usage license" .
  dct:isPartOf     rdfs:label "is part of" .
  dct:subject      rdfs:label "has domain" .
  dct:publisher    rdfs:label "has publisher" .
  dct:references   rdfs:label "references" .
  dct:source       rdfs:label "has source" .
  rdf:type         rdfs:label "is a" .
  rdfs:label       rdfs:label "has the label" .
  rdfs:comment     rdfs:label "has description" .
"""

# Template declaration. The label, description, label pattern, and the
# nt:hasStatement list (which depends on type-specific statements and
# whether the type carries SPS v1.3 FAIR² cross-references) are slotted
# from config.
TEMPLATE_DECLARATION_PREFIX = """\

  # ---- Template declaration ----

  sub:assertion a nt:AssertionTemplate ;
    rdfs:label "{template_label}" ;
    dct:description "{template_description}" ;
    nt:hasNanopubLabelPattern "{label_pattern}" ;
    nt:hasStatement
"""

TEMPLATE_DECLARATION_SUFFIX = """\
    nt:hasTag "MAC" .
"""

# Common placeholders. sub:fdo / sub:label / sub:description carry
# type-specific noun phrases (e.g. "this variant") slotted from config.
STANDARD_PLACEHOLDERS = """\

  # ---- Placeholders ----

  # Core FDO identifier (introduced resource; this nanopub mints it)
  sub:fdo a nt:IntroducedResource, nt:LocalResource, nt:UriPlaceholder ;
    rdfs:label "{fdo_label_text}" .

  # Standard descriptive placeholders
  sub:label a nt:LiteralPlaceholder ;
    rdfs:label "{label_placeholder_text}" .

  sub:description a nt:LongLiteralPlaceholder ;
    rdfs:label "{description_placeholder_text}" .

  sub:creator a nt:AgentPlaceholder ;
    rdfs:label "ORCID of creator" ;
    nt:hasDefaultValue nt:CREATOR .

  sub:contributor a nt:AgentPlaceholder ;
    rdfs:label "ORCID of contributor" .

  sub:contact a nt:LiteralPlaceholder ;
    rdfs:label "contact email" .

  sub:domain a nt:RestrictedChoicePlaceholder ;
    rdfs:label "domain" ;
    nt:possibleValuesFrom <https://w3id.org/np/RACXDZHEowTYDAzZvdmD0qIGpXZwY5ghMRBBlt6N8Iu5s> .

  sub:publisher a nt:ExternalUriPlaceholder ;
    rdfs:label "ROR of the publishing entity" .

  sub:fip a nt:GuidedChoicePlaceholder ;
    rdfs:label "FAIR Implementation Profile" ;
    nt:possibleValuesFromApi "http://purl.org/nanopub/api/find_signed_things?type=https%3A%2F%2Fw3id.org%2Ffair%2Ffip%2Fterms%2FFAIR-Implementation-Profile&searchterm=" .

  # SPS v1.3 mandatory institutional-provenance placeholder (guided choice from project catalogue)
  sub:project a nt:GuidedChoicePlaceholder ;
    rdfs:label "project" ;
    nt:possibleValuesFromApi "https://w3id.org/np/l/nanopub-query-1.1/api/RAFTZ8GqPOOJQOBcEo5IB8lg5vZCFiIyr_RVLKZDQBHMk/get-projects?searchterm=" .
"""

TYPE_SPECIFIC_PLACEHOLDERS_HEADER = """\

  # {type_label_short} specific placeholders
"""

STATEMENTS_HEADER_AND_FDO_TYPING = """\

  # ---- Statement patterns ----

  # Core FDO typing (mandatory, fixed)
  sub:st0 rdf:object <https://w3id.org/fdof/ontology#FAIRDigitalObject> ;
    rdf:predicate rdf:type ;
    rdf:subject sub:fdo .

  sub:st3 rdf:object {class_curie} ;
    rdf:predicate rdf:type ;
    rdf:subject sub:fdo .

  sub:st4 rdf:object nt:NANOPUB ;
    rdf:predicate <https://w3id.org/fdof/ontology#hasMetadata> ;
    rdf:subject sub:fdo .
"""

STANDARD_DESCRIPTIVE_STATEMENTS = """\

  # Standard descriptive
  sub:st1 a nt:OptionalStatement ;
    rdf:object sub:label ;
    rdf:predicate rdfs:label ;
    rdf:subject sub:fdo .

  sub:st2 a nt:OptionalStatement ;
    rdf:object sub:description ;
    rdf:predicate rdfs:comment ;
    rdf:subject sub:fdo .

  sub:st6 a nt:RepeatableStatement ;
    rdf:object sub:creator ;
    rdf:predicate dct:creator ;
    rdf:subject sub:fdo .

  sub:st7 a nt:OptionalStatement, nt:RepeatableStatement ;
    rdf:object sub:contributor ;
    rdf:predicate dct:contributor ;
    rdf:subject sub:fdo .

  sub:st8 rdf:object sub:contact ;
    rdf:predicate <https://www.w3.org/ns/dcat#contactPoint> ;
    rdf:subject sub:fdo .

  sub:st91 a nt:OptionalStatement ;
    rdf:object sub:domain ;
    rdf:predicate dct:subject ;
    rdf:subject sub:fdo .

  sub:st92 rdf:object sub:publisher ;
    rdf:predicate dct:publisher ;
    rdf:subject sub:fdo .

  sub:st95 a nt:OptionalStatement ;
    rdf:object sub:fip ;
    rdf:predicate <https://w3id.org/fair/fip/terms/implements> ;
    rdf:subject sub:fdo .
"""

SELF_MATERIALIZATION_BLOCK = """\

  # ---- Self-materialization block (mandatory; identical across all 11 MAC FDT templates) ----
  # A nanopub whose substance is its assertion graph self-materializes
  # as the TriG file it is. Generator emits this block from a single constant.

  sub:st5 rdf:subject nt:NANOPUB ;
    rdf:predicate <https://w3id.org/fdof/ontology#materializes> ;
    rdf:object sub:fdo .

  sub:st5b rdf:subject nt:NANOPUB ;
    rdf:predicate <https://w3id.org/fdof/ontology#hasEncodingFormat> ;
    rdf:object <https://www.iana.org/assignments/media-types/application/trig> .

  sub:st5c rdf:subject nt:NANOPUB ;
    rdf:predicate dct:license ;
    rdf:object <https://creativecommons.org/licenses/by/4.0/> .

  sub:st5d rdf:subject nt:NANOPUB ;
    rdf:predicate <https://www.w3.org/ns/dcat#accessURL> ;
    rdf:object nt:NANOPUB .
"""

ST_PP_BLOCK = """\

  # SPS v1.3 institutional-provenance (mandatory, instance-supplied)
  sub:st_pp rdf:object sub:project ;
    rdf:predicate dct:isPartOf ;
    rdf:subject sub:fdo .
"""

TYPE_SPECIFIC_STATEMENTS_HEADER = """\

  # {type_label_short} specific statements
"""

FAIR2_STATEMENTS_BLOCK = """\

  # FAIR² mandatory cross-references (fixed objects per SPS v1.3 §"FAIR² citation policy")
  sub:st_f2a rdf:object <https://doi.org/10.3389/fbinf.2025.1634111> ;
    rdf:predicate dct:references ;
    rdf:subject sub:fdo .

  sub:st_f2p rdf:object <https://doi.org/10.71728/hw56-vj34> ;
    rdf:predicate dct:source ;
    rdf:subject sub:fdo .
"""

ASSERTION_CLOSE = "}\n"

PROVENANCE_BLOCK = """\

sub:provenance {
  sub:assertion prov:wasAttributedTo orcid:0000-0001-8888-635X .
}
"""

PUBINFO_BLOCK = """\

sub:pubinfo {{
  this: dct:created "{created}"^^xsd:dateTime ;
    dct:creator orcid:0000-0001-8888-635X ;
    dct:license <https://creativecommons.org/licenses/by/4.0/> ;
    rdfs:label "Template: {template_label}" ;
    nt:wasCreatedFromTemplate <https://w3id.org/np/RA5reLVXOCPQFWr2UiCJb19ES7NwOpQRmudb17e2iB0c4> ;
    nt:wasCreatedFromProvenanceTemplate <https://w3id.org/np/RA7lSq6MuK_TIC6JMSHvLtee3lpLoZDOqLJCLXevnrPoU> ;
    nt:wasCreatedFromPubinfoTemplate
      <https://w3id.org/np/RA0J4vUn_dekg-U1kK3AOEt02p9mT2WO03uGxLDec1jLw>,
      <https://w3id.org/np/RAukAcWHRDlkqxk7H2XNSegc1WnHI569INvNr-xdptDGI>,
      <https://w3id.org/np/RAMEgudZsQ1bh1fZhfYnkthqH6YSXpghSE_DEN1I-6eAI>,
      <https://w3id.org/np/RARW4MsFkHuwjycNElvEVtuMjpf4yWDL10-0C5l2MqqRQ> .
}}
"""


# ============================================================
# Composition
# ============================================================

def generate(config, created: str) -> str:
    parts = []
    parts.append(PREFIXES_AND_HEAD)
    parts.append(EXTERNAL_LABELS_COMMON_1)
    parts.append(render_external_resource_labels(config))
    parts.append(EXTERNAL_LABELS_COMMON_2)
    parts.append(EXTERNAL_LABELS_COMMON_3)
    parts.append(render_mac_term_labels(config))
    parts.append(TEMPLATE_DECLARATION_PREFIX.format(
        template_label=config["template_label"],
        template_description=config["template_description"],
        label_pattern=config["label_pattern"],
    ))
    parts.append(render_statement_list(config))
    parts.append(TEMPLATE_DECLARATION_SUFFIX)
    parts.append(STANDARD_PLACEHOLDERS.format(
        fdo_label_text=config["fdo_label_text"],
        label_placeholder_text=config["label_placeholder_text"],
        description_placeholder_text=config["description_placeholder_text"],
    ))
    parts.append(TYPE_SPECIFIC_PLACEHOLDERS_HEADER.format(
        type_label_short=config["type_label_short"],
    ))
    parts.append(render_type_specific_placeholders(config))
    parts.append("\n")  # blank line before "Statement patterns" comment
    parts.append(STATEMENTS_HEADER_AND_FDO_TYPING.format(
        class_curie=config["class_curie"],
    ))
    parts.append(STANDARD_DESCRIPTIVE_STATEMENTS)
    parts.append(SELF_MATERIALIZATION_BLOCK)
    parts.append(ST_PP_BLOCK)
    parts.append(TYPE_SPECIFIC_STATEMENTS_HEADER.format(
        type_label_short=config["type_label_short"],
    ))
    parts.append(render_type_specific_statements(config))
    parts.append("\n")
    if config.get("includes_fair2", False):
        parts.append(FAIR2_STATEMENTS_BLOCK)
    parts.append(ASSERTION_CLOSE)
    parts.append(PROVENANCE_BLOCK)
    parts.append(PUBINFO_BLOCK.format(
        created=created,
        template_label=config["template_label"],
    ))
    return "".join(parts)


# ============================================================
# CLI
# ============================================================

def load_config(path: Path) -> dict:
    spec = importlib.util.spec_from_file_location("type_config", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.CONFIG


TIMESTAMP_RE = re.compile(r'dct:created "([^"]+)"\^\^xsd:dateTime')


def normalize_timestamp(text: str, replacement: str = "<<CREATED>>") -> str:
    return TIMESTAMP_RE.sub(f'dct:created "{replacement}"^^xsd:dateTime', text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("config", type=Path)
    ap.add_argument("--diff", type=Path, help="Compare against an existing TriG file (timestamp ignored).")
    ap.add_argument("--out", type=Path, help="Write to this path instead of stdout.")
    ap.add_argument("--created", default=None, help="Override dct:created timestamp (default: now UTC).")
    args = ap.parse_args()

    config = load_config(args.config)
    created = args.created or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    output = generate(config, created)

    if args.diff:
        reference = args.diff.read_text()
        gen_norm = normalize_timestamp(output)
        ref_norm = normalize_timestamp(reference)
        if gen_norm == ref_norm:
            print(f"OK: generator output matches {args.diff} byte-for-byte (modulo dct:created).", file=sys.stderr)
            return 0
        diff = difflib.unified_diff(
            ref_norm.splitlines(keepends=True),
            gen_norm.splitlines(keepends=True),
            fromfile=str(args.diff),
            tofile="<generator>",
        )
        sys.stdout.writelines(diff)
        return 1

    if args.out:
        args.out.write_text(output)
    else:
        sys.stdout.write(output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
