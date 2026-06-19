# Changelog

## 0.1.0 — 2026-06
- Initial public release. Refactor of the project data-acquisition notebook into
  an installable, tested package.
- Secrets removed; all credentials read from the environment.
- Parameterised SQLite persistence with idempotent upserts.
- Sources: Europeana, Smithsonian, OAI-PMH, Scan the World, Hunt Museum,
  Google Landmarks. Enrichment: geocoding, spaCy place extraction, LLM
  classification. Conversion: GLB→USDZ, point-cloud cleaning.
