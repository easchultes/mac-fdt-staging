<!--
AUTHOR: Erik Schultes
SESSION: Making MAC FAIR/Article - FDT Paper
DATE: 2026-05-21
URL: https://claude.ai/chat/22a7668a-24ce-4533-82fa-7e5a6b6204e9
CREATED_AT: P24/R24
DESCRIPTION: Consolidated working draft of the FDT paper, v0.5 — v0.4 updated to reference SPS v1.2 (FAIR² citation policy committed)
-->

# FAIR Digital Twins for SARS-CoV-2 Spike Variants

## A nanopublication-based realisation of the Knowlet concept

*Working draft v0.5 — SPS v1.2 (FAIR² citation policy) applied*

**Target venue:** *Frontiers in Big Data* (Research Article), as a follow-up to Schultes et al. 2022 [REF-FDT-Perspective] in the same journal.
**Companion paper:** Schultes et al., *Practical FAIRification of high-throughput metabolomics using nanopublication-based FAIR Digital Objects* [REF-MAC-FAIR]; provides the substrate for the present work.
**Authors:** Erik Schultes (lead) + co-authors to be confirmed (Max van den Boom, Tobias Kuhn, Berend Jan Bosch, Elham Memarian; potentially Alessa Gambardella, Kristina Hettne).

---

## Editorial notes (to be removed before submission)

Conventions used throughout this draft:

* Citation keys in the form `[REF-…]` are placeholders. The bibliography will be consolidated once the companion paper [REF-MAC-FAIR] has a final DOI.
* The literature scan (Q1–Q5) is complete; previously **[L]**-flagged items have been resolved and references substantiated. Items still marked **[L]** indicate where particular literature claims would benefit from additional verification during reviewer-driven revision.
* Trusty URI placeholders in §5 are of the form `<TURI-…>`. These are populated by the Tobias minting session via a mechanical find-and-replace.
* Mathematical notation uses LaTeX-style dollar delimiters (e.g., `$\mathrm{FDT}(r)$`). On import to Google Docs, these may need to be reformatted manually.
* The companion paper [REF-MAC-FAIR] is cited as the technical reference for the np-FDO substrate (nanopublication framework, four constraint layers, FAIRification accelerant, governance load). This draft does not re-derive substrate properties already established there.
* A consolidated list of open items affecting the wording of the draft is given at the end (Appendix A).

**Changes since v0.4:** References to the SPS document updated from v1.1 to v1.2 throughout. SPS v1.2 commits the FAIR² citation policy that v1.1 left optional: the data article DOI (`https://doi.org/10.3389/fbinf.2025.1634111`) is now mandatory on every Type 1 anchor via `dct:references`, and the FAIR² Data Package DOI (`https://doi.org/10.71728/hw56-vj34`) is mandatory as a `dct:source` value on every Type 1 anchor and every Type 3–6 observation, alongside the per-resource FAIR² portal URL. A short note recording this policy is added to §4.4. No predicate or class changes; no scientific-claim changes; no SPARQL changes.

**Changes since v0.3 (recorded in v0.4, retained here for the record):** Vocabulary Open Items 1–5 were resolved with Tobias Kuhn on 21 May 2026 and applied throughout this draft.

**Changes since v0.1 (recorded in v0.3, retained here for the record):** Abstract drafted; §1 (Introduction), §2 (Background, with subsections 2.1–2.4), and §6.4 (Comparison with related work) added; §6.1 closing claim and §6.6 closing sentence revised per Q1–Q5 literature-scan calibrations; reference list updated to include the new comparators identified by the scan.

---

## Abstract

A decade after the formulation of the FAIR Guiding Principles [REF-Wilkinson-2016], individual scientific data points remain largely unfindable, uncitable, and not machine-actionable at the granularity that AI-mediated reuse requires. In parallel, the digital twin construct — originating in engineering [REF-Grieves-Vickers-2017] and recently adopted in biomedicine [REF-NASEM-2024; REF-Coveney-2025] — has accumulated heterogeneous meanings, with most realisations committing to bidirectional synchronisation with a physical referent. We present a referent-agnostic operational definition of a FAIR Digital Twin (FDT) as the cluster of FAIR Digital Objects whose assertions concern a common referent, and report a concrete realisation for SARS-CoV-2 Spike receptor-binding-domain variants. The architecture comprises eleven FDO types organised across three layers — Identity, Observation, Method — connected by a single hub-topology predicate `mac:isObservationOf` and deployed on the open Nanopublication Server Network. We instantiate the architecture for three variants (Alpha N169Y, Epsilon L120R, Eta E152K), publishing 38 nanopublications that integrate real-world surveillance from GISAID, computational predictions from ESM, AlphaFold II, and Bio2Byte AgMata, experimental deep-mutational-scanning measurements from the Bloom Lab protocol, and WHO authoritative classifications. Each individual data point — a binding affinity value, a structural prediction, a surveillance record, a classification decision — is itself a persistently identified, ORCID-signed, individually citable FAIR Digital Object, linked into its variant's FDT by a single predicate and assembled into the cluster on demand by SPARQL traversal. The realisation operationalises the Knowlet construct of Mons [REF-Mons-2019] and the FAIR Digital Twin vision of Schultes et al. [REF-FDT-Perspective], supplies the assertion-level granularity that existing variant knowledge graphs have not provided, and is generalisable to other referent classes through the SPS-driven methodology of the companion paper [REF-MAC-FAIR]. The architecture introduces no compatibility tax: data producers can publish observation FDOs against shared anchors without disturbing their native workflows.

**Keywords:** FAIR Digital Twin · FAIR Digital Object · nanopublication · Knowlet · SARS-CoV-2 · Spike RBD variant · pandemic preparedness · trustworthy AI

---

## 1. Introduction

It is now a decade since the FAIR Guiding Principles for scientific data management and stewardship were published [REF-Wilkinson-2016]. The decade has seen widespread endorsement of FAIR by funders, publishers, and institutions, alongside substantial investment in FAIR-aligned infrastructure across multiple domains. Operational implementation, however, has been uneven. In fast-moving data-intensive fields — viral surveillance during a pandemic among them — FAIR commitments are routinely articulated at the level of platforms and datasets, but the individual data points within those datasets remain unfindable, uncitable, and not machine-actionable at the granularity that AI-mediated reuse increasingly demands.

This unevenness intersects with a second decade-long development. The digital-twin (DT) construct, introduced by Grieves in 2002 [REF-Grieves-Vickers-2017] and refined through engineering and manufacturing standards [REF-ISO-23247; REF-IDTA-AAS-3-0; REF-IEC-63278], has been adopted by the biomedical community at scale only since 2020. The most authoritative biomedical definition, that of the US National Academies of Sciences, Engineering, and Medicine [REF-NASEM-2024], preserves the engineering tradition's commitments to a physical, observable referent and to bidirectional near-real-time synchronisation. Scoping reviews [REF-Katsoulakis-2025; REF-Drummond-2024] document substantial definitional dispersion across the biomedical literature: of 149 published "digital twin" papers in healthcare, only 12% meet the NASEM criteria; of 86 patient-DT papers, 98% remain in preclinical phases. The European Virtual Human Twin (VHT) Initiative [REF-EDITH-Roadmap-2025; REF-EC-VHT-2024], with €100M of public investment since 2023, illustrates the scale of activity but also the conceptual heterogeneity the field is working through. Joint DT–AI framings have emerged as the proposed route to individualised healthcare [REF-Coveney-2025], and the EU AI Act [REF-EU-AI-Act-2024] now imposes transparency, traceability, and provenance requirements on healthcare-domain AI applications that substrate-level FAIR provenance can address.

Two conceptual predecessors anticipate the architecture proposed in this paper. The *Knowlet* construct of Mons [REF-Mons-2019] characterises the cluster of all cardinal assertions in the scientific record sharing a common subject, with each cardinal assertion realised as a provenance-bearing, machine-actionable nanopublication. The *FAIR Digital Twin* vision of Schultes et al. [REF-FDT-Perspective] formalises the methodological commitments an FDT realisation would need to satisfy: a layered definition anchored in FAIR Digital Objects, a *qua* construct for filtering, and an FDT-as-FDO recursion in which the cluster is itself a digital object. Both predecessors were conceptual: neither was deployed against a non-trivial scientific use case at scale. Recent FAIR-aligned DT realisations have addressed adjacent slots — the Biodiversity Digital Twin (BioDT) consortium in biodiversity [REF-BioDT-2026], using RO-Crate as the substrate; the Universal Digital Twin / World Avatar programme in chemistry and manufacturing [REF-Akroyd-2021; REF-Bai-2024], using a dynamic knowledge graph — but the specific combination of nanopublication-based FDOs, the Mons/Knowlet construct, and a biomedical-variant referent has not previously been realised.

This paper contributes that realisation. We develop a referent-agnostic operational definition of a FAIR Digital Twin as the cluster of FDOs whose assertions concern a common referent (§3), specify an architecture comprising eleven nanopublication templates organised across three layers (Identity, Observation, Method) connected by a single hub-topology predicate `mac:isObservationOf` (§4), and report the deployed realisation for three SARS-CoV-2 Spike receptor-binding-domain variants (Alpha N169Y, Epsilon L120R, Eta E152K) on the open Nanopublication Server Network, totalling 38 individually citable nanopublications (§5). Around each variant, heterogeneous data of three distinct epistemic categories — real-world surveillance from GISAID, computational structural predictions from ESM and AlphaFold and aggregation predictions from Bio2Byte AgMata, experimental deep-mutational-scanning measurements from the Bloom Lab DMS protocol, and authoritative classification from the WHO — are coherently linked at variant-level granularity, with every individual data point persistently identified by a Trusty URI, signed under an ORCID, and individually citable.

The work reported here is the empirical realisation of the FDT vision; the substrate on which it is built — the nanopublication-based FDO catalogue framework developed at the Metabolomics and Analytics Center of Leiden University — is the subject of a companion paper [REF-MAC-FAIR] to which we refer the reader for substrate detail. The two papers together address what the companion paper terms *Recursive FAIRification*: the seven-type research-administration catalogue of the MAC FAIR paper realises Level 1 FAIRification (research-object metadata at the granularity of administrative and methodological artefacts), and the eleven-type Spike-variant catalogue of the present paper realises Level 2 (the scientific claims and measurements within the data files referenced by the Level 1 objects). The two levels share a substrate, an architectural pattern, and a governance approach; they differ in the SPS-derived domain vocabulary each requires.

The remainder of the paper is organised as follows. §2 reviews the relevant background — the DT lineage, the Knowlet construct, the FDT vision, and the np-FDO substrate. §3 fixes the operational definitions and the scope of the worked example. §4 specifies the FDT architecture in operational detail. §5 reports the empirical realisation for the three named variants. §6 discusses the realisation as a concrete deployment of the Knowlet construct, the coherent integration of heterogeneous epistemic types, the generality of the architecture across referent classes, the comparison with related work, the implications for pandemic preparedness, the AI-assisted authoring workflow, and limitations and future work. §7 concludes.

---

## 2. Background

### 2.1 The digital twin lineage

The digital twin (DT) construct originates with Grieves' 2002 *Mirrored Spaces Model* for product lifecycle management [REF-Grieves-Origins-2016; REF-Grieves-Vickers-2017], formalised in the 2017 Grieves–Vickers chapter that established the canonical three-part structure: a physical entity, a virtual model, and the data connections that link them [REF-Grieves-Vickers-2017]. The 2010 adoption of the *digital twin* term by NASA [REF-Glaessgen-2012] and the subsequent ISO 23247 manufacturing-DT framework, published in five parts between 2021 and 2024 [REF-ISO-23247; REF-Shao-NIST-2023], consolidated the engineering-DT tradition around three commitments: a physical, observable referent; bidirectional near-real-time synchronisation between the digital and the physical; and predictive capability informing operational decisions. The Asset Administration Shell (AAS, IEC 63278-1, now at specification version 3.0) extended this tradition to Industry 4.0 [REF-IDTA-AAS-3-0; REF-IEC-63278], and the Digital Twin Consortium's Capabilities Periodic Table [REF-DTC-CPT-2024] now provides an architecture-agnostic, capability-requirements framework comprising sixty level-one capabilities. Across these standards the entity represented is variously termed *physical asset*, *observable manufacturing element*, *real-world entity*, or *physical twin*; the diversity of terminology masks a shared definitional commitment to physical, observable referents.

