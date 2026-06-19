# heritage3d-retrieval

Retrieval and enrichment toolkit for **3D cultural-heritage data**. It harvests
records from cultural-heritage providers, normalises them into a single SQLite
table, and offers optional enrichment and 3D-asset conversion.

This package is a clean, publishable refactor of the project's original
data-acquisition notebook (`15_retrieval.ipynb`).

## Features
- **Sources:** Europeana, Smithsonian 3D, generic OAI-PMH (e.g. nfdi4ing,
  university libraries), Scan the World (MyMiniFactory), Hunt Museum, Google
  Landmarks.
- **Enrichment (optional):** geocoding (Google/geopy), place extraction (spaCy),
  LLM classification / geolocation (OpenAI-compatible).
- **Conversion (optional):** GLB → USDZ, point-cloud cleaning (Open3D).
- **Safe by design:** no hard-coded secrets, parameterised SQL, idempotent
  ingestion, structured logging, retries.

## Install
```bash
pip install -e .                 # core
pip install -e ".[europeana]"    # + Europeana extras
pip install -e ".[enrich]"       # + geocoding/NER/LLM
pip install -e ".[convert]"      # + 3D conversion
pip install -e ".[all]"          # everything + dev tools
```

## Configure
```bash
cp .env.example .env
# edit .env and add the keys for the features you need
```
All credentials are read from environment variables; see `.env.example`.

## Use (CLI)
```bash
heritage3d init-db
heritage3d europeana --query building --limit 500
heritage3d smithsonian --limit 1000
heritage3d oai nfdi4ing
heritage3d scan-the-world --query cathedral
```

## Use (library)
```python
from heritage3d.config import get_settings
from heritage3d.sources import europeana

europeana.ingest("building", limit=200, settings=get_settings())
```

## Data model
All sources write to one `object` table keyed by a unique `uid`
(see `src/heritage3d/models.py` and `docs/architecture.md`).

## Licence
MIT — see [LICENSE](LICENSE). Funded under the *3D Big Data Space for Cultural
Heritage* project (see `docs/` for the accompanying software deliverable).
