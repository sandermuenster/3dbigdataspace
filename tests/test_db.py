from heritage3d.db import connect, object_exists, upsert_object


def test_upsert_is_idempotent(tmp_path):
    db = tmp_path / "t.sqlite3"
    row = {"source": "Test", "uid": "u1", "name": "First", "uri": "http://x/1"}
    with connect(db) as conn:
        upsert_object(conn, row)
        upsert_object(conn, {**row, "name": "Updated"})  # same uid -> update
        assert object_exists(conn, uid="u1")
        cur = conn.execute("SELECT COUNT(*) AS n, MAX(name) AS name FROM object")
        r = cur.fetchone()
        assert r["n"] == 1
        assert r["name"] == "Updated"


def test_rejects_row_without_uid(tmp_path):
    with connect(tmp_path / "t.sqlite3") as conn:
        try:
            upsert_object(conn, {"source": "Test", "name": "no uid"})
            assert False, "expected ValueError"
        except ValueError:
            pass