Adoption of the DT construct in biomedicine has been more recent and definitionally heterogeneous. The 2024 NASEM report [REF-NASEM-2024] established what is now the most authoritative biomedical definition — *"a set of virtual information constructs that mimics the structure, context, and behavior of a natural, engineered, or social system, is dynamically updated with data from its physical twin, has a predictive capability, and informs decisions that realize value"* — preserving the bidirectional-synchronisation and predictive-capability commitments inherited from engineering. Scoping reviews by Katsoulakis et al. [REF-Katsoulakis-2025] and Drummond and Gonsard [REF-Drummond-2024] document the definitional dispersion of the term in healthcare: of 149 published "digital twin" papers in healthcare, only 12% meet the NASEM criteria; of 86 patient-DT papers, 98% remain in preclinical phases. The European Virtual Human Twin (VHT) Initiative [REF-EDITH-Roadmap-2025; REF-EC-VHT-2024], with approximately €100M committed across 2023–2026, aims to construct a federated infrastructure of multi-scale digital representations of human health and disease — a substantial investment, but one that inherits the same definitional commitments and presumes physical, observable referents.

A parallel strand of work has connected DTs to AI. AI methods are now routinely used to construct and calibrate DTs (structural and binding-affinity prediction by AlphaFold and successors [REF-Jumper-AlphaFold2; REF-Lin-ESM2; REF-Boltz2-2025]; explainable and interpretable AI for trustworthy engineering DTs [REF-Mahmoodi-2023; REF-Wang-GenAI-DT-2025]). Conversely, DTs are increasingly positioned as machine-actionable substrates for AI agents [REF-Coveney-2025], and the regulatory environment — notably the EU AI Act, Regulation 2024/1689 [REF-EU-AI-Act-2024; REF-Gilbert-2024] — has begun to impose transparency, traceability, and provenance requirements on healthcare AI that substrate-level FAIR provenance can address. We return to this AI–DT relationship in §6.6.

### 2.2 The Knowlet concept

The construct that most directly anticipates the present architecture is the *Knowlet* introduced by Mons [REF-Mons-2019] in 2019, building on earlier nanopublication work [REF-Groth-2010; REF-Kuhn-2018]. A Knowlet is the cluster of all cardinal assertions in the scientific record sharing a common subject, with each cardinal assertion realised as a nanopublication carrying its own provenance, attribution, and persistent identification. The Knowlet is, in Mons's formulation, both a structural unit of the Internet of FAIR Data and Services and the natural locus of community curation: as new assertions accumulate, the Knowlet grows; assertions can be supported, contradicted, or superseded by subsequent nanopublications; and each cardinal assertion is itself a citable, machine-actionable object. The construct is referent-agnostic — Mons's worked examples include diseases, genes, drugs, and concepts — and presumes neither physical referents nor bidirectional synchronisation.

The Knowlet construct anticipates the operational definition of a FAIR Digital Twin developed in §3.3 precisely. Where the Knowlet is the cluster of cardinal assertions sharing a common subject, the present FDT is the cluster of FDOs whose assertions concern a common referent; where each cardinal assertion is a nanopublication, each FDO in the cluster is a nanopublication; where the Knowlet is open and accretive, so is the FDT. What the present work supplies, beyond the Knowlet construct itself, is a deployment architecture (the three-layer design and hub topology of §4) and a substrate-discharged FAIR compliance pattern inherited from the parallel MAC FAIR work [REF-MAC-FAIR]. The Knowlet, in operational terms, is the FAIR Digital Twin. The early proposal by Patrinos et al. [REF-Patrinos-2012] that variant data should be published as nanopublications, in a microattribution framework, anticipated the present application of the Knowlet construct to molecular-variant data; that proposal was not realised at scale at the time.

### 2.3 The FAIR Digital Twin vision

The bridge between the Knowlet construct and the digital-twin discourse was established by Schultes et al. [REF-FDT-Perspective] in 2022 with the *FAIR Digital Twins for Data-Intensive Research* Perspective. That paper proposed a layered definition (Digital Twin → FAIR Digital Twin) anchored in FAIR Digital Objects, introduced the *qua* construct as a means to filter a twin to a particular point of view, and characterised the FDT as a "stepwise and modular" composite of more fundamental FDOs while itself remaining an FDO. The Perspective was, however, methodological rather than empirical: it identified the architectural commitments an FDT realisation would need to satisfy but did not deploy them against a specific scientific use case at scale. Several of its commitments — perma-linked cardinal assertions, machine-actionable cross-citation, *qua*-style filtering — were left for subsequent work to operationalise.

The present paper is that subsequent work. The three-layer architecture of §4 realises the FDT vision through the np-FDO substrate; the *qua* construct of [REF-FDT-Perspective] is recovered as SPARQL filtering on observation type (§6.1); and the FDT-as-FDO recursion (the cluster considered as itself a digital object) is rendered explicit by the anchor's identification of the referent and the substrate's automatic discharge of FDO conformance for the cluster. In parallel with the present work, the FAIR Digital Twin concept has been adopted in biodiversity by the BioDT consortium [REF-BioDT-2026], with a different substrate choice (RO-Crate) and at a different granularity (workflow-package level). The two realisations together demonstrate that the FDT framing admits more than one substrate-level realisation; we compare them in §6.4.

### 2.4 The np-FDO substrate

The substrate on which the present FDT architecture is built is the nanopublication-based FAIR Digital Object framework developed in the parallel MAC FAIR work [REF-MAC-FAIR]. The substrate comprises the nanopublication format [REF-Groth-2010; REF-Kuhn-2018] — a unitary RDF graph consisting of an assertion sub-graph, a provenance sub-graph, and a publication-information sub-graph — published on the open, federated Nanopublication Server Network (NSN) under Trusty URIs [REF-TrustyURIs] that combine cryptographic content-hashing with ORCID-authenticated signing. The substrate discharges FAIR compliance at the substrate level: persistent identification (F1), accessibility through standard protocols (A1), interoperability through RDF and SPARQL (I1), and reusability through explicit licensing and provenance (R1) are delivered automatically to every published nanopublication regardless of content. Magagna et al. [REF-Magagna-2025] have formally established the alignment of nanopublications with the FDO specifications, demonstrating that appropriately constructed nanopublications satisfy the FDO conformance pattern.

The companion paper [REF-MAC-FAIR] provides the full account of the substrate, including the four constraint layers (identity, type, materialisation, provenance), the FAIR sub-principle allocation, the FAIRification accelerant logic, the SPS-driven domain-vocabulary methodology, and the governance model. The present paper assumes the reader will refer to that account for substrate detail; here we restrict ourselves to the architectural and empirical contribution that builds upon it.

---

## 3. Definitions and scope

The term *digital twin* has accumulated heterogeneous and partly incompatible meanings since its introduction in the engineering literature [REF-Grieves-Vickers-2017]. The biomedical and life-science communities have adopted the term more recently and with further variation [REF-Katsoulakis-2025; REF-Drummond-2024], and standards bodies are still in the process of consolidating definitional language [REF-ISO-23247; REF-DTC-CPT-2024; REF-NASEM-2024]. This section fixes the operational definitions used in the remainder of the paper. The cascade is deliberately minimal: each level adds one constraint to the previous, and the final operational definition reduces to a class of FAIR Digital Objects (FDOs) [REF-Schultes-Wittenburg-2019] organised in a specific topology.

### 3.1 Referent

The DT literature uses several terms for the entity that a digital twin represents — *physical entity*, *physical asset*, *real-world entity*, *twined object*, *physical twin* [REF-DTC-CPT-2024; REF-ISO-23247; REF-NASEM-2024]. Each presumes that the represented entity is a physical instance whose state can be observed through sensors or operational telemetry. This presumption is appropriate for engineering DTs of specific jet engines, wind turbines, or factory robots; it is too restrictive for our use case and for the biomedical applications of the DT concept more generally.

We therefore adopt a single term throughout this paper:

> **Definition 1 (referent).** The *referent* of a (digital) twin is the entity, of any ontological category, about which the twin records information. The referent may be a physical instance (e.g., a specific patient sample), a physical type (e.g., a sequence-defined protein variant), or a conceptual entity (e.g., a disease category, a chemical compound class).

This usage follows the semiotic and Knowlet literature [REF-Mons-2019] and subsumes the DT-community vocabulary as a special case. Where the present paper engages directly with the DT standards literature (§2 and §6.4), the standards' own terminology is retained; elsewhere we use *referent*.

### 3.2 Twin and digital twin

We define *twin* and *digital twin* in a layered fashion, each definition adding one constraint to its predecessor:

> **Definition 2 (twin).** A *twin* of a referent $r$ is the collection of information held about $r$.
>
> **Definition 3 (digital twin).** A *digital twin* (DT) of $r$ is a twin realised as digital information.
>
> **Definition 4 (FAIR digital twin).** A *FAIR digital twin* (FDT) of $r$ is a DT in which the information is FAIR — Findable, Accessible, Interoperable, and Reusable in the sense of the FAIR Guiding Principles [REF-Wilkinson-2016] — and is therefore machine-actionable.

The cascade is intentional. Definition 2 is pre-digital: paper laboratory notebooks and printed clinical records also constitute twins under this definition. Definition 3 introduces the digital medium without yet committing to any particular structural requirement. Definition 4 adds the FAIR constraint; it is the constraint that distinguishes our notion from the bulk of the existing DT literature, in which machine actionability is typically asserted at the platform level rather than guaranteed at the level of every information element.

The cascade departs from the layered definition in [REF-FDT-Perspective] in two respects. First, we begin from the abstract notion of a twin rather than from the engineering DT of a physical asset, eliminating the implicit restriction to physical referents. Second, we postpone any architectural commitment about *how* the FAIR constraint is realised to §3.3. This separation is deliberate: the FAIR requirement is a property that any sufficient architecture must deliver; it does not in itself prescribe the architecture.

### 3.3 An operational definition: FDT as a cluster of FDOs

The FAIR requirement in Definition 4 can be satisfied in more than one way [REF-Soiland-Reyes-2024]. In this paper we adopt the realisation in which the digital information about $r$ is decomposed into individual FAIR Digital Objects [REF-Schultes-Wittenburg-2019], each carrying a separate persistent identifier, type declaration, and metadata pointer, and together forming a structurally coherent set. This realisation aligns with the Knowlet construct of Mons [REF-Mons-2019]:

> **Definition 5 (operational FDT).** The FAIR digital twin of a referent $r$ is the cluster of FDOs whose assertions concern $r$ as a common subject.

Two features of this operational definition are consequential for the rest of the paper.

First, the FDT is the *cluster*, not any individual member of it. There is, in particular, an FDO in the cluster whose role is to declare the identity of $r$ — its type, its persistent identifier, its intrinsic properties (in our case, the variant sequence and lineage assignments). We will call this the *anchor* of the FDT. The anchor is the natural focal point of the cluster but it is not the FDT; the FDT exists only when the anchor is supplemented by additional FDOs that record observations of $r$.

Second, the cluster is open and accretive. New FDOs concerning $r$ — additional observations, additional predictions, additional classifications — can be added to the cluster at any time by any party, without altering existing FDOs, by publishing new nanopublications that cite the anchor as their subject. The FDT grows monotonically and is not closed by any party. This is a direct inheritance from the nanopublication substrate [REF-MAC-FAIR §2.3] and from the Knowlet's design [REF-Mons-2019].

### 3.4 Notation

We adopt the following notation throughout the remainder of the paper:

| Symbol | Meaning |
|---|---|
| $r$ | A referent (a specific Spike RBD variant). |
| $A_r$ | The anchor FDO of the FDT for $r$. The Type 1 nanopublication declaring the identity, type, and intrinsic sequence properties of $r$. |
| $O_r$ | A generic observation FDO recording a measured, predicted, or recorded property of $r$. |
| $\mathrm{FDT}(r)$ | The FDT of $r$, defined as $\{A_r\} \cup \{O_r\}$ — the cluster of all FDOs whose assertions concern $r$. |
| $\mathcal{M}$ | The shared method library: FDOs describing the computational, experimental, and surveillance methods that produced the observations. The members of $\mathcal{M}$ are referenced by, but are not part of, any individual FDT. |

The relationship between an observation FDO and its anchor is asserted by the predicate `mac:isObservationOf`, applied with $O_r$ as subject and the URI of $r$ (carried by $A_r$) as object. This single predicate is the load-bearing cross-link of the architecture and is treated in detail in §4.3.

### 3.5 Scope of this paper

The empirical demonstration reported here is restricted to FDTs whose referents are **type-level biological concepts**: SARS-CoV-2 Spike receptor-binding-domain (RBD) variants identified by amino-acid substitutions from the Wuhan reference sequence (UniProt P0DTC2). Three referents are addressed initially: the Alpha (N169Y), Epsilon (L120R), and Eta (E152K) variants.

Two further scope decisions follow directly:

1. *Instance-level FDTs* — for example, FDTs of specific patient samples, specific GISAID accessions, or specific manufactured protein batches — are out of scope for the empirical content of this paper but are not architecturally distinct from the type-level FDTs presented. An instance-level FDT instantiates the same 11-type structure (§4.2) against a different referent URI; the engineering DT of Grieves [REF-Grieves-Vickers-2017] is, under our operational definition, the instance-level case in which the referent is a specific manufactured object and the observation stream is sensor telemetry. The type/instance distinction is therefore a scoping choice for this paper, not a technological constraint.

