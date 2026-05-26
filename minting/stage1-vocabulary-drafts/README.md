# Stage 1 vocabulary drafts — for review

**Status:** Signed and **test-published** (test registry only — NOT production). Prepared 2026-05-22 on branch `stage1-vocabulary-draft`; revised the same day to apply all four items from Tobias Kuhn's PR #1 review (see `../../Stage1_hierarchy_and_domain_range_proposal.md`); namespace corrected 2026-05-26; "(draft, unsigned)" label suffix removed and pubinfo `dct:created` timestamp added per `nanopub-skill/SKILL.md` on the same date. 45 signed nanopubs live on `https://test.registry.knowledgepixels.com/`; Trusty URIs recorded in `manifest_test.csv`. Production publish is gated on Tobias sign-off (see "Intended next step" below).

## What this folder contains

Forty-five TriG nanopub draft files, one per MAC-namespace vocabulary term defined in `../../specs/MAC_FDT_Vocabulary_v1_2.md`.

| Kind | Count | Filename pattern |
|---|---:|---|
| Predicates | 26 | `predicate_<lowerCamelCaseLocalName>.trig` |
| Classes (14 concrete + 5 abstract) | 19 | `class_<CamelCaseLocalName>.trig` |
| **Total** | **45** | |

### Predicate inventory (26)

`hasWHOVariantName`, `hasPangoLineage`, `hasGISAIDSeqId`, `hasMACSeqId`, `hasParentProtein`, `hasRBDSequence`, `hasGISAIDAccession`, `isObservationOf`, `hasSurveillanceMethod`, `hasOccurrenceDate`, `hasCollectionLocation`, `hasPredictionMethod`, `hasRMSD`, `hasSASA`, `haspLDDT`, `hasAgMataScore`, `hasExperimentalMethod`, `hasBind`, `hasDeltaBind`, `hasExpr`, `hasDeltaExpr`, `hasConfidenceBind`, `hasConfidenceExpr`, `hasWHOClassification`, `hasClassificationDate`, `hasWHOClassificationReference`.

### Class inventory (19 = 14 concrete + 5 abstract)

**Abstract parents (5, new in Vocabulary v1.2):** `Observation`, `ComputationalPrediction`, `ExperimentalObservation`, `Method`, `WHODesignation`.

**Concrete (14):** FDT/observation (8): `SpikeRBDVariant`, `RealWorldOccurrence`, `ComputationalPredictionRMSD`, `ComputationalPredictionSASA`, `ComputationalPredictionPLDDT`, `ComputationalPredictionAgMata`, `ExperimentalDMSObservation`, `WHOVariantClassification`. Method (3): `ComputationalMethod`, `ExperimentalMethod`, `ObservationalMethod`. WHO controlled values (3): `VOC`, `VOI`, `VUM`.

## Changes since the first (40-file) draft

This revision applies all four items of Tobias's PR #1 review:

1. **`dct:partOf` replaces `rdfs:isDefinedBy`** in every assertion graph. Each term is now declared as part of the MAC ontology resource at `https://w3id.org/spaces/mac/r/ontology/MAC-Ontology` via `dct:partOf`.
2. **Class hierarchy.** Five new abstract parent classes have been added (`Observation`, `ComputationalPrediction`, `ExperimentalObservation`, `Method`, `WHODesignation`), each emitted as its own TriG file. All 14 concrete classes carry an `rdfs:subClassOf` triple pointing at the appropriate parent; the 4 hierarchy roots (`SpikeRBDVariant`, `Observation`, `Method`, `WHODesignation`) have no `rdfs:subClassOf` triple.
3. **Predicate `rdfs:domain` and `rdfs:range`.** Every predicate carries domain and range per `../../specs/MAC_FDT_Vocabulary_v1_2.md` §"Predicate domain and range". Predicates whose range is an `xsd:*` datatype are declared `owl:DatatypeProperty`; predicates with class range or omitted range remain `owl:ObjectProperty`. Five edge cases follow the proposal's recommended option 1 (omit the constraint): `hasGISAIDAccession` (dual-use → omit domain); `hasParentProtein`, `hasCollectionLocation`, `hasWHOClassificationReference` (foreign or generic URI → omit range); `hasOccurrenceDate` (range is `xsd:string` to admit imprecision).
4. **Slash separator confirmed** for the `mac:` namespace expansion. The slash form was already in use in the previous draft; v1.2 retains it.

