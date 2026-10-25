# FAULT LINES

European Macro-Financial Stress Thesis — 2026/27. An ex-ante European macro-financial stress thesis tracking potential fault lines into 2027. Information cutoff: 25 October 2026.

Research & analysis — Jonatan Pabón  
Economics · University of Málaga

**Original thesis v1.0 — frozen and published on 25 October 2026.**

Live site: https://jonapv.github.io/fault-lines-2026/

## Read and validate
Open `index.html` directly in a browser. Charts and interactions work offline; external source links need internet access. HTML, CSS, vanilla JavaScript and SVG. No installation, backend, API keys, analytics or AI calls.

Run `python3 scripts/build_snapshot.py` for focused validation. Add `--build` to refresh the ignored `dist/` preview directory. GitHub Pages can serve the tracked root directly; `.nojekyll` is included. No deployment workflow is installed.

## Research files
- `thesis/THESIS.md`, `thesis/SHA256SUMS`: exact author-approved text and frozen SHA-256.
- `METHODOLOGY.md`: benchmark, first-crossing timing rules, non-market tests, falsification and limitations.
- `data/baseline.json`: ten macro indicators with dates and provenance.
- `data/sources.json`: official sources plus explicitly identified market-data fallback sources.
- `data/market-seed.json`: SX5E EUR Price Return, 23 October 2026 close 6,068.22; Yahoo Finance and Investing.com historical cross-check, with official-export limitation disclosed.
- `data/series.json`, `data/series/*.json`: all five charts' observations and provenance.
- `updates/README.md`: subsequent observations and corrections.
- `assets/social-preview.png`: 1200×630 editorial social preview; `assets/favicon.svg`: FL favicon.

## Freeze and publication
Public repository: https://github.com/jonapv/fault-lines-2026. GitHub Pages deploys directly from `main`, repository root.

The ≥20% threshold must first be crossed within 1 December 2026–30 June 2027 for a qualifying episode. A pre-December crossing cannot qualify just by persisting. Thresholds and benchmark are unchanged.

The official STOXX interface verified index identity but did not provide an accessible reproducible historical export for the seed. The documented fallback is an accepted limitation, not a claim of an official archive. Use complete dated closes for future evaluation.

Information cutoff and thesis freeze: 25 October 2026. Public publication date: 25 October 2026. The annotated tag `thesis-v1.0-2026-10-25` identifies the publication commit. Preserve the author-approved thesis unchanged and record subsequent observations under `updates/`. Do not move the tag or backdate publication. A hash checks bytes; it is not proof of a public timestamp.

Canonical and `og:url`: https://jonapv.github.io/fault-lines-2026/. Open Graph and Twitter image: https://jonapv.github.io/fault-lines-2026/assets/social-preview.png (1200×630). Crawler previews may depend on cache and crawl timing.

Review screenshots, private handoff notes and Git bundles are excluded from the public tree. The published research consists of substantive methodology, source records, data, thesis and site assets.