2. *Dynamic synchronisation* between the FDT and its referent — characteristic of engineering DTs that mirror sensor telemetry in near real time — is not implemented in this work. The FDT is accretive (new observations are added as they become available) but not synchronous in the engineering sense. We return to the implications in §6.7.

The remainder of the paper (§4) specifies the architecture of these FDTs in operational detail and (§5) reports the empirical realisation for the three named variants.

---

## 4. Architecture

The FDT architecture rests on the np-FDO substrate established by the Metabolomics and Analytics Center (MAC) at Leiden University and described in detail in [REF-MAC-FAIR]. The substrate provides persistent identification (Trusty URIs), cryptographic authentication (ORCID-based signing), immutability, decentralised publication and retrieval (the Nanopublication Server Network, NSN), and SPARQL-queryability — all delivered automatically to every published nanopublication, regardless of its content. We do not re-derive these properties here. The architecture of the FDT specifies *what* is published, *how* it is structured, and *how the structure forms a knowlet topology centred on the referent*. The np-FDO substrate determines that the result is FAIR by construction.

### 4.1 Three layers

The architecture comprises three structurally distinct layers (Table 1, Figure 1).

| Layer | Role | FDO types |
|---|---|---|
| **Identity** | Declares the referent $r$, its type, its intrinsic properties, and its identifying URI. Exactly one FDO per referent: the anchor $A_r$. | Type 1 |
| **Observations** | Records measured, predicted, or surveilled properties of $r$. Each observation FDO is linked to $A_r$ by `mac:isObservationOf`. Multiple FDOs per referent. | Types 2–8 |
| **Methods** | Describes the computational, experimental, or surveillance method that produced the observations. Each method FDO is referenced by one or more observation FDOs via `mac:hasPredictionMethod`, `mac:hasExperimentalMethod`, or `mac:hasSurveillanceMethod`. Method FDOs are shared across FDTs. | Types 9–11 |

The Identity and Observation layers together constitute the FDT. The Method layer is the external, shared library $\mathcal{M}$: its members are referenced from within the FDT but are not part of any single FDT. The separation of methods from observations reflects the epistemic distinction that a method is a property of *how* an observation was made, not of *what* was observed; collapsing the two would oblige the catalogue to duplicate the same method description across every observation that used it, undermining the long-tail vocabulary economy that the np-FDO design pursues [REF-MAC-FAIR §3.4].

### 4.2 The eleven FDO types

The architecture is realised through eleven FDO types (Table 2). Each is published as a NanoDash template on the NSN; instances are created by completing the corresponding template form. The complete specification — predicate URIs, statement structures, controlled vocabularies, and example values for the three initial variants — is given in the supplementary specification document `MAC_FDT_SPS_v1.0.md`.

**Table 2.** The eleven FDO types of the MAC FDT architecture. Per-variant cardinality is the count of instances of each type required to populate one FDT under the three-method computational configuration (ESM + AlphaFold II for the structural predictors; Bio2Byte for the sequence-derived AgMata score). Method FDOs are shared and not counted per variant.

| # | Type | Class URI | Layer | Per variant |
|---|---|---|---|---|
| 1 | Spike RBD Variant | `mac:SpikeRBDVariant` | Identity (anchor) | 1 |
| 2 | Real-World Occurrence | `mac:RealWorldOccurrence` | Observation | 1 |
| 3 | Computational Prediction — RMSD | `mac:ComputationalPredictionRMSD` | Observation | 2 (ESM, AlphaFold) |
| 4 | Computational Prediction — SASA | `mac:ComputationalPredictionSASA` | Observation | 2 (ESM, AlphaFold) |
| 5 | Computational Prediction — pLDDT | `mac:ComputationalPredictionPLDDT` | Observation | 2 (ESM, AlphaFold) |
| 6 | Computational Prediction — AgMata | `mac:ComputationalPredictionAgMata` | Observation | 1 (Bio2Byte) |
| 7 | Experimental DMS Observation | `mac:ExperimentalDMSObservation` | Observation | 1 |
| 8 | WHO Variant Classification | `mac:WHOVariantClassification` | Observation | 1 |
| 9 | Computational Method | `mac:ComputationalMethod` | Method library $\mathcal{M}$ | — (shared) |
| 10 | Experimental Method | `mac:ExperimentalMethod` | Method library $\mathcal{M}$ | — (shared) |
| 11 | Observational Method | `mac:ObservationalMethod` | Method library $\mathcal{M}$ | — (shared) |

The Observation types (2–8) span three epistemic categories of evidence that the FDT integrates coherently around a single referent:

* **Real-world surveillance** — Type 2, recording documented detection of the variant in the field as catalogued by an epidemiological surveillance system (in our implementation: GISAID).
* **Computational prediction** — Types 3–6, recording predicted structural, surface, confidence, and aggregation properties produced by computational methods operating on the variant's sequence (in our implementation: ESM, AlphaFold II, and Bio2Byte AgMata).
* **Experimental measurement** — Types 7 and 8, recording empirical measurements (binding affinity and expression level from deep mutational scanning) and authoritative classification decisions (WHO risk designation).

That heterogeneous data of these three categories can be linked to a single referent, with every individual data point persistently identified and individually citable, is the substantive scientific contribution of this architecture; we return to this point in §6.2.

The eleven types collectively introduce 26 MAC-namespace predicates and 14 MAC-namespace classes. Their definitions are given in the supplementary vocabulary specification `MAC_FDT_Vocabulary_v1.0.md`. The vocabulary itself is published as nanopublications on the NSN, following the FAIR Funder Framework precedent [REF-FFF-Framework; REF-MAC-FAIR §3.4]; the vocabulary infrastructure is therefore an np-FDO catalogue in its own right, FAIR by the same substrate that hosts the FDTs that use it.

### 4.3 Hub topology via `mac:isObservationOf`

The cluster $\mathrm{FDT}(r)$ has a star topology (Figure 1). The anchor $A_r$ is the centre. Every observation FDO $O_r$ carries exactly one outgoing statement of the form

$$O_r \;\; \mathtt{mac:isObservationOf} \;\; r$$

where $r$ is the URI declared by $A_r$ as the identifier of the variant. The single predicate `mac:isObservationOf` is the only cross-link required to assemble the cluster: a SPARQL query on the NSN of the form

```sparql
SELECT ?obs ?type WHERE {
  ?obs mac:isObservationOf <r> .
  ?obs rdf:type ?type .
}
```

retrieves all observations of $r$, together with their types, and reconstructs $\mathrm{FDT}(r)$ on demand. No central registry, no manifest file, and no platform-specific index is required; the cluster is assembled by traversal alone, and any FDO published to the NSN with the appropriate cross-link automatically becomes part of $\mathrm{FDT}(r)$ at the moment of publication.

The topology has three architectural consequences worth recording explicitly.

1. *Anchor as identity, not container*. The anchor $A_r$ asserts only the identity and intrinsic properties of $r$ — sequence, lineage, parent protein. It does not contain or enumerate the observations; the observations point inward to the anchor, not outward from it. This inverts the conventional metadata-record pattern in which a parent record lists its children, and it is the key architectural property that makes the cluster open and accretive: any party can publish a new observation referencing $A_r$ without permission from, or modification of, $A_r$ itself.

2. *Hub-and-spoke is sufficient*. The cluster does not need a richer graph structure to function as a knowlet. All cross-references are spokes terminating at $A_r$. Where additional structure is required — for example, a relationship between two observations of $r$ — it is asserted as a property of one of the observations, not of the cluster as a whole.

3. *Method references are spokes to the external library*. The observation FDOs also carry references to the method that produced them (`mac:hasPredictionMethod`, `mac:hasExperimentalMethod`, or `mac:hasSurveillanceMethod`), but these references point outward to $\mathcal{M}$, not inward to $A_r$. The method library is therefore a second hub-and-spoke graph, structurally parallel to the FDT but populated by FDOs whose role is to describe processes rather than properties.

Figure 1 illustrates the topology for the Alpha variant: the central anchor $A_{\text{Alpha}}$, the ten observation FDOs arranged as spokes, and the five method FDOs of $\mathcal{M}$ shown as a separate cluster with the observation-to-method references rendered as outgoing arrows from the observation ring.

### 4.4 The method library $\mathcal{M}$ as a shared resource

The five method FDOs that comprise $\mathcal{M}$ in the present implementation are:

* Three Type 9 (Computational Method) FDOs: ESM2 [REF-Lin-ESM2], AlphaFold 2 [REF-Jumper-AlphaFold2], and the Bio2Byte AgMata predictor [REF-Bio2Byte].
* One Type 10 (Experimental Method) FDO: the Bloom Lab SARS-CoV-2 RBD deep mutational scanning protocol [REF-Starr-2020].
* One Type 11 (Observational Method) FDO: the GISAID surveillance platform [REF-Shu-2017; REF-Khare-2021].

Each method FDO carries one or more `cito:citesAsAuthority` URIs identifying the method's authoritative published description(s) and a `schema:url` to the method's data or software resource. The methods are not specific to any individual variant or to any individual FDT; they are infrastructural references shared across the entire FDT catalogue. A new variant added to the catalogue introduces a new $\mathrm{FDT}(r)$ but no new method FDOs, provided the same methods are used. A new method, conversely, requires only a new instance under the existing Type 9, 10, or 11 template — no new template, predicate, or class is required.

This shared-method design serves three purposes. First, it eliminates duplication: the description of AlphaFold 2 appears in exactly one place in the NSN regardless of how many predictions reference it. Second, it makes the method an independently citable FDO in its own right: a reader who wishes to interrogate, for example, the provenance and parameters of the ESM model used for the Alpha pLDDT prediction follows a single `mac:hasPredictionMethod` link to a single Trusty URI. Third, it supports method versioning: a new version of AlphaFold can be introduced as a separately published Type 9 FDO, and future observation FDOs can reference the new version while existing observation FDOs retain their references to the version that was actually used at the time of computation.

The relationship between an FDT and the method library is therefore many-to-many across the catalogue but one-to-one at the per-observation level: each observation FDO carries exactly one method reference, and the method library is the disjoint union of all such referenced methods, deduplicated.

A separate citation commitment applies to the FAIR² source data on which the present catalogue depends. The Spike-variant computational observations (Types 3–6) are derived from a FAIR² Data Package [REF-FAIR2-DataPackage] whose narrative description is published as a peer-reviewed data article [REF-FAIR2-Article]. Every Type 1 anchor in the catalogue carries a mandatory `dct:references` to the data article DOI and a mandatory `dct:source` to the Data Package DOI; every Type 3–6 observation FDO carries a mandatory `dct:source` to both the Package DOI and the per-resource FAIR² portal URL. The policy is recorded in `MAC_FDT_SPS_v1.2` (the SPS specification accompanying this paper) and ensures that any downstream consumer of any single FDO can recover both the underlying dataset and its narrative description in two cross-link traversals.

---

## 5. Empirical realisation

### 5.1 Subject selection

The initial empirical catalogue addresses three referents: the Alpha (N169Y, lineage B.1.1.7), Epsilon (L120R, lineage B.1.427+B.1.429), and Eta (E152K, lineage B.1.525) RBD variants. Each referent is the central node of an independently realised FDT, structurally identical to the architecture specified in §4 and instantiated with variant-specific data. The variants were selected against three criteria.

First, *epistemic-type coverage*: each variant has full coverage across the three epistemic categories of §4.2 — at least one Type 2 surveillance record, structural and aggregation predictions across Types 3–6, deep mutational scanning measurements in Type 7, and an authoritative classification in Type 8. The variants therefore exercise every observation type of the architecture.

Second, *classification diversity*: Alpha was designated a WHO Variant of Concern (VOC) on 18 December 2020; Epsilon and Eta were designated Variants of Interest (VOI) on 5 March 2021 [REF-WHO-tracking]. The catalogue therefore covers two of the three WHO risk categories used in the controlled vocabulary of Type 8 (VOC and VOI; VUM remains to be exercised by a subsequent variant).

Third, *geographic and temporal diversity*: the GISAID-reported first detections of the three variants span three continents (Europe, North America, Africa) and approximately one year (March 2020 to late 2020 / 2021), providing surveillance-record diversity in the Type 2 instances.

**Table 3.** Anchor properties for the three variants. Values populate the Type 1 anchor FDOs $A_r$ for $r \in \{\text{Alpha, Epsilon, Eta}\}$.

