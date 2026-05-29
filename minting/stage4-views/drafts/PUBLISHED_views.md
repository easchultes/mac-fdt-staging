# Stage 4 — Standing SPARQL views pinned to incubator/project4

> **2026-05-29 follow-up fix.** Tobias flagged that two stray ViewDisplay
> nanopubs (created via NanoDash UI on 2026-05-28 after the P135 pin-action
> publish) incorrectly fed our grlc-queries into `gen:isDisplayOfView`,
> which expects a `gen:View` wrapper (not a bare grlc-query). Two
> invalidation nanopubs published on 2026-05-29 retire them; the P135
> pin-actions below are the canonical view-pinning mechanism and remain
> correct. See "Invalidations" section at the bottom.

Four grlc-query nanopubs + four pin-query action nanopubs published to
the live NSN on 2026-05-28. Each query is bounded (GROUP BY aggregates
or one fixed-referent knowlet) and remains scale-correct at Tranche-2
volume.

## Query nanopubs (4)

| Key | Trusty URI | Label |
|---|---|---|
| catalogue-summary       | `https://w3id.org/np/RAGlsCUDZrgFmlRQ8RNIpaWHaKAnRX7SGjEqOCGoWsM8A` | MAC FDT — catalogue summary by type |
| variants-by-who         | `https://w3id.org/np/RAlD3u-iOS5P95TlvydUePQCOqKyVsPLebBNTnu4lw7po` | MAC FDT — variants by WHO classification |
| observations-per-method | `https://w3id.org/np/RAIKnskDgF8ZX-hOIC1UKLSxDapH1K1FjkNKi5Or-A3ws` | MAC FDT — observations per method |
| alpha-knowlet           | `https://w3id.org/np/RAecvUbvUWiIOKP7ZEQk7hnUsb8lWWUr1lRbVN2PsSUSA` | MAC FDT — Alpha variant digital twin (knowlet) |

Publish window: 2026-05-28T10:52:37Z → 10:52:51Z (sequential).

