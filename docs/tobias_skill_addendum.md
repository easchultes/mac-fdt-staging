# Nanopub Skill — Operational Addendum

**Author:** Erik Schultes
**Date:** 2026-06-01
**Context:** Observations from the MAC FDT v2 cleanup pass, Stage 3 catalogue re-mint with `/`-form addressing convention.
Companion to the prior PR #1 nanopub-skill addition (https://github.com/knowledgepixels/nanopub-skill/pull/1) — publisher-facing vs admin-derived retraction distinction.

These four operational findings emerged during the cleanup pass from PROMPTs 1.5 through 3 (May 31 – June 1, 2026). They are offered as input to the nanopub-skill maintenance work, not yet vetted against the broader ecosystem.

---

## Section 1 — `npx:retracts` subject convention

**Observation.** nanopub-java's `retract` subcommand emits

```turtle
<publisher-ORCID> npx:retracts <target-Trusty> .
```

where the **subject is the publisher's ORCID**, not the retracting nanopub itself. Manually constructed retraction nanopubs using

```turtle
this: npx:retracts <target-Trusty> .
```

(subject = retraction nanopub) were **registry-rejected** during the upstream cleanup pass (PROMPT 1.5 / PROMPT 2.0). All three registries returned:

```
HTTP 400 — Error processing nanopub: Nanopublication not supported
```

The auto-retract form succeeded immediately. The convention check is registry-side, not signature-side: the nanopub validates cryptographically but is refused on policy grounds.

This empirically confirms PR #1's publisher-facing convention as the operational truth.

**Suggested skill addition.** An explicit example of the correct subject form for hand-authored retraction TriGs:

```turtle
# Correct (registry-accepted)
sub:assertion {
  <https://orcid.org/your-orcid> npx:retracts <https://w3id.org/np/RA...target> .
}
```

```turtle
# Incorrect (registry-rejected as "Nanopublication not supported")
sub:assertion {
  this: npx:retracts <https://w3id.org/np/RA...target> .
}
```

*Origin: PROMPTs 1.5 / 2.0 — upstream `#`-form defective Project + 2 Dataset retraction work.*

---

## Section 2 — Content-negotiation for registry GET

**Observation.** The nanopub registry (`registry.petapico.org`, `registry.knowledgepixels.com`, and `w3id.org/np/<Trusty>`) returns an HTML viewer page by default — a browser-oriented wrapper around the nanopub display. Raw TriG content requires an explicit `Accept` header.

During Pass-1 verification, the first GET on the freshly-published Alpha-RBD-Variant Trusty URI was misclassified as a failure because the verifier read the HTML wrapper's `<title>Nanopublication RA... - Nanopub Registry</title>` rather than the TriG body. Switching to:

```bash
curl -s -H "Accept: application/trig" -L "https://w3id.org/np/<Trusty>"
```

returns the raw TriG, beginning with `@prefix this: <https://w3id.org/np/<Trusty>>`.

This matters for any verification script that wants to check substantive content (not just HTTP 200): the registry returns 200 with an HTML 404 page for non-existent nanopubs, so HTTP status alone is not a liveness indicator.

**Suggested skill addition.** A one-line note in the registry-GET example specifying `Accept: application/trig` for content-level verification.

*Origin: PROMPT 3 PHASE 2 — Pass-1 publish-verify loop, Alpha-RBD-Variant first verification.*

---

## Section 3 — SPARQL `DISTINCT` on `/repo/full`

**Observation.** The `/repo/full` SPARQL endpoint (at `query.knowledgepixels.com`) indexes the same triple across multiple graph views — empirically observed: 3× per triple, consistent with per-server cache views being indexed alongside the canonical assertion graph.

PROMPT 3 Q1 (`npx:supersedes` verification across 38 v2 mints) returned a raw `COUNT(*)` of **114** = 38 × 3. The `SELECT DISTINCT ?new ?old` formulation correctly yielded **38**. Without `DISTINCT`, count-based verification queries will systematically over-report by an integer multiplier.

This is not a bug — the multi-graph indexing is a feature for queries that join across cache and admin views — but it is a footgun for verification scripts that expect unique-triple counts.

**Suggested skill addition.** `DISTINCT` is **recommended** (not optional) for any count-based verification query against `/repo/full`. Example:

```sparql
# Correct: yields the actual number of distinct supersession pairs
SELECT (COUNT(*) AS ?n) WHERE {
  SELECT DISTINCT ?new ?old WHERE {
    GRAPH ?g { ?new npx:supersedes ?old }
  }
}

# Misleading: returns a multiple of the actual count
SELECT (COUNT(*) AS ?n) WHERE {
  GRAPH ?g { ?new npx:supersedes ?old }
}
```

*Origin: PROMPT 3 PHASE 4 — Q1 supersession verification on `/repo/full`.*

---

## Section 4 — Publish-to-GET propagation lag

**Observation.** Immediate HTTP GET on a freshly published Trusty URI returned **404 in 2 of 8** Pass-1 publishes during PROMPT 3 PHASE 2. The publish-side registry (`registry.petapico.org`) confirmed the nanopub was published; the read-side resolution (via `w3id.org/np/<Trusty>` redirecting to one of the registry mirrors) hadn't yet propagated.

A 10-second wait + retry resolved both first-attempt failures. Pass-2 (30 instances) used a pre-emptive 5-second wait between publish and GET, with optional 10-second retry on 404; all 30 verified on first or second try. No third-retry was needed across the 38-instance batch.

**Suggested skill addition.** Recommended publish-verify pattern:

```bash
java -jar nanopub-1.88.0-jar-with-dependencies.jar publish <signed.trig>
sleep 5
curl -sI -H "Accept: application/trig" \
  -o /dev/null -w "%{http_code}\n" \
  "https://w3id.org/np/<expected-Trusty>"
# If 404, sleep 10 and retry once. Both retries succeeded across the
# 38-instance PROMPT 3 batch.
```

The receiving registry is `registry.petapico.org`. Read-side resolution may reach any of the registered mirrors; propagation between them takes seconds, not minutes, but is non-zero.

*Origin: PROMPT 3 PHASE 2 — Pass-1 Epsilon-RBD-Variant first verification (404 on immediate GET, resolved on retry); pattern formalized for Pass-2.*

---

## Closing

These observations are offered as input to the nanopub-skill maintenance work; they are not yet vetted against the broader ecosystem (other registry mirrors, other client implementations, other jar versions). Operationally validated against:

- `nanopub-java 1.88.0` (signing, retract, publish, check subcommands)
- `registry.petapico.org` (publish-side)
- `registry.knowledgepixels.com` (resolution-side, also SPARQL endpoint)
- `w3id.org/np/<Trusty>` (canonical resolution alias)
- JDK 21 (the jar requires class file version 65)

Contact: Erik Schultes <https://orcid.org/0000-0001-8888-635X>