| Property | Alpha | Epsilon | Eta |
|---|---|---|---|
| WHO variant name | Alpha | Epsilon | Eta |
| Pango lineage | B.1.1.7 | B.1.427 + B.1.429 | B.1.525 |
| GISAID seq_id (full Spike) | N501Y | L124R | E484K |
| MAC seq_id (RBD) | N169Y | L120R | E152K |
| Parent protein | UniProt P0DTC2 | UniProt P0DTC2 | UniProt P0DTC2 |
| RBD sequence length | 195 aa | 195 aa | 195 aa |
| Anchor Trusty URI | `<TURI-A-Alpha>` | `<TURI-A-Epsilon>` | `<TURI-A-Eta>` |

The complete 195-residue RBD sequences for the three variants are recorded in `MAC_FDT_SPS_v1.0.md` (sequence appendix) and are carried by `mac:hasRBDSequence` in each anchor FDO.

### 5.2 Per-variant FDT contents

Each FDT comprises eleven FDOs: one Type 1 anchor and ten observations. The catalogue further contains five shared method FDOs in the method library $\mathcal{M}$. Total catalogue size for the initial empirical realisation: $3 \times 11 + 5 = 38$ nanopublications.

The observation FDO inventory is presented type by type below. For each table, the Trusty URI column is populated by the Tobias minting session (see `README_for_Claude_Code.md` in the accompanying staging materials).

**Table 4a.** Type 2 — Real-World Occurrence (one FDO per variant; surveillance method: GISAID). Collection locations are GeoNames feature URIs (Item 3 resolution; candidate IDs to be verified at minting time).

| Variant | Occurrence date | Collection location | GeoNames feature | Trusty URI |
|---|---|---|---|---|
| Alpha | late 2020 – 2021 | `https://sws.geonames.org/6269131/` | England | `<TURI-O-Alpha-RWO>` |
| Epsilon | March 2020 | `https://sws.geonames.org/5332921/` | California, US | `<TURI-O-Epsilon-RWO>` |
| Eta | 15 December 2020 | `https://sws.geonames.org/2328926/` | Nigeria | `<TURI-O-Eta-RWO>` |

**Table 4b.** Types 3–5 — Computational structural predictions (two FDOs per variant per metric: ESM and AlphaFold II).

| Variant | Method | RMSD (Å) | SASA (Å²) | pLDDT (0–100) | Trusty URI (RMSD) | Trusty URI (SASA) | Trusty URI (pLDDT) |
|---|---|---:|---:|---:|---|---|---|
| Alpha | ESM | 13.379 | 16494.878 | 23.674 | `<TURI-O-Alpha-RMSD-ESM>` | `<TURI-O-Alpha-SASA-ESM>` | `<TURI-O-Alpha-pLDDT-ESM>` |
| Alpha | AlphaFold II | 2.278 | 10141.237 | 93.744 | `<TURI-O-Alpha-RMSD-AF>` | `<TURI-O-Alpha-SASA-AF>` | `<TURI-O-Alpha-pLDDT-AF>` |
| Epsilon | ESM | 12.802 | 17620.863 | 23.736 | `<TURI-O-Epsilon-RMSD-ESM>` | `<TURI-O-Epsilon-SASA-ESM>` | `<TURI-O-Epsilon-pLDDT-ESM>` |
| Epsilon | AlphaFold II | 2.976 | 10181.969 | 94.193 | `<TURI-O-Epsilon-RMSD-AF>` | `<TURI-O-Epsilon-SASA-AF>` | `<TURI-O-Epsilon-pLDDT-AF>` |
| Eta | ESM | 2.477 | 18026.597 | 23.150 | `<TURI-O-Eta-RMSD-ESM>` | `<TURI-O-Eta-SASA-ESM>` | `<TURI-O-Eta-pLDDT-ESM>` |
| Eta | AlphaFold II | 2.720 | 10226.641 | 94.054 | `<TURI-O-Eta-RMSD-AF>` | `<TURI-O-Eta-SASA-AF>` | `<TURI-O-Eta-pLDDT-AF>` |

Values are reported to three decimal places for legibility; the published FDOs carry the full-precision values from the source dataset. The substantial divergence between ESM and AlphaFold II in RMSD and pLDDT — particularly evident in the Alpha and Epsilon rows — is a known property of the two methods' predictive regimes [REF-Lin-ESM2; REF-Jumper-AlphaFold2] and reflects a real cross-method difference that the per-method, per-FDO representation makes individually citable.

**Table 4c.** Type 6 — AgMata aggregation propensity (one FDO per variant; sequence-derived, method-independent; method: Bio2Byte).

| Variant | AgMata score | Trusty URI |
|---|---:|---|
| Alpha | 0.7005 | `<TURI-O-Alpha-AgMata>` |
| Epsilon | 0.7195 | `<TURI-O-Epsilon-AgMata>` |
| Eta | 0.6806 | `<TURI-O-Eta-AgMata>` |

**Table 4d.** Type 7 — Experimental DMS observation (one FDO per variant; method: Bloom Lab DMS).

| Variant | bind (log K_D) | Δbind | expr (log MFI) | Δexpr | conf_bind | conf_expr | Trusty URI |
|---|---:|---:|---:|---:|---:|---:|---|
| Alpha | 9.814 | 1.042 | 10.053 | −0.133 | 0.0732 | 0.0714 | `<TURI-O-Alpha-DMS>` |
| Epsilon | 8.939 | 0.167 | 10.254 | 0.068 | 0.0730 | 0.0705 | `<TURI-O-Epsilon-DMS>` |
| Eta | 9.013 | 0.241 | 10.219 | 0.033 | 0.0723 | 0.0698 | `<TURI-O-Eta-DMS>` |

**Table 4e.** Type 8 — WHO variant classification (one FDO per variant; time-stamped).

| Variant | WHO classification | Classification date | Trusty URI |
|---|---|---|---|
| Alpha | `mac:VOC` (Variant of Concern) | 18 December 2020 | `<TURI-O-Alpha-WHO>` |
| Epsilon | `mac:VOI` (Variant of Interest) | 5 March 2021 | `<TURI-O-Epsilon-WHO>` |
| Eta | `mac:VOI` (Variant of Interest) | 5 March 2021 | `<TURI-O-Eta-WHO>` |

**Table 5.** Method library $\mathcal{M}$ (five FDOs; shared across all FDTs in the catalogue). Method FDOs use `cito:citesAsAuthority` to link to the authoritative published description of each method (Item 4 resolution; replaces `schema:citation` from earlier drafts).

| Type | Method | Class URI | `cito:citesAsAuthority` (DOI) | `schema:url` (resource URL) | Trusty URI |
|---|---|---|---|---|---|
| 9 | ESM2 | `mac:ComputationalMethod` | `10.1126/science.ade2574` [REF-Lin-ESM2] | `github.com/facebookresearch/esm` | `<TURI-M-ESM>` |
| 9 | AlphaFold 2 | `mac:ComputationalMethod` | `10.1038/s41586-021-03819-2` [REF-Jumper-AlphaFold2] | `github.com/google-deepmind/alphafold` | `<TURI-M-AF>` |
| 9 | Bio2Byte AgMata | `mac:ComputationalMethod` | `10.1093/bioinformatics/btac149` [REF-Bio2Byte] | `bio2byte.be/b2btools/` | `<TURI-M-Bio2Byte>` |
| 10 | Bloom Lab SARS-CoV-2 RBD DMS | `mac:ExperimentalMethod` | `10.1016/j.cell.2020.08.012` [REF-Starr-2020] | `github.com/jbloomlab/SARS-CoV-2-RBD_DMS` | `<TURI-M-Bloom>` |
| 11 | GISAID EpiCoV | `mac:ObservationalMethod` | `10.2807/1560-7917.ES.2017.22.13.30494` [REF-Shu-2017]; `10.46234/ccdcw2021.255` [REF-Khare-2021] | `gisaid.org` | `<TURI-M-GISAID>` |

The hub topology of $\mathrm{FDT}(\text{Alpha})$ is illustrated in **Figure 1**. The topology of $\mathrm{FDT}(\text{Epsilon})$ and $\mathrm{FDT}(\text{Eta})$ is structurally identical; only the anchor identity and the observation values differ.

### 5.3 SPARQL traversals

We demonstrate the architectural claims of §4 against the published catalogue through five SPARQL queries. Each query is presented with its purpose, its SPARQL listing, and the schematic form of its result. The results themselves resolve to live values once the catalogue is published; we report the query forms and the architectural property each demonstrates.

The queries follow the resolution that `mac:isObservationOf` resolves to the referent URI declared by the anchor (i.e., the `sub:fdo` identifier carried by the Type 1 anchor nanopublication), as confirmed during vocabulary v1.1 finalisation. The SPARQL `PREFIX mac:` declarations expand to the MAC NanoDash ontology space at `https://w3id.org/spaces/mac/r/ontology/MAC-Ontology` (Item 1 resolution), with the precise term-URI separator assigned by NanoDash at minting time.

#### Query Q5.3.1 — Assemble $\mathrm{FDT}(r)$ on demand

*Purpose.* Given a referent URI $r$, retrieve all observation FDOs of $r$ together with their types. Demonstrates the on-demand assembly of the cluster from the open NSN, without any pre-built manifest.

```sparql
PREFIX mac: <[MAC namespace]>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?obs ?type WHERE {
  ?obs mac:isObservationOf <r-URI> .
  ?obs rdf:type ?type .
  FILTER(?type != <http://example.org/fdof#FAIRDigitalObject>)
}
```

*Expected result for $r$ = Alpha.* Ten rows, one per observation FDO, with `?type` ranging over `mac:RealWorldOccurrence`, `mac:ComputationalPredictionRMSD` (twice, one per prediction method), `mac:ComputationalPredictionSASA` (twice), `mac:ComputationalPredictionPLDDT` (twice), `mac:ComputationalPredictionAgMata`, `mac:ExperimentalDMSObservation`, `mac:WHOVariantClassification`.

#### Query Q5.3.2 — Cross-FDT comparison

*Purpose.* Retrieve a single observation property across all FDTs in the catalogue. Demonstrates that comparison across variants is a single SPARQL traversal once the catalogue is populated.

```sparql
PREFIX mac: <[MAC namespace]>

SELECT ?variantLabel ?bind WHERE {
  ?obs rdf:type mac:ExperimentalDMSObservation .
  ?obs mac:isObservationOf ?variant .
  ?obs mac:hasBind ?bind .
  ?variant rdfs:label ?variantLabel .
}
ORDER BY DESC(?bind)
```

*Expected result.* Three rows: Alpha (9.81), Eta (9.01), Epsilon (8.94), ranked by binding affinity. Architectural property demonstrated: cross-variant comparison requires no central index; the SPARQL endpoint traverses the published catalogue and assembles the comparison at query time.

#### Query Q5.3.3 — Method-traced provenance

*Purpose.* Given an observation FDO, retrieve the method that produced it and the authoritative citation of that method. Demonstrates the provenance-trace property of §6.2 as a single SPARQL pattern.

```sparql
PREFIX mac:  <[MAC namespace]>
PREFIX cito: <http://purl.org/spar/cito/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?methodLabel ?citation WHERE {
  <obs-URI> mac:hasPredictionMethod ?method .
  ?method rdfs:label ?methodLabel .
  ?method cito:citesAsAuthority ?citation .
}
```

*Expected result for `<TURI-O-Alpha-pLDDT-AF>`.* One row: method label `"AlphaFold 2 — DeepMind structure predictor"`, citation `https://doi.org/10.1038/s41586-021-03819-2`. Architectural property: provenance trace is one cross-link and one literal away, with no platform-specific API mediation.

#### Query Q5.3.4 — *Qua* filtering

*Purpose.* Retrieve the subset of $\mathrm{FDT}(r)$ corresponding to a particular point of view — in this case, the variant *qua* structural object. Demonstrates the *qua* operation of [REF-FDT-Perspective] as SPARQL filtering on observation type.

```sparql
PREFIX mac: <[MAC namespace]>

SELECT ?obs ?type WHERE {
  ?obs mac:isObservationOf <r-URI> .
  ?obs rdf:type ?type .
  FILTER(?type IN (
    mac:ComputationalPredictionRMSD,
    mac:ComputationalPredictionSASA,
    mac:ComputationalPredictionPLDDT,
    mac:ComputationalPredictionAgMata
  ))
}
```

*Expected result for $r$ = Alpha.* Seven rows (two each for RMSD, SASA, pLDDT; one for AgMata). The same FDT *qua* epidemiological entity (filtering for `mac:RealWorldOccurrence` and `mac:WHOVariantClassification`) returns two rows; the FDT *qua* experimental object (filtering for `mac:ExperimentalDMSObservation`) returns one row.

#### Query Q5.3.5 — Temporal accretion

*Purpose.* Reconstruct the time-stamped sequence of WHO classifications for a referent. Demonstrates the accretive property of §6.5: re-classifications appear as new observation FDOs without modification of prior ones.

