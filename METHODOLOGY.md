# Methodology and pre-specified evaluation protocol

## Epistemic layers
FACT: attributed observations or institutional assessments, each with its vintage.
INFERENCE: a possible interpretation or transmission mechanism.
HYPOTHESIS: the author's underpricing and December–June timing claim.
SCENARIO: conditional outcomes, not forecasts presented as observations.

## Baseline and transformations
Cutoff: 25 October 2026 (Europe/Madrid). Only evidence available by this cutoff is admissible. Record actual later retrieval dates in future updates. No probabilistic risk score. No missing-value imputation. Charts use selected release-table observations rather than a complete historical download. The source manifest contains institution, URL, publication/reference information and retrieval date; baseline records include individual reference dates and units. Series metadata identify transformation and vintage. EA21 composition is used for 2026. Debt is a stock-to-trailing-GDP ratio; HICP is an annual rate; BLS is net percentage of banks, not percentage loan growth. Brent is spot FOB, not an exchange futures contract.

Energy HICP: use final 18.9%, not the 18.8% flash estimate. Consumer confidence: September −16.8 is explicitly derived from October −17.9 and its reported 1.1-point monthly fall; September was revised following reinclusion of Italian data. There is an Italian methodological break between August and September. September ESI 97.9 is the September publication vintage; do not imply it includes October revisions. Its previous-month 98.4 is not plotted. Market valuations are supported by qualitative ESMA evidence; this is not a quantitative valuation backtest.

## Market test
Benchmark fixed in advance: EURO STOXX 50, SX5E, EUR price-return daily closes of the STOXX index. Start the running peak with the cross-checked 23 October 2026 close of 6,068.22, then include every subsequent trading-day close through the evaluation date. Drawdown D(t) = 100 × (P(t) / max(P(s), s from 23 October 2026 through t) − 1). A qualifying severe-repricing event must FIRST cross D ≤ −20% during 1 December 2026–30 June 2027. If an episode first crosses before 1 December, it does not validate the post-election timing claim merely by remaining below −20% during December. Record the first crossing date for each threshold. An episode runs from a running peak until that peak is regained; a recovery above −20% alone does not reset it. Only a genuinely new peak-to-trough episode can supply a new first crossing. Report earlier episodes separately.

Descriptive thresholds: D ≤ −10% correction; D ≤ −20% severe bear-market repricing. Crash convention: ≥25% peak-to-trough fall within 60 trading sessions, with the episode’s first crossing of the −25% threshold and its qualifying trough in the observation window. These are research conventions, not universal definitions. Freeze this benchmark and do not switch to whichever index later falls most. Price return excludes dividends. A concentrated blue-chip index does not cover every European asset class.

STOXX verifies SX5E, EUR Price Return, ISIN EU0009658145. The 23 October 2026 close of 6,068.22 is cross-checked against Yahoo Finance and Investing.com historical data. These are separate publishers, not proof of independent upstream feeds. An official dated historical export was not available through the accessible interface; no official export is claimed. The seed is archived in `data/market-seed.json` with source rows and access limitations. Future observations must identify their provider and use the same index/variant; do not mix intraday observations, futures or dividend-return series. This documented source limitation does not prevent publication; future evaluation still requires complete dated closing observations.

## Independent channel tests
Evaluate monthly using the latest releases available at each month-end. Relative to the frozen baseline, a deterioration flag is:
1. Sovereign / fiscal vulnerability: EA debt/GDP ≥89.8% (baseline 88.8 + 1.0 percentage point), in a subsequent comparable quarterly release. Debt/GDP measures fiscal vulnerability, not real-time sovereign market stress; report bond-spread evidence separately, without changing the primary test.
2. Energy/inflation: final EA headline annual HICP ≥4.3% (baseline 3.8 + 0.5 pp) for two consecutive monthly releases. Energy and headline inflation count as ONE channel; oil corroborates but is not an extra vote.
3. Credit/liquidity: actual BLS enterprise net tightening ≥12% (baseline 7 + 5 pp) in a subsequent survey. Expected tightening does not count. Fund liquidity evidence is corroborative, not a second vote.
4. Real economy/confidence: CCI ≤−19.9 (baseline −17.9 − 2 points) for two consecutive releases. Use comparable methodology; if a break prevents comparison, mark unavailable. ESI corroborates but does not count separately.
5. Geopolitical/operational: ECB, ESMA or an affected public authority documents a NEW cross-border disruption of energy supply, payments, settlement or critical financial infrastructure after the cutoff. Record exact incident dates, scope and source. Existing warnings alone do not qualify. This test requires a documented human assessment, with ambiguity marked unresolved.

These are economically distinct channels, not a claim of statistical independence. They can share causes. Thresholds are deliberately transparent author conventions, not statistically calibrated cutoffs. Report continuous observations and sensitivity to halving/doubling the numeric channel thresholds alongside the primary result; never replace the primary thresholds after seeing outcomes.

## Outcome rules
Polycrisis/severe repricing: the episode’s first market drawdown crossing of ≤−20% occurs during the window AND at least three of the five non-market flags active at the same month-end, with that qualifying first crossing in that month or either preceding month. Qualifying flags must use releases available by 30 June 2027. A stock decline and one shock are insufficient. Correlation and co-occurrence do not establish causal contagion.
Stress without crash: at least three deterioration flags active but no qualifying first ≥20% threshold crossing in the window. This supports vulnerability accumulation but contradicts the severe-repricing timing claim.
Resilience: no qualifying first ≥20% threshold crossing and at least three numeric channels improve by the same absolute thresholds used above, with the same persistence requirements (debt ≤87.8%; headline ≤3.3%; enterprise BLS ≤2%; CCI ≥−15.9). This materially weakens the thesis.
Mixed/unresolved: all other combinations, including severe repricing without three channels, or insufficient observations. Report missing evidence; do not equate unavailable data with improvement or deterioration. Failure to observe a qualifying first crossing by June 30 counts against the primary timing claim regardless of category. A pre-window severe episode is disclosed separately and does not itself demonstrate resilience.

## Vintage and publication limitations
No post-cutoff backfill in the original baseline. Later revisions go in updates with both old and new values. The June 30 real-time verdict can miss later releases describing June; append a separately labeled retrospective assessment, never overwrite the real-time verdict. Sources are live URLs and may change. This package preserves manually extracted numerical snapshots and evidence notes, not complete certified archives of all source pages. Primary-source retrieval was through text extraction; numeric transcription was checked against the returned tables. External authors have not endorsed this thesis. A SHA-256 and local commit do not provide third-party proof of the claimed freeze date. Final freeze, publication timestamp and final tag are still pending. The thesis text is author-approved.

## Institutional context
In its May 2026 Financial Stability Review (Overview, p. 6), the ECB links geopolitical and fiscal risks, non-bank liquidity and leverage exposures, and bank credit, liquidity and funding vulnerabilities. It warns that their joint materialisation could intensify financial instability. This institutional assessment does not endorse the author’s polycrisis forecast or its timing.

## Authorship
Research & analysis — Jonatan Pabón

Economics · University of Málaga
