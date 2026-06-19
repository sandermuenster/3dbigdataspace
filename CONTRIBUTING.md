# Contributing

Thanks for your interest in improving **heritage3d-retrieval**.

## Development setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

## Before opening a pull request
- Format and lint: `black . && ruff check .`
- Type-check: `mypy src`
- Run tests: `pytest`
- Never commit secrets. Credentials belong in `.env` (git-ignored). Add new
  settings to `config.py` and document them in `.env.example`.

## Adding a new data source
1. Create `src/heritage3d/sources/<name>.py`.
2. Provide a **pure** `map_*` function (record -> normalised dict) and an
   `ingest()` driver that uses `db.connect` and `sources.base.ingest_records`.
3. Add a unit test for the mapping function (no network).
4. Wire a subcommand into `cli.py`.

## Code of conduct
Be respectful and constructive. By contributing you agree to license your work
under the project's MIT licence.
