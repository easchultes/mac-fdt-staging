# MAC FDT Implementation Guide

## A prescriptive procedure for nanopublishing a FAIR Digital Twin catalogue of SARS-CoV-2 Spike RBD variants

**Version:** 1.0 (complete §§1–6)
**Status:** Complete. Companion specification: `specs/MAC_FDT_SPS_v1_4.md`.
**Repository:** `easchultes/mac-fdt-staging` on GitHub.

---

## Contents

- §1 — Overview and prerequisites
- §2 — Stage 1: Vocabulary
- §3 — Stage 2: Templates
- §4 — Stage 3: Instances
- §5 — Stage 4: Standing views
- §6 — Reference appendices

---
## §1 — Overview and prerequisites

### 1.1 What this guide produces

Following this procedure end-to-end yields, on the live Nanopublication Server Network (NSN), the demonstration catalogue summarised below:

| Layer | Artifact | Count | Identifier scheme |
|---|---|---|---|
| Vocabulary | MAC-namespace predicates and classes | 45 (26 + 19) | Trusty URIs under `https://w3id.org/np/RA…`; referents under `https://w3id.org/spaces/mac/r/ontology/<term>` |
| Templates | NanoDash assertion templates, one per FDT type | 11 | Trusty URIs; pinned to a Space |
| Instances | FDO nanopubs (variant anchors, methods, observations) | 38 | Trusty URIs; referents under `<Trusty URI>/<instance_id>` |
| Views | Standing SPARQL queries + sidebar pins + embedded panels | 4 queries × 3 artifacts each | Trusty URIs; pinned to the same Space |

All artifacts are content-addressed (Trusty URIs), cryptographically signed (ORCID), immutable, and individually retrievable via HTTP. The catalogue resolves to a NanoDash Space view at `https://nanodash.knowledgepixels.com/space?id=https://w3id.org/spaces/knowledgepixels/incubator/project4`.

The data demonstrated is three SARS-CoV-2 Spike RBD variants — Alpha (N169Y), Epsilon (L120R), Eta (E152K) — with their real-world occurrences, computational structure predictions (RMSD, SASA, pLDDT, AgMata) by two methods (ESM2, AlphaFold 2), experimental deep-mutational-scanning measurements (Bloom Lab), and WHO risk classifications. The procedure generalises without modification to larger catalogues; the same generator code path produces the 3705-mutation Tranche 2 scale-up.

### 1.2 Why this stack (nanopublications, FDOs, NanoDash)

The architectural rationale is laid out in full in the MAC FAIR v2 paper (Schultes et al., *in preparation*); this guide adopts those decisions and extends them from the dataset-publishing case to the FAIR Digital Twin case. The recap below states the *why* compactly so the *how* in §§2–5 reads as the natural consequence.

**Nanopublications** are the smallest unit of attributable RDF assertion — a four-graph structure (head / assertion / provenance / pubinfo) wrapped in a content-addressed Trusty URI and cryptographically signed by the publisher's ORCID. Properties that matter here: (i) **content-addressed identity** (the Trusty URI is a hash of the content; tampering breaks the URI), (ii) **immutability** (a published nanopub cannot be edited — only superseded or retracted by a successor nanopub), (iii) **decentralised publishing** via the Nanopublication Server Network (the NSN replicates nanopubs across independent servers; no single point of failure or control), and (iv) **FAIR-by-construction** (Findable via the Trusty URI; Accessible over HTTP; Interoperable as RDF; Reusable under explicit license). The catalogue's claims about openness, decentralisation, and real-time publishing are properties the substrate delivers; this guide does not re-prove them per artifact.

**The FAIR Funder Framework (FFF)** specifies the FDO typing layer the catalogue inherits. FFF (`https://w3id.org/fair/ff/terms/`) defines the institutional and dataset anchors: `ff:Project`, `ff:Dataset`, `ff:Funder`, with the relations that link them. MAC FAIR v2 published the StayAhead Project FDO and its companion Dataset FDOs (ESM and AlphaFold) under FFF, establishing the institutional context every FDT instance in this guide inherits via `dct:isPartOf` → StayAhead Project FDO. The FFF layer makes the funding-institutional provenance machine-traversable: a downstream consumer of any observation can trace it back to the project that funded it without consulting external systems.

**np-FDOs** (nanopublication-based FAIR Digital Objects) are the architectural commitment that lets the same artifact satisfy two specifications simultaneously. The FDO Framework (Bonino, De Smedt, Hardisty et al.) specifies that an FDO must declare a persistent identifier, a type, and type-specific metadata; nanopubs satisfy these requirements when properly structured (Trusty URI → persistent ID; `rdf:type fdof:FAIRDigitalObject` → type; the assertion graph → type-specific metadata). A nanopub correctly typed *is* an FDO; no separate FDO repository or registry is needed. This identification — "the nanopub is the FDO" — is the central architectural move this guide rests on. It is what allows the digital twin to be a *cluster of nanopublications*, each one independently a FAIR digital object, collectively a FAIR Digital Twin.

**NanoDash** (Knowledge Pixels) is the web UI for the NSN at `https://nanodash.knowledgepixels.com/`. It provides three capabilities this guide relies on: (i) **assertion templates** — a declarative grammar (the `nt:` "ntemplate" vocabulary) for specifying the form of a nanopub, with placeholders, mandatory/optional/repeatable statement flags, regex validation, and guided-choice lookups; templates render as forms and constrain authoring at publication time (Stage 2); (ii) **Space pages** — curated views of nanopubs grouped by project, with a federated pinning mechanism (`gen:hasPinnedTemplate`, `gen:hasPinnedQuery`) for templates and standing queries (Stage 4); and (iii) **resource pages** — type-specific renderings that traverse the FDO graph and display the assembled view (where a FAIR Digital Twin becomes visible as a coherent object rather than a set of independent nanopubs). NanoDash is the authoring environment for Stage 2 and the consumption environment for Stage 4; it sits over the NSN as a usability layer without altering the underlying decentralised substrate.

The full architectural argument — including why these choices satisfy FAIR's R-principles rigorously (provenance chains, immutable references, license carriage), and why the FDT pattern generalises across domains (the COVID variant case is the demonstration; AMR, mass spectrometry, and mathematical formalisation are mapped in companion papers) — is in the MAC FAIR v2 paper. Readers building a new catalogue without prior context should read the MAC v2 paper first, then return here.

### 1.3 The four-stage architecture

The build proceeds in four stages, each producing a self-contained layer of the catalogue:

1. **Stage 1 — Vocabulary.** Mint and publish 45 nanopubs, one per MAC-namespace term (predicates and classes). These terms are the controlled vocabulary the templates and instances will use. Stage 1 has no dependencies; it can be redone in isolation if vocabulary changes are needed.

2. **Stage 2 — Templates.** Mint and publish 11 NanoDash assertion templates, one per FDT type (variant anchor, seven observation types, three method types). Each template encodes the structural commitment for instances of its type. Stage 2 depends on Stage 1 (templates reference vocabulary terms).

3. **Stage 3 — Instances.** Mint and publish 38 instance nanopubs — three variant anchors, five shared methods, thirty observations — populating the templates with concrete values. Stage 3 depends on Stage 2 (each instance declares `nt:wasCreatedFromTemplate` → a Stage 2 template).

4. **Stage 4 — Views.** Mint and publish four grlc-query nanopubs (the standing SPARQL views), plus pin-action nanopubs (sidebar visibility) and View/ViewDisplay nanopubs (embedded panels). Stage 4 depends on Stage 3 (the queries operate over the instance graph).

The stages are independent in their generators and validation, but ordered in their dependencies. Each completes with a verification checklist before the next begins.

### 1.4 Tooling and prerequisites