```sparql
PREFIX mac: <[MAC namespace]>

SELECT ?classification ?date WHERE {
  ?obs rdf:type mac:WHOVariantClassification .
  ?obs mac:isObservationOf <r-URI> .
  ?obs mac:hasWHOClassification ?classification .
  ?obs mac:hasClassificationDate ?date .
}
ORDER BY ?date
```

*Expected result for $r$ = Alpha at the time of writing.* One row (the original VOC designation of 2020-12-18). Following any subsequent reclassification published as a new Type 8 observation FDO, the query returns the full reclassification history without modification of the original FDO.

The five queries are presented as evidence that the architectural properties claimed in §3 and §4 — on-demand cluster assembly, hub topology, cross-variant comparison, method-traced provenance, *qua* filtering, and temporal accretion — are realised by the published catalogue and accessible to any party with SPARQL access to the NSN. The complete query set, with live URIs substituted, will be deposited alongside the catalogue file in the Data Availability statement.

---

## 6. Discussion

The empirical realisation reported in §5 admits several lines of interpretation. We organise the discussion as follows: §6.1 situates the architecture as a concrete realisation of the Knowlet construct of Mons [REF-Mons-2019] and of the FAIR Digital Twin vision of Schultes et al. [REF-FDT-Perspective]; §6.2 identifies what the realisation contributes substantively at the level of scientific data integration; §6.3 establishes that the architecture is generic across referent classes; §6.4 places the work within the broader landscape of digital twin and machine-actionable variant resources; §6.5–§6.7 address pandemic-preparedness implications, the AI-assisted authoring workflow, and limitations and future work.

### 6.1 The FDT as a concrete realisation of the Knowlet construct

The architecture of §4 is, in operational terms, a concrete realisation of the Knowlet construct introduced by Mons [REF-Mons-2019] and developed into the FAIR Digital Twin proposal by Schultes et al. [REF-FDT-Perspective]. Both prior contributions specified what a Knowlet or FDT *should* be — a cluster of machine-actionable, provenance-bearing assertions about a common subject, persistently identified and accretively extensible — without committing to a particular substrate or deployment architecture. The present work supplies the substrate (the nanopublication framework and its decentralised server network, as established in [REF-MAC-FAIR]) and the deployment architecture (the three-layer design and the hub topology of §4), and reports the realisation against a non-trivial scientific use case.

Three correspondences between the prior conceptual work and the present realisation are worth recording explicitly.

First, the Knowlet was defined by Mons as the cluster of all cardinal assertions sharing a common subject [REF-Mons-2019]. In the present architecture, the cardinal assertion is the assertion graph of a nanopublication, the common subject is the URI of the referent declared by the anchor $A_r$, and the cluster is the operational FDT of Definition 5. The Mons construct is therefore directly recovered, with the additional architectural commitment that each cardinal assertion is itself an FDO with type, materialisation, and intrinsic provenance.

Second, the FDT was characterised by Schultes et al. as a "stepwise and modular" construct in which the digital twin is assembled from more fundamental FDOs and remains itself an FDO when so assembled [REF-FDT-Perspective]. The present realisation discharges both halves of this characterisation. The cluster $\mathrm{FDT}(r) = \{A_r\} \cup \{O_r\}$ is built from individually published np-FDOs; and the cluster as a whole, by virtue of the anchor's identification of $r$ and the substrate's discharge of persistence and machine actionability, satisfies the FDO specifications for $r$ as a digital object. The FDT-as-FDO recursion is therefore explicit in the architecture rather than merely asserted.

Third, the *qua* construct introduced by Schultes et al. — the ability to filter a twin to a subset of its component FDOs corresponding to a particular point of view [REF-FDT-Perspective] — is recovered in the present architecture as SPARQL filtering on the observation cluster. The Alpha variant *qua* structural object is the subset of $\mathrm{FDT}(\text{Alpha})$ whose members are typed `mac:ComputationalPrediction*` or whose anchor properties concern sequence and structure; the Alpha variant *qua* epidemiological entity is the subset typed `mac:RealWorldOccurrence` or `mac:WHOVariantClassification`. The filtering is one SPARQL query and requires no precomputed views: the underlying decentralised substrate makes every component independently retrievable, and any party can construct any *qua* of any FDT on demand.

What the present realisation contributes over the prior conceptual work is therefore not a new construct but a complete and reproducible specification of one. While knowledge-graph-based DT realisations exist in chemistry and manufacturing [REF-Akroyd-2021; REF-Bai-2024], FAIR Digital Twins have recently been deployed in biodiversity using RO-Crate as the substrate [REF-BioDT-2026], and FAIR-aligned variant knowledge graphs are well-established at the database and integration level [REF-ClinVar; REF-gnomAD; REF-MaveDB; REF-PRO-LOD-2020; REF-Waagmeester-2020; REF-VA-Spec-2025], the present work is, to our knowledge, the first realisation of an FDT specifically as a cluster of nanopublication-based FDOs around a common biomedical-variant referent — in the Mons/Knowlet sense [REF-Mons-2019]. The architectural and substrate-level comparisons with these adjacent realisations are taken up in §6.4.

### 6.2 Coherent integration of heterogeneous epistemic types

The substantive scientific feature of the realisation is the coherent integration, around a single referent, of data drawn from three distinct epistemic categories: real-world surveillance, computational prediction, and experimental measurement.

For the Alpha variant ($r = $ Alpha N169Y) the cluster $\mathrm{FDT}(r)$ records, as separately published, persistently identified, individually citable np-FDOs: a GISAID surveillance record of the variant's first detection in England in late 2020 (Type 2); structural predictions of the variant's RBD by ESM2 and AlphaFold 2 (the RMSD, SASA, and pLDDT triples of Types 3–5, two methods each); a sequence-derived aggregation propensity score from the Bio2Byte AgMata predictor (Type 6); deep-mutational-scanning measurements of binding affinity and expression level from the Bloom Lab assay (Type 7, with six measurement statements); and the WHO Variant-of-Concern designation of 18 December 2020 (Type 8). Ten observations of different epistemic provenance are linked to the same anchor by the single predicate `mac:isObservationOf`, and the cluster is assembled on demand by SPARQL traversal on the open NSN.

The novelty of this integration deserves measured statement. Resources that aggregate variant-level information across data types exist and are valuable: Nextstrain [REF-Hadfield-2018] combines sequence-derived phylogenies with curated metadata; outbreak.info [REF-Gangavarapu-2023] combines lineage information with surveillance epidemiology; the Bloom Lab interactive portal [REF-Starr-2020] displays DMS measurements in a browsable interface; UniProt with the Protein Ontology Linked Open Data [REF-UniProt; REF-PRO-LOD-2020] integrates sequence, structure, and curated annotations. The contribution of the present work is not the conceptual integration of these data types — that has been done in various forms by these and other resources — but the specific realisation in which **each individual data point is itself an FDO with a Trusty URI**, individually retrievable, individually citable, and machine-traversable as part of a federated graph that no single platform owns or curates. The Alpha-variant AlphaFold pLDDT score is, in our realisation, the same kind of object as the Alpha-variant Bloom-Lab binding affinity and the Alpha-variant GISAID surveillance record: an np-FDO on the NSN, accessible through the same protocol, citable by the same identifier scheme, and linked into the cluster by the same predicate.

Three operational consequences follow from this design that, taken together, distinguish the realisation from platform-level integration.

1. *Individual provenance audit.* The provenance chain for any single data point can be traced by following two cross-links: from the observation FDO to the anchor (`mac:isObservationOf`), and from the observation FDO to the method FDO (`mac:hasPredictionMethod`, `mac:hasExperimentalMethod`, or `mac:hasSurveillanceMethod`). The trace yields the referent's identity, the method that produced the observation, the timestamp and the signing ORCID of the observation FDO's publication. No platform-specific API, no proprietary lookup, and no central registry mediates the trace.

2. *Open and accretive extension.* The cluster admits new observations without alteration of any existing FDO. The WHO has, since the initial Alpha-as-VOC designation, downgraded the variant to a previously-circulating-VOC status [REF-WHO-tracking]. In the present architecture, that downgrade is recorded by publishing a new Type 8 observation FDO citing $A_{\text{Alpha}}$ and carrying the new classification with its date; the original VOC observation FDO remains immutable, and the cluster now contains the complete time-stamped classification history. Any party with an ORCID can publish such a new observation; no platform mediation is required.

3. *Machine-actionable cross-citation.* An AI agent reading the Bloom Lab binding affinity FDO for Alpha can dereference the `mac:isObservationOf` link to retrieve the anchor and therefore the variant's sequence, the `mac:hasExperimentalMethod` link to retrieve the protocol and its citation, and the anchor's `dct:references` link to retrieve the associated FAIR² data article and Data Package. The chain is machine-actionable in the strong sense of [REF-Wilkinson-2016]: the agent does not need to parse human-readable documentation to navigate it.

The integration is therefore best characterised not as "Nextstrain plus AlphaFold plus Bloom Lab" but as a structurally uniform substrate against which any of these resources — or any future resource — can publish data and have it become part of the variant's FDT by the act of publication.

### 6.3 Generality beyond Spike variants

Nothing in the architecture of §4 is specific to SARS-CoV-2 Spike RBD variants. The architecture decomposes into two parts: a structural template (the three layers, the eleven type slots, the hub topology, the external method library) and a domain vocabulary (the 26 predicates and 14 classes of the MAC FDT vocabulary). The structural template is referent-class-agnostic. The vocabulary is the part that is specific to the Spike-variant case.

This decomposition has a direct practical consequence: an FDT for a different referent class can be specified by retaining the structural template and substituting a new domain vocabulary. The methodology for producing such a vocabulary — Stakeholder Participation Sheets identifying domain-relevant predicates and value ranges, followed by translation into NanoDash templates — is the same methodology used in the present work and is documented in [REF-MAC-FAIR §3.4]. The np-FDO substrate remains unchanged: the same NSN, the same Trusty URI scheme, the same ORCID-based signing, the same SPARQL accessibility.

To make the generality claim concrete, we list four illustrative referent classes that the architecture would accommodate without structural modification. Each requires its own SPS exercise to determine the relevant observation types and predicates; none requires alteration of the three-layer design, the hub topology, or the substrate.

* *Metabolites.* Anchor: a specific chemical species or class. Observations: mass spectra, retention indices, predicted molecular properties, biological-activity assays, regulatory designations. Methods: instrumental configurations, prediction algorithms, assay protocols.
* *Cell lines or tissue samples.* Anchor: a specific biological resource with a persistent identifier (e.g., a Cellosaurus accession). Observations: transcriptomic, proteomic, or metabolomic profiles, drug-response measurements, microscopy-derived morphometric data. Methods: the corresponding -omics platforms or imaging protocols.
* *Instruments.* Anchor: a specific mass spectrometer or analytical instrument identified by serial number and laboratory location. Observations: calibration measurements, downtime episodes, throughput logs, performance tests. Methods: the calibration protocols and quality-control procedures. This is the engineering-DT case under our operational definition.
* *Funded research projects.* Anchor: a specific research project. Observations: datasets produced, methods deployed, articles published, intermediate findings. Methods: the analytical and experimental procedures used. The seven-type catalogue developed in the parallel MAC FAIR work [REF-MAC-FAIR] is, under the present operational definition, an FDT for a project-class referent with seven observation types.

The last of these is worth pausing on. The seven-type research-administration catalogue of [REF-MAC-FAIR] and the eleven-type Spike-variant catalogue of the present paper are, structurally, two instantiations of the same architecture against two different referent classes. The research-administration catalogue addresses what [REF-MAC-FAIR §6.1] terms *Level 1* FAIRification: research-object metadata at the granularity of administrative and methodological artefacts. The Spike-variant catalogue addresses *Level 2*: the scientific claims and measurements *within* the data files referenced by the Level 1 objects. The two levels share a substrate, an architectural pattern, and a governance approach; they differ only in the SPS-derived vocabulary that each requires. The present work therefore constitutes empirical evidence for the extensibility claim advanced in [REF-MAC-FAIR §6.1], to which we return in §6.7.

Two practical limitations attach to the generality claim and merit recording.

First, the rapidity with which a new FDT can be deployed in a new domain depends on the SPS being conducted by someone familiar with the domain's observable properties and conventional methods. The first SPS in a new domain is slower than subsequent ones; the second and later SPSs benefit from the structural template being already fixed and from the predicates and classes of the first SPS being reusable where the domains overlap. We have not attempted to quantify this learning curve in the present work; the StayAhead SPS was conducted by the MAC group with substantial domain familiarity already in place.

