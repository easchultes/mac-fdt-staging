# Stage 4 SPARQL Verification Results (PROMPT 5 PHASE 6)

Endpoint: `https://query.knowledgepixels.com/repo/full`
Run UTC: 2026-06-02 (post 60s indexing wait)

## Q1 — Stage 4 supersessions (expect 4 distinct pairs)

```sparql
PREFIX npx: <http://purl.org/nanopub/x/>
SELECT (COUNT(*) AS ?n) WHERE {
  SELECT DISTINCT ?new ?old WHERE {
    GRAPH ?g {
      ?new npx:supersedes ?old .
      VALUES ?new {
        <https://w3id.org/np/RAPZD8J9dac_FbBmOsjx_5vggqTFlprf_UpYUHgfJGHaM>
        <https://w3id.org/np/RAEUR-AJ6AbnFBylxYVZ2y4eyY3UIRn5gBTCSugIDF04w>
        <https://w3id.org/np/RArre4b4u68anFDe6CknbAVLLtOBSGy1Izm-J3XGjILTs>
        <https://w3id.org/np/RAM9wl0_gIlu3Txr3st7Um1lNsMFLwOKcbaBMRdWNmwrY>
      }
    }
  }
}
```

Result: **4** ✅ (4/4 expected)

Each of the 4 v2 Stage 4 nanopubs has its `npx:supersedes <v1>` triple indexed.

## Q2 — Cross-reference resolution

```sparql
PREFIX gen: <https://w3id.org/kpxl/gen/terms/>
SELECT ?subj ?pred ?obj WHERE {
  GRAPH ?g {
    ?subj ?pred ?obj .
    FILTER(?obj IN (
      <https://w3id.org/np/RAPZD8J9dac_FbBmOsjx_5vggqTFlprf_UpYUHgfJGHaM>,
      <https://w3id.org/np/RArre4b4u68anFDe6CknbAVLLtOBSGy1Izm-J3XGjILTs/fdt-alpha-knowlet-view>
    ))
    FILTER(?subj IN (
      <https://w3id.org/np/RArre4b4u68anFDe6CknbAVLLtOBSGy1Izm-J3XGjILTs/fdt-alpha-knowlet-view>,
      <https://w3id.org/np/RAM9wl0_gIlu3Txr3st7Um1lNsMFLwOKcbaBMRdWNmwrY/display>
    ))
  }
}
```

Result: **2 rows** ✅ (≥2 expected)

```csv
subj,pred,obj
<wrapper-v2-referent>,gen:hasViewQuery,<query-v2-Trusty>            ← bare-Trusty form
<viewdisplay-v2-subject>,gen:isDisplayOfView,<wrapper-v2-referent>  ← referent form
```

Both cross-references in the asymmetric URI-form pattern (per P38/R38 lock):
- Wrapper → Query via **bare Trusty URI** (P38: query accessed as artifact)
- ViewDisplay → Wrapper via **`gen:View` referent URI** (P38: View has FDO-like referent)

## Confirmation: 4/4 supersessions + 2/2 cross-references indexed; no retry needed