**System requirements:**
- Python 3.11 or newer.
- The `nanopub` CLI: `pip install nanopub`. This provides `nanopub sign`, `nanopub check`, and `nanopub publish`. See [https://github.com/peta-pico/nanopub-py](https://github.com/peta-pico/nanopub-py).
- A signing profile: an RSA keypair registered to the publisher's ORCID. Configured via `nanopub setup` (one-time). See the nanopub-skill at `~/nanopub-work/nanopub-skill/` (companion documentation by Tobias Kuhn et al.).
- A GitHub repository for staging the build artifacts and version-controlling the generators, configs, and signed TriG files.

**Identifiers required for the publisher:**
- ORCID (used as `dct:creator`, `prov:wasAttributedTo`, and the signing identity).
- Institutional ROR (used as `dct:publisher`).
- Contact email (used as `dcat:contactPoint`).

For the MAC FDT catalogue:
- ORCID: `https://orcid.org/0000-0001-8888-635X` (Erik Schultes).
- ROR: `https://ror.org/027bh9e22` (Leiden University).
- Contact: `e.a.schultes@lacdr.leidenuniv.nl`.

Replace these throughout for a different publisher.

**External resources referenced by the catalogue:**
- The MAC-Ontology NanoDash space, declared at `https://w3id.org/spaces/mac/r/ontology/MAC-Ontology` (this guide's Stage 1 populates it).
- A NanoDash Space for publishing templates and views. For this catalogue: KP incubator project4, `https://w3id.org/spaces/knowledgepixels/incubator/project4`. The publisher must hold `gen:hasAdmin` on the Space to pin artifacts; in this case Erik holds admin rights granted by Tobias Kuhn.
- The FDO Framework vocabulary (`https://w3id.org/fdof/ontology#`).
- The FAIR² Data Package for the source observations: `https://doi.org/10.71728/hw56-vj34`. The corresponding peer-reviewed data article: `https://doi.org/10.3389/fbinf.2025.1634111`.
- The StayAhead Project FDO (the funder/institutional anchor): `https://w3id.org/np/RAFPOe4OIl_urs-U_7-FostjzcUo8ra6LasfSvGplOvto/StayAhead-Project`.

### 1.5 The companion specification

This guide is paired with the Stakeholder Participation Sheets (SPS) at `specs/MAC_FDT_SPS_v1_4.md` in the repository. The SPS specifies, for each FDT type, the mandatory and optional statements, the predicate URIs, the object ranges, and the per-type provenance obligations. The guide implements the SPS — it does not redefine or override it.

When a question arises about *what* an instance should declare, consult the SPS. When a question arises about *how* to mint, sign, validate, or publish the instance, consult this guide. The two documents are kept in sync; the SPS is the contractual specification, the guide is the procedural implementation.

The SPS itself rests on a separately-published vocabulary specification (`specs/MAC_FDT_Vocabulary_v1_2.md`) that defines the 26 predicates and 19 classes minted in Stage 1.

### 1.6 Repository layout

The build artifacts are organised by stage:

```
mac-fdt-staging/
├── specs/
│   ├── MAC_FDT_Vocabulary_v1_2.md
│   ├── MAC_FDT_SPS_v1_2.md           (audit, superseded)
│   ├── MAC_FDT_SPS_v1_3.md           (audit, superseded)
│   └── MAC_FDT_SPS_v1_4.md           (current)
├── minting/
│   ├── stage1-vocabulary-drafts/
│   │   ├── generator/
│   │   │   ├── generate_vocabulary.py
│   │   │   └── vocabulary_terms_v1_2.csv
│   │   ├── drafts/                   (unsigned TriG, one per term)
│   │   ├── signed/                   (signed TriG, one per term)
│   │   ├── manifest_live_v1.csv      (audit, v1 Trusty URIs)
│   │   └── manifest_live_v2.csv      (current, the authoritative lookup)
│   ├── stage2-templates/
│   │   ├── generator/
│   │   │   ├── generate_template.py
│   │   │   └── configs/type{1-11}_config.py
│   │   ├── drafts/                   (unsigned and signed TriG per template)
│   │   ├── reference/                (the meta-template and exemplars, for audit)
│   │   ├── SESSION_STATE.md          (cross-stage tracking document)
│   │   └── Post_demonstration_cleanup.md
│   ├── stage3-instances/
│   │   ├── generator/
│   │   │   ├── generate_instance.py
│   │   │   ├── generate_predictions_from_csv.py
│   │   │   ├── generate_type6_7_from_csv.py
│   │   │   ├── instance_configs/    (per-instance Python dicts where not CSV-driven)
│   │   │   └── FDT4Claude_small_v1_2.csv
│   │   ├── drafts/                   (one TriG per instance)
│   │   ├── signed/
│   │   └── PUBLISHED_*.md            (one per batch — publication records)
│   └── stage4-views/
│       ├── drafts/
│       │   ├── query/                (grlc-query nanopubs)
│       │   ├── pin/                  (sidebar pin-actions)
│       │   ├── wrapper/              (gen:View wrappers)
│       │   └── display/              (ViewDisplay nanopubs)
│       ├── signed/                   (parallel structure)
│       └── PUBLISHED_views.md
└── docs/
    └── implementation_guide.md       (this document)
```

The convention throughout is: unsigned TriG → `drafts/`; signed TriG → `signed/`; once published to live NSN, the publication record (live Trusty URI, publish timestamp, render status) is appended to a `PUBLISHED_*.md` file in the same stage directory.

The branch model used during the build is: each work item (per-type template, per-instance batch, view round) lives on its own short-lived branch (`stage{N}-templates-type{M}`, `stage3-instances-methods`, etc.) and is merged into `main` after validation. The `main` branch is the canonical state at any moment.

---

## §2 — Stage 1: Vocabulary

### 2.1 What Stage 1 produces

Forty-five nanopubs, one per MAC-namespace term, published live on the NSN and indexed under the MAC-Ontology Space resource `https://w3id.org/spaces/mac/r/ontology/MAC-Ontology`. The split:

- 26 predicates (the relations used by templates and instances).
- 19 classes (the types instances declare via `rdf:type`).

Each term has a stable referent URI of the form `https://w3id.org/spaces/mac/r/ontology/<TermLocalName>` (the FAIR-by-construction identifier the catalogue uses downstream), and a stable Trusty URI of the form `https://w3id.org/np/RA…` (the immutable nanopub that *introduces* the term). The two URIs are related by `nt:introduces` in the introducing nanopub's pubinfo.

The Stage 1 artifact downstream stages consume is the manifest:

```
minting/stage1-vocabulary-drafts/manifest_live_v2.csv
```

This CSV maps each term's local name to its v2 Trusty URI. Stages 2–4 read it to resolve term references; nothing else from Stage 1's filesystem is needed at later stages.

### 2.2 Term inventory

The 45 terms are defined in the vocabulary specification at `specs/MAC_FDT_Vocabulary_v1_2.md`. Reproduced here in compact form:

**Predicates (26):**

The variant-anchor predicates (Type 1): `mac:hasWHOVariantName`, `mac:hasPangoLineage`, `mac:hasGISAIDSeqId`, `mac:hasMACSeqId`, `mac:hasParentProtein`, `mac:hasRBDSequence`, `mac:hasGISAIDAccession`.

The observation linkage predicate: `mac:isObservationOf` (`rdfs:domain mac:Observation`, `rdfs:range mac:SpikeRBDVariant`).

The method linkage predicates: `mac:hasSurveillanceMethod`, `mac:hasPredictionMethod`, `mac:hasExperimentalMethod`.

The Type 2 (real-world occurrence) predicates: `mac:hasOccurrenceDate`, `mac:hasCollectionLocation`.

The Types 3–6 (computational prediction) value predicates: `mac:hasRMSD`, `mac:hasSASA`, `mac:haspLDDT`, `mac:hasAgMataScore`.

The Type 7 (DMS) value predicates: `mac:hasBind`, `mac:hasDeltaBind`, `mac:hasExpr`, `mac:hasDeltaExpr`, `mac:hasConfidenceBind`, `mac:hasConfidenceExpr`.

The Type 8 (WHO classification) predicates: `mac:hasWHOClassification`, `mac:hasClassificationDate`, `mac:hasWHOClassificationReference`.

**Classes (19):**

Abstract parents (5): `mac:Observation`, `mac:ComputationalPrediction`, `mac:ExperimentalObservation`, `mac:Method`, `mac:WHODesignation`.

FDT and observation classes (8, concrete): `mac:SpikeRBDVariant`, `mac:RealWorldOccurrence`, `mac:ComputationalPredictionRMSD`, `mac:ComputationalPredictionSASA`, `mac:ComputationalPredictionPLDDT`, `mac:ComputationalPredictionAgMata`, `mac:ExperimentalDMSObservation`, `mac:WHOVariantClassification`.

Method classes (3, concrete): `mac:ComputationalMethod`, `mac:ExperimentalMethod`, `mac:ObservationalMethod`.

WHO controlled values (3, concrete): `mac:VOC`, `mac:VOI`, `mac:VUM`.

Each predicate carries `rdfs:domain`, `rdfs:range`, `rdfs:label`, and `dct:description`. Each class carries `rdfs:subClassOf` (where applicable), `rdfs:label`, and `dct:description`. The exact values per term are in `MAC_FDT_Vocabulary_v1_2.md` §§"Predicate domain and range" and "Class hierarchy"; reproduce verbatim from there into `vocabulary_terms_v1_2.csv` rather than retyping.

### 2.3 Vocabulary nanopub structure (per term)

Each of the 45 nanopubs has the same four-graph structure. The assertion graph carries the term definition; the pubinfo graph carries the FAIR-namespace declaration and the introducing flag.

**Assertion graph (predicate term, example `mac:isObservationOf`):**

```turtle
sub:assertion {
  mac:isObservationOf
      rdf:type rdf:Property ;
      rdfs:label "is observation of" ;
      dct:description "Links an observation FDO to the FAIR Digital Twin anchor (the variant) it observes." ;
      rdfs:domain mac:Observation ;
      rdfs:range mac:SpikeRBDVariant .
}
```

**Assertion graph (class term, example `mac:SpikeRBDVariant`):**

```turtle
sub:assertion {
  mac:SpikeRBDVariant
      rdf:type owl:Class ;
      rdfs:label "Spike RBD Variant" ;
      dct:description "A variant of the SARS-CoV-2 Spike receptor-binding domain (RBD, 195 residues) produced by one or more amino acid substitutions from the wild-type Wuhan isolate (UniProt P0DTC2). Anchors a FAIR Digital Twin knowlet." .
}
```

(Abstract parent classes carry `rdfs:subClassOf` where applicable; e.g., `mac:ComputationalPredictionRMSD rdfs:subClassOf mac:ComputationalPrediction`.)

**Pubinfo graph (uniform across all 45):**

```turtle
sub:pubinfo {
  this:
      dct:created "<UTC timestamp>"^^xsd:dateTime ;
      dct:creator orcid:0000-0001-8888-635X ;
      dct:license <https://creativecommons.org/licenses/by/4.0/> ;
      rdfs:label "<term-local-name> term definition" ;
      npx:introduces <https://w3id.org/spaces/mac/r/ontology/{TermLocalName}> ;
      dct:partOf <https://w3id.org/spaces/mac/r/ontology/MAC-Ontology> .
}
```

The two pubinfo lines that matter for indexing:
- `npx:introduces` declares the term URI this nanopub mints. Required for the NSN to recognise the nanopub as a term introduction.
- `dct:partOf` declares the Space resource. Required for the NanoDash MAC-Ontology view to list the term.

**Provenance graph:**

```turtle
sub:provenance {
  sub:assertion prov:wasAttributedTo orcid:0000-0001-8888-635X .
}
```

### 2.4 Generation

The generator is a Python script that reads a CSV of term metadata and emits one TriG file per term into `drafts/`. The CSV has columns: `term_type` (predicate / class), `term_local_name`, `rdfs_label`, `dct_description`, `rdfs_domain` (predicates only), `rdfs_range` (predicates only), `rdfs_subClassOf` (classes only).

The full CSV (`vocabulary_terms_v1_2.csv`) is transcribed from the vocabulary specification. Both the spec and the CSV are version-controlled; the CSV is the input to the generator, the spec is the human-readable companion.

Generation command:

```
cd minting/stage1-vocabulary-drafts/
python generator/generate_vocabulary.py \
    --csv generator/vocabulary_terms_v1_2.csv \
    --out drafts/
```

Output: 45 TriG files, one per term, named `<term_local_name>_term.trig`. Each is unsigned (Trusty URI placeholder is `http://purl.org/nanopub/temp/np001/`; substituted by `nanopub sign`).

### 2.5 Signing and publishing

Order: publish classes before predicates. Predicates carry `rdfs:domain` and `rdfs:range` referencing class URIs (e.g., `mac:isObservationOf rdfs:range mac:SpikeRBDVariant`). These references resolve to the class URIs (not Trusty URIs), so the order does not affect publishability — but indexing is cleaner if class terms exist first.

Per term:

```
nanopub sign drafts/<term>_term.trig
mv drafts/signed.<term>_term.trig signed/<term>_term.trig
nanopub check signed/<term>_term.trig    # expect: 1 trusty with signature
nanopub publish signed/<term>_term.trig  # publishes to live NSN
```

After publication, the live Trusty URI is recorded into `manifest_live_v2.csv` along with the term local name, term type, and publish timestamp.

The v1 / v2 history of this catalogue: the initial Stage 1 publish (v1, manifest_live_v1.csv) omitted `npx:introduces` in pubinfo, which prevented the NanoDash MAC-Ontology view from listing the terms. The v2 round (this guide's reference state) republishes each term with the correct pubinfo, declaring `npx:supersedes <v1-Trusty-URI>` per term. New deployments should publish with v2's pubinfo from the start; the v1 → v2 supersession is documented here only for the existing catalogue's audit trail.

### 2.6 Validation

After all 45 terms are published, run the following checks:

**(a) HTTP resolution:**

```bash
while read term_uri; do
    curl -s -o /dev/null -w "%{http_code}\n" -L "$term_uri"
done < <(cut -d, -f4 manifest_live_v2.csv | tail -n +2)
```

Expect 45 occurrences of `200`. (`-L` follows the `307 Temporary Redirect` from `w3id.org` to `registry.knowledgepixels.com`.)

**(b) SPARQL count via the live nanopub-query endpoint:**

Endpoint: `https://w3id.org/np/l/nanopub-query-1.1/repo/full`.

```sparql
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX np:  <http://www.nanopub.org/nschema#>
PREFIX npa: <http://purl.org/nanopub/admin/>
PREFIX npx: <http://purl.org/nanopub/x/>

SELECT (COUNT(?n1) AS ?count) WHERE {
  GRAPH npa:graph {
    ?n1 npa:hasValidSignatureForPublicKey ?pubkey .
    FILTER NOT EXISTS {
      ?np2 npx:invalidates ?n1 ;
           npa:hasValidSignatureForPublicKey ?pubkey .
    }
    ?n1 dct:partOf <https://w3id.org/spaces/mac/r/ontology/MAC-Ontology> .
  }
}
```

Expect `count = 45`.

**(c) NanoDash MAC-Ontology view:**

Open `https://nanodash.knowledgepixels.com/space?id=https://w3id.org/spaces/mac/r/ontology/MAC-Ontology` in a browser. After indexing (minutes to hours), all 45 terms appear in the term list. Indexing lag is normal; if no terms appear after 2 hours, verify the SPARQL count and consult the operator.

### 2.7 The manifest artifact

`manifest_live_v2.csv` is the Stage 1 deliverable that subsequent stages depend on. Schema:

| Column | Content |
|---|---|
| `term_type` | `predicate` or `class` |
| `term_local_name` | The local name (e.g., `isObservationOf`, `SpikeRBDVariant`) |
| `trig_file` | Filesystem path of the signed TriG (in `signed/`) |
| `trusty_uri_v2` | The live Trusty URI of the v2 introducing nanopub |
| `superseded_trusty_uri_v1` | The v1 Trusty URI (empty for terms minted directly as v2) |
| `signed_at` | UTC timestamp of `nanopub sign` |
| `published_at` | UTC timestamp of `nanopub publish` |

Stages 2–4 read this CSV to resolve `mac:`-prefixed terms when generating templates and instances. Specifically: the generators look up the Trusty URI of the introducing nanopub for each `mac:` term to populate `rdfs:label` entries in the external-resource-labels block (NanoDash UI rendering), and to confirm that referenced classes and predicates are live before signing dependent artifacts.

**Stage 1 closes when:** all 45 terms are published live (validation (a), (b), (c) all pass), and `manifest_live_v2.csv` is committed to `main`. The catalogue can now consume MAC-namespace terms downstream.

---

## §3 — Stage 2: Templates

### 3.1 What Stage 2 produces

Eleven nanopubs, one per FDT type, each a NanoDash assertion template that constrains the form of subsequent instances of that type. Each template is published live on the NSN, pinned to the working Space (`https://w3id.org/spaces/knowledgepixels/incubator/project4` for this catalogue), and renderable in NanoDash's "use this template" form.

The eleven templates and their live Trusty URIs for the demonstration catalogue:

| Type | Template label | Trusty URI |
|---|---|---|
| 1 | Declaring a Spike RBD Variant | `RADOnITa1gjGIQtuENvlB2I7hykzrASzake1bIjGLiAtM` |
| 2 | Declaring a Real-World Occurrence | `RA_-AALlM1rIYcJRsFUrIfSb5KYSvjiHUZbQbN-cpeV6w` |
| 3 | Declaring a Computational Prediction — RMSD | `RALJKysR8vqqqZYXPGHcsI_J0BvPFUmzwOnV9WCGvUjcY` |
| 4 | Declaring a Computational Prediction — SASA | `RALSYeUQIciUad7GTfKjdNkfhP-505fesw6yYtdLoyW18` |
| 5 | Declaring a Computational Prediction — pLDDT | `RAm5j8EmzrS_ZDXEEOkvG2icT27GlbaGoNAS0sCDS72wc` |
| 6 | Declaring a Computational Prediction — AgMata | `RAuCu_OnyqK_dlaJ9l1EDdbtu_Wbpdw2pTlcTimQ9mqV0` |
| 7 | Declaring a Deep Mutational Scanning Observation | `RAp-dZcpmyNxtFsh7G0G1CDzzP2vPqoXVZSnlYRVQ_5Yk` |
| 8 | Declaring a WHO Variant Classification | `RAWyoHGVyB3Rh-fizZguS1zzf8Cim3q5ngWSoQNs2Sgcs` |
| 9 | Declaring a Computational Method | `RA5f4FtcnAGRtdt-vDTCvwXT1yVX7oMoXmvv-B8nfMelc` |
| 10 | Declaring an Experimental Method | `RALExfuvWjR8Lezp7I64cWCHgqyLb52js6-CTDIoINohs` |
| 11 | Declaring an Observational Method | `RAW9DfO6hmmt2sz_H4pHWWAX72BzTsnYjb9hi5wVQIQdE` |

Stage 3 instances will consume these eleven URIs as the values of `nt:wasCreatedFromTemplate` in their pubinfo graphs. The Trusty URIs above are the demonstration catalogue's; new builds against this guide produce new Trusty URIs (content-addressed).

### 3.2 The ntemplate vocabulary primer

NanoDash templates are themselves nanopubs whose assertion graph declares a *template* — a form specification — using the ntemplate vocabulary (`nt:` → `https://w3id.org/np/o/ntemplate/`). The authoritative schema is the meta-template:

```
https://w3id.org/np/RA5reLVXOCPQFWr2UiCJb19ES7NwOpQRmudb17e2iB0c4
```

Title: "Defining an assertion template". This meta-template defines every ntemplate predicate and placeholder class. Treat it as the schema authority; the MAC FDT templates are concrete instances of this schema.

A template's assertion graph contains three kinds of resource, side-by-side:

**(i) The template declaration itself**, naming `sub:assertion` as the template's subject:

```turtle
sub:assertion a nt:AssertionTemplate ;
    rdfs:label "Declaring a Spike RBD Variant (MAC FDT Type 1)" ;
    dct:description "Spike RBD variant FDO …" ;
    nt:hasStatement sub:st0, sub:st3, sub:st4, sub:st1, …, sub:st_a ;
    nt:hasNanopubLabelPattern "Spike RBD Variant ${whoVariantName} (${macSeqId})" ;
    nt:hasTag "MAC" .
```

The `nt:hasStatement` list enumerates every statement pattern in the template. A statement defined in the assertion graph but missing from this list will not render in the form. Order in the list controls UI rendering order (in absence of explicit `nt:statementOrder`).

**(ii) Statement patterns** — each is a reified triple with `rdf:subject`, `rdf:predicate`, `rdf:object`. Mandatory/optional/repeatable is a type annotation on the statement resource:

```turtle
sub:st0 rdf:subject sub:fdo ;                  # mandatory (no rdf:type annotation)
        rdf:predicate rdf:type ;
        rdf:object <https://w3id.org/fdof/ontology#FAIRDigitalObject> .

sub:st1 a nt:OptionalStatement ;               # optional, single-valued
        rdf:subject sub:fdo ;
        rdf:predicate rdfs:label ;
        rdf:object sub:label .

sub:st6 a nt:RepeatableStatement ;             # mandatory, repeatable
        rdf:subject sub:fdo ;
        rdf:predicate dct:creator ;
        rdf:object sub:creator .

sub:st7 a nt:OptionalStatement, nt:RepeatableStatement ;  # optional + repeatable
        rdf:subject sub:fdo ;
        rdf:predicate dct:contributor ;
        rdf:object sub:contributor .
```

A statement can also be **grouped** (children added/removed as a unit) via `nt:GroupedStatement`. The MAC FDT scaffold does not currently use grouped statements at the assertion level (the self-materialization block is structured as four independent mandatory statements; see §3.3).

**(iii) Placeholders** — the form fields. Each is typed by a placeholder class:

| Placeholder class | Form behaviour | Used by MAC FDT templates for |
|---|---|---|
| `nt:UriPlaceholder` | Free-form URI entry | (Used for `sub:fdo`, the introduced URI) |
| `nt:ExternalUriPlaceholder` | URI to a resource outside the nanopub | Method references, variant references, GeoNames, DOIs |
| `nt:LiteralPlaceholder` | Single-line text | Most literals (dates, accessions, metric values) |
| `nt:LongLiteralPlaceholder` | Multi-line text | Description fields |
| `nt:GuidedChoicePlaceholder` | Search-as-you-type from an API | Project picker, FIP picker |
| `nt:RestrictedChoicePlaceholder` | Dropdown from enumerated values | WHO classification (VOC/VOI/VUM) |
| `nt:AgentPlaceholder` | ORCID picker | `sub:creator`, `sub:contributor` |
| `nt:IntroducedResource` | URI minted by this nanopub | The FDO URI (`sub:fdo`) — combined with `nt:LocalResource` and a base placeholder class |

Modifier predicates that constrain placeholder values:

| Predicate | Effect |
|---|---|
| `nt:hasDefaultValue` | Pre-fill the form field |
| `nt:hasRegex` | Validate literal input against a regex |
| `nt:possibleValuesFromApi` | Populate guided-choice from a URL prefix (search term appended) |
| `nt:possibleValuesFrom` | Populate restricted choice from a separate nanopub |
| `nt:possibleValue` | Inline enumeration for restricted choice |

**Special URIs** that NanoDash substitutes at sign/render time:

| URI | Substituted by |
|---|---|
| `nt:NANOPUB` | The Trusty URI of the nanopub being authored (after signing) |
| `nt:ASSERTION` | The URI of the assertion graph |
| `nt:CREATOR` | The signer's ORCID |

The MAC FDT scaffold uses `nt:NANOPUB` in both subject and object positions of the self-materialization block (§3.3). Both positions are admissible.

### 3.3 The common scaffold

All eleven MAC FDT templates share an identical scaffold — the same assertion-graph layout, the same provenance, the same pubinfo bundle — and differ only in their **type-specific layer**: the class URI at `st3`, the type-specific placeholders, and the type-specific statements. The scaffold itself is hardcoded in the generator (§3.5) and reused verbatim across types. Read this subsection once; per-type subsections in §3.4 specify only the differences.

**Namespace declarations** (every template emits exactly these):

```turtle
@prefix this: <http://purl.org/nanopub/temp/np001/> .
@prefix sub:  <http://purl.org/nanopub/temp/np001/> .
@prefix np:   <http://www.nanopub.org/nschema#> .
@prefix dct:  <http://purl.org/dc/terms/> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix nt:   <https://w3id.org/np/o/ntemplate/> .
@prefix npx:  <http://purl.org/nanopub/x/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix orcid: <https://orcid.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix mac:  <https://w3id.org/spaces/mac/r/ontology/> .
```

`fdof:`, `dcat:`, `cito:`, and `schema:` are intentionally **not** declared as prefixes in the common header (a Stage 2 implementation decision documented in SPS v1.4 §"Implementation notes"). Predicates from these namespaces appear as full URIs throughout. A future coordinated revision may consolidate them into the header; see §6 (Appendices) for the cleanup item.

**The head graph** (uniform):

```turtle
sub:Head {
  this: a np:Nanopublication ;
        np:hasAssertion sub:assertion ;
        np:hasProvenance sub:provenance ;
        np:hasPublicationInfo sub:pubinfo .
}
```

**The assertion graph — five blocks in order:**

*Block 1: External-resource labels for NanoDash UI rendering.*

NanoDash renders the form using `rdfs:label` triples it finds adjacent to placeholders and predicates. Templates therefore emit human-readable labels for every external URI they reference. The common scaffold emits the labels for the FDO-vocabulary URIs, the FAIR² DOIs, the encoding format, the CC BY license, and the standard Dublin Core / RDF predicates:

```turtle
sub:assertion {

  <https://w3id.org/fdof/ontology#FAIRDigitalObject> rdfs:label "FAIR Digital Object (FDO)" .
  <https://w3id.org/fdof/ontology#hasMetadata>       rdfs:label "has its metadata in" .
  <https://w3id.org/fdof/ontology#materializes>      rdfs:label "is a concrete materialization of" .
  <https://w3id.org/fdof/ontology#hasEncodingFormat> rdfs:label "has format" .
  <https://www.w3.org/ns/dcat#accessURL>             rdfs:label "has access URL" .
  <https://www.w3.org/ns/dcat#contactPoint>          rdfs:label "has contact point" .
  <https://w3id.org/fair/fip/terms/implements>       rdfs:label "implements" .

  # FAIR² (Type 1 only — omit for Types 2-11)
  <https://doi.org/10.3389/fbinf.2025.1634111> rdfs:label "FAIR² data article (Frontiers in Bioinformatics)" .
  <https://doi.org/10.71728/hw56-vj34>         rdfs:label "FAIR² Data Package DOI" .

  <https://www.iana.org/assignments/media-types/application/trig>
                                               rdfs:label "TriG (RDF named-graph serialization)" .
  <https://creativecommons.org/licenses/by/4.0/> rdfs:label "Attribution 4.0 International (CC BY 4.0)" .

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

  # Per-type: labels for mac:* class and predicates this template uses (see §3.4).
  # Per-type: cito:citesAsAuthority full-URI label when used (Types 2-11; not Type 1).
}
```

*Block 2: Template declaration.*

```turtle
  sub:assertion a nt:AssertionTemplate ;
    rdfs:label "<type-specific template label>" ;
    dct:description "<type-specific description>" ;
    nt:hasNanopubLabelPattern "<type-specific pattern>" ;
    nt:hasStatement
      sub:st0, sub:st3, sub:st4,
      sub:st1, sub:st2,
      sub:st6, sub:st7, sub:st8,
      sub:st91, sub:st92, sub:st95,
      sub:st5, sub:st5b, sub:st5c, sub:st5d,
      sub:st_pp,
      # <type-specific statement IDs>
      # <plus, for Type 1: sub:st_f2a, sub:st_f2p>
    ;
    nt:hasTag "MAC" .
```

The list contains 16 common statement IDs plus the type-specific ones. The order in the list controls UI render order; the order shown above is the convention used across the eleven templates.

*Block 3: Placeholders.*

The ten **standard placeholders** (uniform across all templates):

```turtle
  # Core FDO identifier (the URI this nanopub mints)
  sub:fdo a nt:IntroducedResource, nt:LocalResource, nt:UriPlaceholder ;
    rdfs:label "<noun-phrase suffix, e.g. 'full URI or short suffix for this RMSD observation FDO'>" .

  # Standard descriptive
  sub:label a nt:LiteralPlaceholder ;
    rdfs:label "<example label, type-specific>" .

  sub:description a nt:LongLiteralPlaceholder ;
    rdfs:label "<noun phrase, type-specific>" .

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

  # SPS v1.3+ institutional-provenance placeholder
  sub:project a nt:GuidedChoicePlaceholder ;
    rdfs:label "project" ;
    nt:possibleValuesFromApi "https://w3id.org/np/l/nanopub-query-1.1/api/RAFTZ8GqPOOJQOBcEo5IB8lg5vZCFiIyr_RVLKZDQBHMk/get-projects?searchterm=" .
```

Type-specific placeholders follow in a Block 3b (see §3.4 per-type subsections).

*Block 4: Statement patterns — FDO-constituting, descriptive, and self-materialization.*

The **three FDO-constituting statements** (mandatory; non-negotiable per the FDO Forum specification):

```turtle
  sub:st0 rdf:subject sub:fdo ;
          rdf:predicate rdf:type ;
          rdf:object <https://w3id.org/fdof/ontology#FAIRDigitalObject> .

  sub:st3 rdf:subject sub:fdo ;
          rdf:predicate rdf:type ;
          rdf:object <type-specific class URI, e.g. mac:SpikeRBDVariant> .

  sub:st4 rdf:subject sub:fdo ;
          rdf:predicate <https://w3id.org/fdof/ontology#hasMetadata> ;
          rdf:object nt:NANOPUB .
```

The **standard descriptive statements** (eight, uniform):

```turtle
  sub:st1 a nt:OptionalStatement ;
          rdf:subject sub:fdo ; rdf:predicate rdfs:label ;     rdf:object sub:label .
  sub:st2 a nt:OptionalStatement ;
          rdf:subject sub:fdo ; rdf:predicate rdfs:comment ;   rdf:object sub:description .
  sub:st6 a nt:RepeatableStatement ;
          rdf:subject sub:fdo ; rdf:predicate dct:creator ;    rdf:object sub:creator .
  sub:st7 a nt:OptionalStatement, nt:RepeatableStatement ;
          rdf:subject sub:fdo ; rdf:predicate dct:contributor ; rdf:object sub:contributor .
  sub:st8 rdf:subject sub:fdo ; rdf:predicate <https://www.w3.org/ns/dcat#contactPoint> ;
          rdf:object sub:contact .
  sub:st91 a nt:OptionalStatement ;
           rdf:subject sub:fdo ; rdf:predicate dct:subject ;   rdf:object sub:domain .
  sub:st92 rdf:subject sub:fdo ; rdf:predicate dct:publisher ; rdf:object sub:publisher .
  sub:st95 a nt:OptionalStatement ;
           rdf:subject sub:fdo ; rdf:predicate <https://w3id.org/fair/fip/terms/implements> ;
           rdf:object sub:fip .
```

The **institutional-provenance statement** (SPS v1.3+, mandatory):

```turtle
  sub:st_pp rdf:subject sub:fdo ;
            rdf:predicate dct:isPartOf ;
            rdf:object sub:project .
```

The object is the `sub:project` placeholder, which the instance fills with the referent URI of the Project FDO (for the demonstration catalogue: `https://w3id.org/np/RAFPOe4OIl_urs-U_7-FostjzcUo8ra6LasfSvGplOvto/StayAhead-Project`).

The **self-materialization block** (four mandatory statements, byte-identical across all eleven templates):

```turtle
  sub:st5  rdf:subject nt:NANOPUB ;
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
```

Rationale: the assertion graph is the substance of the FDO; the nanopub TriG file *is* the digital object. Each instance therefore declares itself as its own FDMO (FAIR Digital Media Object). The four statements are not grouped (`nt:GroupedStatement`); they are four independent mandatory statements with `nt:NANOPUB` as subject. SPS v1.4 §"Architectural commitments" formalises this pattern. The block is emitted by the generator from a single constant; no per-type variation.

Type-specific statements follow in a Block 4b (see §3.4).

*Block 5 (Type 1 only): FAIR² fixed cross-references.*

Type 1 anchors carry two additional mandatory statements pointing to the FAIR² data article and Data Package:

```turtle
  sub:st_f2a rdf:subject sub:fdo ;
             rdf:predicate dct:references ;
             rdf:object <https://doi.org/10.3389/fbinf.2025.1634111> .

  sub:st_f2p rdf:subject sub:fdo ;
             rdf:predicate dct:source ;
             rdf:object <https://doi.org/10.71728/hw56-vj34> .
```

Types 2–8 omit these (per SPS v1.4 §"Per-type provenance obligations"); Types 9–11 omit them entirely.

**The provenance graph** (uniform):

```turtle
sub:provenance {
  sub:assertion prov:wasAttributedTo orcid:0000-0001-8888-635X .
}
```

**The pubinfo graph** (uniform except the `rdfs:label` and `dct:created` per template):

```turtle
sub:pubinfo {
  this:
    dct:created "<UTC at signing>"^^xsd:dateTime ;
    dct:creator orcid:0000-0001-8888-635X ;
    dct:license <https://creativecommons.org/licenses/by/4.0/> ;
    rdfs:label "Template: <type-specific template label>" ;
    nt:wasCreatedFromTemplate
      <https://w3id.org/np/RA5reLVXOCPQFWr2UiCJb19ES7NwOpQRmudb17e2iB0c4> ;
    nt:wasCreatedFromProvenanceTemplate
      <https://w3id.org/np/RA7lSq6MuK_TIC6JMSHvLtee3lpLoZDOqLJCLXevnrPoU> ;
    nt:wasCreatedFromPubinfoTemplate
      <https://w3id.org/np/RA0J4vUn_dekg-U1kK3AOEt02p9mT2WO03uGxLDec1jLw>,    # License
      <https://w3id.org/np/RAukAcWHRDlkqxk7H2XNSegc1WnHI569INvNr-xdptDGI>,    # Creator
      <https://w3id.org/np/RAMEgudZsQ1bh1fZhfYnkthqH6YSXpghSE_DEN1I-6eAI>,    # Hand-coded
      <https://w3id.org/np/RARW4MsFkHuwjycNElvEVtuMjpf4yWDL10-0C5l2MqqRQ> .   # Derived
}
```

The four `nt:wasCreatedFromPubinfoTemplate` references are the standard MAC FDT pubinfo bundle. For revisions to an existing template (v2+, superseding a prior version), append a fifth: `RAoTD7…` (the Supersedes template) and add a `npx:supersedes` line. The Stage 2 v1 publish in this guide omits Supersedes.

### 3.4 Per-type configurations

This subsection specifies the type-specific layer for each of the eleven templates. Each entry gives: class URI, type-specific placeholders, type-specific statements, label pattern, and (for Type 1) the worked example in full.

#### 3.4.1 Type 1 — Spike RBD Variant (worked example)

**Class URI:** `mac:SpikeRBDVariant`

**Description (for the template's `dct:description`):**

> "A variant of the SARS-CoV-2 Spike receptor-binding domain (RBD, 195 residues) produced by one or more amino acid substitutions from the wild-type Wuhan isolate (UniProt P0DTC2). This FDO is the central node (the anchor) of a FAIR Digital Twin knowlet; all observation FDOs linking to it via mac:isObservationOf collectively constitute the knowlet. The nanopublication self-materializes (assertion graph is the FDO)."

**Label pattern:** `"Spike RBD Variant ${whoVariantName} (${macSeqId})"`

**MAC-namespace external labels (Block 1 additions):**

```turtle
mac:SpikeRBDVariant      rdfs:label "Spike RBD Variant" .
mac:hasWHOVariantName    rdfs:label "has WHO variant name" .
mac:hasPangoLineage      rdfs:label "has Pango lineage" .
mac:hasGISAIDSeqId       rdfs:label "has GISAID seq_id (full Spike, amino acid change notation)" .
mac:hasMACSeqId          rdfs:label "has MAC seq_id (RBD, amino acid change notation)" .
mac:hasParentProtein     rdfs:label "has parent protein" .
mac:hasRBDSequence       rdfs:label "has RBD amino acid sequence (one-letter code, 195 residues)" .
mac:hasGISAIDAccession   rdfs:label "has GISAID accession number" .
```

**Type-specific placeholders (Block 3b):**

```turtle
sub:whoVariantName a nt:LiteralPlaceholder ;
  rdfs:label "WHO variant name (e.g. Alpha, Epsilon, Eta)" .

sub:pangoLineage a nt:LiteralPlaceholder ;
  rdfs:label "Pango lineage (e.g. B.1.1.7)" .

sub:gisaidSeqId a nt:LiteralPlaceholder ;
  rdfs:label "GISAID seq_id, full-Spike notation (e.g. N501Y)" ;
  nt:hasRegex "^[ACDEFGHIKLMNPQRSTVWY]\\d{1,3}[ACDEFGHIKLMNPQRSTVWY]$" .

sub:macSeqId a nt:LiteralPlaceholder ;
  rdfs:label "MAC seq_id, RBD notation (e.g. N169Y)" ;
  nt:hasRegex "^[ACDEFGHIKLMNPQRSTVWY]\\d{1,3}[ACDEFGHIKLMNPQRSTVWY]$" .

sub:rbdSequence a nt:LongLiteralPlaceholder ;
  rdfs:label "RBD amino-acid sequence (one-letter code, exactly 195 residues)" ;
  nt:hasRegex "^[ACDEFGHIKLMNPQRSTVWY]{195}$" .

sub:gisaidAccession a nt:LiteralPlaceholder ;
  rdfs:label "canonical GISAID accession (EPI_ISL_XXXXXXX)" ;
  nt:hasRegex "^EPI_ISL_\\d+$" .
```

The four regexes constrain biological identifiers at authoring time. The RBD-sequence length check (`{195}`) catches the most consequential class of error — a truncated paste from an external sequence source. The seq_id patterns enforce single-substitution notation; multi-substitution catalogues (e.g., the planned 3705-mutation Tranche 2 scale-up) will require relaxed patterns or a different representation.

**Type-specific statements (Block 4b):**

```turtle
sub:st_w rdf:subject sub:fdo ; rdf:predicate mac:hasWHOVariantName ;  rdf:object sub:whoVariantName .
sub:st_p rdf:subject sub:fdo ; rdf:predicate mac:hasPangoLineage ;    rdf:object sub:pangoLineage .
sub:st_g rdf:subject sub:fdo ; rdf:predicate mac:hasGISAIDSeqId ;     rdf:object sub:gisaidSeqId .
sub:st_m rdf:subject sub:fdo ; rdf:predicate mac:hasMACSeqId ;        rdf:object sub:macSeqId .
sub:st_u rdf:subject sub:fdo ; rdf:predicate mac:hasParentProtein ;
         rdf:object <https://www.uniprot.org/uniprot/P0DTC2> .                      # hardcoded
sub:st_s rdf:subject sub:fdo ; rdf:predicate mac:hasRBDSequence ;     rdf:object sub:rbdSequence .
sub:st_a a nt:OptionalStatement ;
         rdf:subject sub:fdo ; rdf:predicate mac:hasGISAIDAccession ; rdf:object sub:gisaidAccession .
```

`mac:hasParentProtein` is the one statement with a hardcoded object (the UniProt URI for the wild-type Spike). All RBD variants in this catalogue derive from the same parent; encoding it at the template level rather than as a per-instance placeholder eliminates an error class. The `sub:st_a` (GISAID accession) is optional — Type 1 anchors carry a canonical representative accession, but the SPS treats it as exemplary rather than definitive (occurrences carry their own accessions at Type 2).

**Statement-ID order in `nt:hasStatement`:**

```
sub:st0, sub:st3, sub:st4,                                              # FDO-constituting
sub:st1, sub:st2,                                                       # label, comment
sub:st6, sub:st7, sub:st8,                                              # creator, contributor, contact
sub:st91, sub:st92, sub:st95,                                           # domain, publisher, FIP
sub:st5, sub:st5b, sub:st5c, sub:st5d,                                  # self-materialization
sub:st_pp,                                                              # dct:isPartOf
sub:st_w, sub:st_p, sub:st_g, sub:st_m, sub:st_u, sub:st_s, sub:st_a,   # Type-1 specific
sub:st_f2a, sub:st_f2p                                                  # FAIR² (Type 1 only)
```

**Live Trusty URI of the published Type 1 template:**

```
https://w3id.org/np/RADOnITa1gjGIQtuENvlB2I7hykzrASzake1bIjGLiAtM
```

Stage 3 Type 1 instances declare `nt:wasCreatedFromTemplate` → this URI in their pubinfo. Verification of the template's correctness is in §3.8.

#### 3.4.2 Type 2 — Real-World Occurrence

**Class URI:** `mac:RealWorldOccurrence`. **Label pattern:** `"Real-world occurrence (${occurrenceDate})"`. **Includes FAIR² block:** No.

**Type-specific placeholders (6):** `sub:variant` (ExternalUri, the Type 1 referent URI), `sub:surveillanceMethod` (ExternalUri, Type 11 method), `sub:authority` (ExternalUri, optional one-hop citation), `sub:occurrenceDate` (Literal, no regex; SPS accepts fuzzy dates like "late 2020–2021"), `sub:location` (ExternalUri, GeoNames feature URI), `sub:gisaidAccession` (Literal, regex `^EPI_ISL_\d+$`).

**Type-specific statements (6):**

| ID | Predicate | Object | Flags |
|---|---|---|---|
| `st_obs` | `mac:isObservationOf` | `sub:variant` | mandatory |
| `st_sm` | `mac:hasSurveillanceMethod` | `sub:surveillanceMethod` | optional |
| `st_oc` | `cito:citesAsAuthority` (full URI) | `sub:authority` | optional, repeatable |
| `st_d` | `mac:hasOccurrenceDate` | `sub:occurrenceDate` | mandatory |
| `st_l` | `mac:hasCollectionLocation` | `sub:location` | mandatory |
| `st_gi` | `mac:hasGISAIDAccession` | `sub:gisaidAccession` | optional |

**Live Trusty URI:** `https://w3id.org/np/RA_-AALlM1rIYcJRsFUrIfSb5KYSvjiHUZbQbN-cpeV6w`.

#### 3.4.3–3.4.5 Types 3, 4, 5 — Computational Predictions (RMSD, SASA, pLDDT)

Structurally identical. Per-type differences are tabulated.

| Field | Type 3 (RMSD) | Type 4 (SASA) | Type 5 (pLDDT) |
|---|---|---|---|
| Class URI | `mac:ComputationalPredictionRMSD` | `mac:ComputationalPredictionSASA` | `mac:ComputationalPredictionPLDDT` |
| Metric predicate | `mac:hasRMSD` | `mac:hasSASA` | `mac:haspLDDT` |
| Value placeholder label | "RMSD value (Angstroms)" | "SASA value (square Angstroms)" | "pLDDT score (0-100, unitless)" |
| Label pattern | `"RMSD = ${value} A (${predictionMethod})"` | `"SASA = ${value} A^2 (${predictionMethod})"` | `"pLDDT = ${value} (${predictionMethod})"` |
| Live Trusty URI | `RALJKysR8vqqqZYXPGHcsI_J0BvPFUmzwOnV9WCGvUjcY` | `RALSYeUQIciUad7GTfKjdNkfhP-505fesw6yYtdLoyW18` | `RAm5j8EmzrS_ZDXEEOkvG2icT27GlbaGoNAS0sCDS72wc` |

**Common to all three** — type-specific placeholders (5): `sub:variant` (ExternalUri, Type 1 anchor), `sub:predictionMethod` (ExternalUri, Type 9 method), `sub:authority` (ExternalUri, optional one-hop), `sub:source` (ExternalUri, repeatable; carries FAIR² package DOI + resource URL + optional OSF), `sub:value` (Literal, no regex; decimal verbatim).

**Type-specific statements (5):**

| ID | Predicate | Object | Flags |
|---|---|---|---|
| `st_obs` | `mac:isObservationOf` | `sub:variant` | mandatory |
| `st_pm` | `mac:hasPredictionMethod` | `sub:predictionMethod` | mandatory |
| `st_oc` | `cito:citesAsAuthority` | `sub:authority` | optional, repeatable |
| `st_val` | *(metric predicate per type)* | `sub:value` | mandatory |
| `st_src` | `dct:source` | `sub:source` | mandatory, repeatable |

**Includes FAIR² block:** No (the per-observation `dct:source` carries the FAIR² Package + resource URL on each instance).

#### 3.4.6 Type 6 — Computational Prediction (AgMata)

Identical structure to Types 3–5. **Class URI:** `mac:ComputationalPredictionAgMata`. **Metric predicate:** `mac:hasAgMataScore`. **Value placeholder label:** "AgMata score (unitless)". **Label pattern:** `"AgMata = ${value}"` (method-fixed: Bio2Byte; not parameterised per instance). **Live Trusty URI:** `RAuCu_OnyqK_dlaJ9l1EDdbtu_Wbpdw2pTlcTimQ9mqV0`.

#### 3.4.7 Type 7 — Deep Mutational Scanning Observation

**Class URI:** `mac:ExperimentalDMSObservation`. **Label pattern:** `"DMS observation (bind=${bind}, expr=${expr})"`. **Includes FAIR² block:** No.

**Type-specific placeholders (10):** `sub:variant`, `sub:experimentalMethod`, `sub:authority`, `sub:source`, plus six measured values: `sub:bind`, `sub:deltaBind`, `sub:expr`, `sub:deltaExpr`, `sub:confidenceBind`, `sub:confidenceExpr` (all `nt:LiteralPlaceholder`, no regex).

**Type-specific statements (10):** `st_obs` (`mac:isObservationOf` → variant, mandatory); `st_em` (`mac:hasExperimentalMethod` → method, mandatory); `st_oc` (`cito:citesAsAuthority`, optional + repeatable); six mandatory metric statements (`st_bi mac:hasBind`, `st_db mac:hasDeltaBind`, `st_ex mac:hasExpr`, `st_de mac:hasDeltaExpr`, `st_cb mac:hasConfidenceBind`, `st_ce mac:hasConfidenceExpr`); `st_src` (`dct:source`, optional + repeatable — note: differs from Types 3–6 where `dct:source` is mandatory).

**Live Trusty URI:** `RAp-dZcpmyNxtFsh7G0G1CDzzP2vPqoXVZSnlYRVQ_5Yk`.

#### 3.4.8 Type 8 — WHO Variant Classification

**Class URI:** `mac:WHOVariantClassification`. **Label pattern:** `"WHO classification: ${classification} (${classificationDate})"`. **Includes FAIR² block:** No.

**Type-specific placeholders (5):** `sub:variant` (ExternalUri), `sub:authority` (ExternalUri), `sub:classification` (**`nt:RestrictedChoicePlaceholder`** with inline enumeration: `nt:possibleValue mac:VOC, mac:VOI, mac:VUM`), `sub:classificationDate` (Literal), `sub:classificationRef` (ExternalUri).

**Type-specific statements (5):** `st_obs` (mandatory); `st_oc` (`cito:citesAsAuthority`, optional + repeatable); `st_wc` (`mac:hasWHOClassification` → `sub:classification`, mandatory); `st_cd` (`mac:hasClassificationDate`, optional); `st_cr` (`mac:hasWHOClassificationReference`, optional).

**Live Trusty URI:** `RAWyoHGVyB3Rh-fizZguS1zzf8Cim3q5ngWSoQNs2Sgcs`. **No method link** (WHO classifications are designations, not observation-by-method outputs).

#### 3.4.9–3.4.11 Types 9, 10, 11 — Methods (Computational, Experimental, Observational)

Structurally identical to each other; simpler than the observation types. Differences:

| Field | Type 9 | Type 10 | Type 11 |
|---|---|---|---|
| Class URI | `mac:ComputationalMethod` | `mac:ExperimentalMethod` | `mac:ObservationalMethod` |
| URL placeholder label | "software URL" | "data resource URL" | "platform URL" |
| Referenced by | Types 3–6 (via `mac:hasPredictionMethod`) | Type 7 (via `mac:hasExperimentalMethod`) | Type 2 (via `mac:hasSurveillanceMethod`) |
| Live Trusty URI | `RA5f4FtcnAGRtdt-vDTCvwXT1yVX7oMoXmvv-B8nfMelc` | `RALExfuvWjR8Lezp7I64cWCHgqyLb52js6-CTDIoINohs` | `RAW9DfO6hmmt2sz_H4pHWWAX72BzTsnYjb9hi5wVQIQdE` |

**Common to all three** — type-specific placeholders (3): `sub:authority` (ExternalUri, **mandatory + repeatable**; method must declare ≥1 published authority), `sub:url` (ExternalUri, optional).

**Type-specific statements (2):**

| ID | Predicate | Object | Flags |
|---|---|---|---|
| `st_ci` | `cito:citesAsAuthority` (full URI) | `sub:authority` | mandatory, repeatable |
| `st_su` | `schema:url` (full URI) | `sub:url` | optional |

**Important difference from observation types:** `cito:citesAsAuthority` is **mandatory** on method templates (every method declares its published description) but **optional** on observation templates (one-hop attribution is permitted but not required; the two-hop method-attribution path is the default).

**Method templates carry no `mac:isObservationOf`, no `dct:source`, no `dct:references`, no FAIR² block.**

### 3.5 The template generator

The generator architecture is one Python module (`generate_template.py`) that emits any of the eleven templates from a per-type config dictionary plus the hardcoded common scaffold. Configs are Python files under `configs/type{1-11}_config.py`.

**Per-type config schema** (a Python `dict` named `CONFIG`):

```python
CONFIG = {
    "type_id":             "type1",
    "type_label_short":    "Type 1",
    "class_curie":         "mac:SpikeRBDVariant",
    "includes_fair2":      True,                          # only Type 1
    "template_label":      "Declaring a Spike RBD Variant (MAC FDT Type 1)",
    "template_description": "<full description>",
    "label_pattern":       "Spike RBD Variant ${whoVariantName} (${macSeqId})",

    # Noun-phrase texts for sub:fdo, sub:label, sub:description labels
    "fdo_label_text":              "full URI or short suffix for this variant FDO",
    "label_placeholder_text":      "label or name for this variant (e.g. \"Alpha (N169Y)\")",
    "description_placeholder_text": "free-text description of this variant",

    # Non-mac external URIs whose labels go in Block 1
    "external_resource_labels": [
        ("https://www.uniprot.org/uniprot/P0DTC2", "wild-type Spike (UniProt P0DTC2)"),
    ],

    # mac:* terms used in this template (class + predicates)
    "mac_term_labels": [
        ("mac:SpikeRBDVariant",    "Spike RBD Variant"),
        ("mac:hasWHOVariantName",  "has WHO variant name"),
        # … one entry per mac: term referenced …
    ],

    # Statement-ID list (Block 2's nt:hasStatement type-specific portion)
    "type_specific_statement_ids": [
        "sub:st_w", "sub:st_p", "sub:st_g", "sub:st_m",
        "sub:st_u", "sub:st_s", "sub:st_a",
    ],

    # Type-specific placeholder declarations (Block 3b)
    "placeholders": [
        {"id": "sub:whoVariantName", "types": ["nt:LiteralPlaceholder"],
         "label": "WHO variant name (e.g. Alpha, Epsilon, Eta)"},
        # … one per placeholder, with optional extras for regex / API / etc.
    ],

    # Type-specific statement patterns (Block 4b)
    "statements": [
        {"id": "sub:st_w", "subject": "sub:fdo",
         "predicate": "mac:hasWHOVariantName", "object": "sub:whoVariantName"},
        # … one per statement, with optional st_types list for flags …
    ],
}
```

The generator:
1. Loads the config module.
2. Concatenates: prefixes + head graph + assertion-graph blocks (1 external labels, 2 template declaration, 3 standard placeholders, 3b type-specific placeholders, 4 standard statements + self-materialization, 4b type-specific statements, 5 FAIR² if `includes_fair2`) + provenance graph + pubinfo graph.
3. Writes to `drafts/template_<type_id>_<descriptor>_v1.trig`.

The common scaffold blocks (1 partial, 2 wrapper, 3, 4 partial, provenance, pubinfo) are hardcoded constants in `generate_template.py`. Per-type variation is entirely in the config dict.

**Validation requirement:** the generator must round-trip Type 1 v4 byte-for-byte (modulo `dct:created`). This regression check, run after every modification, prevents the generator from drifting away from the canonical template structure. SHA256 hash of the output (after timestamp normalisation) is the regression invariant.

Full generator source: `minting/stage2-templates/generator/generate_template.py` (~400 lines).

Generation command:

```
cd minting/stage2-templates/
python generator/generate_template.py generator/configs/type1_config.py \
    --out drafts/template_type1_spike_rbd_variant_v1.trig
```

### 3.6 Signing and publishing

Per template:

```
nanopub sign drafts/template_<type_id>_<descriptor>_v1.trig
mv drafts/signed.template_<type_id>_<descriptor>_v1.trig signed/
nanopub check signed/template_<type_id>_<descriptor>_v1.trig
    # expect: 1 trusty with signature
nanopub publish signed/template_<type_id>_<descriptor>_v1.trig
    # publishes to live NSN
```

**Order does not matter at the assertion level.** Templates do not cross-reference each other (each is independent; instances do the cross-referencing later). Practical order used in the demonstration build: Type 1, then Type 2, then Types 3–5 batched, then Type 6, Type 7, Type 8, Types 9–11 batched. Any order is valid.

After each publish, record the live Trusty URI plus publish timestamp in `PUBLISHED_templates.md` (or per-type files; the convention in the demonstration build was per-type `PUBLISHED_v4.md`).

### 3.7 Pinning to the Space

Pinning makes the template appear under "Pinned templates" on the Space page and selectable via "use this template" links. The mechanism is **federated per-action**: one pin-action nanopub per template, not a monolithic Space-definition supersession.

**Pin-action template:** `https://w3id.org/np/RA2YwreWrGW9HkzWls8jgwaIINKUB5ZTli1aFKQt13dUk` ("Declare a pinned template for a Space").

**Assertion graph of a pin-action** (two statements):

```turtle
sub:assertion {
  <project4-space> gen:hasPinnedTemplate <template-Trusty-URI> .
  <template-Trusty-URI> gen:hasPinGroupTag "<group label, e.g. 'MAC FDT Type 1'>" .
}
```

Where `<project4-space>` = `https://w3id.org/spaces/knowledgepixels/incubator/project4` for the demonstration; `<template-Trusty-URI>` is the bare Trusty URI of the published template; the group tag is a freeform label used by NanoDash to group pinned templates in the sidebar.

The pin-action carries `npx:hasNanopubType <gen:hasPinnedTemplate>` in pubinfo (set by the pin-template authoring flow).

**Authorisation:** the signer must hold `gen:hasAdmin` (for Space-typed projects) or `gen:hasOwner` (for NanodashProject-typed projects) on the target Space, declared in the Space-definition nanopub. For project4, Erik holds `gen:hasAdmin`.

**Method:** authoring via NanoDash UI is the practical path (the form picks the Space and the template from search-as-you-type lookups). Eleven pin-actions, one per template, signed by the admin. No supersession of the Space-definition nanopub is required — the federated model is purely additive.

### 3.8 Validation

After all eleven templates are published and pinned, run the following checks:

**(a) HTTP resolution per template:**

```bash
for trusty in RADOnITa1gj... RA_-AALlM1r... RALJKysR8vqq... \
              RALSYeUQIciU... RAm5j8EmzrS_... RAuCu_OnyqK_... \
              RAp-dZcpmyNx... RAWyoHGVyB3R... RA5f4FtcnAGR... \
              RALExfuvWjR8... RAW9DfO6hmmt...; do
  curl -s -o /dev/null -w "%{http_code} $trusty\n" \
       -L "https://w3id.org/np/$trusty"
done
```

Expect eleven `200` responses.

**(b) "use this template" form rendering:**

For each Trusty URI, open `https://nanodash.knowledgepixels.com/publish?template=https://w3id.org/np/<trusty>` (authenticated session via ORCID OAuth). The form should render with all type-specific placeholders visible and the correct regex validation behaviour (test by entering an out-of-spec value for a regex-validated field — submit should be refused).

**(c) Pin-listing on the Space page:**

```sparql
PREFIX gen: <https://w3id.org/kpxl/gen/terms/>
PREFIX np:  <http://www.nanopub.org/nschema#>
PREFIX npa: <http://purl.org/nanopub/admin/>
PREFIX npx: <http://purl.org/nanopub/x/>

SELECT ?template ?tag WHERE {
  GRAPH npa:graph {
    ?n1 npa:hasValidSignatureForPublicKey ?pubkey .
    FILTER NOT EXISTS { ?np2 npx:invalidates ?n1 ;
                            npa:hasValidSignatureForPublicKey ?pubkey . }
    ?n1 np:hasAssertion ?a .
  }
  GRAPH ?a {
    <https://w3id.org/spaces/knowledgepixels/incubator/project4>
        gen:hasPinnedTemplate ?template .
    OPTIONAL { ?template gen:hasPinGroupTag ?tag . }
  }
}
```

Endpoint: `https://w3id.org/np/l/nanopub-query-1.1/repo/full`. Expect eleven rows, one per template.

**(d) NanoDash Space-page rendering:**

Open `https://nanodash.knowledgepixels.com/space?id=https://w3id.org/spaces/knowledgepixels/incubator/project4`. After indexing (minutes to hours), the "Pinned templates" panel lists all eleven templates with their labels.

**Stage 2 closes when:** all eleven templates are published live (validation (a), (b) pass), all eleven pin-actions are published (validation (c) returns eleven rows), and NanoDash renders the Pinned-templates panel (validation (d)). The catalogue can now consume the templates to produce Stage 3 instances.

---

## §4 — Stage 3: Instances

### 4.1 What Stage 3 produces

Thirty-eight instance nanopubs, each one a typed FAIR Digital Object populated against a Stage 2 template, published live on the NSN. For the demonstration catalogue covering the Alpha, Epsilon, and Eta variants:

| Group | Type(s) | Count | Per twin | Path |
|---|---|---|---|---|
| Variant anchors | 1 | 3 | 1 | Hand-written configs |
| Methods (shared) | 9, 10, 11 | 5 | — | Hand-written configs |
| Computational predictions | 3, 4, 5 | 18 | 6 | CSV-driven |
| AgMata predictions | 6 | 3 | 1 | CSV-driven |
| DMS observations | 7 | 3 | 1 | CSV-driven (within Types 6+7 driver) |
| Real-world occurrences | 2 | 3 | 1 | Hand-written configs |
| WHO classifications | 8 | 3 | 1 | Hand-written configs |
| **Total** | | **38** | | |

The thirty Type 2–8 observations are partitioned across three FAIR Digital Twins (ten observations per variant), each twin anchored on one Type 1 FDO and sharing the five Type 9–11 method FDOs.

Stage 3 deliverables, by filesystem location:

- `minting/stage3-instances/generator/` — `generate_instance.py` plus three CSV-driven drivers and per-instance Python configs.
- `minting/stage3-instances/drafts/` — 38 unsigned TriG files.
- `minting/stage3-instances/signed/` — 38 signed TriG files.
- `minting/stage3-instances/PUBLISHED_type1_instances.md`, `PUBLISHED_methods.md`, `PUBLISHED_predictions.md`, `PUBLISHED_observations_final.md` — publication records, one per batch.

The published Trusty URIs are listed in §4.4 by type and summarised in the Reference Appendices (§6).

### 4.2 The instance-vs-template distinction

A Stage 2 template declares `sub:assertion a nt:AssertionTemplate` and contains placeholders; a Stage 3 instance declares the typed FDO directly and contains concrete values in the positions placeholders previously occupied. Structurally:

| Element | Template (Stage 2) | Instance (Stage 3) |
|---|---|---|
| Assertion subject | `sub:assertion a nt:AssertionTemplate` | `sub:<instance_id> a fdof:FAIRDigitalObject, mac:<class>` |
| Placeholders | Declared as `nt:LiteralPlaceholder`, `nt:ExternalUriPlaceholder`, etc. | Absent — replaced by concrete values |
| Reified statements | `sub:st0 rdf:subject … rdf:predicate … rdf:object …` | Absent — replaced by direct RDF assertions |
| `nt:hasStatement` list | Present | Absent |
| Pubinfo `nt:wasCreatedFromTemplate` | Points to the meta-template `RA5reLVX…` | Points to the Stage 2 template (e.g. Type 1 URI `RADOnITa1gj…`) |
| Pubinfo `npx:hasNanopubType` | `nt:AssertionTemplate` | (none — instances are plain typed nanopubs) |
| Self-materialization block | Reified four-statement pattern | Direct four-statement assertions, byte-identical structure |

An instance is therefore a *populated form*: the template's `sub:st0`/`st3`/`st4` become direct triples on the instance's `sub:fdo`; the type-specific placeholders are replaced by their values; the self-materialization block is emitted as four direct triples on `nt:NANOPUB`.

The instance's pubinfo declares `nt:wasCreatedFromTemplate` pointing at the Stage 2 template's live Trusty URI. This is the machine-traversable claim that the instance conforms to the template — NanoDash uses it for "edit this instance" workflows; consumers use it to discover which template's schema applies.

### 4.3 The instance generator

The generator is one Python module (`generate_instance.py`) with three published code paths plus per-instance configs:

| Path | Used for | Driver |
|---|---|---|
| `kind: "type1"` | Variant anchors (Type 1) | Hand-written configs in `instance_configs/type1_*.py` |
| `kind: "method"` | Method FDOs (Types 9–11) | Hand-written configs in `instance_configs/method_*.py` |
| `kind: "prediction"` | Types 3–6 (single-value computational predictions) | `generate_predictions_from_csv.py` (Types 3-5) and `generate_type6_7_from_csv.py` (Types 6, 7) |
| `kind: "occurrence"` | Type 2 real-world occurrences | Hand-written configs in `instance_configs/type2_*.py` |
| `kind: "who"` | Type 8 WHO classifications | Hand-written configs in `instance_configs/type8_*.py` |
| `kind: "dms"` | Type 7 DMS (6 simultaneous metric values) | CSV-driven via `generate_type6_7_from_csv.py` |

The generator factors the work as follows:

1. **Common scaffold constants** — the prefix block, head graph, provenance graph, and pubinfo bundle are identical across all 38 instances (modulo `dct:created` timestamp and `nt:wasCreatedFromTemplate` target). Defined once as Python string templates.

2. **The self-materialization block** — four lines, byte-identical to the Stage 2 templates' `st5`/`st5b`/`st5c`/`st5d` statements but as direct triples rather than reified patterns:

   ```turtle
   nt:NANOPUB <https://w3id.org/fdof/ontology#materializes> sub:<instance_id> .
   nt:NANOPUB <https://w3id.org/fdof/ontology#hasEncodingFormat>
              <https://www.iana.org/assignments/media-types/application/trig> .
   nt:NANOPUB dct:license <https://creativecommons.org/licenses/by/4.0/> .
   nt:NANOPUB <https://www.w3.org/ns/dcat#accessURL> nt:NANOPUB .
   ```

   `nt:NANOPUB` is substituted by `nanopub sign` to the instance's Trusty URI at signing time. The block is emitted from a single constant; every instance carries it identically.

3. **Per-kind assertion builders** — each kind has an assertion-graph builder that takes a config dict and returns the assertion-graph block as a string. The builder handles type-specific placeholders → concrete values and emits type-specific statements (`mac:hasRMSD`, `mac:isObservationOf`, etc.).

4. **A single `generate(config, created)` dispatch** — switches on `config["kind"]`, calls the right builder, concatenates with the shared scaffold, and returns the full TriG.

Per-instance config schema (Type 1 example):

```python
CONFIG = {
    "kind":               "type1",
    "instance_id":        "Alpha-RBD-Variant",
    "instance_label":     "Spike RBD Variant Alpha (N169Y)",
    "instance_description": "Spike RBD variant Alpha, the WHO designation \
        for SARS-CoV-2 lineage B.1.1.7. Carries the single Spike substitution \
        N501Y (full Spike numbering); in MAC RBD-only numbering this is N169Y. \
        Real-world emergence in late 2020 in southeast England; designated \
        Variant of Concern by WHO on 18 December 2020.",
    "who_variant_name":   "Alpha",
    "pango_lineage":      "B.1.1.7",
    "gisaid_seq_id":      "N501Y",
    "mac_seq_id":         "N169Y",
    "rbd_sequence":       "TNLCPFGEVFNATRFASVYAWNRKR...VCGP",  # 195 chars
    "gisaid_accession":   "EPI_ISL_601443",
    "creator_orcid":      "https://orcid.org/0000-0001-8888-635X",
    "contact_email":      "e.a.schultes@lacdr.leidenuniv.nl",
    "publisher_ror":      "https://ror.org/027bh9e22",
    "template_uri":       "https://w3id.org/np/RADOnITa1gjGIQtuENvlB2I7hykzrASzake1bIjGLiAtM",
}
```

Per-instance config schema (method example):

```python
CONFIG = {
    "kind":               "method",
    "instance_id":        "AlphaFold2-Method",
    "instance_label":     "AlphaFold 2 — DeepMind structure predictor",
    "instance_description": "AlphaFold 2 (DeepMind) protein structure prediction system.",
    "class_curie":        "mac:ComputationalMethod",
    "template_uri":       "https://w3id.org/np/RA5f4FtcnAGRtdt-vDTCvwXT1yVX7oMoXmvv-B8nfMelc",
    "authorities":        ["https://doi.org/10.1038/s41586-021-03819-2"],
    "url":                "https://github.com/google-deepmind/alphafold",
    "creator_orcid":      "https://orcid.org/0000-0001-8888-635X",
    "contact_email":      "e.a.schultes@lacdr.leidenuniv.nl",
    "publisher_ror":      "https://ror.org/027bh9e22",
}
```

**Validation embedded in the generator:**

- `validate_config(config)` — checks all required keys for the given `kind` are present, that regex-constrained fields match (MAC seq_id, GISAID accession, RBD sequence length 195 + alphabet), that `authorities` is a non-empty list for methods.
- `check_mandatory_statements(trig)` — after generation, scans the TriG text for markers of every mandatory statement the SPS requires for that type. Returns a `(missing, forbidden_present)` tuple; both must be empty for the instance to be considered valid.
- `nanopub check` (external) — confirms the unsigned TriG is structurally valid as a nanopublication.

**Regression invariant:** running the generator against any unchanged config must produce byte-identical output (modulo `dct:created`). Enforced by computing SHA256 of the timestamp-normalised TriG and comparing against a recorded baseline. Run after every modification to `generate_instance.py`.

Full generator source: `minting/stage3-instances/generator/generate_instance.py` (~600 lines).

### 4.4 Per-type instance production

This subsection walks through the production of all 38 instances, in the order they were published (which is also the dependency order — anchors and methods before observations).

#### 4.4.1 Type 1 anchors (3 instances, hand-written configs)

Three instances: Alpha, Epsilon, Eta. Configs in `instance_configs/type1_{alpha,epsilon,eta}.py`. Per-config shared fields: `kind`, `creator_orcid`, `contact_email`, `publisher_ror`, `template_uri`. Per-variant fields: `instance_id`, `instance_label`, `instance_description`, `who_variant_name`, `pango_lineage`, `gisaid_seq_id`, `mac_seq_id`, `rbd_sequence` (195 chars), `gisaid_accession`.

**Per-variant data:**

| Field | Alpha | Epsilon | Eta |
|---|---|---|---|
| instance_id | `Alpha-RBD-Variant` | `Epsilon-RBD-Variant` | `Eta-RBD-Variant` |
| who_variant_name | "Alpha" | "Epsilon" | "Eta" |
| pango_lineage | "B.1.1.7" | "B.1.427 + B.1.429" | "B.1.525" |
| gisaid_seq_id | "N501Y" | "L452R" | "E484K" |
| mac_seq_id | "N169Y" | "L120R" | "E152K" |
| gisaid_accession | "EPI_ISL_601443" | "EPI_ISL_2295356" | "EPI_ISL_941290" |

**Note on the Epsilon gisaid_seq_id correction.** The Stage 1 SPS v1.3 and the demonstration CSV (`FDT4Claude_small_v1_2.csv`) carry `L124R` for Epsilon's full-Spike notation. This is an upstream data-entry error: Epsilon's canonical defining Spike substitution is `L452R` (lineages B.1.427/B.1.429), and the position math is consistent with the other two variants (MAC RBD position + 332 = full-Spike position: Alpha N169 + 332 = N501 ✓, Eta E152 + 332 = E484 ✓, Epsilon L120 + 332 = **L452** — not L124). The instance config carries the correct value `L452R`; the SPS and CSV are flagged for correction in the coordinated cleanup pass (`Post_demonstration_cleanup.md`). Demo data is right at publication; documentation catches up later.

**Worked Alpha example — assembled assertion graph after generation:**

```turtle
sub:assertion {

  # External-resource labels (Block 1) — same set as the Type 1 template

  sub:Alpha-RBD-Variant a <https://w3id.org/fdof/ontology#FAIRDigitalObject> ;
      a mac:SpikeRBDVariant ;
      <https://w3id.org/fdof/ontology#hasMetadata> nt:NANOPUB ;

      rdfs:label   "Spike RBD Variant Alpha (N169Y)" ;
      rdfs:comment "Spike RBD variant Alpha, the WHO designation for …" ;

      dct:creator orcid:0000-0001-8888-635X ;
      <https://www.w3.org/ns/dcat#contactPoint> "e.a.schultes@lacdr.leidenuniv.nl" ;
      dct:publisher <https://ror.org/027bh9e22> ;

      dct:isPartOf <https://w3id.org/np/RAFPOe4OIl_urs-U_7-FostjzcUo8ra6LasfSvGplOvto/StayAhead-Project> ;

      mac:hasWHOVariantName    "Alpha" ;
      mac:hasPangoLineage      "B.1.1.7" ;
      mac:hasGISAIDSeqId       "N501Y" ;
      mac:hasMACSeqId          "N169Y" ;
      mac:hasParentProtein     <https://www.uniprot.org/uniprot/P0DTC2> ;
      mac:hasRBDSequence       "TNLCPFGEVFNATRFASVYAWNRKR…VCGP" ;
      mac:hasGISAIDAccession   "EPI_ISL_601443" ;

      dct:references <https://doi.org/10.3389/fbinf.2025.1634111> ;
      dct:source     <https://doi.org/10.71728/hw56-vj34> .

  # Self-materialization block — identical four statements as in Stage 2 templates,
  # emitted as direct triples on nt:NANOPUB.

  nt:NANOPUB <https://w3id.org/fdof/ontology#materializes> sub:Alpha-RBD-Variant .
  nt:NANOPUB <https://w3id.org/fdof/ontology#hasEncodingFormat>
             <https://www.iana.org/assignments/media-types/application/trig> .
  nt:NANOPUB dct:license <https://creativecommons.org/licenses/by/4.0/> .
  nt:NANOPUB <https://www.w3.org/ns/dcat#accessURL> nt:NANOPUB .
}
```

**Published Trusty URIs (Type 1 anchors):**

| Variant | Trusty URI | Referent URI (for downstream cross-references) |
|---|---|---|
| Alpha | `https://w3id.org/np/RA4BHII2Bz7HfpUkaSJqNmhjF8F7hyWpCJnvXYkA4EP_M` | `<Trusty>/Alpha-RBD-Variant` |
| Epsilon | `https://w3id.org/np/RAbyuWWdW-j1rYt7Eqnva6aBvMyTkM9_Ka2FbA9dJHR7s` | `<Trusty>/Epsilon-RBD-Variant` |
| Eta | `https://w3id.org/np/RAikllrKWQoo81RYYvGJjWfzE0QiGrLquMMIwDD6xem2s` | `<Trusty>/Eta-RBD-Variant` |

**Generation command** (per variant):

```
cd minting/stage3-instances/
python generator/generate_instance.py \
    generator/instance_configs/type1_alpha.py \
    --out drafts/instance_type1_alpha_v1.trig
```

**Important — the referent URI form.** The instance declares `sub:Alpha-RBD-Variant` (a subject in the assertion graph). After signing, the `sub:` prefix becomes the published Trusty URI plus a trailing path component, yielding `https://w3id.org/np/RA4BHII2Bz7HfpUkaSJqNmhjF8F7hyWpCJnvXYkA4EP_M/Alpha-RBD-Variant`. This is the **referent URI**: the address of the FDO itself, distinct from the address of the nanopublication that introduces it. Stage 3 observations and Stage 4 queries reference the variant by its referent URI, **not** by the bare Trusty URI of the introducing nanopub.

#### 4.4.2 Method instances (5 instances, hand-written configs)

Five method FDOs, shared across all three twins. Three Type 9 (computational), one Type 10 (experimental), one Type 11 (observational).

| Method | Type | `class_curie` | Authorities (DOIs) | URL | Used by |
|---|---|---|---|---|---|
| ESM2 | 9 | `mac:ComputationalMethod` | `10.1126/science.ade2574` | `github.com/facebookresearch/esm` | Types 3-5 (ESM rows), Type 6 (AgMata input) |
| AlphaFold 2 | 9 | `mac:ComputationalMethod` | `10.1038/s41586-021-03819-2` | `github.com/google-deepmind/alphafold` | Types 3-5 (AF rows) |
| AgMata (Bio2Byte) | 9 | `mac:ComputationalMethod` | `10.1093/bioinformatics/btac149` | `bio2byte.be/b2btools/` | Type 6 |
| Bloom Lab DMS | 10 | `mac:ExperimentalMethod` | `10.1016/j.cell.2020.08.012` | `github.com/jbloomlab/SARS-CoV-2-RBD_DMS` | Type 7 |
| GISAID | 11 | `mac:ObservationalMethod` | `10.2807/1560-7917.ES.2017.22.13.30494`, `10.46234/ccdcw2021.255` | `gisaid.org` | Type 2 |

**Method instance structure** (worked AlphaFold 2 example, assertion graph):

```turtle
sub:assertion {
  sub:AlphaFold2-Method a <https://w3id.org/fdof/ontology#FAIRDigitalObject> ;
      a mac:ComputationalMethod ;
      <https://w3id.org/fdof/ontology#hasMetadata> nt:NANOPUB ;

      rdfs:label   "AlphaFold 2 — DeepMind structure predictor" ;
      rdfs:comment "AlphaFold 2 (DeepMind) protein structure prediction system." ;

      dct:creator orcid:0000-0001-8888-635X ;
      <https://www.w3.org/ns/dcat#contactPoint> "e.a.schultes@lacdr.leidenuniv.nl" ;
      dct:publisher <https://ror.org/027bh9e22> ;

      dct:isPartOf <https://w3id.org/np/RAFPOe4OIl_urs-U_7-FostjzcUo8ra6LasfSvGplOvto/StayAhead-Project> ;

      <http://purl.org/spar/cito/citesAsAuthority> <https://doi.org/10.1038/s41586-021-03819-2> ;
      <https://schema.org/url> <https://github.com/google-deepmind/alphafold> .

  # Self-materialization block — four direct triples, identical to Type 1.
  nt:NANOPUB <https://w3id.org/fdof/ontology#materializes> sub:AlphaFold2-Method .
  nt:NANOPUB <https://w3id.org/fdof/ontology#hasEncodingFormat>
             <https://www.iana.org/assignments/media-types/application/trig> .
  nt:NANOPUB dct:license <https://creativecommons.org/licenses/by/4.0/> .
  nt:NANOPUB <https://www.w3.org/ns/dcat#accessURL> nt:NANOPUB .
}
```

Notable contrasts with Type 1:
- **No `mac:isObservationOf`** — method FDOs do not observe anything; they enable observations.
- **No `dct:source`, no `dct:references`** — methods are not derived from datasets.
- **No FAIR² block** — methods reference their own published authorities via `cito:citesAsAuthority`, not the FAIR² Data Package.
- **`cito:citesAsAuthority` is mandatory** — every method declares at least one published authority (GISAID declares two).

**Published Trusty URIs (method instances):**

| Method | Trusty URI | Referent URI |
|---|---|---|
| ESM2 | `https://w3id.org/np/RADJxd-U-p7VpA01uXlsp3nkUo3oXFMSOam04-fcF0ZyM` | `<Trusty>/ESM2-Method` |
| AlphaFold 2 | `https://w3id.org/np/RA3zXmeaYZxYSPXzH7CK8-m5T31NWr9nvUCeyKz2mbvNI` | `<Trusty>/AlphaFold2-Method` |
| AgMata | `https://w3id.org/np/RA3JGJN1R1uTyj1puobq1cEwHT52LNmM_67dzb0oRAz2U` | `<Trusty>/AgMata-Method` |
| Bloom DMS | `https://w3id.org/np/RA0Bz7doV8fCSO9lEmpbtNTOnMu5lB3jVudjo-tD0T_Q0` | `<Trusty>/BloomLab-DMS-Method` |
| GISAID | `https://w3id.org/np/RA7XLn4SiwTU4L_5YFYW8KBefgKeYXRu5DSFvYtlZE-o4` | `<Trusty>/GISAID-Method` |

The five referent URIs are the values that Type 2–8 observation instances will use for `mac:has{Prediction,Experimental,Surveillance}Method`.

#### 4.4.3 CSV-driven computational predictions (Types 3–5, 18 instances)

Eighteen instances: 3 variants × 2 prediction methods (ESM2, AlphaFold 2) × 3 metrics (RMSD, SASA, pLDDT). This is the batch where the CSV-driven approach pays off: instead of 18 hand-written configs (one per row), the driver reads `FDT4Claude_small_v1_2.csv` and emits 18 TriG files from 6 CSV rows.

**CSV structure** (relevant columns):

```
variant,method,RMSD,SASA,pLDDT,...
Alpha,ESM2,13.378861773140596,16494.878394358453,23.673561732385306,...
Alpha,AlphaFold2,2.277628683231952,10141.236988525969,93.74392833444035,...
Epsilon,ESM2,12.801648143493145,17620.862527029858,23.73609314359643,...
Epsilon,AlphaFold2,2.975776098053212,10181.968717666516,94.19297808764844,...
Eta,ESM2,2.476768477258109,18026.596842240684,23.15035644847704,...
Eta,AlphaFold2,2.7195180252543003,10226.641288430395,94.05421698739244,...
```

**Driver:** `generator/generate_predictions_from_csv.py`. For each (variant, method) row, the driver emits three instances — one per metric — calling `generate_instance.generate({...})` with a freshly constructed config dict per metric.

**Per-instance config** (constructed by the driver, AlphaFold-method-row example):

```python
{
    "kind":                "prediction",
    "instance_id":         "Alpha-RMSD-AlphaFold2",   # {Variant}-{Metric}-{Method}
    "instance_label":      "Alpha RMSD = 2.277628683231952 Å — AlphaFold 2",
    "instance_description": "RMSD = 2.277628683231952 Å, AlphaFold 2 …",
    "metric_class_curie":  "mac:ComputationalPredictionRMSD",
    "metric_predicate":    "mac:hasRMSD",
    "metric_value":        "2.277628683231952",       # verbatim from CSV
    "template_uri":        "https://w3id.org/np/RALJKysR8vqqqZYXPGHcsI_J0BvPFUmzwOnV9WCGvUjcY",
    "variant_referent":    "https://w3id.org/np/RA4BHII2Bz7HfpUkaSJqNmhjF8F7hyWpCJnvXYkA4EP_M/Alpha-RBD-Variant",
    "method_referent":     "https://w3id.org/np/RA3zXmeaYZxYSPXzH7CK8-m5T31NWr9nvUCeyKz2mbvNI/AlphaFold2-Method",
    "sources":             [
        "https://w3id.org/np/RAv6JJe-lvoadhNwml8pzSLs5aOtbU1xbHT5qgFtgwQ-s",  # AF dataset FDO
        "https://doi.org/10.71728/hw56-vj34",                                  # FAIR² Package
        "https://sen.science/doi/10.71728/hw56-vj34/resources/af_wuhan_1step_v1",
    ],
    "creator_orcid":       "https://orcid.org/0000-0001-8888-635X",
    "contact_email":       "e.a.schultes@lacdr.leidenuniv.nl",
    "publisher_ror":       "https://ror.org/027bh9e22",
}
```

**Method-to-URI mapping** is explicit in the driver — CSV method label "ESM2" → ESM2 method referent; "AlphaFold2" → AlphaFold2 method referent. Each method also selects a different `sources` triple (ESM-method instances use the ESM Dataset FDO + ESM resource URL; AlphaFold-method instances use the AlphaFold Dataset FDO + AlphaFold resource URL). Unrecognised method labels fail loudly.

**Metric value handling**: emit verbatim from the CSV (do not round). The values are stored as bare decimal literals (no `xsd:double` type tag) because the Type 3-5 templates' `sub:value` placeholder is `nt:LiteralPlaceholder` with no constrained range; the literals match this open policy.

**Published Trusty URIs** (excerpt — 6 of 18, full list in §6):

| instance_id | Trusty URI |
|---|---|
| `Alpha-RMSD-AlphaFold2` | `https://w3id.org/np/RAjn5zJQoLUFSMpDLEEG6Pc_oONJNDlMnPi4grKHOsxOE` |
| `Alpha-RMSD-ESM2` | `https://w3id.org/np/RASyg7i8HV4TxiN_-b2KKY6lAuFUkU4_T9pBrtAPA0Uac` |
| `Alpha-SASA-AlphaFold2` | `https://w3id.org/np/RAXXa3_lWNc_NYn9Hd8uaA_bHZVeUhiRJDf8Ugkfu6vLM` |
| `Alpha-SASA-ESM2` | `https://w3id.org/np/RAxIOCQ4MnuGhYt3jLW9QMoWLdRtYThQVVo2kGPL7Rluc` |
| `Alpha-pLDDT-AlphaFold2` | `https://w3id.org/np/RAd9HOScIMpFwHd5U14cg8ez6mSKV2w7y9ow433mL9quA` |
| `Alpha-pLDDT-ESM2` | `https://w3id.org/np/RA3i18Z4N8YQgl-BfudZ42DI7Bbg53MotI6RaNs9fqUz0` |

**This is the code path Tranche 2 reuses.** Scaling from 18 to 22,230 (3705 mutations × 2 methods × 3 metrics) requires no new generator work — only a larger CSV.

#### 4.4.4 CSV-driven AgMata + DMS observations (Types 6 + 7, 6 instances)

**Type 6 (AgMata):** 3 instances, one per variant. Method-fixed (AgMata only); no method placeholder needed. Each carries `mac:hasAgMataScore <value>`. Values from the CSV's `AgMata` column (ESM row per variant): Alpha `0.7004717948717948`, Epsilon `0.7194974358974362`, Eta `0.680579487179487`.

**Type 7 (DMS):** 3 instances, one per variant. Each carries six metric statements (`mac:hasBind`, `mac:hasDeltaBind`, `mac:hasExpr`, `mac:hasDeltaExpr`, `mac:hasConfidenceBind`, `mac:hasConfidenceExpr`). Values from the CSV's six DMS columns. `dct:source` is omitted on the demonstration instances (per the deferred-attribution posture from §3.4.7); the Bloom GitHub URL lives on the Bloom-Method FDO via `schema:url`, so the dataset linkage is reachable via the two-hop method path.

**Driver:** `generator/generate_type6_7_from_csv.py`. Same CSV, different columns, different output shapes (one Type-6 instance + one Type-7 instance per variant row).

**Published Trusty URIs:**

| instance_id | Type | Trusty URI |
|---|---|---|
| `type6_alpha` (Alpha AgMata) | 6 | `https://w3id.org/np/RArJqTu2lE7v02BrY-UmChPKJEwR004azwXfZhZ3d5ZjQ` |
| `type6_epsilon` | 6 | `https://w3id.org/np/RAmPs3MytCSM__DOeyHDJQP9mwYJU6UXKKU8WGhrw5_KY` |
| `type6_eta` | 6 | `https://w3id.org/np/RAcm_5ysAXUPBHcvhNVo_Xnu6OGO0SBEGvzqb4wGfVm-g` |
| `type7_alpha` (Alpha DMS) | 7 | `https://w3id.org/np/RARb0NfCsCVn6tTY3m1sXor6mEbZzIZ6WzBSEjtmftLgs` |
| `type7_epsilon` | 7 | `https://w3id.org/np/RAfI_EQBRQvVh3LRb0WLQFvXra2gINrvxaOZQprZ0KngE` |
| `type7_eta` | 7 | `https://w3id.org/np/RAmrs8u-EM7ejf5shyxo9OVXf2fgAcmB_HB4F-smPQJL0` |

#### 4.4.5 Type 2 real-world occurrences (3 instances, hand-written configs)

Three instances — these data points are not in the metric CSV (occurrence metadata is qualitatively distinct from per-row metric values). Configs in `instance_configs/type2_{alpha,epsilon,eta}.py`.

**Per-variant data:**

| Field | Alpha | Epsilon | Eta |
|---|---|---|---|
| `occurrence_date` | "late 2020–2021" | "2021-01-13" | "2020-12-15" |
| `location` (GeoNames URI) | `https://sws.geonames.org/6269131/` (England) | `https://sws.geonames.org/6252001/` (United States) | `https://sws.geonames.org/2328926/` (Nigeria) |
| `gisaid_accession` | "EPI_ISL_601443" | "EPI_ISL_2295356" | "EPI_ISL_941290" |

All three carry `mac:hasSurveillanceMethod` → GISAID method referent (`<RA7XLn4S…>/GISAID-Method`).

**Published Trusty URIs:**

| instance_id | Trusty URI |
|---|---|
| `type2_alpha` | `https://w3id.org/np/RAyjkMnXEnRF09TI4R531mYM4LKEm3HL5seHnVgQcqHN0` |
| `type2_epsilon` | `https://w3id.org/np/RATGfqd-Sy27F_M9NXKkbL-GzIO9IYXJguGTXBb2VEyQA` |
| `type2_eta` | `https://w3id.org/np/RAnwHIpm48gC4xB4d6ZxG1cDonBDEWGM-RyMf56_a5bk0` |

#### 4.4.6 Type 8 WHO classifications (3 instances, hand-written configs)

Three instances. Configs in `instance_configs/type8_{alpha,epsilon,eta}.py`.

**Per-variant data:**

| Field | Alpha | Epsilon | Eta |
|---|---|---|---|
| `classification` (controlled value) | `mac:VOC` | `mac:VOI` | `mac:VOI` |
| `classification_date` | "2020-12-18" | "2021-03-05" | "2021-03-05" |

**On the classification object form.** The instance writes `mac:hasWHOClassification mac:VOC` (curie form). The `mac:` prefix expands to `https://w3id.org/spaces/mac/r/ontology/`, so the actual object URI is `https://w3id.org/spaces/mac/r/ontology/VOC` — the class URI itself, defined in Stage 1. This is the correct form. **Do not** point at the Trusty URI of the Stage 1 introducing nanopub (e.g., `RAYOlJ43…`); the introducing nanopub is *where* the class is defined, not the class itself. The Type 8 template's `nt:possibleValue` declaration uses the curie form, and instances match.

**No method link, no `dct:source`** — WHO classifications are designations, not observation-by-method outputs.

**Published Trusty URIs:**

| instance_id | Trusty URI |
|---|---|
| `type8_alpha` | `https://w3id.org/np/RApoAkERvI9mPGcz-ExkSSDvXbNAYZygNFW2IAZpaRsGk` |
| `type8_epsilon` | `https://w3id.org/np/RAn5yBad0gMJPsVE5rIiJvWP1GemI-2Wmi91KcCOSFQSg` |
| `type8_eta` | `https://w3id.org/np/RAJRZGtEnHkqBERKZg34r8iX7sbEemtqOURYyRgB0MSa4` |

### 4.5 Publication order

Cross-references must resolve at publish time, so dependency order matters. The procedure used in the demonstration build:

1. **Type 1 anchors first (3 instances).** No cross-references; nothing depends on a prior publication.
2. **Methods second (5 instances).** Methods are referenced by observations via `mac:has{Prediction,Experimental,Surveillance}Method`; they must exist before observations are published.
3. **Observations third (30 instances).** Each observation references a Type 1 anchor (`mac:isObservationOf`) and, for most types, a method.

Within each group, order is free. The demonstration build batched anchors first, then methods, then computational predictions (18), then AgMata + DMS (6), then occurrences + WHO (6).

Per instance, the sign/publish/record loop:

```
nanopub sign drafts/instance_<descriptor>_v1.trig
mv drafts/signed.instance_<descriptor>_v1.trig signed/
nanopub check signed/instance_<descriptor>_v1.trig   # 1 trusty + signature
nanopub publish signed/instance_<descriptor>_v1.trig # publish to live NSN
```

Record the Trusty URI plus publish timestamp in the relevant `PUBLISHED_*.md` file as each batch completes.

### 4.6 Cross-reference resolution

The single most consequential rule for instance correctness: **observations and views reference FDOs by their referent URIs, not by the bare Trusty URIs of their introducing nanopubs.**

A referent URI has the form `<Trusty URI>/<instance_id>`. Examples for the demonstration catalogue:

| FDO | Trusty URI (the introducing nanopub) | Referent URI (the FDO itself) |
|---|---|---|
| Alpha variant | `…/RA4BHII2Bz7HfpUkaSJqNmhjF8F7hyWpCJnvXYkA4EP_M` | `…/RA4BHII2Bz7H…/Alpha-RBD-Variant` |
| ESM2 method | `…/RADJxd-U-p7VpA01uXlsp3nkUo3oXFMSOam04-fcF0ZyM` | `…/RADJxd-U-p7Vp…/ESM2-Method` |
| StayAhead Project | `…/RAFPOe4OIl_urs-U_7-FostjzcUo8ra6LasfSvGplOvto` | `…/RAFPOe4OIl_…/StayAhead-Project` |

**Where this rule applies:**

- `mac:isObservationOf` → variant **referent** URI (not the variant nanopub's Trusty URI).
- `mac:has{Prediction,Experimental,Surveillance}Method` → method **referent** URI.
- `dct:isPartOf` → Project **referent** URI.
- `gen:isDisplayOfView` (Stage 4) → view-wrapper **referent** URI.

**Common error mode:** linking to the bare Trusty URI. The link "resolves" (returns the introducing nanopub) but does not satisfy SPARQL queries that traverse the FDO graph by referent — observations linked by Trusty URI will not appear in knowlet queries.

The generator constructs referent URIs by concatenating `<template_uri's namespace>/<instance_id>` for hand-written configs, and by carrying explicit `variant_referent` / `method_referent` fields for CSV-driven configs (avoiding string concatenation in performance-critical loops).

### 4.7 Validation

After all 38 instances are published, run the following checks:

**(a) HTTP resolution:**

```bash
for trusty in $(cut -d, -f3 PUBLISHED_*.md_combined.csv); do
  curl -s -o /dev/null -w "%{http_code} $trusty\n" -L "https://w3id.org/np/$trusty"
done
```

Expect 38 occurrences of `200`.

**(b) Total FDO count via SPARQL:**

```sparql
PREFIX fdof: <https://w3id.org/fdof/ontology#>
PREFIX mac:  <https://w3id.org/spaces/mac/r/ontology/>
PREFIX dct:  <http://purl.org/dc/terms/>
PREFIX np:   <http://www.nanopub.org/nschema#>
PREFIX npa:  <http://purl.org/nanopub/admin/>
PREFIX npx:  <http://purl.org/nanopub/x/>

SELECT (COUNT(DISTINCT ?fdo) AS ?count) WHERE {
  GRAPH npa:graph {
    ?n1 npa:hasValidSignatureForPublicKey ?pubkey .
    FILTER NOT EXISTS { ?np2 npx:invalidates ?n1 ;
                              npa:hasValidSignatureForPublicKey ?pubkey . }
    ?n1 np:hasAssertion ?a .
  }
  GRAPH ?a {
    ?fdo a fdof:FAIRDigitalObject .
    ?fdo dct:isPartOf
      <https://w3id.org/np/RAFPOe4OIl_urs-U_7-FostjzcUo8ra6LasfSvGplOvto/StayAhead-Project> .
  }
}
```

Endpoint: `https://w3id.org/np/l/nanopub-query-1.1/repo/full`. Expect `count = 38`.

**(c) Per-twin observation count (the knowlet check):**

```sparql
SELECT (COUNT(?obs) AS ?count) WHERE {
  GRAPH npa:graph {
    ?n1 npa:hasValidSignatureForPublicKey ?pubkey .
    FILTER NOT EXISTS { ?np2 npx:invalidates ?n1 ;
                              npa:hasValidSignatureForPublicKey ?pubkey . }
    ?n1 np:hasAssertion ?a .
  }
  GRAPH ?a {
    ?obs mac:isObservationOf
      <https://w3id.org/np/RA4BHII2Bz7HfpUkaSJqNmhjF8F7hyWpCJnvXYkA4EP_M/Alpha-RBD-Variant> .
  }
}
```

Expect 10 (Alpha's 10 observations: 1 occurrence + 6 predictions + 1 AgMata + 1 DMS + 1 WHO). Repeat for Epsilon and Eta referents — both should also return 10.

**(d) Catalogue-summary breakdown by type:**

```sparql
SELECT ?type (COUNT(?fdo) AS ?count) WHERE {
  GRAPH npa:graph { ?n1 npa:hasValidSignatureForPublicKey ?pk .
                    ?n1 np:hasAssertion ?a . }
  GRAPH ?a {
    ?fdo a fdof:FAIRDigitalObject ; a ?type .
    FILTER(?type != fdof:FAIRDigitalObject)
    FILTER(STRSTARTS(STR(?type), "https://w3id.org/spaces/mac/r/ontology/"))
  }
} GROUP BY ?type ORDER BY DESC(?count)
```

Expect 11 rows (one per instantiated MAC class) summing to 38. The breakdown that matches the demonstration catalogue: ComputationalPredictionRMSD/SASA/PLDDT 6 each, ComputationalMethod 3, ComputationalPredictionAgMata 3, ExperimentalDMSObservation 3, RealWorldOccurrence 3, SpikeRBDVariant 3, WHOVariantClassification 3, ExperimentalMethod 1, ObservationalMethod 1 — total 6+6+6+3+3+3+3+3+3+1+1 = 38.

**(e) NanoDash render spot-check:**

Open the Trusty URI of any instance in a browser (e.g., `https://nanodash.knowledgepixels.com/explore?id=https://w3id.org/np/RA4BHII2Bz7HfpUkaSJqNmhjF8F7hyWpCJnvXYkA4EP_M`). The assertion graph should render with the FDO label as the page title and the type-specific statements visible.

**Stage 3 closes when:** all 38 instances are published live (validation (a) and (b) pass), per-twin knowlet counts are correct (validation (c)), and the catalogue summary breakdown is exact (validation (d)). The catalogue can now be queried as the FAIR Digital Twin catalogue it was designed to be — Stage 4 builds the standing queries that expose it.

---

## §5 — Stage 4: Standing views

### 5.1 What Stage 4 produces

Four standing SPARQL views over the Stage 3 catalogue, exposed on the working Space (`https://w3id.org/spaces/knowledgepixels/incubator/project4` for this catalogue) through two distinct NanoDash visibility mechanisms — *sidebar pinning* (left-rail links the user clicks to open results) and *embedded panels* (boxes on the Space's main page that render results inline). Both mechanisms operate over the same four underlying grlc-query nanopubs.

For each of the four views, Stage 4 produces three artifacts (the underlying query, plus one nanopub per visibility layer):

| View | grlc-query nanopub | Sidebar pin-action | Wrapper + ViewDisplay |
|---|---|---|---|
| Catalogue summary by type | 1 | 1 | 1 + 1 |
| Variants by WHO classification | 1 | 1 | 1 + 1 |
| Observations per method | 1 | 1 | 1 + 1 |
| Alpha digital-twin knowlet | 1 | 1 | 1 + 1 |
| **Total nanopubs** | **4** | **4** | **8** |

Sixteen Stage 4 nanopubs in total: 4 queries, 4 sidebar pin-actions, 4 View wrappers, 4 ViewDisplays.

Stage 4 deliverables, by filesystem location:

- `minting/stage4-views/drafts/{query,pin,wrapper,display}/` — unsigned TriG files, grouped by artifact kind.
- `minting/stage4-views/signed/` — parallel layout, signed.
- `minting/stage4-views/PUBLISHED_views.md` — publication record listing all 16 live Trusty URIs.

### 5.2 The two visibility layers

Stage 4 deliberately produces *both* layers because they serve different user paths and the cost of adding the second once the first is built is small. The procedure is to author the query nanopubs once and then attach them to the Space twice — once through the sidebar-pin mechanism, once through the View/ViewDisplay mechanism. The four query nanopubs are shared between layers.

**Sidebar pinning.** The Space's left-rail "Queries" panel lists pinned queries by label. The user clicks a name; NanoDash opens a results page that runs the query against the configured endpoint and displays the rows. Mechanism: a *pin-action* nanopub asserts `<space> gen:hasPinnedQuery <query-Trusty-URI>` with an optional `gen:hasPinGroupTag` for visual grouping. The object of `gen:hasPinnedQuery` is the **bare query Trusty URI**.

**Embedded panels.** Each panel renders on the Space's main page as a box showing the query's results (or a header + "run" affordance, depending on the view kind). Mechanism: two nanopubs — a `gen:View` *wrapper* that carries display metadata and points at the query via `gen:hasViewQuery`; a `gen:ViewDisplay` that asserts `<space> gen:isDisplayOfView <wrapper-referent-URI>`. The wrapper layer sits between the query and the display because NanoDash's renderer expects display metadata (view kind, structural position, page size, applies-to scope) separately from the query itself.

A cautionary note for future builds: the object of `gen:isDisplayOfView` must be the **wrapper's referent URI** (`<Trusty URI>/<view-local-name>`), never the bare grlc-query Trusty URI. The error mode (pointing the ViewDisplay directly at the query) produces nanopubs that publish cleanly but render no panel. The earlier MAC FDT build encountered this confusion and the fix required publishing four `npx:retracts` nanopubs; the procedure below avoids it by going through the wrapper layer from the start.

Side-by-side comparison of the two layers:

| Aspect | Sidebar pinning | Embedded panels |
|---|---|---|
| Discovery surface | Left-rail link list | Inline boxes on main page |
| Click required to see data? | Yes | No (renders on page load) |
| Predicate | `gen:hasPinnedQuery` | `gen:isDisplayOfView` |
| Nanopubs per view | 1 (pin-action) | 2 (wrapper + ViewDisplay) |
| Object of the linking predicate | Bare query Trusty URI | Wrapper *referent* URI |
| Authoring template | `RAuLESdeRUlk1…` (pin-query) | `RARLsTlqbTesu1b0WJZ…` (resource view) + `RAsc8FMsGih955…` (ViewDisplay) |
| Supersession of Space definition? | No (federated additive) | No (federated additive) |
| Required signer privilege | `gen:hasAdmin` on Space | `gen:hasAdmin` on Space |

### 5.3 Authoring grlc-query nanopubs

Four query nanopubs are minted first; both visibility-layer artifacts reference them.

**Template:** `https://w3id.org/np/RAEFAt-QcFK0ZhqfvlsmS10BnzGJA0xwOICZXkO-ai87k` ("Defining a grlc query"). Tag: `Queries`.

**Mandatory statements** the template requires the instance to declare:

| Predicate | Object | Notes |
|---|---|---|
| `rdf:type` | `<https://w3id.org/kpxl/grlc/grlc-query>` | The grlc-query type |
| `rdfs:label` | literal | Display label (the sidebar text) |
| `dct:description` | literal | Long-form description |
| `dct:license` | URI | `<https://www.apache.org/licenses/LICENSE-2.0>` matches the MAC-FDO exemplar |
| `<https://w3id.org/kpxl/grlc/endpoint>` | URI | The SPARQL endpoint to run against |
| `<https://w3id.org/kpxl/grlc/sparql>` | literal | The verbatim SPARQL text |

**Endpoint for all four MAC FDT views:**

```
https://w3id.org/np/l/nanopub-query-1.1/repo/full
```

This is the signature-validated nanopub-query repository (validates signatures, filters retracted/invalidated nanopubs). Alternative repositories exist (e.g., `/repo/text` for Lucene full-text); pinned-query nanopubs explicitly choose which.

**Assertion-graph skeleton** (uniform across all four MAC FDT queries):

```turtle
sub:assertion {
  sub:query a <https://w3id.org/kpxl/grlc/grlc-query> ;
      rdfs:label   "<view label>" ;
      dct:description "<view description>" ;
      dct:license  <https://www.apache.org/licenses/LICENSE-2.0> ;
      <https://w3id.org/kpxl/grlc/endpoint>
                   <https://w3id.org/np/l/nanopub-query-1.1/repo/full> ;
      <https://w3id.org/kpxl/grlc/sparql>
                   "<verbatim SPARQL text>" .
}
```

The shared **signature-validation block** that every MAC FDT query uses inside its `WHERE` clause (drops retracted/invalidated nanopubs from results):

```sparql
GRAPH npa:graph {
  ?n1 npa:hasValidSignatureForPublicKey ?pubkey .
  filter not exists {
    ?np2 npx:invalidates ?n1 ;
         npa:hasValidSignatureForPublicKey ?pubkey .
  }
  ?n1 np:hasAssertion ?a .
}
```

This block uses `npx:invalidates` (the internal generalisation used inside the nanopub-query repos). When a publisher retracts a nanopub via `npx:retracts`, the repo derives an `npx:invalidates` triple in the admin graph automatically — so this filter catches both retractions and the repo's other invalidation cases. Do not write `npx:retracts` in the query's filter; the admin-graph form is `npx:invalidates`.

Shared prefixes prepended to every query:

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX np:   <http://www.nanopub.org/nschema#>
PREFIX npa:  <http://purl.org/nanopub/admin/>
PREFIX npx:  <http://purl.org/nanopub/x/>
PREFIX dct:  <http://purl.org/dc/terms/>
PREFIX fdof: <https://w3id.org/fdof/ontology#>
PREFIX mac:  <https://w3id.org/spaces/mac/r/ontology/>
```

### 5.4 The four query texts

Reproduced verbatim. These are the live SPARQL strings stored inside the four published query nanopubs.

**Query 1 — MAC FDT — catalogue summary by type.** Returns one row per instantiated MAC class with the count of FDOs of that type. Bounded by the number of MAC classes (≤ 19 in this vocabulary, 11 actually instantiated in the demonstration catalogue).

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX np:   <http://www.nanopub.org/nschema#>
PREFIX npa:  <http://purl.org/nanopub/admin/>
PREFIX npx:  <http://purl.org/nanopub/x/>
PREFIX dct:  <http://purl.org/dc/terms/>
PREFIX fdof: <https://w3id.org/fdof/ontology#>
PREFIX mac:  <https://w3id.org/spaces/mac/r/ontology/>

SELECT ?type (COUNT(?thing) AS ?count) WHERE {
  GRAPH npa:graph {
    ?n1 npa:hasValidSignatureForPublicKey ?pubkey .
    filter not exists {
      ?np2 npx:invalidates ?n1 ;
           npa:hasValidSignatureForPublicKey ?pubkey .
    }
    ?n1 np:hasAssertion ?a .
  }
  graph ?a {
    ?thing a fdof:FAIRDigitalObject .
    ?thing a ?type .
    FILTER(?type != fdof:FAIRDigitalObject)
    FILTER(STRSTARTS(STR(?type), "https://w3id.org/spaces/mac/r/ontology/"))
  }
} GROUP BY ?type ORDER BY DESC(?count)
```

Expected on the demonstration catalogue: 11 rows summing to 38.

**Query 2 — MAC FDT — variants by WHO classification.** Returns one row per WHO class with the count of variants assigned to it. Bounded by the number of WHO classes (3: `mac:VOC`, `mac:VOI`, `mac:VUM`).

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX np:   <http://www.nanopub.org/nschema#>
PREFIX npa:  <http://purl.org/nanopub/admin/>
PREFIX npx:  <http://purl.org/nanopub/x/>
PREFIX mac:  <https://w3id.org/spaces/mac/r/ontology/>

SELECT ?whoClass (COUNT(?variant) AS ?count) WHERE {
  GRAPH npa:graph {
    ?n1 npa:hasValidSignatureForPublicKey ?pubkey .
    filter not exists {
      ?np2 npx:invalidates ?n1 ;
           npa:hasValidSignatureForPublicKey ?pubkey .
    }
    ?n1 np:hasAssertion ?a .
  }
  graph ?a {
    ?obs a mac:WHOVariantClassification .
    ?obs mac:hasWHOClassification ?whoClass .
    ?obs mac:isObservationOf ?variant .
  }
} GROUP BY ?whoClass ORDER BY DESC(?count)
```

Expected: VOC 1, VOI 2 (demonstration catalogue).

**Query 3 — MAC FDT — observations per method.** Returns one row per method FDO with the count of observations that reference it. Bounded by the number of method FDOs in the catalogue (5 in the demonstration; the bound grows as new methods are added but stays in the single digits or low tens for any plausible catalogue).

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX np:   <http://www.nanopub.org/nschema#>
PREFIX npa:  <http://purl.org/nanopub/admin/>
PREFIX npx:  <http://purl.org/nanopub/x/>
PREFIX mac:  <https://w3id.org/spaces/mac/r/ontology/>

SELECT ?method (COUNT(?obs) AS ?count) WHERE {
  GRAPH npa:graph {
    ?n1 npa:hasValidSignatureForPublicKey ?pubkey .
    filter not exists {
      ?np2 npx:invalidates ?n1 ;
           npa:hasValidSignatureForPublicKey ?pubkey .
    }
    ?n1 np:hasAssertion ?a .
  }
  graph ?a {
    ?obs ?methodPred ?method .
    VALUES ?methodPred {
      mac:hasPredictionMethod
      mac:hasExperimentalMethod
      mac:hasSurveillanceMethod
    }
  }
} GROUP BY ?method ORDER BY DESC(?count)
```

Expected: ESM2 9, AlphaFold 2 9, AgMata 3, Bloom DMS 3, GISAID 3.

**Query 4 — MAC FDT — Alpha variant digital twin (knowlet).** Returns the bounded set of observation FDOs whose `mac:isObservationOf` points at Alpha. The query is fixed-referent (the Alpha referent URI is hardcoded); other variants would require parallel query nanopubs with the appropriate referent.

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX np:   <http://www.nanopub.org/nschema#>
PREFIX npa:  <http://purl.org/nanopub/admin/>
PREFIX npx:  <http://purl.org/nanopub/x/>
PREFIX fdof: <https://w3id.org/fdof/ontology#>
PREFIX mac:  <https://w3id.org/spaces/mac/r/ontology/>

SELECT ?obs ?type ?label WHERE {
  GRAPH npa:graph {
    ?n1 npa:hasValidSignatureForPublicKey ?pubkey .
    filter not exists {
      ?np2 npx:invalidates ?n1 ;
           npa:hasValidSignatureForPublicKey ?pubkey .
    }
    ?n1 np:hasAssertion ?a .
  }
  graph ?a {
    ?obs mac:isObservationOf
      <https://w3id.org/np/RA4BHII2Bz7HfpUkaSJqNmhjF8F7hyWpCJnvXYkA4EP_M/Alpha-RBD-Variant> .
    ?obs a ?type .
    FILTER(?type != fdof:FAIRDigitalObject)
    OPTIONAL { ?obs rdfs:label ?label . }
  }
} ORDER BY ?type
```

Expected: 10 rows (Alpha's full observation cluster — the digital twin made visible).

### 5.5 Scale-correctness

Each of the four queries returns a bounded result set whose size does not grow with the catalogue:

| Query | Bound | At 38 instances | At Tranche-2 scale (~22,000 instances) |
|---|---|---|---|
| Catalogue summary | ≤ number of MAC classes | 11 rows | 11 rows (unchanged) |
| Variants by WHO class | ≤ number of WHO classes | 2 rows | 3 rows (max) |
| Observations per method | ≤ number of method FDOs | 5 rows | 5–20 rows (small) |
| Alpha knowlet | observations per variant | 10 rows | 10–12 rows (per variant) |

This is deliberate. A flat catalogue listing ("`SELECT ?fdo WHERE { ?fdo a mac:SpikeRBDVariant }`") would read sensibly at 38 instances and degrade to 3705 unreadable rows at Tranche-2 scale. The chosen forms (`GROUP BY` aggregates, plus one fixed-referent twin view) stay bounded at any catalogue size.

At Tranche-2 scale, *browsing to an arbitrary variant's twin* — picking which referent the knowlet query targets — becomes a NanoDash search operation (the user enters a variant name in NanoDash's search box, NanoDash returns the matching variant FDO's page, the page shows the variant's incoming observations). The fixed-referent Alpha knowlet view remains a worked example, not a per-variant entry point. Per-variant browsability at scale is a separate concern requiring NanoDash search, not a different SPARQL form.

The four query nanopubs themselves do not need to change between the 38-instance demonstration and the Tranche-2 scale-up.

### 5.6 Sidebar pinning

After the four query nanopubs are signed and published, mint four sidebar pin-action nanopubs (one per query) to populate the Space's "Queries" sidebar.

**Template:** `https://w3id.org/np/RAuLESdeRUlk1GcTwvzVXShiBMI0ntJs2DL2Bm5DzW_ZQ` ("Declare a pinned query for a Space"). Tag: `Spaces`.

**Assertion-graph form** (two statements per pin-action):

```turtle
sub:assertion {
  <https://w3id.org/spaces/knowledgepixels/incubator/project4>
      gen:hasPinnedQuery <https://w3id.org/np/<query-Trusty-URI>> .

  <https://w3id.org/np/<query-Trusty-URI>>
      gen:hasPinGroupTag "<group label>" .
}
```

Where `<query-Trusty-URI>` is the bare Trusty URI of the published grlc-query nanopub. The pin-action carries `npx:hasNanopubType <gen:hasPinnedQuery>` in pubinfo (set by the pin-query authoring flow).

**Group tags used in the demonstration build:**

| Query | Group tag |
|---|---|
| Catalogue summary | "Catalogue overview" |
| Variants by WHO class | "Situational dashboards" |
| Observations per method | "Situational dashboards" |
| Alpha knowlet | "Digital twin (worked example)" |

NanoDash groups sidebar pins by tag visually; tags need not be unique.

**Authorisation:** the signer must hold `gen:hasAdmin` on the Space (declared in the Space-definition nanopub). For the demonstration catalogue, Erik holds `gen:hasAdmin` on project4 (Tobias Kuhn also holds it).

**Published Trusty URIs (sidebar pin-actions):**

| View | Pin-action Trusty URI |
|---|---|
| Catalogue summary | `https://w3id.org/np/RAr2do6-Zm_F5tv9NP4iziOpRCX-mJUZzCqUfY-brnNRY` |
| Variants by WHO | `https://w3id.org/np/RAkwEb52MHk6Xe4uzOruIAkmGZAq4URDyg5bPqx4SXY1Y` |
| Observations per method | `https://w3id.org/np/RAZge9g-AM2aYodnkKrlt6ag1s1QPYjTYBCJZaPezTZ6M` |
| Alpha knowlet | `https://w3id.org/np/RAzEolNOqr8I1aiZpafpUxJfqBOQRdTapceYWjXCoEYAE` |

### 5.7 Embedded panels — wrappers and ViewDisplays

To produce embedded panels on the Space's main page, two further nanopubs per view are needed: a `gen:View` *wrapper* (carries display metadata and points at the query) and a `gen:ViewDisplay` (binds the wrapper to the Space).

#### 5.7.1 The `gen:View` wrapper

**Template:** `https://w3id.org/np/RARLsTlqbTesu1b0WJZ-zL1z96xumOiqbK3l_vV6iZoww` ("Declaring a resource view"). Tag: `Spaces`.

**Mandatory statements** (8) and selected optional statements:

| Statement | Subject | Predicate | Object | Notes |
|---|---|---|---|---|
| (m) | `sub:view` | `rdf:type` | `gen:ResourceView` | Fixed |
| (m) | `sub:view` | `rdf:type` | (one of) `gen:TabularView`, `gen:ListView`, `gen:ItemListView`, `gen:NanopubSetView`, `gen:PlainParagraphView` | View kind |
| (m) | `sub:view` | `dct:isVersionOf` | `<this:/<local>-view-kind>` | Stable identifier across supersessions |
| (m) | `sub:view` | `rdfs:label` | literal | Internal label |
| (m) | `sub:view` | `dct:title` | literal | Panel title (visible on page) |
| (m) | `sub:view` | `gen:hasViewQuery` | `<grlc-query-Trusty-URI>` | The query the panel runs |
| (m) | `sub:view` | `gen:hasViewQueryTargetField` | literal | URL-parameter binding; `"resource"` for parameterless queries |
| (m) | `sub:view` | `gen:hasStructuralPosition` | literal matching `[1-9]\.[1-9]\..*` | Positional ordering on the Space page |
| (o, rep) | `sub:view` | `gen:appliesToInstancesOf` | URI(s) | Scope of resource-page types the panel renders on; use `gen:Space` to render only on Space pages |
| (o) | `sub:view` | `gen:hasPageSize` | literal | Page-size for tabular results |
| (o) | `sub:view` | `gen:hasDisplayWidth` | `gen:ColumnWidth<N>of12` | Layout column width |

**MAC FDT wrapper values (uniform across all four):**

- `rdf:type` → `gen:ResourceView`, `gen:TabularView`
- `gen:appliesToInstancesOf` → `gen:Space` (panels render on Space pages only)
- `gen:hasViewQueryTargetField` → `"resource"` (parameterless queries; the field doesn't bind to anything; the default is harmless)
- `gen:hasPageSize`, `gen:hasDisplayWidth` → omit (use defaults: full-width single-column layout)

**Per-view values:**

| Field | Catalogue summary | Variants by WHO | Obs per method | Alpha knowlet |
|---|---|---|---|---|
| `dct:title` | "MAC FDT — catalogue summary by type" | "MAC FDT — variants by WHO classification" | "MAC FDT — observations per method" | "MAC FDT — Alpha variant digital twin" |
| `gen:hasViewQuery` | `RAGlsCUDZ…` | `RAlD3u-…` | `RAIKnskD…` | `RAecvUbv…` |
| `gen:hasStructuralPosition` | `"5.1.fdt-catalogue-summary"` | `"5.2.fdt-variants-by-who"` | `"5.3.fdt-observations-per-method"` | `"5.4.fdt-alpha-knowlet"` |
| `dct:isVersionOf` | `<this:/fdt-catalogue-summary-view-kind>` | `<this:/fdt-variants-by-who-view-kind>` | `<this:/fdt-observations-per-method-view-kind>` | `<this:/fdt-alpha-knowlet-view-kind>` |

Section 5 of the Space page is unused by the pre-existing project4 wrappers (which use sections 3 and 6); positions 5.1–5.4 keep the four MAC FDT panels grouped and ordered.

**Worked example — the Alpha-knowlet wrapper's assertion graph:**

```turtle
sub:assertion {
  sub:fdt-alpha-knowlet-view
      a gen:ResourceView, gen:TabularView ;
      dct:isVersionOf            <this:/fdt-alpha-knowlet-view-kind> ;
      rdfs:label                 "MAC FDT Alpha digital-twin view" ;
      dct:title                  "MAC FDT — Alpha variant digital twin" ;
      gen:appliesToInstancesOf   gen:Space ;
      gen:hasStructuralPosition  "5.4.fdt-alpha-knowlet" ;
      gen:hasViewQuery
        <https://w3id.org/np/RAecvUbvUWiIOKP7ZEQk7hnUsb8lWWUr1lRbVN2PsSUSA> ;
      gen:hasViewQueryTargetField "resource" .
}
```

The wrapper's published Trusty URI is then `https://w3id.org/np/RA_zvbVo3VX6Cy3lYOI6LNHJICb1copbCmJHayjpzCeJ0`, and the **referent URI** that the ViewDisplay uses is:

```
https://w3id.org/np/RA_zvbVo3VX6Cy3lYOI6LNHJICb1copbCmJHayjpzCeJ0/fdt-alpha-knowlet-view
```

(the Trusty URI plus the local name of the wrapper's subject resource).

**Published Trusty URIs (wrappers):**

| View | Wrapper Trusty URI | Wrapper referent URI |
|---|---|---|
| Catalogue summary | `RAUQDFIiL73MByusDvrnMLRJaDW32bImYrq4aQN5CJmLM` | `<Trusty>/fdt-catalogue-summary-view` |
| Variants by WHO | `RA2orwJH_zUQQvUvKk0UHvCr5x8iAVhIopqLUFYyuy-Eg` | `<Trusty>/fdt-variants-by-who-view` |
| Obs per method | `RAS-Wm3ewaQtz8rhzKY-EAyrJnYGZMq3MOz2AZ9fXQ5e8` | `<Trusty>/fdt-observations-per-method-view` |
| Alpha knowlet | `RA_zvbVo3VX6Cy3lYOI6LNHJICb1copbCmJHayjpzCeJ0` | `<Trusty>/fdt-alpha-knowlet-view` |

#### 5.7.2 The `gen:ViewDisplay`

**Template:** `https://w3id.org/np/RAsc8FMsGih955oFSFG0YcB9sDKA62VLbp3VIw86IxMvk` ("Displaying a view for a Space"). Tag: `Spaces`.

**Assertion-graph form** (four predicates on a single local resource, uniform across all four):

```turtle
sub:assertion {
  sub:display a gen:ActivatedViewDisplay, gen:ViewDisplay ;
      gen:appliesTo       <space-URI> ;
      gen:isDisplayFor    <space-URI> ;
      gen:isDisplayOfView <wrapper-referent-URI> .
}
```

**Critical: the object of `gen:isDisplayOfView` is the wrapper's referent URI**, not the wrapper nanopub's bare Trusty URI. Pointing at the bare query Trusty URI (skipping the wrapper layer) produces a syntactically valid nanopub that renders no panel; the renderer expects the typed-wrapper layer to find its `gen:hasViewQuery`. This is the single most consequential error mode in Stage 4; the wrapper layer is mandatory.

**Published Trusty URIs (ViewDisplays):**

| View | ViewDisplay Trusty URI |
|---|---|
| Catalogue summary | `RAvARpXohLClZVC3qZdtn1JihyPU12NsmTQAHoziXXRq4` |
| Variants by WHO | `RAywsGEhq4acHjLNY6rALv2vvhjGwqYsFeFayr3hwZ4iM` |
| Obs per method | `RA-XrE3QY1r0Llm5TLurg0VcasOT_hfta-AM_4qp1srZo` |
| Alpha knowlet | `RA-QuZXXV9ni6b2YW0cM4ADyzYi-Uo4FQDR0p2pdR9tUk` |

#### 5.7.3 Publication order

Each view's three artifacts have an internal dependency order:

1. **grlc-query nanopub** (Trusty URI referenced by both layers).
2. **Sidebar pin-action** OR **`gen:View` wrapper** (independent of each other; can be authored in either order or in parallel).
3. **`gen:ViewDisplay`** (references the wrapper's referent URI; the wrapper must exist first).

The demonstration build authored all four query nanopubs first, then all four pin-actions, then all four wrappers, then all four ViewDisplays — 16 publications in 4 batches.

#### 5.7.4 If a published artifact needs to be removed

A published nanopub cannot be edited. Two mechanisms exist for removal:

- **`npx:retracts`** — the publisher-facing retraction. Publish a new nanopub whose assertion is `<this-orcid> npx:retracts <target-Trusty-URI>` plus an `rdfs:comment` explaining the reason. The retraction must be signed by the same key that signed the target.
- **`npx:invalidates`** — internal to the nanopub-query repos. Do **not** use this directly from publisher-side workflows; it is an admin-graph generalisation derived automatically from `npx:retracts` (and from `npx:supersedes`).

The retraction template is `https://w3id.org/np/RAQP3NJvnLA2Z-2DrYAN0nTC-RFp67td1t4-pQqQ_ZKmo`. The nanopub-query `/repo/full` endpoint filters retracted (and otherwise invalidated) nanopubs from SPARQL results via the `npx:invalidates` admin-graph triple that the retraction derives.

### 5.8 Validation

After all 16 Stage 4 nanopubs are published, run the following checks:

**(a) HTTP resolution per artifact:**

```bash
for trusty in $(cut -d, -f3 PUBLISHED_views.md_combined.csv); do
  curl -s -o /dev/null -w "%{http_code} $trusty\n" \
       -L "https://w3id.org/np/$trusty"
done
```

Expect 16 occurrences of `200`.

**(b) Sidebar pinning attached to the Space:**

```sparql
PREFIX gen: <https://w3id.org/kpxl/gen/terms/>
PREFIX np:  <http://www.nanopub.org/nschema#>
PREFIX npa: <http://purl.org/nanopub/admin/>
PREFIX npx: <http://purl.org/nanopub/x/>

SELECT ?query ?tag WHERE {
  GRAPH npa:graph {
    ?n1 npa:hasValidSignatureForPublicKey ?pubkey .
    FILTER NOT EXISTS { ?np2 npx:invalidates ?n1 ;
                              npa:hasValidSignatureForPublicKey ?pubkey . }
    ?n1 np:hasAssertion ?a .
  }
  GRAPH ?a {
    <https://w3id.org/spaces/knowledgepixels/incubator/project4>
        gen:hasPinnedQuery ?query .
    OPTIONAL { ?query gen:hasPinGroupTag ?tag . }
  }
}
```

Endpoint: `https://w3id.org/np/l/nanopub-query-1.1/repo/full`. Expect 4 rows — the four query Trusty URIs with their group tags.

**(c) Embedded ViewDisplays attached to the Space:**

```sparql
PREFIX gen: <https://w3id.org/kpxl/gen/terms/>
PREFIX np:  <http://www.nanopub.org/nschema#>
PREFIX npa: <http://purl.org/nanopub/admin/>
PREFIX npx: <http://purl.org/nanopub/x/>

SELECT ?display ?view WHERE {
  GRAPH npa:graph {
    ?n1 npa:hasValidSignatureForPublicKey ?pubkey .
    FILTER NOT EXISTS { ?np2 npx:invalidates ?n1 ;
                              npa:hasValidSignatureForPublicKey ?pubkey . }
    ?n1 np:hasAssertion ?a .
  }
  GRAPH ?a {
    ?display a gen:ViewDisplay ;
             gen:appliesTo <https://w3id.org/spaces/knowledgepixels/incubator/project4> ;
             gen:isDisplayOfView ?view .
  }
}
```

Expect the four MAC FDT ViewDisplays (their `?view` values pointing at the four wrapper referent URIs `<wrapper-Trusty>/fdt-*-view`), in addition to any pre-existing ViewDisplays on the Space.

**(d) Each query returns the expected row count when executed:**

Open each query nanopub in NanoDash (the `https://w3id.org/np/<query-Trusty-URI>` URL renders a "Run query" affordance) and execute. Expected row counts:

| Query | Expected rows on the demonstration catalogue |
|---|---|
| Catalogue summary | 11 (summing to 38) |
| Variants by WHO | 2 (VOC 1, VOI 2) |
| Observations per method | 5 (ESM 9, AF 9, AgMata 3, Bloom 3, GISAID 3) |
| Alpha knowlet | 10 |

**(e) NanoDash Space-page rendering:**

Open the Space page in a browser. After NanoDash indexing (minutes to hours), three things should now be present:

1. The "Queries" sidebar lists 4 entries grouped by their tags.
2. Section 5 of the main page displays 4 panels (positions 5.1–5.4) with the dct:title of each panel as its header.
3. Each panel renders its query's results inline (tabular layout, full-width).

Indexing lag is normal; if no panels appear after 2 hours, verify validation (b) and (c) return the expected rows. If the SPARQL is correct but the page still does not render the panels, suspect a renderer-side issue and consult the operator.

**Stage 4 closes when:** all 16 Stage 4 nanopubs are published live (validation (a)), both visibility layers are attached to the Space (validations (b) and (c)), all queries return correct row counts (validation (d)), and the Space page renders the panels (validation (e)). The MAC FDT catalogue is now both *published* (Stages 1–3) and *exposed* (Stage 4): the sidebar gives power-user lookup; the panels give dashboard-style discovery; the Alpha knowlet panel is the digital twin made visible — the worked-example deliverable that the entire build was structured to produce.

---

## §6 — Reference appendices

### Appendix A — Full Trusty URI roster

The published demonstration catalogue, by stage and group. Each row gives the local name (or instance_id) and the live Trusty URI under the prefix `https://w3id.org/np/`.

#### A.1 Stage 1 — Vocabulary (45 terms)

Stage 1 published 45 vocabulary nanopubs (26 predicates + 19 classes) under the MAC namespace. The authoritative lookup table is the manifest at:

```
mac-fdt-staging/minting/stage1-vocabulary-drafts/manifest_live_v2.csv
```

Each row maps `term_local_name` → `trusty_uri_v2`. Term URIs (the values used in templates and instances) take the form `https://w3id.org/spaces/mac/r/ontology/<term_local_name>`. Trusty URIs (the addresses of the introducing nanopubs) take the form `https://w3id.org/np/RA…`.

The 45 terms by group:

- **Variant-anchor predicates (7):** `hasWHOVariantName`, `hasPangoLineage`, `hasGISAIDSeqId`, `hasMACSeqId`, `hasParentProtein`, `hasRBDSequence`, `hasGISAIDAccession`.
- **Observation-linkage predicate (1):** `isObservationOf`.
- **Method-linkage predicates (3):** `hasSurveillanceMethod`, `hasPredictionMethod`, `hasExperimentalMethod`.
- **Occurrence predicates (2):** `hasOccurrenceDate`, `hasCollectionLocation`.
- **Computational-prediction value predicates (4):** `hasRMSD`, `hasSASA`, `haspLDDT`, `hasAgMataScore`.
- **DMS value predicates (6):** `hasBind`, `hasDeltaBind`, `hasExpr`, `hasDeltaExpr`, `hasConfidenceBind`, `hasConfidenceExpr`.
- **WHO classification predicates (3):** `hasWHOClassification`, `hasClassificationDate`, `hasWHOClassificationReference`.
- **Abstract parent classes (5):** `Observation`, `ComputationalPrediction`, `ExperimentalObservation`, `Method`, `WHODesignation`.
- **FDT and observation classes (8):** `SpikeRBDVariant`, `RealWorldOccurrence`, `ComputationalPredictionRMSD`, `ComputationalPredictionSASA`, `ComputationalPredictionPLDDT`, `ComputationalPredictionAgMata`, `ExperimentalDMSObservation`, `WHOVariantClassification`.
- **Method classes (3):** `ComputationalMethod`, `ExperimentalMethod`, `ObservationalMethod`.
- **WHO controlled values (3):** `VOC`, `VOI`, `VUM`.

#### A.2 Stage 2 — Templates (11)

| Type | Class declared | Trusty URI |
|---|---|---|
| 1 | `mac:SpikeRBDVariant` | `RADOnITa1gjGIQtuENvlB2I7hykzrASzake1bIjGLiAtM` |
| 2 | `mac:RealWorldOccurrence` | `RA_-AALlM1rIYcJRsFUrIfSb5KYSvjiHUZbQbN-cpeV6w` |
| 3 | `mac:ComputationalPredictionRMSD` | `RALJKysR8vqqqZYXPGHcsI_J0BvPFUmzwOnV9WCGvUjcY` |
| 4 | `mac:ComputationalPredictionSASA` | `RALSYeUQIciUad7GTfKjdNkfhP-505fesw6yYtdLoyW18` |
| 5 | `mac:ComputationalPredictionPLDDT` | `RAm5j8EmzrS_ZDXEEOkvG2icT27GlbaGoNAS0sCDS72wc` |
| 6 | `mac:ComputationalPredictionAgMata` | `RAuCu_OnyqK_dlaJ9l1EDdbtu_Wbpdw2pTlcTimQ9mqV0` |
| 7 | `mac:ExperimentalDMSObservation` | `RAp-dZcpmyNxtFsh7G0G1CDzzP2vPqoXVZSnlYRVQ_5Yk` |
| 8 | `mac:WHOVariantClassification` | `RAWyoHGVyB3Rh-fizZguS1zzf8Cim3q5ngWSoQNs2Sgcs` |
| 9 | `mac:ComputationalMethod` | `RA5f4FtcnAGRtdt-vDTCvwXT1yVX7oMoXmvv-B8nfMelc` |
| 10 | `mac:ExperimentalMethod` | `RALExfuvWjR8Lezp7I64cWCHgqyLb52js6-CTDIoINohs` |
| 11 | `mac:ObservationalMethod` | `RAW9DfO6hmmt2sz_H4pHWWAX72BzTsnYjb9hi5wVQIQdE` |

Eleven pin-action nanopubs (one per template) attach each template to the Space `https://w3id.org/spaces/knowledgepixels/incubator/project4` via `gen:hasPinnedTemplate`. Pin-action Trusty URIs are recorded in `PUBLISHED_pin_actions.md` (or per-type publication records) in the repository.

#### A.3 Stage 3 — Instances (38)

**Variant anchors (Type 1, 3 instances).**

| instance_id | Trusty URI | Referent URI |
|---|---|---|
| `Alpha-RBD-Variant` | `RA4BHII2Bz7HfpUkaSJqNmhjF8F7hyWpCJnvXYkA4EP_M` | `<Trusty>/Alpha-RBD-Variant` |
| `Epsilon-RBD-Variant` | `RAbyuWWdW-j1rYt7Eqnva6aBvMyTkM9_Ka2FbA9dJHR7s` | `<Trusty>/Epsilon-RBD-Variant` |
| `Eta-RBD-Variant` | `RAikllrKWQoo81RYYvGJjWfzE0QiGrLquMMIwDD6xem2s` | `<Trusty>/Eta-RBD-Variant` |

**Method instances (Types 9–11, 5 instances, shared across all three twins).**

| instance_id | Type | Trusty URI | Referent URI |
|---|---|---|---|
| `ESM2-Method` | 9 | `RADJxd-U-p7VpA01uXlsp3nkUo3oXFMSOam04-fcF0ZyM` | `<Trusty>/ESM2-Method` |
| `AlphaFold2-Method` | 9 | `RA3zXmeaYZxYSPXzH7CK8-m5T31NWr9nvUCeyKz2mbvNI` | `<Trusty>/AlphaFold2-Method` |
| `AgMata-Method` | 9 | `RA3JGJN1R1uTyj1puobq1cEwHT52LNmM_67dzb0oRAz2U` | `<Trusty>/AgMata-Method` |
| `BloomLab-DMS-Method` | 10 | `RA0Bz7doV8fCSO9lEmpbtNTOnMu5lB3jVudjo-tD0T_Q0` | `<Trusty>/BloomLab-DMS-Method` |
| `GISAID-Method` | 11 | `RA7XLn4SiwTU4L_5YFYW8KBefgKeYXRu5DSFvYtlZE-o4` | `<Trusty>/GISAID-Method` |

**Computational predictions (Types 3–5, 18 instances).**

| instance_id | Type | Trusty URI |
|---|---|---|
| `Alpha-RMSD-AlphaFold2` | 3 | `RAjn5zJQoLUFSMpDLEEG6Pc_oONJNDlMnPi4grKHOsxOE` |
| `Alpha-RMSD-ESM2` | 3 | `RASyg7i8HV4TxiN_-b2KKY6lAuFUkU4_T9pBrtAPA0Uac` |
| `Alpha-SASA-AlphaFold2` | 4 | `RAXXa3_lWNc_NYn9Hd8uaA_bHZVeUhiRJDf8Ugkfu6vLM` |
| `Alpha-SASA-ESM2` | 4 | `RAxIOCQ4MnuGhYt3jLW9QMoWLdRtYThQVVo2kGPL7Rluc` |
| `Alpha-pLDDT-AlphaFold2` | 5 | `RAd9HOScIMpFwHd5U14cg8ez6mSKV2w7y9ow433mL9quA` |
| `Alpha-pLDDT-ESM2` | 5 | `RA3i18Z4N8YQgl-BfudZ42DI7Bbg53MotI6RaNs9fqUz0` |
| `Epsilon-RMSD-AlphaFold2` | 3 | `RA6R7bzGLG0TQDCfFITDN9plVjA6uUF7raZLktK8zMi7k` |
| `Epsilon-RMSD-ESM2` | 3 | `RASwHwTv2vBeWJKtUuRz0SoiQz8MW-c2Q2--9-P9aet28` |
| `Epsilon-SASA-AlphaFold2` | 4 | `RA_1MdrIk8wbsgaTZE0jObzWwmxbofD3bcXdRsy6imKDY` |
| `Epsilon-SASA-ESM2` | 4 | `RAfu8HN7te8b0fLOzPqM4FW9RkBJwTgz6tSXajoeErxRQ` |
| `Epsilon-pLDDT-AlphaFold2` | 5 | `RAdQ0Y6Qi1jiguOYaE6KA3UBCHCe5w6WaNCEIXznwhw2E` |
| `Epsilon-pLDDT-ESM2` | 5 | `RAdRQFoeuo9TZOIa0Val0SvFBKk9WNao-hUpgCgAE07vk` |
| `Eta-RMSD-AlphaFold2` | 3 | `RAjl9Ui02eVoJoNbx_EEntYV5a4flxCBWtX3Kd2tQ8SFE` |
| `Eta-RMSD-ESM2` | 3 | `RA4W0pxcS_W5DN19grmRbHbaajsyxyuKcQw7Zpg_W6ycg` |
| `Eta-SASA-AlphaFold2` | 4 | `RAdHQntpPxeWMz2i7U2DbtqwsKHMq1ChPGsSFCldceCik` |
| `Eta-SASA-ESM2` | 4 | `RARSu37G4FkiF7SM9ymgB7x0XYtYM0YU8Pw_4hPa3jvQ8` |
| `Eta-pLDDT-AlphaFold2` | 5 | `RABB4kADKKy-TSQhvWkwvY7Rk907mFd6dQ-Qv2QSfuwuA` |
| `Eta-pLDDT-ESM2` | 5 | `RAJ0NJ-vXIIBmxdR5eR-ndXTc5gQYhBKSvSAtHmvkaSrA` |

**Final observations (Types 2, 6, 7, 8 — 12 instances).**

| instance_id | Type | Trusty URI |
|---|---|---|
| `type2_alpha` (Alpha occurrence) | 2 | `RAyjkMnXEnRF09TI4R531mYM4LKEm3HL5seHnVgQcqHN0` |
| `type2_epsilon` | 2 | `RATGfqd-Sy27F_M9NXKkbL-GzIO9IYXJguGTXBb2VEyQA` |
| `type2_eta` | 2 | `RAnwHIpm48gC4xB4d6ZxG1cDonBDEWGM-RyMf56_a5bk0` |
| `type6_alpha` (Alpha AgMata) | 6 | `RArJqTu2lE7v02BrY-UmChPKJEwR004azwXfZhZ3d5ZjQ` |
| `type6_epsilon` | 6 | `RAmPs3MytCSM__DOeyHDJQP9mwYJU6UXKKU8WGhrw5_KY` |
| `type6_eta` | 6 | `RAcm_5ysAXUPBHcvhNVo_Xnu6OGO0SBEGvzqb4wGfVm-g` |
| `type7_alpha` (Alpha DMS) | 7 | `RARb0NfCsCVn6tTY3m1sXor6mEbZzIZ6WzBSEjtmftLgs` |
| `type7_epsilon` | 7 | `RAfI_EQBRQvVh3LRb0WLQFvXra2gINrvxaOZQprZ0KngE` |
| `type7_eta` | 7 | `RAmrs8u-EM7ejf5shyxo9OVXf2fgAcmB_HB4F-smPQJL0` |
| `type8_alpha` (Alpha WHO) | 8 | `RApoAkERvI9mPGcz-ExkSSDvXbNAYZygNFW2IAZpaRsGk` |
| `type8_epsilon` | 8 | `RAn5yBad0gMJPsVE5rIiJvWP1GemI-2Wmi91KcCOSFQSg` |
| `type8_eta` | 8 | `RAJRZGtEnHkqBERKZg34r8iX7sbEemtqOURYyRgB0MSa4` |

#### A.4 Stage 4 — Standing views (16 nanopubs)

**Query nanopubs (4).**

| View | Trusty URI |
|---|---|
| Catalogue summary by type | `RAGlsCUDZrgFmlRQ8RNIpaWHaKAnRX7SGjEqOCGoWsM8A` |
| Variants by WHO classification | `RAlD3u-iOS5P95TlvydUePQCOqKyVsPLebBNTnu4lw7po` |
| Observations per method | `RAIKnskDgF8ZX-hOIC1UKLSxDapH1K1FjkNKi5Or-A3ws` |
| Alpha digital-twin knowlet | `RAecvUbvUWiIOKP7ZEQk7hnUsb8lWWUr1lRbVN2PsSUSA` |

**Sidebar pin-actions (4).**

| View | Trusty URI |
|---|---|
| Catalogue summary | `RAr2do6-Zm_F5tv9NP4iziOpRCX-mJUZzCqUfY-brnNRY` |
| Variants by WHO | `RAkwEb52MHk6Xe4uzOruIAkmGZAq4URDyg5bPqx4SXY1Y` |
| Obs per method | `RAZge9g-AM2aYodnkKrlt6ag1s1QPYjTYBCJZaPezTZ6M` |
| Alpha knowlet | `RAzEolNOqr8I1aiZpafpUxJfqBOQRdTapceYWjXCoEYAE` |

**`gen:View` wrappers (4).**

| View | Trusty URI | Referent URI |
|---|---|---|
| Catalogue summary | `RAUQDFIiL73MByusDvrnMLRJaDW32bImYrq4aQN5CJmLM` | `<Trusty>/fdt-catalogue-summary-view` |
| Variants by WHO | `RA2orwJH_zUQQvUvKk0UHvCr5x8iAVhIopqLUFYyuy-Eg` | `<Trusty>/fdt-variants-by-who-view` |
| Obs per method | `RAS-Wm3ewaQtz8rhzKY-EAyrJnYGZMq3MOz2AZ9fXQ5e8` | `<Trusty>/fdt-observations-per-method-view` |
| Alpha knowlet | `RA_zvbVo3VX6Cy3lYOI6LNHJICb1copbCmJHayjpzCeJ0` | `<Trusty>/fdt-alpha-knowlet-view` |

**`gen:ViewDisplay` nanopubs (4).**

| View | Trusty URI |
|---|---|
| Catalogue summary | `RAvARpXohLClZVC3qZdtn1JihyPU12NsmTQAHoziXXRq4` |
| Variants by WHO | `RAywsGEhq4acHjLNY6rALv2vvhjGwqYsFeFayr3hwZ4iM` |
| Obs per method | `RA-XrE3QY1r0Llm5TLurg0VcasOT_hfta-AM_4qp1srZo` |
| Alpha knowlet | `RA-QuZXXV9ni6b2YW0cM4ADyzYi-Uo4FQDR0p2pdR9tUk` |

#### A.5 External templates and resources

NanoDash templates the build consumes (not authored by the catalogue):

| Role | Trusty URI |
|---|---|
| Meta-template ("Defining an assertion template") | `RA5reLVXOCPQFWr2UiCJb19ES7NwOpQRmudb17e2iB0c4` |
| Provenance template | `RA7lSq6MuK_TIC6JMSHvLtee3lpLoZDOqLJCLXevnrPoU` |
| Pubinfo: License | `RA0J4vUn_dekg-U1kK3AOEt02p9mT2WO03uGxLDec1jLw` |
| Pubinfo: Creator | `RAukAcWHRDlkqxk7H2XNSegc1WnHI569INvNr-xdptDGI` |
| Pubinfo: Hand-coded | `RAMEgudZsQ1bh1fZhfYnkthqH6YSXpghSE_DEN1I-6eAI` |
| Pubinfo: Derived | `RARW4MsFkHuwjycNElvEVtuMjpf4yWDL10-0C5l2MqqRQ` |
| Pin-template ("Declare a pinned template for a Space") | `RA2YwreWrGW9HkzWls8jgwaIINKUB5ZTli1aFKQt13dUk` |
| grlc-query ("Defining a grlc query") | `RAEFAt-QcFK0ZhqfvlsmS10BnzGJA0xwOICZXkO-ai87k` |
| Pin-query ("Declare a pinned query for a Space") | `RAuLESdeRUlk1GcTwvzVXShiBMI0ntJs2DL2Bm5DzW_ZQ` |
| `gen:View` wrapper ("Declaring a resource view") | `RARLsTlqbTesu1b0WJZ-zL1z96xumOiqbK3l_vV6iZoww` |
| `gen:ViewDisplay` ("Displaying a view for a Space") | `RAsc8FMsGih955oFSFG0YcB9sDKA62VLbp3VIw86IxMvk` |
| Retraction template | `RAQP3NJvnLA2Z-2DrYAN0nTC-RFp67td1t4-pQqQ_ZKmo` |

External upstream FDOs the catalogue references via `dct:isPartOf` and `dct:source`:

| Resource | URI |
|---|---|
| StayAhead Project FDO (referent) | `https://w3id.org/np/RAFPOe4OIl_urs-U_7-FostjzcUo8ra6LasfSvGplOvto/StayAhead-Project` |
| ESM Dataset FDO | `https://w3id.org/np/RA9YxiABPRNy3rrJm20p1oanJchBcI22IPpSu36zj2MLs` |
| AlphaFold Dataset FDO | `https://w3id.org/np/RAv6JJe-lvoadhNwml8pzSLs5aOtbU1xbHT5qgFtgwQ-s` |
| FAIR² data article | `https://doi.org/10.3389/fbinf.2025.1634111` |
| FAIR² Data Package | `https://doi.org/10.71728/hw56-vj34` |
| Wild-type Spike (UniProt) | `https://www.uniprot.org/uniprot/P0DTC2` |

The Project FDO and the two Dataset FDOs are currently `npx:DraftNanopub`; promotion to non-draft is tracked in `Post_demonstration_cleanup.md` (see Appendix C.1).

#### A.6 Endpoints

| Purpose | URL |
|---|---|
| Signature-validated SPARQL repo | `https://w3id.org/np/l/nanopub-query-1.1/repo/full` |
| NanoDash MAC-Ontology Space view | `https://nanodash.knowledgepixels.com/space?id=https://w3id.org/spaces/mac/r/ontology/MAC-Ontology` |
| NanoDash working Space (project4) | `https://nanodash.knowledgepixels.com/space?id=https://w3id.org/spaces/knowledgepixels/incubator/project4` |
| Project picker API (`get-projects`) | `https://w3id.org/np/l/nanopub-query-1.1/api/RAFTZ8GqPOOJQOBcEo5IB8lg5vZCFiIyr_RVLKZDQBHMk/get-projects?searchterm=` |
| Nanopub registry | `https://registry.knowledgepixels.com/` |

---

### Appendix B — Repository layout

```
mac-fdt-staging/
├── specs/
│   ├── MAC_FDT_Vocabulary_v1_2.md          ← 26 predicates + 19 classes spec
│   ├── MAC_FDT_SPS_v1_4.md                 ← current SPS (this guide implements)
│   ├── MAC_FDT_SPS_v1_3.md                 ← audit (superseded)
│   └── MAC_FDT_SPS_v1_2.md                 ← audit (superseded)
├── minting/
│   ├── stage1-vocabulary-drafts/
│   │   ├── generator/
│   │   │   ├── generate_vocabulary.py
│   │   │   └── vocabulary_terms_v1_2.csv   ← input to the generator
│   │   ├── drafts/                         ← 45 unsigned TriG files
│   │   ├── signed/                         ← 45 signed TriG files
│   │   ├── manifest_live_v1.csv            ← v1 audit
│   │   └── manifest_live_v2.csv            ← current authoritative lookup
│   ├── stage2-templates/
│   │   ├── generator/
│   │   │   ├── generate_template.py
│   │   │   └── configs/type{1..11}_config.py
│   │   ├── drafts/                         ← 11 unsigned + 11 signed templates
│   │   ├── reference/                      ← meta-template + exemplars (audit)
│   │   ├── SESSION_STATE.md                ← cross-stage tracking
│   │   ├── Post_demonstration_cleanup.md   ← deferred items (Appendix C.1)
│   │   └── PUBLISHED_v4.md                 ← Stage 2 publication record
│   ├── stage3-instances/
│   │   ├── generator/
│   │   │   ├── generate_instance.py        ← 6 kinds: type1, method, prediction,
│   │   │   │                                  occurrence, who, dms
│   │   │   ├── generate_predictions_from_csv.py    ← Types 3-5 driver
│   │   │   ├── generate_type6_7_from_csv.py        ← Types 6, 7 driver
│   │   │   ├── instance_configs/
│   │   │   │   ├── type1_{alpha,epsilon,eta}.py
│   │   │   │   ├── method_{esm2,alphafold2,agmata,bloom_dms,gisaid}.py
│   │   │   │   ├── type2_{alpha,epsilon,eta}.py
│   │   │   │   └── type8_{alpha,epsilon,eta}.py
│   │   │   └── FDT4Claude_small_v1_2.csv   ← per-row metric data
│   │   ├── drafts/                         ← 38 unsigned + 38 signed
│   │   ├── PUBLISHED_type1_instances.md
│   │   ├── PUBLISHED_methods.md
│   │   ├── PUBLISHED_predictions.md
│   │   └── PUBLISHED_observations_final.md
│   └── stage4-views/
│       ├── drafts/
│       │   ├── query/                      ← 4 grlc-query nanopubs (unsigned/signed)
│       │   ├── pin/                        ← 4 sidebar pin-actions
│       │   ├── wrapper/                    ← 4 gen:View wrappers
│       │   └── display/                    ← 4 ViewDisplays
│       └── PUBLISHED_views.md              ← all 16 Trusty URIs
└── docs/
    └── implementation_guide.md             ← this document
```

**Branch model.** Each work item lives on a short-lived branch (`stage{N}-templates-type{M}`, `stage3-instances-{methods,type1,types-3-4-5,types-2-6-7-8}`, `stage4-views`) and is merged into `main` after validation. The `main` branch is the canonical state. Branches are retained for audit even after merging.

**File conventions.** Unsigned TriG → `drafts/`; signed TriG → `signed/`. Each batch's publication record (live Trusty URI, publish timestamp, render status) is a `PUBLISHED_*.md` file in the same stage directory.

---

### Appendix C — Common pitfalls and their resolutions

This section catalogues the error modes the demonstration build encountered or identified, with the prescriptive fix in each case. New builds should not need to rediscover any of these.

#### C.1 Referencing draft nanopubs

**Symptom:** Stage 3 instances declare `dct:isPartOf` → a Project FDO that is itself `npx:DraftNanopub`. The instances inherit a draft reference, which propagates to all 38 instance nanopubs.

**Cause:** In the demonstration catalogue, the StayAhead Project FDO and the two Dataset FDOs (ESM, AlphaFold) were minted as drafts during the MAC v2 work and not promoted to non-draft before Stage 3.

**Resolution:** for new builds, promote upstream FDOs to non-draft before Stage 3 instance minting begins. For the demonstration catalogue, the cleanup is deferred to a coordinated revision pass (see `minting/stage2-templates/Post_demonstration_cleanup.md` on `main`). The pass will mint v2 of each draft FDO with `npx:supersedes` linking to the v1 draft, then re-mint affected instances pointing at the v2 referents.

The same cleanup pass corrects:
- The Epsilon `gisaid_seq_id` value in `MAC_FDT_SPS_v1_3.md` and `FDT4Claude_small_v1_2.csv` (`L124R` → `L452R`; the demonstration instances already carry the correct value).
- The "AphaFold2" → "AlphaFold2" typo in the AlphaFold Dataset FDO label.

#### C.2 Bare Trusty URI vs referent URI

**Symptom:** Stage 3 observation instances declare `mac:isObservationOf <bare-anchor-Trusty-URI>` instead of `<anchor-Trusty-URI>/Alpha-RBD-Variant`. The link "resolves" (returns the introducing nanopub) but SPARQL queries traversing the FDO graph by referent return zero rows.

**Cause:** the FDO is identified by its referent URI (`<Trusty URI>/<instance_id>`), not by the Trusty URI of the introducing nanopub. The introducing nanopub is *where* the FDO is declared; the referent URI is *the FDO*.

**Resolution:** every cross-reference uses the referent form. Predicates affected: `mac:isObservationOf`, `mac:hasPredictionMethod`, `mac:hasExperimentalMethod`, `mac:hasSurveillanceMethod`, `dct:isPartOf`, and `gen:isDisplayOfView` (Stage 4).

#### C.3 `npx:retracts` vs `npx:invalidates`

**Symptom:** a publisher writes an "invalidation" nanopub using `<this> npx:invalidates <target>` directly. The resulting nanopub publishes and is structurally well-formed, but the canonical retraction filter in queries (`FILTER NOT EXISTS { ?r npx:retracts ?n1 }`) does not pick it up.

**Cause:** `npx:invalidates` is an internal generalisation used inside the nanopub-query repos to unify retractions and supersessions. It is not the publisher-facing predicate.

**Resolution:** use `npx:retracts` from the retraction template `RAQP3NJvnLA2Z-2DrYAN0nTC-RFp67td1t4-pQqQ_ZKmo`. The query repo derives `npx:invalidates` in the admin graph automatically. In SPARQL filters, the admin-graph form (`npx:invalidates`) is correct because it generalises over both retractions and supersessions.

#### C.4 `gen:isDisplayOfView` pointing at a bare query

**Symptom:** a ViewDisplay nanopub asserts `gen:isDisplayOfView <bare-grlc-query-Trusty-URI>` (skipping the wrapper layer). The nanopub publishes cleanly but no panel renders on the Space page.

**Cause:** the NanoDash renderer expects `gen:isDisplayOfView` to point at a `gen:View` wrapper (which itself carries `gen:hasViewQuery` → the query). The wrapper layer carries display metadata (view kind, structural position, applies-to scope, page size) that the bare query does not.

**Resolution:** always mint a `gen:View` wrapper for each query, then point the ViewDisplay at the wrapper's referent URI (`<wrapper-Trusty>/<view-local-name>`). See §5.7. The demonstration build encountered this error mode during initial Stage 4 work; the broken ViewDisplays were corrected via `npx:retracts`.

#### C.5 Missing statement ID in `nt:hasStatement`

**Symptom:** a Stage 2 template defines a statement pattern (`sub:st_w …`) in the assertion graph but omits `sub:st_w` from the `nt:hasStatement` list of the template declaration. The form does not render that field; users cannot enter a value; the statement is missing from all instances.

**Cause:** `nt:hasStatement` is authoritative for NanoDash. A statement defined in the assertion graph but missing from the list is not part of the template from the renderer's perspective.

**Resolution:** the generator constructs `nt:hasStatement` from the per-type config's statement-ID list and validates that every defined statement appears in the list. The regression check (byte-identical round-trip against Type 1 v4) catches drifts.

#### C.6 Class URI vs Trusty URI of introducing nanopub (Type 8)

**Symptom:** a Type 8 WHO classification instance declares `mac:hasWHOClassification <Trusty-URI-of-VOC-introducing-nanopub>`. The link resolves but does not match the Type 8 template's `nt:possibleValue mac:VOC` and breaks the WHO-classification query's `?obs mac:hasWHOClassification ?whoClass` pattern (the actual class URI is what the template expects).

**Cause:** the class itself has the URI `https://w3id.org/spaces/mac/r/ontology/VOC` (the `mac:` prefix expansion). The Trusty URI of the introducing nanopub is *where the class is defined*, not the class itself.

**Resolution:** instances use the class URI (curie form `mac:VOC` works) as the object of `mac:hasWHOClassification`. The Stage 1 introducing nanopub's Trusty URI is referenced only via the vocabulary manifest, not in instance data.

#### C.7 Missing namespace prefixes for external predicates

**Symptom:** the common scaffold declares `fdof:`, `dcat:`, `cito:`, and `schema:` as prefixes in some templates but not others, leading to byte-divergent output between generator runs.

**Cause:** the MAC FDT scaffold deliberately does *not* declare `fdof:`, `dcat:`, `cito:`, or `schema:` in the common `@prefix` header. Predicates from these namespaces appear as full URIs throughout (e.g., `<https://w3id.org/fdof/ontology#hasMetadata>` rather than `fdof:hasMetadata`).

**Resolution:** preserve this convention. Adding prefixes to the header for these namespaces changes byte-level output across the eleven templates without semantic gain. SPS v1.4 §"Implementation notes" documents this decision; a future coordinated revision may consolidate them.

#### C.8 NanoDash indexing lag

**Symptom:** after publishing a Stage 2 pin-action or a Stage 4 ViewDisplay, the Space page does not immediately show the new pinned template or panel.

**Cause:** NanoDash indexes the NSN periodically (minutes to a few hours after publication). The SPARQL endpoint reflects the published data immediately, but the Space-page renderer reads from a separate index.

**Resolution:** verify via SPARQL first (the SPARQL queries in §3.8 and §5.8 cover all pin and ViewDisplay registrations). If the SPARQL count is correct, the data is correct; the rendering will catch up. Allow up to 2 hours before suspecting a renderer-side issue. The same lag applied to the Stage 1 MAC-Ontology view and to the Stage 4 panels in the demonstration build.

#### C.9 Method link mandatory vs optional

**Symptom:** a Type 2 (real-world occurrence) instance is signed without `mac:hasSurveillanceMethod` even though every occurrence in the catalogue uses GISAID. Validation passes; downstream queries that join occurrences to surveillance methods return no rows for these instances.

**Cause:** Type 2's `mac:hasSurveillanceMethod` is *optional* per SPS v1.4 (an occurrence might be authored without surveillance-source attribution if data provenance is uncertain). Optional fields are not enforced at signing time.

**Resolution:** for catalogues where the method link is universally available, the generator can promote the field to mandatory in the per-type config (`"flags": ["mandatory"]`). The demonstration catalogue declares the field on every Type 2 instance even though the template makes it optional. New catalogues should make the same project-level decision.

---

### Appendix D — The companion SPS v1.4

This guide implements the specification at:

```
specs/MAC_FDT_SPS_v1_4.md
```

The SPS specifies *what* (the contractual data shape); this guide specifies *how* (the procedural implementation). When a question arises about the catalogue's data, consult the SPS. When a question arises about minting, signing, validating, or publishing, consult this guide.

**SPS v1.4 sections cross-referenced by this guide:**

| SPS section | Referenced from this guide |
|---|---|
| §"Type 1" (Spike RBD Variant) | §3.4.1 (template config), §4.4.1 (instance values) |
| §"Type 2" (Real-World Occurrence) | §3.4.2, §4.4.5 |
| §"Types 3-5" (RMSD/SASA/pLDDT) | §3.4.3–3.4.5, §4.4.3 |
| §"Type 6" (AgMata) | §3.4.6, §4.4.4 |
| §"Type 7" (DMS) | §3.4.7, §4.4.4 |
| §"Type 8" (WHO Classification) | §3.4.8, §4.4.6 |
| §"Types 9-11" (Methods) | §3.4.9–3.4.11, §4.4.2 |
| §"RBD sequences" | §4.4.1 (195-character sequences) |
| §"Types 3-6 All instance values" | §4.4.3, §4.4.4 (metric values cross-check) |
| §"Source URLs" | §4.4.3 (`dct:source` triplets per method) |
| §"Architectural commitments" | §3.3 (self-materialization block) |
| §"Per-type provenance obligations" | §3.3, §3.4 (which statements per type) |
| §"Implementation notes" | §3.3 (prefix conventions, regex, label patterns) |

**Architectural commitments locked at SPS v1.4** (relevant to this guide):

1. **Self-materialization mandatory.** The four-statement block (`st5`/`st5b`/`st5c`/`st5d`) is byte-identical and non-optional across all 11 templates.
2. **`dct:isPartOf` mandatory.** Every FDO declares its project anchor.
3. **`cito:citesAsAuthority` mandatory on methods, optional on observations.** Each method declares ≥1 published authority; observations may reach attribution via the two-hop method path (default) or one-hop (when an observation has its own canonical publication).

**Going beyond the SPS.** This guide adds procedural elements not in the SPS: the generator architecture (§3.5, §4.3), the CSV-driven path (§4.4.3, §4.4.4), the publication order (§4.5), the Stage 4 standing-view set and structural positions (§5), and the validation queries throughout (§§2.6, 3.8, 4.7, 5.8). These are implementation choices and may evolve without an SPS change.

**When the SPS and this guide diverge.** The SPS is authoritative on the data shape; this guide is authoritative on the procedure. If a divergence arises (e.g., the SPS declares an optional statement mandatory, while this guide's generator treats it as optional), the SPS wins and this guide must be updated. The reverse — this guide enforcing something stricter than the SPS — is fine; it represents a project-level convention not encoded in the contractual specification.