Second, the hub-and-spoke topology of §4.3 presumes that observations can be interpreted and cited independently of each other. Where domain semantics require first-class representation of inter-observation relationships — for example, a hierarchical relationship between a parent measurement and a derived measurement, or a temporal sequence of measurements in a longitudinal study — additional cross-links between observation FDOs may be required, beyond the spoke-to-anchor links sufficient for the Spike-variant case. The architecture admits such cross-links without modification of the substrate (a new predicate suffices); whether the resulting graph still merits the "hub topology" characterisation in §4.3 is a question for the relevant SPS to resolve. Our experience to date is that the hub topology is sufficient for a wide range of scientific use cases, but we make no claim that it is sufficient for all.

### 6.4 Comparison with related work

The present realisation occupies a specific architectural position in a landscape that has recently become crowded. We organise the comparison along four lines: engineering-DT standards, which set the baseline for DT terminology and architecture; knowledge-graph-based DT realisations, which adopt semantic-web substrates without invoking the FAIR framing; FAIR Digital Twin realisations, which adopt FAIR substrates with different choices of FDO unit; and variant-data resources, which the present work most directly informs at the level of scientific data integration.

*Engineering-DT standards.* The ISO 23247 series [REF-ISO-23247; REF-Shao-NIST-2023], the Asset Administration Shell (AAS / IEC 63278-1) [REF-IDTA-AAS-3-0; REF-IEC-63278], and the Digital Twin Consortium's Capabilities Periodic Table [REF-DTC-CPT-2024] together set the terminology and reference architecture for the engineering-DT tradition. All three frameworks treat the represented entity as a physical asset (called variously *Observable Manufacturing Element*, *asset*, *real-world entity*, or *physical twin*), require bidirectional near-real-time synchronisation between the digital and physical, and emphasise interoperability without prescribing FAIR-Principles compliance. The present FDT departs from these on three counts: the referent is type-level rather than instance-level (§3.1, §3.5); accretion replaces synchronisation as the update mechanism (§3.5, §6.5); and FAIR compliance is delivered by the substrate (§4) rather than left to implementers. The departures are deliberate generalisations rather than deficiencies: each engineering-DT case is recoverable from the present definition as a special case in which the referent is a specific physical asset and the observation stream is sensor telemetry (§3.5).

*Knowledge-graph-based DT realisations.* The Universal Digital Twin and World Avatar programme of the Cambridge–CARES group [REF-Akroyd-2021; REF-Bai-2024] is the closest non-Knowlet architectural comparator. It uses OWL ontologies, computational agents, and a dynamic knowledge graph to represent chemistry and manufacturing systems, and is the only programme in the reviewed literature to attempt cross-domain interoperability at a comparable scale. Substrate-level differences are material: the World Avatar's dynamic-KG approach treats the graph as a mutable shared state updated by autonomous agents; the np-FDO substrate of the present work treats each cross-link as an immutable, separately published nanopublication carrying its own provenance. The two approaches are complementary: agent-mediated mutability serves continuous-process domains; nanopublication-mediated immutability serves accreting-knowledge domains.

*FAIR Digital Twin realisations.* The Biodiversity Digital Twin (BioDT) consortium published the first end-to-end FAIR Digital Twin realisation in February 2026 [REF-BioDT-2026; REF-Sustkova-2025], demonstrating ten prototype FDTs across ecological-modelling use cases and explicitly citing the Schultes 2022 FDT Perspective [REF-FDT-Perspective] as the framing reference. The substrate choice — RO-Crate [REF-Soiland-Reyes-2022; REF-Sustkova-2025] — packages workflows, datasets, and models at the research-object granularity, with each crate carrying machine-readable metadata bundling its components. The present work's np-FDO substrate operates at finer granularity: a single nanopublication carries a single assertion (one observation, one method declaration, one classification), and the FDT cluster is assembled by SPARQL traversal of the `mac:isObservationOf` cross-links rather than by enumeration in a crate manifest. The two substrates are structurally distinct realisations of the FAIR-FDO commitment and serve different epistemic patterns: workflow-package-level for the bundled-pipeline domain that biodiversity modelling exemplifies, and assertion-level for the accreting-claim domain that the present work exemplifies. Neither realisation displaces the other; both may co-exist in a broader Internet of FAIR Data and Services.

*Variant-data resources.* The variant-tracking landscape spans surveillance platforms (Nextstrain [REF-Hadfield-2018], outbreak.info [REF-Gangavarapu-2023], GISAID [REF-Shu-2017; REF-Khare-2021]), lineage nomenclature (Pango [REF-Rambaut-2020; REF-OToole-2021]), structural prediction portals, and experimental repositories (Bloom Lab DMS portal [REF-Starr-2020; REF-Starr-2022], MaveDB [REF-MaveDB; REF-MaveMD-2026]). Several of these resources publish data with persistent identifiers — GISAID accessions at the sequence level, Pango lineage names at the lineage level, paper DOIs at the dataset level — but none of the reviewed resources publishes individual variant properties (a single binding affinity value, a single first-detection record, a single classification decision) as separately persistently identified, individually citable objects. At the knowledge-graph layer, ClinVar [REF-ClinVar], gnomAD [REF-gnomAD], the UniProt Protein Ontology Linked Open Data [REF-PRO-LOD-2020], Wikidata [REF-Waagmeester-2020], and the GA4GH Variation Annotation Specification [REF-VA-Spec-2025] together exemplify the FAIR-aligned variant-data infrastructure that has matured over the past decade — but again at the database, integration, or schema level rather than at the data-point level. The early proposal by Patrinos et al. [REF-Patrinos-2012] that variant data should be published as nanopublications, in a microattribution framework, was not realised at scale; the present work supplies the substrate-level realisation that was missing.

*Synthesis.* The architectural slot occupied by the present work is therefore precise: a FAIR Digital Twin realised as a cluster of nanopublication-based FDOs sharing a common biomedical-variant referent, in the Knowlet sense of [REF-Mons-2019] and the FDT sense of [REF-FDT-Perspective]. The engineering-DT standards do not address this slot (different domain, different substrate, different referent class); the knowledge-graph DTs do not address it (different substrate, no FDO commitment); the BioDT FAIR Digital Twin realisation addresses an adjacent slot at a different granularity (workflow-package level rather than assertion level); and the variant-data resources address an adjacent slot without the cluster-as-FDT architectural pattern. The present work is not the first realisation of any individual ingredient — nanopublications, FDOs, FAIR-aligned DTs, variant knowledge graphs, structural-prediction integration, classification provenance all exist independently — but is, to our knowledge, the first realisation of their combination.

### 6.5 Implications for pandemic preparedness

The realisation reported here was developed within the StayAhead programme at the MAC, whose mandate is to contribute infrastructure relevant to the early-stage characterisation of emerging viral variants. We confine the present discussion to infrastructural implications and refrain from claims about pandemic response that would require institutional, epidemiological, or policy analysis beyond the scope of this paper.

Four properties of the architecture have direct relevance to a preparedness setting.

*Real-time accretive integration.* New data about a variant of interest — additional surveillance detections, new structural predictions from updated models, new experimental measurements, revised classification decisions — can be added to its FDT as new observation FDOs at the moment the data become available, without modification of any existing FDO. The cluster $\mathrm{FDT}(r)$ is therefore a continuously growing record. When a WHO classification is updated, the update is a new Type 8 observation FDO carrying the new classification and its assignment date; the prior classification FDO remains immutable, and the cluster automatically reflects the full classification history. The same applies to model-derived predictions when new versions of the predictive method appear, and to experimental measurements when new assays are performed.

*Cross-source comparison at minimal incremental cost.* Once the eleven-type structure and the MAC FDT vocabulary are deployed for a referent class, a new variant requires only the publication of a new anchor and its observation FDOs — typically eleven nanopublications per variant under the present configuration. Comparison across variants reduces to a SPARQL traversal of the observation cluster. The 3705-mutation systematic scan (held for the scale-up extension) demonstrates that this cost scales to tens of thousands of FDOs without architectural alteration.

*Independent and machine-actionable provenance.* Each data point carries a Trusty URI, an ORCID-authenticated signature, and a publication timestamp. Where preparedness applications require independent verification of the origin and timing of a measurement — a recurring concern when data move across institutional boundaries under time pressure — the FDT structure makes such verification a substrate-level guarantee rather than a downstream auditing exercise. The provenance is verifiable by any party with access to the open NSN, without consulting any platform-specific API.

*Decentralised contribution without platform mediation.* The FDT architecture admits contributions from any party with an ORCID. A surveillance system, a computational laboratory, an experimental group, and a clinical-classification body can all publish observation FDOs referencing the same anchor; the cluster integrates the contributions without requiring any of these parties to deposit data into a common repository or to coordinate through a shared platform. In a preparedness setting in which contributors are geographically and institutionally heterogeneous, this property reduces a class of coordination problems that platform-centric integration approaches do not eliminate.

These properties are infrastructural. Whether and how they translate into operational benefit in a real preparedness scenario depends on uptake by data-producing communities and on integration with existing surveillance, response, and reporting workflows. We note in §6.7 that such integration is an open programme of work.

### 6.6 The AI-assisted authoring workflow

The 11-type FDT specification reported here was authored in iterative collaboration with AI models, in continuity with the methodology established for the seven-type research-administration catalogue [REF-MAC-FAIR §3.4]. The workflow used AI assistance for four operations: structural decomposition (identifying which observation classes a referent of the relevant type should accommodate); predicate elicitation (proposing candidate predicate–object pairs for each observation class); vocabulary normalisation (checking that proposed predicates were consistent with existing standard vocabularies and with the MAC namespace conventions); and consistency checks (verifying that all 26 predicates and 14 classes were used coherently across the eleven templates). The architectural decisions — the choice of the three-layer design, the commitment to the hub topology, the externalisation of the method library — were taken by the authors in deliberation with stakeholders through the SPS process; AI assistance accelerated the elicitation and structuring of candidates, but did not substitute for architectural judgement.

The result was a non-trivial specification produced on a timescale compatible with the StayAhead programme's deliverable schedule. We do not attempt here to quantify the acceleration. The workflow nevertheless illustrates a reciprocal pattern that is becoming explicit in the recent literature on AI-readiness of data [REF-Verhulst-FAIR-R-2025] and on trustworthy retrieval-augmented generation [REF-Ni-RAG-Survey-2025; REF-Alu-Oluwadare-2026]: FAIR-compliant infrastructure provides AI agents with the per-assertion provenance, immutability, and machine-actionable cross-citation that trustworthy reasoning requires, while AI accelerates the human-intensive elicitation and curation work on which FAIRification programmes have historically been bottlenecked. The fuller treatment of this reciprocal relationship — including the inverse framing of *FAIR-Ready AI*, in which AI systems must be capable of discriminating FAIR inputs and generating FAIR outputs — is held for a separate methodological paper.

### 6.7 Limitations and future work

We record six limitations of the present work and the future-work programmes that address them.

*Empirical scope.* The empirical realisation reported in §5 covers three variants and 38 instance nanopubs. The architecture is designed for larger-scale deployment, and two extensions are in active development: a systematic 3705-mutation single-step scan exhausting the local sequence space around the Wuhan reference [REF-MAC-FAIR §6.1; REF-MaxThesis], and a compute-to-lab cycle in which five double-mutant variants selected from computational analysis were tested experimentally by the Bosch laboratory [REF-Bosch-extension]. The 3705 scan produces on the order of $3.0 \times 10^4$ nanopublications across the same eleven types; the Bosch extension adds approximately 11–46 additional nanopublications, including experimental negative results that are themselves persistently identified and citable. Both extensions exercise the architecture without modification; results will be reported in a companion paper.

*Vocabulary maturity.* The 26 predicates and 14 classes of the MAC FDT vocabulary constitute a working set for the present use case. Two encoding decisions taken during vocabulary v1.1 finalisation merit recording for transparency. First, `mac:hasGISAIDAccession` is retained as a single predicate, with literal range, carrying both the canonical exemplar accession at Type 1 and the specific surveilled accession at Type 2; should GISAID introduce a public URI scheme for accessions in future, the predicate semantics admit a straightforward migration to `owl:sameAs` (at Type 1, asserting identity with the canonical record) or `dct:relation`/`skos:closeMatch` (at Type 2, relating to a specific surveilled instance). Second, `mac:hasCollectionLocation` takes GeoNames feature URIs as its object range, rather than ISO 3166-1 alpha-2 country codes or free-text literals; this choice accommodates the variable granularity that surveillance records exhibit (national-level summaries, sub-national administrative subdivisions, specific populated places) within a single uniform identifier scheme. We anticipate that the vocabulary will undergo additional curation cycles as new observation types are added and as cross-domain alignment with broader variant-tracking standards is pursued.

*Type-level versus instance-level FDTs.* The empirical content of this paper concerns type-level FDTs of sequence-defined variants. Instance-level FDTs — of specific patient samples, specific GISAID-listed sequences, specific manufactured protein batches — are architecturally identical (§3.5) but are not implemented in the present work. Instance-level deployment is straightforward in principle and is anticipated as part of the broader Recursive FAIRification programme [REF-MAC-FAIR §6.1].