## File structure

Each TriG file follows the nanopublication four-graph layout per `nanopub-skill/SKILL.md`:

| Graph | Contents |
|---|---|
| `sub:Head` | Declares the nanopub and references the other three graphs. |
| `sub:assertion` | Asserts the term as `owl:ObjectProperty` (predicates with class range or omitted range), `owl:DatatypeProperty` (predicates with `xsd:*` range), or `owl:Class` (classes), with `rdfs:label` and `rdfs:comment` taken verbatim from `../../specs/MAC_FDT_Vocabulary_v1_2.md`; `rdfs:domain` and `rdfs:range` per the same spec (predicates only, with the 5 omission cases noted above); `rdfs:subClassOf` per the hierarchy (classes only, except the 4 hierarchy roots); and `dct:partOf <https://w3id.org/spaces/mac/r/ontology/MAC-Ontology>`. |
| `sub:provenance` | `sub:assertion prov:wasAttributedTo <https://orcid.org/0000-0001-8888-635X> ; dct:created "2026-05-22"^^xsd:date`. |
| `sub:pubinfo` | `this: dct:created "<UTC>"^^xsd:dateTime ; dct:creator <ORCID> ; dct:license <CC BY 4.0> ; rdfs:label "Vocabulary term: mac:<local>"`. The `dct:created` timestamp is refreshed each time the generator runs (per `nanopub-skill/SKILL.md` line 465: refresh on every revision before publishing). The RSA signature block (`npx:hasAlgorithm`, `npx:hasPublicKey`, `npx:hasSignature`, `npx:hasSignatureTarget`, `npx:signedBy`) is inserted by the nanopub jar's `sign` subcommand at signing time. |

## Base URI — why the temp placeholder

All files use `http://purl.org/nanopub/temp/np001/` as the base URI for both `this:` and `sub:`. This is mandatory per `nanopub-skill/SKILL.md`: the `sign` step rewrites the placeholder into a Trusty URI throughout the file as part of computing the content-addressed hash. Using `https://w3id.org/np/temp` instead "causes the signed trusty URI to be malformed", per the skill's own warning. The trailing slash is required so that `sub:foo` correctly derives a sub-IRI of the eventual trusty root.

## MAC term namespace — corrected 26 May 2026

The `mac:` prefix expands to `https://w3id.org/spaces/mac/r/ontology/` (slash-terminated). Each term sits as a sibling to the `MAC-Ontology` resource in the same namespace:

- `mac:hasWHOVariantName` → `https://w3id.org/spaces/mac/r/ontology/hasWHOVariantName`
- `mac:SpikeRBDVariant` → `https://w3id.org/spaces/mac/r/ontology/SpikeRBDVariant`
- `mac:MAC-Ontology` (target of every `dct:partOf`) → `https://w3id.org/spaces/mac/r/ontology/MAC-Ontology`

An earlier round of drafts placed terms under `…/MAC-Ontology/{local}` (one path level too deep); Erik corrected this on 26 May 2026, and the 45 draft files plus the 45 signed-and-test-published nanopubs were regenerated, re-signed, and re-published to the test registry. The Trusty URIs in `manifest_test.csv` are the post-correction set.

## Provenance for definitions

Every `rdfs:label` and `rdfs:comment` string for the 14 concrete classes and 26 predicates is copied verbatim from `../../specs/MAC_FDT_Vocabulary_v1_2.md` (Parts A and B). The 5 new abstract-parent comments (Part B.0 of the spec) were drafted to match the voice of the existing entries; they follow the convention *"This class is abstract: all instances belong to one of its concrete subclasses."* and are reproduced verbatim from the spec into the TriG drafts.

## Validation status

`nanopub-skill/SKILL.md` prescribes `java -jar nanopub-<version>-jar-with-dependencies.jar check <file>` for syntactic validation. **All 45 files pass.**

