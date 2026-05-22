<!--
AUTHOR: Erik Schultes
SESSION: Making MAC FAIR/Article - FDT Paper
DATE: 2026-05-22
URL: https://claude.ai/chat/22a7668a-24ce-4533-82fa-7e5a6b6204e9
CREATED_AT: P23/R23
DESCRIPTION: Orientation README v1.2 for the Claude Code nanopub-minting session — updated to track SPS v1.2 (FAIR² citation policy supersedes v1.1) and the workspace reorganisation into `specs/`, `data/`, `minting/`, `extensions/`, `paper/`. Supersedes v1.1.
-->

# README — Claude Code FDT Minting Session (v1.2)

## What this is

This directory contains the working materials for minting a set of nanopublication-based FAIR Digital Objects (np-FDOs) that collectively realise three FAIR Digital Twins (FDTs) for SARS-CoV-2 Spike RBD variants (Alpha N169Y, Epsilon L120R, Eta E152K).

The session uses the `nanopub-skill` (https://github.com/knowledgepixels/nanopub-skill) loaded into Claude Code, with Tobias Kuhn available for live guidance on identity setup, signing, and any minting-time decisions.

**Status (21 May 2026):** All five vocabulary-affecting open items have been resolved (see §"Resolved open items" below). The session is cleared to proceed through Stages 1–3.

## Changes since v1.1

* SPS updated to v1.2 (FAIR² citation policy: data article DOI mandatory on Type 1; FAIR² Package DOI + portal URL mandatory on Types 3–6). Vocabulary v1.1 unchanged.
* Workspace reorganised into `specs/`, `data/`, `minting/`, `extensions/`, `paper/`. File paths in this README updated accordingly.
* Filename conventions normalised to underscores (`v1_2`, `v1_1`).

## How to use this directory with Claude Code

1. From `~/nanopub-work/`, ensure `nanopub-skill/` has been cloned and `mac-fdt-staging/` (this directory) contains all the files listed below.
2. Start Claude Code in `~/nanopub-work/`.
3. Instruct Claude Code: *"Load the skill in the `nanopub-skill` subfolder. Then read `mac-fdt-staging/minting/README_for_Claude_Code_v1_1.md` and the v1.1 vocabulary and v1.2 SPS specs, and report back with your understanding of the task before taking any action."*
4. Verify the understanding with Tobias before any minting begins.

## Inventory of working materials

| File | Role |
|---|---|
| `../specs/MAC_FDT_SPS_v1_2.md` | **Authoritative specification (v1.2).** 11 FDO types, 26 predicates, 14 classes, three-layer architecture. Updated for resolved open items. Structural source of truth. |
| `../specs/MAC_FDT_Vocabulary_v1_1.md` | **Definitions for every MAC-namespace predicate and class (v1.1).** Records the five resolutions. Semantic source of truth. |
| `../data/FDT4Claude_small_v1_1.csv` | The empirical content: per-variant values for all observation types, for the three initial variants. |
| `(not in this repo — see companion paper)` | Foundational paper for the np-FDO substrate (context, not a minting target). |
| `README_for_Claude_Code_v1_1.md` | This document. |

## Task summary

Mint, in this order, the following nanopublications to the Nanopublication Server Network (NSN) under Erik Schultes's ORCID (0000-0001-8888-635X):

### Stage 1 — Vocabulary (26 predicate + 14 class nanopubs = 40)

For each entry in `../specs/MAC_FDT_Vocabulary_v1_1.md` Parts A and B: one nanopub asserting the term as either an `owl:ObjectProperty` (predicates) or `owl:Class` (classes), with `rdfs:label`, `rdfs:comment` (from the document), `dct:creator`, `dct:license` (CC BY 4.0), and standard provenance. Use the namespace `https://w3id.org/spaces/mac/r/ontology/MAC-Ontology` (Item 1, resolved); the term URI separator (slash or hash) is assigned by NanoDash. Record the Trusty URI of each vocabulary term for use in Stage 2.

### Stage 2 — Templates (11 NanoDash templates)

For each of the 11 FDO types in `../specs/MAC_FDT_SPS_v1_2.md`: one NanoDash-compatible template nanopub encoding the assertion structure, with mandatory and optional statement patterns, controlled-vocabulary constraints, and references to the Stage 1 vocabulary URIs. Record the Trusty URI of each template.

Key template properties confirmed in v1.2:

* Types 2–8 carry `mac:isObservationOf` with object range = **referent URI** (the `sub:fdo` declared by the Type 1 anchor), not the anchor's Trusty URI.
* Type 2 carries `mac:hasCollectionLocation` with object range = **GeoNames URI** of the form `https://sws.geonames.org/{id}/`.
* Types 9, 10, 11 use `cito:citesAsAuthority` (not `schema:citation`) to link a method FDO to its authoritative published description.
* `mac:hasGISAIDAccession` is used at Types 1 and 2 as a single predicate with **literal** (string) object range. No split.

### Stage 3 — Instances (38 instance nanopubs)

Following the count breakdown in `../specs/MAC_FDT_SPS_v1_2.md` §"Nanopub count":

* 3 Type 1 (Spike RBD Variant — the anchor FDOs $A_r$, one per variant)
* 3 Type 2 (Real-World Occurrence)
* 6 Type 3 (RMSD; ESM + AlphaFold per variant)
* 6 Type 4 (SASA; ESM + AlphaFold per variant)
* 6 Type 5 (pLDDT; ESM + AlphaFold per variant)
* 3 Type 6 (AgMata; one per variant — sequence-derived, method-independent)
* 3 Type 7 (DMS Experimental)
* 3 Type 8 (WHO Classification)
* 3 Type 9 (Computational Method — ESM, AlphaFold 2, Bio2Byte)
* 1 Type 10 (Experimental Method — Bloom Lab DMS)
* 1 Type 11 (Observational Method — GISAID)

**Total: 38 instance nanopubs.** Each carries a Trusty URI; the Types 2–8 instances cross-link to the corresponding Type 1 anchor's referent URI via `mac:isObservationOf`, forming the FDT cluster topology.

## Resolved open items (record of decisions)

| # | Item | Resolution (21 May 2026, with Tobias Kuhn) |
|---|---|---|
| 1 | MAC NanoDash ontology space URI | `https://w3id.org/spaces/mac/r/ontology/MAC-Ontology` (NanoDash viewer at `https://nanodash.petapico.org/resource?5&id=https://w3id.org/spaces/mac/r/ontology/MAC-Ontology`) |
| 2 | `mac:isObservationOf` resolution target | Resolves to the **referent URI** (`sub:fdo` of the anchor), not the Trusty URI of the anchor nanopub |
| 3 | `mac:hasCollectionLocation` encoding | **GeoNames URI** (`https://sws.geonames.org/{id}/`); free-text literals not used |
| 4 | Method citation predicate (Types 9–11) | **`cito:citesAsAuthority`** (SPAR CiTO ontology), replacing `schema:citation` |
| 5 | `mac:hasGISAIDAccession` dual use | Kept as **single predicate, literal range**; URI-typed re-encoding deferred pending public GISAID URI scheme |
| 6 | Class count consistency | Class count is **14**, not 16. SPS v1.0 header was a counting error; corrected in v1.1. |
| 7 | Minting order | **Vocabulary → templates → instances.** Each layer references the previous via Trusty URI. |

## Open items still pending at minting time (non-blocking)

| Item | Action at minting time |
|---|---|
| GISAID accession numbers (EPI_ISL_XXXXXXX) for Alpha, Epsilon, Eta | Supply at minting time if available; otherwise leave optional fields unset and add in follow-up instances |
| FAIR² source dataset URL resolution | Verify each FAIR² resource URL resolves correctly before publishing |
| StayAhead dataset FDO Trusty URIs | Substitute for raw OSF URLs in `dct:source` of Types 3–6 once StayAhead FDOs are minted |
| GeoNames feature IDs | Verify the working candidates in SPS v1.2 §Type 2 resolve to the intended features (England `6269131`, California `5332921`, Nigeria `2328926`); substitute precise IDs from GeoNames if any differs |
| `dct:publisher` ROR URI for Leiden / LACDR | Tobias to confirm at session start |

## Source data — `../data/FDT4Claude_small_v1_1.csv`

The CSV contains seven rows (one per variant × ESM/AlphaFold for the structural metrics, with AgMata as a single per-variant value carried on the ESM row by convention). Values for the three Type 7 (DMS) instances and the three Type 8 (WHO Classification) instances are supplied in `../specs/MAC_FDT_SPS_v1_2.md` directly.

Per-variant content map:

| Variant | Anchor ($A_r$) | Observations $O_r$ |
|---|---|---|
| Alpha (N169Y, B.1.1.7) | 1 × Type 1 | 1 RWO + 2 RMSD + 2 SASA + 2 pLDDT + 1 AgMata + 1 DMS + 1 WHO = 10 |
| Epsilon (L120R, B.1.427+B.1.429) | 1 × Type 1 | 10 (as above) |
| Eta (E152K, B.1.525) | 1 × Type 1 | 10 (as above) |

Per-variant FDT size: $|\text{FDT}(r)| = 1 + 10 = 11$ FDOs. Plus 5 shared method FDOs (Type 9 × 3, Type 10 × 1, Type 11 × 1) in the external method library $\mathcal{M}$.

## Provenance and licensing

* All nanopubs to be signed under ORCID `0000-0001-8888-635X` (Erik Schultes).
* All nanopubs to carry `dct:license` = CC BY 4.0 (`https://creativecommons.org/licenses/by/4.0/`).
* Where applicable, `dct:isPartOf` cross-links each instance to the StayAhead Project FDO (whose Trusty URI is to be confirmed).
* `dct:publisher` ROR URI for Leiden University / LACDR to be confirmed by Tobias at session start.

## Recommended verification before full publication

1. Mint Stage 1 to a **test server** or in **dry-run** mode first; verify Trusty URIs resolve and the `rdfs:comment` definitions render correctly.
2. Mint one Stage 2 template; verify it loads in NanoDash; verify the form fields match the SPS specification.
3. Mint one Stage 3 instance (suggest: the Alpha Type 1 anchor $A_{\text{Alpha}}$); verify SPARQL retrieval of all statements; verify cross-reference resolution.
4. Mint one Type 2 observation referencing $A_{\text{Alpha}}$; verify the `mac:isObservationOf` traversal returns the observation when queried from the referent URI.
5. Only then proceed to the full batch.

## After the session

Generate a catalogue file listing all 89 Trusty URIs (40 vocabulary + 11 templates + 38 instances) for substitution into the FDT paper's §5 placeholder URIs (`<TURI-…>`). The catalogue file is the empirical content of §5.2 and §5.3 of the FDT paper.

## Version history

| Version | Date | Notes |
|---|---|---|
| v1.0 | 20 May 2026 | Initial README; seven open items gating Stage 1. |
| v1.1 | 21 May 2026 | Open items 1–7 resolved or captured. Session cleared to proceed. |
| v1.2 | 22 May 2026 | Updated to track SPS v1.2 (FAIR² citation policy supersedes v1.1); paths updated for the workspace reorganisation into `specs/`, `data/`, `minting/`, `extensions/`, `paper/`. This document. |
