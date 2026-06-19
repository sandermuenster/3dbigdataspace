# Architecture

```
            +-------------------+
 providers  |  sources/*.py     |  map_* (pure) -> normalised dict
 (HTTP/OAI) |  base.ingest_*    |
            +---------+---------+
                      | upsert_object (parameterised)
                      v
            +-------------------+      +------------------+
            |  db.py (SQLite)   |<-----|  enrich/*.py     |
            |  object table     |----->|  geocode/NER/LLM |
            +---------+---------+      +------------------+
                      |
                      v
            +-------------------+
            |  convert/*.py     |  GLB->USDZ, point clouds
            +-------------------+

 cross-cutting: config.py (env), http.py (session+retry), logging_utils.py
```

## Principles
- **Single normalised schema** (`models.OBJECT_FIELDS`) shared by all sources.
- **Pure mapping functions** are unit-tested without network access.
- **Idempotent ingestion** via a UNIQUE `uid` and `INSERT ... ON CONFLICT`.
- **Lazy heavy imports** keep the base install small.