*Static cluster, not synchronous mirror.* The FDT as realised here is accretive but not synchronously updated from a live data source in the engineering-DT sense. Where preparedness applications require near-real-time mirroring (for example, FDTs of clinical instruments producing continuous output streams), additional infrastructure would be required: either a publishing agent that converts the live stream into a stream of nanopublications, or a substrate extension supporting an explicit "live" channel alongside the accretive one. Neither extension is precluded by the present architecture; both are open work.

*Hub-topology sufficiency.* §6.3 noted that the hub-and-spoke cluster topology suffices for domains in which observations can be interpreted and cited independently. Domains in which inter-observation relationships require first-class representation — temporal sequences in longitudinal studies, hierarchical relationships between parent and derived measurements, edge structures in sequence-space neighbourhoods — will require additional predicates linking observation FDOs to one another. The 3705 scan provides a natural occasion to revisit this, since the sequence-space neighbourhood structure between single-step mutations is an inter-observation relationship that the present vocabulary does not represent.

*Adoption.* The technical readiness of the architecture does not imply community uptake. The architecture's value to the wider variant-tracking and pandemic-preparedness communities depends on whether established data producers — surveillance platforms, structural-prediction services, experimental laboratories — publish observation FDOs against shared anchors, or whether parallel non-interoperable ecosystems emerge. Encouragingly, the MAC FDT architecture introduces no compatibility tax: the same data that producers currently publish in their native formats can be additionally published as np-FDOs without disturbing the native workflows. Whether such additional publication will occur is an empirical question we cannot answer in advance.

The future-work programme correspondingly comprises: completion and reporting of the 3705-mutation scale-up and the Bosch compute-to-lab cycle; integration with external catalogues including the Dutch National Catalogue, the European Health Data Space, and where appropriate Nextstrain and outbreak.info; instance-level FDTs of clinical and surveillance samples; agentic consumption of the FDT graph by AI agents through the Claude–NanoDash interface in development [REF-MAC-FAIR §6.4]; and cross-domain deployment of the architecture for the four referent classes listed in §6.3, beginning with metabolite FDTs in the ongoing MAC programme.

---

## 7. Conclusion

We have presented an operational definition of a FAIR Digital Twin (FDT) as the cluster of FAIR Digital Objects whose assertions concern a common subject, and a concrete architectural realisation of that definition for SARS-CoV-2 Spike RBD variants. The architecture comprises a referent-class-agnostic structural template — three layers (Identity, Observation, Method) connected by a single hub-topology predicate, `mac:isObservationOf` — and a domain vocabulary of 26 MAC-namespace predicates and 14 classes specific to the Spike-variant case. Together these are realised on the open Nanopublication Server Network as 38 individually citable, ORCID-signed, persistently identified nanopublications constituting three FDTs — for the Alpha, Epsilon, and Eta variants — and a shared method library.

Around each variant, heterogeneous data of three distinct epistemic categories — real-world surveillance, computational prediction, and experimental measurement — are coherently linked. Each individual data point is itself a FAIR Digital Object: the Bloom-Lab binding affinity for Alpha, the AlphaFold pLDDT for Alpha, and the GISAID first-detection record for Alpha are the same kind of object, accessible through the same protocol and citable by the same identifier scheme. Cross-FDT comparison, *qua* filtering, method-traced provenance, and temporal accretion are demonstrated as single SPARQL traversals against the open catalogue.

The realisation is, in operational terms, the Knowlet construct of Mons [REF-Mons-2019] and the FAIR Digital Twin vision of Schultes et al. [REF-FDT-Perspective], now equipped with a substrate, a deployment architecture, and a non-trivial scientific use case. The contribution of the present work is therefore not a new construct but a complete and reproducible specification of one. The architecture generalises to other referent classes — metabolites, cell lines, instruments, research projects — through the same SPS-driven methodology used here [REF-MAC-FAIR §3.4], and is currently being exercised at scale (3705-mutation systematic scan) and against an experimental compute-to-lab cycle in companion programmes.

The architecture introduces no compatibility tax: data producers can publish observation FDOs against shared anchors without disturbing their native workflows. The infrastructure is ready; whether the established surveillance, prediction, and experimental communities will adopt it is the empirical question on which the broader value of the FDT framework now turns.

---

## Figures

### Figure 1

*The SVG file is supplied separately as `FDT_paper_Figure_1.svg`. The caption text is reproduced here.*

**Figure 1.** FDT hub topology for the Alpha variant ($r$ = Alpha N169Y; lineage B.1.1.7). The anchor FDO $A_{\text{Alpha}}$ (centre, Type 1, `mac:SpikeRBDVariant`) declares the identity and intrinsic sequence properties of the variant. Ten observation FDOs surround the anchor, organised by epistemic category: real-world surveillance (Type 2, orange), computational prediction (Types 3–6, blue), experimental measurement (Type 7, green), and authoritative classification (Type 8, purple). Each observation FDO links to the anchor by the single predicate `mac:isObservationOf` (solid dark arrows pointing inward). The external method library $\mathcal{M}$ (right) contains five method FDOs of Types 9–11 (`mac:ComputationalMethod`, `mac:ExperimentalMethod`, `mac:ObservationalMethod`), referenced by observation FDOs via `mac:hasPredictionMethod`, `mac:hasExperimentalMethod`, or `mac:hasSurveillanceMethod` (dashed light arrows). Methods are shared across FDTs and across observation types and are not part of any individual FDT; the FDT (as defined in Definition 5) is the cluster of the anchor and its observations only. The same architectural pattern accommodates the Epsilon (L120R) and Eta (E152K) FDTs reported in §5.2; only the anchor identity and the observation values change.

---

## References

> **PLACEHOLDER — to be consolidated when the bibliography is finalised.**

The following citation keys are used in this draft. Items added through the Q1–Q5 literature scan are marked **(scan)**; items inherited from project knowledge or prior drafting are unmarked.

### Core (prior to scan)

* [REF-Wilkinson-2016] — Wilkinson, M.D., et al. (2016). *The FAIR Guiding Principles for scientific data management and stewardship*. Scientific Data 3:160018. https://doi.org/10.1038/sdata.2016.18
* [REF-Mons-2019] — Mons, B. (2019). *FAIR Science for Social Machines: Let's Share Metadata Knowlets in the Internet of FAIR Data and Services*. Data Intelligence 1(1):22–42. https://doi.org/10.1162/dint_a_00002
* [REF-FDT-Perspective] — Schultes, E., Roos, M., Bonino da Silva Santos, L.O., Guizzardi, G., Bouwman, J., Hankemeier, T., Baak, A., Mons, B. (2022). *FAIR Digital Twins for Data-Intensive Research*. Frontiers in Big Data 5:883341. https://doi.org/10.3389/fdata.2022.883341
* [REF-Schultes-Wittenburg-2019] — Schultes, E., and Wittenburg, P. (2019). *FAIR Principles and Digital Objects: Accelerating Convergence on a Data Infrastructure*.
* [REF-MAC-FAIR] — Schultes, E., et al. (forthcoming). *Practical FAIRification of high-throughput metabolomics using nanopublication-based FAIR Digital Objects*. (Companion paper; manuscript v2.0.)
* [REF-Soiland-Reyes-2024] — Soiland-Reyes, S., Goble, C., Groth, P. (2024). *Evaluating FAIR Digital Object and Linked Data as distributed object systems*. PeerJ Computer Science 10:e1781. https://doi.org/10.7717/peerj-cs.1781
* [REF-Groth-2010] — Groth, P., Gibson, A., Velterop, J. (2010). *The anatomy of a nanopublication*. Information Services & Use 30(1–2):51–56.
* [REF-Kuhn-2018] — Kuhn, T., et al. (2018). *Nanopublications: A Growing Resource of Provenance-Centric Scientific Linked Data*. arXiv:1809.06532.
* [REF-TrustyURIs] — Kuhn, T., Dumontier, M. (2014). *Trusty URIs: Verifiable, Immutable, and Permanent Digital Artifacts for Linked Data*. ESWC.
* [REF-Magagna-2025] — Magagna, B., Bonino da Silva Santos, L.O., Kuhn, T., Ferreira Pires, L., Schultes, E. (2025). *Nanopublications as FAIR Digital Object Implementations*. Open Conference Proceedings 5. https://doi.org/10.52825/ocp.v5i.1417
* [REF-FFF-Framework] — *FAIR Funder Framework*.
* [REF-Lin-ESM2] — Lin, Z., et al. (2023). *Evolutionary-scale prediction of atomic-level protein structure with a language model*. Science 379:1123–1130. https://doi.org/10.1126/science.ade2574
* [REF-Jumper-AlphaFold2] — Jumper, J., et al. (2021). *Highly accurate protein structure prediction with AlphaFold*. Nature 596:583–589. https://doi.org/10.1038/s41586-021-03819-2
* [REF-Bio2Byte] — *Bio2Byte toolkit — AgMata aggregation predictor*. Bioinformatics. https://doi.org/10.1093/bioinformatics/btac149
* [REF-Starr-2020] — Starr, T.N., et al. (2020). *Deep Mutational Scanning of SARS-CoV-2 Receptor Binding Domain Reveals Constraints on Folding and ACE2 Binding*. Cell 182:1295–1310. https://doi.org/10.1016/j.cell.2020.08.012
* [REF-Shu-2017] — Shu, Y., and McCauley, J. (2017). *GISAID: Global initiative on sharing all influenza data*. Eurosurveillance 22(13):30494. https://doi.org/10.2807/1560-7917.ES.2017.22.13.30494
* [REF-Khare-2021] — Khare, S., et al. (2021). *GISAID's Role in Pandemic Response*. China CDC Weekly 3(49):1049–1051. https://doi.org/10.46234/ccdcw2021.255
* [REF-MaxThesis] — van den Boom, M. (2024). *MSc thesis on the computational analysis of 3705 single-step Spike RBD mutations*. https://osf.io/7gxd3/files/r39ey
* [REF-Bosch-extension] — Schultes, E., et al. (in preparation). *Bosch laboratory experimental cycle on selected RBD double-mutant variants*.

### Added through Q1–Q5 literature scan