Each query carries: `rdfs:label`, `dct:description`, `dct:license <Apache-2.0>`,
`<grlc/endpoint> <…/nanopub-query-1.1/repo/full>`, `<grlc/sparql>` (verbatim
SPARQL text). Created from template `RAEFAt-QcFK0Zhqfvls…` ("Defining a grlc
query"). Signed by `orcid:0000-0001-8888-635X` (Erik).

## Pin-query action nanopubs (4)

| Key | Pin action Trusty URI | Group tag |
|---|---|---|
| catalogue-summary       | `https://w3id.org/np/RAr2do6-Zm_F5tv9NP4iziOpRCX-mJUZzCqUfY-brnNRY` | Catalogue overview |
| variants-by-who         | `https://w3id.org/np/RAkwEb52MHk6Xe4uzOruIAkmGZAq4URDyg5bPqx4SXY1Y` | Situational dashboards |
| observations-per-method | `https://w3id.org/np/RAZge9g-AM2aYodnkKrlt6ag1s1QPYjTYBCJZaPezTZ6M` | Situational dashboards |
| alpha-knowlet           | `https://w3id.org/np/RAzEolNOqr8I1aiZpafpUxJfqBOQRdTapceYWjXCoEYAE` | Digital twin (worked example) |

Publish window: 2026-05-28T10:53:25Z → 10:53:38Z (sequential).

Each pin action asserts:
```
<https://w3id.org/spaces/knowledgepixels/incubator/project4>
    gen:hasPinnedQuery <query-Trusty-URI> .
<query-Trusty-URI> gen:hasPinGroupTag "<group-tag>" .
```
…and carries `npx:hasNanopubType <gen:hasPinnedQuery>`. Created from template
`RAuLESdeRUlk1Gc…` ("Declare a pinned query for a Space"). Signed by Erik
(admin of project4 via `gen:hasAdmin`).

Bare Trusty URI form used for `gen:hasPinnedQuery` value (matching
project4's existing pin-template convention) — not the MAC-FDO
NanoDash-UI-URL form.

## Verification

- All 8 nanopubs (4 queries + 4 pins): registry HEAD `307 → 200`, signature roundtrip **MATCH** — **8/8 OK**.
- SPARQL query on `…/repo/full`:
  ```
  SELECT ?query ?tag WHERE { …
    GRAPH ?pinA {
      <project4-space> gen:hasPinnedQuery ?query .
      ?query gen:hasPinGroupTag ?tag .
    }
  }
  ```
  returns **4 rows**, each with the correct query Trusty URI and group tag.
- Labels resolve via the query nanopubs' assertion graphs: all 4 query `rdfs:label`s match the published values.

## NanoDash space-view render

URL: `https://nanodash.knowledgepixels.com/space?id=https://w3id.org/spaces/knowledgepixels/incubator/project4`

The space view is a Wicket SPA — the curl-fetched HTML body (44,850 bytes) does not yet show the new pinned-query items (they render via JS after page load). The underlying NSN data is correct (verified via SPARQL above); the views will appear in a browser session. Manual browser inspection recommended for final visual confirmation.

## SPARQL queries — verbatim

All four queries share these prefixes:
```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX np:   <http://www.nanopub.org/nschema#>
PREFIX npa:  <http://purl.org/nanopub/admin/>
PREFIX npx:  <http://purl.org/nanopub/x/>
PREFIX dct:  <http://purl.org/dc/terms/>
PREFIX fdof: <https://w3id.org/fdof/ontology#>
PREFIX mac:  <https://w3id.org/spaces/mac/r/ontology/>
```
…and the signature-validation block:
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

### View A — catalogue summary by type
```sparql
SELECT ?type (COUNT(?thing) AS ?count) WHERE {
  <sig block>
  graph ?a {
    ?thing a fdof:FAIRDigitalObject .
    ?thing a ?type .
    FILTER(?type != fdof:FAIRDigitalObject)
    FILTER(STRSTARTS(STR(?type), "https://w3id.org/spaces/mac/r/ontology/"))
  }
} GROUP BY ?type ORDER BY DESC(?count)
```
Phase-1 dry-run: 11 rows, sums to 38.

### View B — variants by WHO classification
```sparql
SELECT ?whoClass (COUNT(?variant) AS ?count) WHERE {
  <sig block>
  graph ?a {
    ?obs a mac:WHOVariantClassification .
    ?obs mac:hasWHOClassification ?whoClass .
    ?obs mac:isObservationOf ?variant .
  }
} GROUP BY ?whoClass ORDER BY DESC(?count)
```
Phase-1 dry-run: VOI=2, VOC=1.

### View C — observations per method
```sparql
SELECT ?method (COUNT(?obs) AS ?count) WHERE {
  <sig block>
  graph ?a {
    ?obs ?methodPred ?method .
    VALUES ?methodPred { mac:hasPredictionMethod mac:hasExperimentalMethod mac:hasSurveillanceMethod }
  }
} GROUP BY ?method ORDER BY DESC(?count)
```
Phase-1 dry-run: ESM2=9, AlphaFold2=9, Bloom=3, AgMata=3, GISAID=3.

### View D — Alpha knowlet
```sparql
SELECT ?obs ?type ?label WHERE {
  <sig block>
  graph ?a {
    ?obs mac:isObservationOf <https://w3id.org/np/RA4BHII2Bz7HfpUkaSJqNmhjF8F7hyWpCJnvXYkA4EP_M/Alpha-RBD-Variant> .
    ?obs a ?type .
    FILTER(?type != fdof:FAIRDigitalObject)
    OPTIONAL { ?obs rdfs:label ?label . }
  }
} ORDER BY ?type
```
Phase-1 dry-run: 10 rows (Alpha's complete observation set).

## Architecture notes

- **Federated pin model** for project4: per-action nanopubs, no supersession of the space-definition (`RAuHVN25piF5…`). Erik's `gen:hasAdmin` on project4 is sufficient authorization.
- **Endpoint choice** `…/nanopub-query-1.1/repo/full` (signature-validated). Each result is restricted to nanopubs with valid signatures and not invalidated by their own signer.
- **Scale**: all four views remain bounded under Tranche-2 (~22 230+ prediction instances). View A's rows are capped by MAC type cardinality (11). View B by WHO class cardinality (3). View C by method cardinality (5). View D by Alpha's observation set (constant at 10 in the demonstration; would grow modestly if more observation types are added to Alpha, but not with Tranche 2 since Tranche 2 introduces NEW variants, not new Alpha observations).

## Invalidations (2026-05-29 fix)

After P135 we noticed two stray ViewDisplay nanopubs that Erik had
created via NanoDash UI experimentally on 2026-05-28 — they fed our
grlc-query nanopubs into `gen:isDisplayOfView`, but that predicate
expects a `gen:View` wrapper (e.g. `gen:ResourceView` with
`gen:hasViewQuery`), not a bare grlc-query. Tobias flagged the
mismatch.

Fix: two invalidation nanopubs, each asserting `this: npx:invalidates
<broken-trusty>` plus an `rdfs:comment` explanatory note. Both signed
by Erik and published 2026-05-29.

| Broken ViewDisplay | Invalidation nanopub |
|---|---|
| `https://w3id.org/np/RAq9o-TF0vcyIvK7Rn79IBIj1ePoZI1mAcErhVQjUb4vA` (catalogue-summary VD, 2026-05-28 11:14Z) | `https://w3id.org/np/RAUVFxrhms_YLANEQdoQjn8nNgDRW18ZcRx3m-mndVXRY` |
| `https://w3id.org/np/RAD5G7Z3kY14tsHLtunCJ26xpimAJ2-q1Thpf-4B8be84` (alpha-knowlet VD, 2026-05-28 17:56Z; Tobias's flag) | `https://w3id.org/np/RA0aGsMc41L8xLWfJeXpTUMz-py1vMpBJSIy1P13xaxX8` |

Publish window: 2026-05-29T07:30:24Z → 07:30:31Z (sequential, 7s).

### Post-invalidation verification

SPARQL on `…/repo/full`:
```sparql
SELECT ?n1 ?view WHERE {
  GRAPH npa:graph {
    ?n1 npa:hasValidSignatureForPublicKey ?pk .
    FILTER NOT EXISTS { ?inv npx:invalidates ?n1 ; … }
    ?n1 np:hasAssertion ?a .
  }
  GRAPH ?a {
    ?display a gen:ViewDisplay .
    ?display gen:appliesTo <project4-space> .
    ?display gen:isDisplayOfView ?view .
  }
}
```
returns **5 rows** — the 5 pre-existing, correctly-formed ViewDisplays
(simple-message-view, news-list-view, relevant-resource-view, and two
pinned-templates-view entries). The 2 broken ViewDisplays no longer
appear; direct invalidates-query confirms both are filtered.

The 4 P135 pin-action nanopubs (`gen:hasPinnedQuery` on the bare
queries) remain canonical for the "Queries" sidebar pinning on
project4.
