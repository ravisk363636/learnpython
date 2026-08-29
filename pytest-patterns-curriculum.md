# Pytest Patterns — Curriculum

**Skill:** Pytest Patterns  
**Author:** thetestingacademy (The Testing Academy)  
**Source:** [qaskills.sh/skills/thetestingacademy/pytest-patterns](https://qaskills.sh/skills/thetestingacademy/pytest-patterns)  
**Canonical SKILL.md:** [github.com/PramodDutta/qaskills/.../pytest-patterns/SKILL.md](https://github.com/PramodDutta/qaskills/blob/main/packs/qa-essentials/skills/pytest-patterns/SKILL.md)

This file is a self-study map of the public QASkills pytest skill: fixtures, parametrize, markers, plugins, mocking, and test layout. Install the skill into an AI agent, then work the modules below against official pytest docs and practice repos.

---

## Skill snapshot

| Item | Detail |
|------|--------|
| Name | `pytest-patterns` |
| Version | 1.0.0 |
| License | MIT |
| Quality score (listing) | 88 |
| Tags | unit, integration, pytest, python, api, web |
| Category | Unit & integration testing |
| Author | The Testing Academy |
| Related paid cohort | [AI Tester Blueprint](https://qaskills.sh) (Playwright, LLM evals, CI) — advertised on the skill page |

**What the skill teaches:** Python testing with pytest fixtures, `@pytest.mark.parametrize`, markers, `conftest.py`, plugins, mocking, exception tests, `tmp_path`, coverage, and CI.

---

## Install the skill (AI agents)

```bash
npx @qaskills/cli add pytest-patterns
```

Works with Claude Code, Cursor, Copilot, and other agents listed on the skill page. Download `SKILL.md` from the same listing if you want the file without the CLI.

**CI install snippet (from the skill page):**

```yaml
- name: Install QA Skills
  run: npx @qaskills/cli add pytest-patterns
```

---

## Official hubs

| What | Link |
|------|------|
| Skill page | https://qaskills.sh/skills/thetestingacademy/pytest-patterns |
| Related skill: Python Testing Patterns | https://qaskills.sh/skills/thetestingacademy/python-testing-patterns |
| Related skill: Pytest Best Practices | search on https://qaskills.sh |
| QASkills catalog | https://github.com/PramodDutta/qaskills |
| QASkills site | https://qaskills.sh |
| The Testing Academy | https://thetestingacademy.com |
| YouTube | https://youtube.com/@TheTestingAcademy |
| pytest docs (home) | https://docs.pytest.org/en/stable/ |

---

## Learning path (skill sections as modules)

Work these in order. Each module maps to a section of the skill plus official docs.

| Module | Skill section | Goal |
|--------|---------------|------|
| 1 | Core principles + project structure | Discover tests by convention; separate `src/` and `tests/` |
| 2 | Configuration | `pytest.ini` / `pyproject.toml`, markers, coverage |
| 3 | Fixtures | Basic fixtures, scopes, factories, yield teardown |
| 4 | Parametrize | Data-driven tests, ids, stacked parametrize |
| 5 | Markers | smoke / unit / integration / slow, skip, skipif, xfail |
| 6 | Mocking | `pytest-mock` `mocker`, retries, datetime |
| 7 | Conftest | Shared vs integration-only fixtures, autouse |
| 8 | Exceptions + tmp files | `pytest.raises`, `tmp_path` |
| 9 | Best practices, anti-patterns, CLI, CI | Run subsets, xdist, GitHub Actions |

---

### Module 1 — Core principles and layout

**Principles from the skill**

1. Convention over configuration — pytest finds `test_*.py`, `Test*`, `test_*`.
2. Fixtures for setup — not unittest `setUp`/`tearDown`.
3. Parametrize for coverage — `@pytest.mark.parametrize`.
4. Descriptive names — the name states expected behavior.
5. Minimal scope — one behavior per test.

**Recommended layout**

```
project/
  src/myapp/          # services, models, utils
  tests/
    conftest.py
    unit/
    integration/
      conftest.py
    fixtures/
  pyproject.toml
  pytest.ini
```

**Resources**

- [Good Integration Practices](https://docs.pytest.org/en/stable/explanation/goodpractices.html)
- [Test discovery](https://docs.pytest.org/en/stable/explanation/goodpractices.html#test-discovery)
- [Python Testing 101 (pytest)](https://docs.pytest.org/en/stable/getting-started.html)

---

### Module 2 — Configuration

Register paths, naming, default flags, and custom markers. Prefer **one** config source (`pytest.ini` **or** `[tool.pytest.ini_options]` in `pyproject.toml`).

Skill defaults:

- `testpaths = tests`
- `-v --tb=short --strict-markers`
- markers: `slow`, `integration`, `smoke`, `unit`
- coverage: `--cov=src`, omit tests/`__init__.py`, `fail_under = 80`

**Resources**

- [Configuration](https://docs.pytest.org/en/stable/reference/customize.html)
- [pytest.ini options](https://docs.pytest.org/en/stable/reference/reference.html#ini-options-ref)
- [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/)
- [Coverage.py](https://coverage.readthedocs.io/)

---

### Module 3 — Fixtures

| Pattern | When to use |
|---------|-------------|
| Basic fixture | Shared sample objects (`sample_user`, `admin_user`) |
| Fixture depending on fixtures | Compose services with mocked deps |
| `scope="session"` | Expensive shared resource (DB connection) |
| `scope="module"` | Seed data once per module |
| `scope="class"` | Shared resource for a test class |
| `scope="function"` (default) | Fresh instance per test |
| Factory fixture | `make_user(**kwargs)` for many variants + cleanup |
| Yield fixture | Setup / teardown (server start/stop, transaction rollback) |

**Resources**

- [How to use fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [Fixture reference](https://docs.pytest.org/en/stable/reference/fixtures.html)
- [Yield fixtures / teardown](https://docs.pytest.org/en/stable/how-to/fixtures.html#teardown-cleanup-aka-fixture-finalization)

**Practice:** implement `sample_user`, `user_service(mock_user_repo, mock_email_service)`, then a `make_user` factory with cleanup.

---

### Module 4 — Parametrize

- Table of `(input, expected)` for validators (email, password).
- Multiple columns: `a, b, expected`.
- `pytest.param(..., id="strong-password")` for readable failure names.
- Stack two `@pytest.mark.parametrize` decorators for a cartesian product (HTTP methods × auth on/off).

**Resources**

- [Parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html)
- [Parametrizing fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html#parametrizing-fixtures)

---

### Module 5 — Markers

Custom: `slow`, `integration`, `smoke`, `unit`. Built-in: `skip`, `skipif`, `xfail`.

```bash
pytest -m smoke
pytest -m "not slow"
pytest -m "unit and not integration"
```

`--strict-markers` fails on typos.

**Resources**

- [Marking test functions](https://docs.pytest.org/en/stable/how-to/mark.html)
- [skip and xfail](https://docs.pytest.org/en/stable/how-to/skipping.html)
- [Working with custom markers](https://docs.pytest.org/en/stable/example/markers.html)

---

### Module 6 — Mocking with pytest-mock

Install: `pip install pytest-mock`. Use the `mocker` fixture.

Skill examples:

- `mocker.patch.object` on email send + repo create
- `side_effect` list for retry (fail, fail, success)
- Patch `datetime.now` for deterministic greetings

**Resources**

- [pytest-mock](https://pytest-mock.readthedocs.io/en/latest/)
- [unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
- [Monkeypatching](https://docs.pytest.org/en/stable/how-to/monkeypatch.html)

---

### Module 7 — Conftest patterns

| File | Scope |
|------|--------|
| `tests/conftest.py` | Shared mocks, optional `autouse` env reset |
| `tests/integration/conftest.py` | `api_base_url`, `httpx` `api_client`, `auth_client` |

Keep conftest small; move bulky fixtures to `tests/fixtures/`.

**Resources**

- [conftest.py](https://docs.pytest.org/en/stable/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files)
- [httpx](https://www.python-httpx.org/) for API clients (as in the skill)

---

### Module 8 — Exceptions and temp files

- `with pytest.raises(ValueError, match="Invalid email"):`
- `exc_info` for attributes on custom errors
- `tmp_path` for CSV/JSON/YAML without leftover files

**Resources**

- [Assertions / raises](https://docs.pytest.org/en/stable/how-to/assert.html)
- [tmp_path](https://docs.pytest.org/en/stable/how-to/tmp_path.html)

---

### Module 9 — Best practices, anti-patterns, running tests, CI

**Do**

1. Fixtures for shared setup  
2. `conftest.py` at the right directory level  
3. Names like `test_create_user_with_duplicate_email_raises_conflict`  
4. Parametrize data-driven cases  
5. Markers for subsets  
6. `tmp_path` for files  
7. `mocker` instead of raw `unittest.mock` when using pytest  
8. `--strict-markers`  
9. `autouse` only for truly global reset  
10. Split large conftest files  

**Avoid**

1. `unittest.TestCase` (loses fixtures/parametrize)  
2. Module-level global state  
3. One giant `setup_everything` fixture  
4. Testing private internals  
5. Fixtures that do too much  
6. Skipping `yield` teardown  
7. Wrong fixture scope (session when function is needed)  
8. Hardcoded file paths  
9. Mocking every dependency (tests nothing real)  
10. Never shuffling order — use `pytest-randomly` to find hidden coupling  

**CLI from the skill**

```bash
pytest
pytest tests/unit/test_user_service.py
pytest tests/unit/test_user_service.py::test_create_user
pytest -m smoke
pytest --cov=src --cov-report=html
pytest -n auto          # pytest-xdist
pytest -v
pytest -x
pytest --lf
pytest --log-cli-level=DEBUG
```

**Plugins to add**

| Plugin | Why |
|--------|-----|
| [pytest-cov](https://pypi.org/project/pytest-cov/) | Coverage in `addopts` |
| [pytest-mock](https://pypi.org/project/pytest-mock/) | `mocker` fixture |
| [pytest-xdist](https://pytest-xdist.readthedocs.io/) | `pytest -n auto` |
| [pytest-randomly](https://github.com/pytest-dev/pytest-randomly) | Catch order-dependent tests |

**Resources**

- [How to invoke pytest](https://docs.pytest.org/en/stable/how-to/usage.html)
- [Plugins](https://docs.pytest.org/en/stable/how-to/plugins.html)
- [GitHub Actions + pytest](https://docs.pytest.org/en/stable/explanation/ci.html) (plus the QASkills install step above)

---

## Practice sites and sample APIs

Use these when writing integration tests with `httpx` as in the skill’s `api_client` / `auth_client` fixtures.

- [httpbin.org](https://httpbin.org/)
- [jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com/)
- [reqres.in](https://reqres.in/)
- [restful-booker.herokuapp.com](https://restful-booker.herokuapp.com/)

Local: run a small FastAPI/Flask app under `src/` and hit it from `tests/integration/`.

---

## Related QASkills (same publisher)

| Skill | URL |
|-------|-----|
| Python Testing Patterns (broader: property-based, architecture) | https://qaskills.sh/skills/thetestingacademy/python-testing-patterns |
| Playwright E2E | https://qaskills.sh/skills/thetestingacademy/playwright-e2e |
| Playwright API | https://qaskills.sh/skills/thetestingacademy/playwright-api |
| Jest unit | https://qaskills.sh/skills/thetestingacademy/jest-unit |
| Full pack listing | https://github.com/PramodDutta/qaskills |

---

## Suggested weekly rhythm

1. Install the skill (`npx @qaskills/cli add pytest-patterns`) so your editor follows the same rules.  
2. Create a tiny `src/myapp` + `tests/` tree matching Module 1.  
3. Add `pyproject.toml` from Module 2 and run `pytest -v`.  
4. Add fixtures and a factory (Module 3), then parametrize validators (Module 4).  
5. Mark smoke vs slow; fail CI on unknown markers.  
6. Mock email/repo with `mocker`; add one integration file with `httpx`.  
7. Turn on coverage (`fail_under = 80`) and `pytest -n auto` in GitHub Actions.

---

## Copyright note

Skill text and examples are published by The Testing Academy under **MIT** on QASkills / GitHub. This file restates that public skill as a study curriculum and points at official pytest docs. It is not a paid-course video dump.