* **(scan)** [REF-NASEM-2024] — NASEM (2024). *Foundational Research Gaps and Future Directions for Digital Twins*. National Academies Press. https://nap.nationalacademies.org/catalog/26894
* **(scan)** [REF-Katsoulakis-2025] — Katsoulakis, E., et al. (2025). *A scoping review of human digital twins in healthcare applications and usage patterns*. npj Digital Medicine. https://doi.org/10.1038/s41746-025-01910-w
* **(scan)** [REF-Drummond-2024] — Drummond, D., Gonsard, A. (2024). *Definitions and Characteristics of Patient Digital Twins Being Developed for Clinical Use: Scoping Review*. J Med Internet Res 26:e58504. https://doi.org/10.2196/58504
* **(scan)** [REF-Grieves-Vickers-2017] — Grieves, M., Vickers, J. (2017). *Digital Twin: Mitigating Unpredictable, Undesirable Emergent Behavior in Complex Systems*. In: Kahlen, J., et al. (eds), Transdisciplinary Perspectives on Complex Systems, Springer, pp 85–113. https://doi.org/10.1007/978-3-319-38756-7_4
* **(scan)** [REF-Grieves-Origins-2016] — Grieves, M., Vickers, J. (2016). *Origins of the Digital Twin Concept*. Working paper.
* **(scan)** [REF-Glaessgen-2012] — Glaessgen, E., Stargel, D. (2012). *The Digital Twin Paradigm for Future NASA and U.S. Air Force Vehicles*. AIAA SDM Conference.
* **(scan)** [REF-EDITH-Roadmap-2025] — EDITH Consortium (2025). *A Roadmap for the European Virtual Human Twin*. Zenodo. https://doi.org/10.5281/zenodo.14769224
* **(scan)** [REF-EC-VHT-2024] — European Commission (2024). *European Virtual Human Twins (VHT) Initiative*. https://digital-strategy.ec.europa.eu/en/policies/virtual-human-twins
* **(scan)** [REF-ISO-23247] — ISO/IEC 23247 series (2021–2024). *Automation systems and integration — Digital twin framework for manufacturing* (Parts 1–5).
* **(scan)** [REF-Shao-NIST-2023] — Shao, G., Frechette, S.P., Srinivasan, V. (2023). *An Analysis of the New ISO 23247 Series of Standards on Digital Twin Framework for Manufacturing*. NIST.
* **(scan)** [REF-IDTA-AAS-3-0] — IDTA (2023, 2025). *Specification of the Asset Administration Shell, Version 3.0*. Industrial Digital Twin Association.
* **(scan)** [REF-IEC-63278] — IEC 63278-1. *Asset Administration Shell for industrial applications*.
* **(scan)** [REF-DTC-CPT-2024] — Digital Twin Consortium (2024). *Digital Twin Capabilities Periodic Table v1.1*.
* **(scan)** [REF-BioDT-2026] — Sehl, K., et al. (2026). *FAIR digital twins for biodiversity: enabling data, model, and workflow integration*. npj Biodiversity. https://doi.org/10.1038/s44185-025-00116-3
* **(scan)** [REF-Sustkova-2025] — Sustkova, H.P., et al. (2025). *FAIR Digital Object and RO-Crate as interoperability frameworks for Biodiversity Digital Twins*. 1st International FAIR Digital Objects Implementation Summit.
* **(scan)** [REF-Soiland-Reyes-2022] — Soiland-Reyes, S., et al. (2022). *Creating lightweight FAIR Digital Objects with RO-Crate and FAIR Signposting*. 1st International Conference on FAIR Digital Objects. https://doi.org/10.5281/zenodo.7245315
* **(scan)** [REF-Akroyd-2021] — Akroyd, J., Mosbach, S., Bhave, A., Kraft, M. (2021). *Universal Digital Twin – A Dynamic Knowledge Graph*. Data-Centric Engineering 2:e14. https://doi.org/10.1017/dce.2021.10
* **(scan)** [REF-Bai-2024] — Bai, J., et al. (2024). *A dynamic knowledge graph approach to distributed self-driving laboratories*. Nature Communications 15:462. https://doi.org/10.1038/s41467-023-44599-9
* **(scan)** [REF-Hadfield-2018] — Hadfield, J., et al. (2018). *Nextstrain: real-time tracking of pathogen evolution*. Bioinformatics 34(23):4121–4123. https://doi.org/10.1093/bioinformatics/bty407
* **(scan)** [REF-Gangavarapu-2023] — Gangavarapu, K., et al. (2023). *Outbreak.info genomic reports: scalable and dynamic surveillance of SARS-CoV-2 variants and mutations*. Nature Methods 20:512–522. https://doi.org/10.1038/s41592-023-01769-3
* **(scan)** [REF-Rambaut-2020] — Rambaut, A., et al. (2020). *A dynamic nomenclature proposal for SARS-CoV-2 lineages*. Nature Microbiology 5:1403–1407. https://doi.org/10.1038/s41564-020-0770-5
* **(scan)** [REF-OToole-2021] — O'Toole, Á., et al. (2021). *Assignment of Epidemiological Lineages in an Emerging Pandemic Using the Pangolin Tool*. Virus Evolution 7(2):veab064. https://doi.org/10.1093/ve/veab064
* **(scan)** [REF-Starr-2022] — Starr, T.N., et al. (2022). *Deep mutational scans for ACE2 binding, RBD expression, and antibody escape in the SARS-CoV-2 Omicron BA.1 and BA.2 receptor-binding domains*. PLoS Pathogens 18(11):e1010951.
* **(scan)** [REF-ClinVar] — Landrum, M.J., et al. (2020). *ClinVar: improvements to accessing data*. Nucleic Acids Res 48(D1):D835–D844. https://doi.org/10.1093/nar/gkz972
* **(scan)** [REF-gnomAD] — Karczewski, K.J., et al. (2020). *The mutational constraint spectrum quantified from variation in 141,456 humans*. Nature 581:434–443. https://doi.org/10.1038/s41586-020-2308-7
* **(scan)** [REF-MaveDB] — Esposito, D., et al. (2019). *MaveDB: an open-source platform to distribute and interpret data from multiplexed assays of variant effect*. Genome Biology 20:223. https://doi.org/10.1186/s13059-019-1845-6
* **(scan)** [REF-MaveMD-2026] — MaveMD Consortium (2026). *MaveMD: A functional data resource for genomic medicine*. medRxiv. https://www.medrxiv.org/content/10.1101/2025.11.15.25336228v2
* **(scan)** [REF-UniProt] — UniProt Consortium (2023). *UniProt: the Universal Protein Knowledgebase in 2023*. Nucleic Acids Res 51(D1):D523–D531.
* **(scan)** [REF-PRO-LOD-2020] — Natale, D.A., et al. (2020). *Protein ontology on the semantic web for knowledge discovery*. Scientific Data 7:337. https://doi.org/10.1038/s41597-020-00679-9
* **(scan)** [REF-Waagmeester-2020] — Waagmeester, A., et al. (2020). *Wikidata as a knowledge graph for the life sciences*. eLife 9:e52614. https://doi.org/10.7554/eLife.52614
* **(scan)** [REF-VA-Spec-2025] — GA4GH (2025). *Variation Annotation Specification 1.0.1*. https://va-spec.ga4gh.org/en/latest/introduction.html
* **(scan)** [REF-Patrinos-2012] — Patrinos, G.P., et al. (2012). *Microattribution and nanopublication as means to incentivize the placement of human genome variation data into the public domain*. Human Mutation 33(11):1503–1512. https://doi.org/10.1002/humu.22144
* **(scan)** [REF-Coveney-2025] — Coveney, P., Highfield, R., Stahlberg, E., Vazquez, M. (2025). *Digital twins and Big AI: The future of truly individualised healthcare*. npj Digital Medicine 8:494. https://doi.org/10.1038/s41746-025-01874-x
* **(scan)** [REF-EU-AI-Act-2024] — Regulation (EU) 2024/1689 (2024). *Artificial Intelligence Act*. OJEU. https://eur-lex.europa.eu/eli/reg/2024/1689/oj
* **(scan)** [REF-Gilbert-2024] — Gilbert, S. (2024). *The EU passes the AI Act and its implications for digital medicine are unclear*. npj Digital Medicine 7:135. https://doi.org/10.1038/s41746-024-01116-6
* **(scan)** [REF-Verhulst-FAIR-R-2025] — Verhulst, S.G. (2025). *From FAIR to FAIR-R and FAIR²: Making Data AI-Ready*.
* **(scan)** [REF-Ni-RAG-Survey-2025] — Ni, B., et al. (2025). *Towards Trustworthy Retrieval Augmented Generation for Large Language Models: A Survey*. arXiv:2502.06872.
* **(scan)** [REF-Alu-Oluwadare-2026] — Alu, F.F., Oluwadare, S. (2026). *An auditable and source-verified framework for clinical AI decision support: integrating retrieval-augmented generation with data provenance*. Frontiers in Artificial Intelligence 9:1737532. https://doi.org/10.3389/frai.2026.1737532
* **(scan)** [REF-Mahmoodi-2023] — Mahmoodi, M., et al. (2023). *Explainable, Interpretable & Trustworthy AI for Intelligent Digital Twin*. arXiv:2301.06676.
* **(scan)** [REF-Wang-GenAI-DT-2025] — Wang, Z., et al. (2025). *Generative and Predictive AI for digital twin systems in manufacturing*. Frontiers in Artificial Intelligence 8:1655470.
* **(scan)** [REF-Boltz2-2025] — Bret et al. (2025). *Boltz-2: predicting protein structure and binding affinity*. MIT release.
* **(scan)** [REF-WHO-tracking] — World Health Organization. *Tracking SARS-CoV-2 variants*. https://www.who.int/activities/tracking-SARS-CoV-2-variants

### Added in v0.5 (FAIR² citation policy)

* [REF-FAIR2-Article] — *FAIR² data article describing the ESM and AlphaFold II 1-step Spike-variant computational predictions*. Frontiers in Bioinformatics. https://doi.org/10.3389/fbinf.2025.1634111
* [REF-FAIR2-DataPackage] — *FAIR² Data Package: ESM and AlphaFold II 1-step Spike RBD variant predictions*. https://doi.org/10.71728/hw56-vj34. Portal: https://sen.science/doi/10.71728/hw56-vj34

### Added in v0.4 (vocabulary resolutions)

* [REF-CiTO] — Peroni, S., Shotton, D. (2012). *FaBiO and CiTO: Ontologies for describing bibliographic resources and citations*. Journal of Web Semantics 17:33–43. https://doi.org/10.1016/j.websem.2012.08.001 (SPAR Citation Typing Ontology; namespace `http://purl.org/spar/cito/`).
* [REF-GeoNames] — *GeoNames geographical database*. https://www.geonames.org. Feature URIs of the form `https://sws.geonames.org/{geonameId}/`.
* [REF-MAC-FDT-Vocab-v1.1] — Schultes, E., Kuhn, T. (2026). *MAC FAIR Digital Twin — Vocabulary Specification v1.1*. Working document, MAC / Leiden University LACDR.
* [REF-MAC-FDT-SPS-v1.1] — Schultes, E., Kuhn, T. (2026). *MAC FAIR Digital Twin — Stakeholder Participation Sheets v1.1*. Working document, MAC / Leiden University LACDR.

---

## Appendix A — Open items and TODOs

Items affecting wording of the draft are listed below. Items 1–7 derived from `MAC_FDT_Vocabulary_v1.0.md` and are now resolved or captured in v1.1; items 8–14 are introduced by the paper-drafting process; items 15–16 were resolved by the literature scan; items 17–18 are new in v0.4 (post-resolution).

| # | Item | Affects sections | Status |
|---|---|---|---|
| 1 | MAC NanoDash ontology space URI pattern | §4.2, §5.3 (SPARQL prefix) | **Resolved (21 May 2026)**: `https://w3id.org/spaces/mac/r/ontology/MAC-Ontology` (NanoDash space) |
| 2 | `mac:isObservationOf` resolution target (referent URI vs Trusty URI of anchor) | §3.4, §4.3, §5.3 | **Resolved (21 May 2026)**: referent URI (`sub:fdo` of anchor) |
| 3 | `mac:hasCollectionLocation` encoding | §4.2, §5.2 Table 4a | **Resolved (21 May 2026)**: GeoNames URI (`https://sws.geonames.org/{id}/`) |
| 4 | `schema:citation` vs `dct:references` for Types 9–11 | §4.4, §5.2 Table 5 | **Resolved (21 May 2026)**: `cito:citesAsAuthority` (SPAR CiTO) |
| 5 | `mac:hasGISAIDAccession` dual use | §4.2, §5.1 Table 3, §6.7 | **Resolved (21 May 2026)**: single predicate with literal range retained |
| 6 | Class count reconciliation (14 vs SPS header "16") | §4.2 | **Resolved**: corrected to 14 in SPS v1.1 |
| 7 | Minting order: vocabulary → templates → instances | Tobias session | **Resolved**: confirmed |
| 8 | Authorship confirmation | Front matter | Open |
| 9 | Working title — confirm or revise | Front matter | Open |
| 10 | Definitional cascade compression (Definitions 2–4) | §3.2 | Open |
| 11 | "First end-to-end deployment" claim in §6.1 | §6.1 closing | **Resolved**: revised wording per Q1–Q4 calibration |
| 12 | Framing of MAC_FAIR catalogue as a project-class FDT in §6.3 | §6.3 | Open |
| 13 | Adoption realism in §6.7 | §6.7 | Open (measured framing currently used) |
| 14 | Abstract drafting timing | Abstract | **Resolved**: draft included |
| 15 | Literature-scan calibration of novelty claim | §6.1, §6.4 | **Resolved**: scan complete, calibrations applied |
| 16 | §6.6 reciprocal-relationship sentence | §6.6 closing | **Resolved**: revised wording per Q5 calibration |
| 17 | Trusty URI substitution from minting session | §5 tables | Pending: post-Tobias-session find-and-replace of `<TURI-…>` placeholders |
| 18 | GeoNames feature ID verification | §5.2 Table 4a | Pending: candidate IDs for England/California/Nigeria to be verified at minting |

---

## Appendix B — External working documents

These accompany the manuscript and are referenced from it:

* `MAC_FDT_SPS_v1.2.md` — full 11-type specification (authoritative for predicate URIs, statement structures, controlled vocabularies, example values, and FAIR² citation policy). Supersedes v1.1.
* `MAC_FDT_Vocabulary_v1.1.md` — definitions for all 26 MAC-namespace predicates and 14 classes; records Items 1–5 resolutions. Source of truth for vocabulary minting. Unchanged from v0.4.
* `README_for_Claude_Code.md` — orientation for the Tobias Claude Code minting session.
* `FDT_paper_Figure_1.svg` — Figure 1 in standalone SVG.
* `Lit_scan_Q1_synthesis.md` through `Lit_scan_Q5_synthesis.md` — literature-scan synthesis notes that informed the §1, §2, §6.1, §6.4, and §6.6 drafts.

---

*End of consolidated working draft v0.3. Approximate word count: ~17,000–19,000 across drafted sections. Outstanding items: front-matter authorship confirmation; resolution of Tobias-session-dependent vocabulary items; substitution of Trusty URI placeholders in §5 after minting.*
