"""Shared fixtures for the distributed pipeline tests."""

import os
import sys
import textwrap
import tempfile
from pathlib import Path

import pytest

# ── Make the distributed package and generator importable ────────────────────
_DISTRIBUTED = Path(__file__).resolve().parents[1] / "distributed"
_GEN_DIR = _DISTRIBUTED / "tasks" / "generator"

for _p in [str(_DISTRIBUTED), str(_GEN_DIR)]:
    if _p not in sys.path:
        sys.path.insert(0, _p)


@pytest.fixture(scope="session")
def stub_parser_dir():
    """Write two minimal Python URL-parser scripts to a persistent temp dir.

    Returns dict mapping name -> command string.
    Scope=session so we only write the files once.
    """
    tmpdir = tempfile.mkdtemp(prefix="test_parsers_")

    strict = Path(tmpdir) / "parser_strict.py"
    strict.write_text(textwrap.dedent(f"""\
        #!/usr/bin/env python3
        import sys, json
        from urllib.parse import urlparse
        url = sys.argv[1] if len(sys.argv) > 1 else ""
        try:
            p = urlparse(url)
            print(json.dumps({{
                "scheme":    p.scheme   or None,
                "authority": p.netloc   or None,
                "userinfo":  (p.username + (":" + p.password if p.password else "")) if p.username else None,
                "username":  p.username or None,
                "password":  p.password or None,
                "host":      p.hostname or None,
                "port":      str(p.port) if p.port else None,
                "path":      p.path     or None,
                "query":     p.query    or None,
                "fragment":  p.fragment or None,
            }}))
        except Exception as e:
            print(json.dumps({{"error": str(e)}}))
    """))
    strict.chmod(0o755)

    lenient = Path(tmpdir) / "parser_lenient.py"
    lenient.write_text(textwrap.dedent(f"""\
        #!/usr/bin/env python3
        import sys, json, re
        from urllib.parse import urlparse
        url = sys.argv[1] if len(sys.argv) > 1 else ""
        try:
            working = url if re.match(r'^[a-zA-Z][a-zA-Z0-9+\\-.]*://', url) else "x://" + url
            p = urlparse(working)
            scheme = p.scheme if not working.startswith("x://") else None
            print(json.dumps({{
                "scheme":    scheme,
                "authority": p.netloc   or None,
                "userinfo":  (p.username + (":" + p.password if p.password else "")) if p.username else None,
                "username":  p.username or None,
                "password":  p.password or None,
                "host":      p.hostname or None,
                "port":      str(p.port) if p.port else None,
                "path":      p.path     or None,
                "query":     p.query    or None,
                "fragment":  p.fragment or None,
            }}))
        except Exception as e:
            print(json.dumps({{"error": str(e)}}))
    """))
    lenient.chmod(0o755)

    return {
        "strict":  f"{sys.executable} {strict}",
        "lenient": f"{sys.executable} {lenient}",
    }


@pytest.fixture
def db(stub_parser_dir, tmp_path):
    """Initialise a fresh file-based SQLite DB per test with two stub libraries.

    Uses tmp_path (pytest-provided per-test temp dir) so each test gets a
    completely isolated database. File-based SQLite avoids the NullPool /
    :memory: issue where each connection sees a different in-memory database.
    """
    db_path = str(tmp_path / "test.db")

    # Directly replace the engine in core.database so every subsequent
    # get_session() / init_db() / drop_db() call uses this test-specific DB.
    from sqlalchemy import create_engine
    from sqlalchemy.pool import NullPool
    from sqlalchemy.orm import sessionmaker
    import core.database as _db_mod

    new_engine = create_engine(
        f"sqlite:///{db_path}",
        echo=False,
        pool_pre_ping=True,
        poolclass=NullPool,
    )
    _db_mod.engine = new_engine
    _db_mod.SessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=new_engine
    )

    from core.database import init_db, drop_db, get_session
    from core.models import Library, ParserLanguage, ParserWeights

    drop_db()
    init_db()

    def _zero(group):
        return {
            "p_valid":   {"logit": 0.0, "group": group},
            "p_invalid": {"logit": 0.0, "group": group},
            "p_null":    {"logit": 0.0, "group": group},
        }

    with get_session() as session:
        for name, command in stub_parser_dir.items():
            session.add(Library(
                name=name,
                language=ParserLanguage.PYTHON,
                version="test",
                command=command,
                enabled=True,
            ))

        session.add(ParserWeights(
            id=1,
            scheme=_zero("SCHEME"),
            schemeauthdelim=_zero("DELIM"),
            username=_zero("USERNAME"),
            userpassdelim=_zero("USER_PASS_DELIM"),
            password=_zero("PASSWORD"),
            userinfohostdelim=_zero("USERINFO_HOST_DELIM"),
            host=_zero("HOST"),
            hostportdelim=_zero("HOST_PORT_DELIM"),
            port=_zero("PORT"),
            authpathdelim=_zero("AUTH_PATH_DELIM"),
            path=_zero("PATH"),
            pathquerydelim=_zero("PATH_QUERY_DELIM"),
            query=_zero("QUERY"),
            queryfragdelim=_zero("FRAGMENT_DELIM"),
            fragment=_zero("FRAGMENT"),
        ))

    yield db_path

    drop_db()


@pytest.fixture
def eager_celery():
    """Configure Celery to run tasks synchronously in-process, no broker needed."""
    from tasks.celery_app import app
    app.conf.update(task_always_eager=True, task_eager_propagates=True)
    yield app
    app.conf.update(task_always_eager=False, task_eager_propagates=False)
