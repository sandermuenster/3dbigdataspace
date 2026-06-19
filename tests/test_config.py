import importlib

from heritage3d import config


def test_settings_from_env(monkeypatch, tmp_path):
    monkeypatch.setenv("HERITAGE3D_DB", str(tmp_path / "x.sqlite3"))
    monkeypatch.setenv("HERITAGE3D_MAX_RETRIES", "5")
    monkeypatch.setenv("EUROPEANA_API_KEY", "abc123")
    importlib.reload(config)
    s = config.get_settings()
    assert str(s.database_path).endswith("x.sqlite3")
    assert s.max_retries == 5
    assert s.require("europeana_api_key") == "abc123"


def test_require_missing_raises(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    importlib.reload(config)
    s = config.get_settings()
    try:
        s.require("openai_api_key")
        assert False, "expected RuntimeError"
    except RuntimeError as exc:
        assert "OPENAI_API_KEY" in str(exc)
