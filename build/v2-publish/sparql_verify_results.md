# SPARQL Verification Results — Stage 3 v2 publish (PROMPT 3 PHASE 4)

Endpoint: `https://query.knowledgepixels.com/repo/full`
Run UTC: 2026-06-01T11:16:59Z

## Summary

| Query | Expected | Actual | Status |
|---|---|---|---|
| Q1 — npx:supersedes (v2 → v1, distinct pairs) | 38 | 38 | ✅ |
| Q2 — dct:isPartOf to Project v2 referent (38 v2 Stage 3 referents) | 38 | 38 | ✅ |
| Q3 — dct:source to Dataset v2 referents (distinct ?fdo ?dataset pairs) | 21 | 21 | ✅ |
| Q4 — mac: cross-refs to Pass-1 v2 referents (distinct ?subject ?pred ?target) | 57 | 57 | ✅ |

## Q1 detail — supersedes by class

Sample rows (4 first; full set 38):
```csv
new,old
https://w3id.org/np/RAngbyT2iZe4xYUcPnTnDFKDaiL5-tSmoUYzF9RK3LHdE,https://w3id.org/np/RA4BHII2Bz7HfpUkaSJqNmhjF8F7hyWpCJnvXYkA4EP_M
https://w3id.org/np/RADWPV5jeyK-7pxen6hMrxjP4hPNLk3EJTibcxJCInv30,https://w3id.org/np/RAbyuWWdW-j1rYt7Eqnva6aBvMyTkM9_Ka2FbA9dJHR7s
https://w3id.org/np/RA8yS9sU1tq87fXelVb4Q7uwjpoDXOsoelXM5--tfu6IQ,https://w3id.org/np/RAikllrKWQoo81RYYvGJjWfzE0QiGrLquMMIwDD6xem2s
https://w3id.org/np/RAV_9iAUAyUyNLhVQxpTaE54ko_liTnBpIarZBnkBcbgw,https://w3id.org/np/RADJxd-U-p7VpA01uXlsp3nkUo3oXFMSOam04-fcF0ZyM
```

## Q4 detail — cross-refs by predicate

```csv
predicate,n
https://w3id.org/spaces/mac/r/ontology/hasSurveillanceMethod,3
https://w3id.org/spaces/mac/r/ontology/hasExperimentalMethod,3
https://w3id.org/spaces/mac/r/ontology/isObservationOf,30
https://w3id.org/spaces/mac/r/ontology/hasPredictionMethod,21
```