- **JDK:** Temurin 21.0.11 LTS, installed self-contained at `~/nanopub-work/jdk/jdk-21.0.11+10/Contents/Home` (the system `/usr/bin/java` is Java 14 and is too old to run the current nanopub jar — see `UnsupportedClassVersionError` note below). The Temurin JDK was downloaded directly from Adoptium because Homebrew is not installed on this machine; no system Java was modified.
- **Nanopub jar:** `nanopub-1.88.0-jar-with-dependencies.jar` from Maven Central, at `~/nanopub-work/`.
- **Result:** When invoked on the 45 unsigned drafts, the jar reports `Summary: 45 valid (not trusty);` — parses cleanly, structurally valid nanopublications; "not trusty" simply indicates the files are unsigned (no Trusty URI yet), which is the expected pre-signing state. The 45 signed files in `signed/` are trusty.

The structural grep used as a fallback in earlier iterations (four-graph layout, label/comment counts, brace balance, `prov:wasAttributedTo` in provenance, `dct:creator` in pubinfo only) was used at 40/40 in the v1.1 round and is retained as a fast sanity check for future regenerations. In v1.2 the canonical `nanopub check` is now passing on the same machine and the structural grep is no longer load-bearing.

> Note for anyone re-running this loop on a fresh machine: if the system Java is < 21, the nanopub jar will refuse to load with `UnsupportedClassVersionError: class file version 65.0 ... only recognizes class file versions up to 58.0`. The fix is to point at a Java 21+ JDK directly (either via `JAVA_HOME` or by invoking its `bin/java` explicitly). Brew install path: `brew install openjdk@21`. Tarball path (used here): download Temurin 21 from `https://api.adoptium.net/v3/binary/latest/21/ga/mac/x64/jdk/hotspot/normal/eclipse`.

## Current state — what is, and is not, present

The 45 unsigned drafts in this directory are the canonical pre-signing source; their signed counterparts live in `signed/` and are the artifacts that were test-published.

| Aspect | State in unsigned drafts (this folder root) | State in `signed/` |
|---|---|---|
| Base URI | `http://purl.org/nanopub/temp/np001/` (temp placeholder per skill) | Replaced with the Trusty URI by `nanopub sign` |
| Trusty URI | Not present | **Present** — recorded in `manifest_test.csv` |
| RSA signature block (`npx:hasAlgorithm`, `npx:hasPublicKey`, `npx:hasSignature`, `npx:hasSignatureTarget`, `npx:signedBy`) | Not present | **Present** — signed under ORCID `0000-0001-8888-635X` with key at `~/.nanopub/id_rsa` |
| Pubinfo `dct:created` (publication timestamp) | **Present** — current UTC at generation time (refreshed every regen per `nanopub-skill/SKILL.md` line 465) | Same (carried through signing) |
| Provenance assertion-creation date | **Present** — `sub:assertion dct:created "2026-05-22"^^xsd:date` (the day the definitions were authored; not refreshed on republish) | Same |
| `mac:` namespace | `https://w3id.org/spaces/mac/r/ontology/` (slash-terminated; corrected 2026-05-26) | Same |
| Vocabulary content (labels, comments, hierarchy, domain/range, `dct:partOf`) | **Final**, copied verbatim from `../../specs/MAC_FDT_Vocabulary_v1_2.md` | Same |
| License | CC BY 4.0 | Same |

## Intended next step (production gating)

1. Tobias sign-off on the post-correction post-timestamp set (the 45 Trusty URIs in `manifest_test.csv`).
2. Optional but recommended before production: build at least one Stage 2 template against the test-registry Trusty URIs to confirm the vocabulary "works" in template context.
3. Optional: mint an introduction nanopub (key declaration) so consumers can validate the signing key by dereference rather than trust-on-first-use. `profile.yaml`'s `introduction_nanopub_uri` is currently empty.
4. On explicit go-ahead: publish the 45 signed files to the live NSN with the same batch command but no `-u` flag (default is the live registry). Trusty URIs will be identical to the test ones because the same signed bytes hash to the same content-addressed ID.

Stage 1 vocabulary URIs feed Stage 2 (templates) which feed Stage 3 (instances). Stage 2 work can begin against the test-registry Trusty URIs immediately and will not need rework when those same URIs are promoted to production.
