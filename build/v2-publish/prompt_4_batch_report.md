# PROMPT 4 — Doc Patch Batch Summary

Date: 2026-06-01
Branch: `cleanup-upstream-v2` (off `9e47c33` PROMPT 3 commit)
Scope: 5 documentation items queued in SESSION_STATE.md during PROMPT 3 PHASE 6.3.

## Items applied

| # | File | Action | Status |
|---|---|---|---|
| 1 — Epsilon `L124R` → `L452R` (Epsilon context) | `specs/MAC_FDT_SPS_v1_4.md` | 1 replacement (variant table row, line 232) | ✅ |
| 1 — Epsilon `L124R` → `L452R` (Epsilon context) | `data/FDT4Claude_small_v1_2.csv` | 2 replacements (ESM row line 4, AlphaFold row line 5) | ✅ |
| 1 — Epsilon historical-context narrative | `minting/stage3-instances/generator/instance_configs/type1_epsilon.py` | docstring rewrite (past tense; references this cleanup pass) | ✅ |
| 1 — Epsilon historical-context narrative | `docs/implementation_guide.md` | 2 paragraphs rewritten (lines 1236 and 2387, past tense) | ✅ |
| 2 — §6 Appendix C narrative correction (dct:source count) | `docs/implementation_guide.md` | **NO EDIT APPLIED** — see note below | ✅ (no-op confirmed) |
| 3 — Prefix-convention note | `docs/implementation_guide.md` (§6 Appendix C.10 — NEW subsection) | full Symptom/Cause/Resolution block, including retraction URIs + JDK 21 requirement | ✅ |
| 4 — File-name vs referent-local-name asymmetry footnote | `docs/implementation_guide.md` (§6 Appendix A.3, expanded existing footnote) | replaced 1-paragraph footnote with explicit version (count, example, byte-identity claim, both use cases, supersession_registry.md pointer, v3 forward-looking note) | ✅ |
| 5 — Tobias addendum | `docs/tobias_skill_addendum.md` (NEW file, 6.6 KB, 4 sections + closing) | full draft per spec with §1-§4 + Origin footers + PR #1 URL inline | ✅ |

## PHASE 3 finding (logged per user directive)

**No edit applied** — `docs/implementation_guide.md` narrative was already correct on `dct:source`. The SESSION_STATE.md anomaly framing from PROMPT 3 PHASE 6.3 was the artifact, not the guide.

Tracing artifact: the "absent on 17" claim was in **PROMPT 1's spec text** (the audit's sanity-check #7 expected value), NOT in the implementation guide. PROMPT 3's commit message and SESSION_STATE.md entry inaccurately framed this as "§6 Appendix C narrative correction needed in implementation guide". That framing was wrong; the guide narrative makes no such erroneous claim (verified by `grep -n "absent on 17|17 instances|14 instances|absent"` returning zero matches anywhere in the guide).

SESSION_STATE.md will be amended at PHASE 8 staging to replace the original entry with the corrected framing (per Erik's directive in PROMPT 4 PHASE 3 confirmation).

## Verification counts

```
L124R remaining:
  specs/MAC_FDT_SPS_v1_4.md                      : 0  (target — replaced)
  data/FDT4Claude_small_v1_2.csv                 : 0  (target — replaced)
  type1_epsilon.py                               : 1  (past-tense narrative remnant; expected)
  docs/implementation_guide.md                   : 2  (past-tense narrative remnants; expected)

L452R now present:
  specs/MAC_FDT_SPS_v1_4.md                      : 1
  data/FDT4Claude_small_v1_2.csv                 : 2
  type1_epsilon.py                               : 4
  docs/implementation_guide.md                   : 3

§6 Appendix C.10 (prefix convention) present     : line 2454
§6 Appendix A footnote (file-name asymmetry)     : line 2214
docs/tobias_skill_addendum.md                    : 6618 bytes
  - "## Section " headings                       : 4 (✅)
  - "Origin: PROMPT" footers                     : 4 (✅)
```

## Out-of-scope L124R locations (preserved as historical audit trail)

Per user directive at PHASE 2 confirmation, the following 4 files were left unmodified:

- `specs/MAC_FDT_SPS_v1_3.md` (superseded SPS revision)
- `specs/MAC_FDT_SPS_v1_2.md` (superseded SPS revision)
- `minting/stage2-templates/SESSION_STATE.md` (session-state record)
- `minting/stage3-instances/drafts/PUBLISHED_type1_instances.md` (Stage 3 publication record)

These retain `L124R` as a historical record of when the typo lived in those documents. The current SPS (v1.4), current CSV, and current generator config now all carry `L452R`. The narrative explaining the historical typo references it explicitly in past-tense form (in `type1_epsilon.py` docstring and `docs/implementation_guide.md` worked-example narrative + Appendix C.1 cleanup-pass log).

## Files modified

```
specs/MAC_FDT_SPS_v1_4.md                                              (1 edit)
data/FDT4Claude_small_v1_2.csv                                         (2 edits)
minting/stage3-instances/generator/instance_configs/type1_epsilon.py   (1 docstring rewrite)
docs/implementation_guide.md                                           (4 edits: §3 paragraph, §6 App A footnote, §6 App C.1 bullet, §6 App C.10 insert)
docs/tobias_skill_addendum.md                                          (NEW)
build/v2-publish/prompt_4_batch_report.md                              (NEW — this file)
```

## Pending at PHASE 8 staging

SESSION_STATE.md entry amendment (per PROMPT 4 PHASE 3 directive):
- REMOVE: "Spec audit text: Type 1 anchors do carry dct:source (FAIR² DOI), §6 Appendix C narrative correction needed."
- ADD: "PROMPT 1 audit sanity-check #7 expected dct:source absent on 17 instances; ground truth was 14 (Type 1 anchors carry dct:source → FAIR² Package DOI, a permanent identifier unchanged v1→v2). Implementation Guide narrative was already correct on this point; the discrepancy was confined to the audit spec text, not the guide itself."

This amendment lands in PHASE 8 (commit batch).
