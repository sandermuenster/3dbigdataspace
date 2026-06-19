from heritage3d.http import build_session


def test_session_has_user_agent_and_adapters():
    s = build_session()
    assert "User-Agent" in s.headers
    assert s.get_adapter("https://example.org") is not None
