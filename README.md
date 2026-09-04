# learnpython

Python learning repository. This tree includes a **production-ready Selenium + pytest UI automation framework**.

## What you get

- **Page Object Model** with explicit waits (no implicit waits)
- **Driver factory** for Chrome, Firefox, and Edge, local or Selenium Grid
- **Environment-based config** (`.env` + CLI overrides)
- **pytest** fixtures, markers, HTML + Allure reporting
- **Failure artifacts**: screenshot, page source, URL
- **Data-driven tests** from JSON
- **Parallel runs** via `pytest-xdist` and retries via `pytest-rerunfailures`
- **GitHub Actions** CI and **Docker Compose** Grid

Sample tests run against [the-internet](https://the-internet.herokuapp.com), a public practice site. Point `BASE_URL` at your own app when you are ready.

## Layout

```text
src/selenium_framework/     reusable framework library
  config.py                 settings from env / .env
  driver_factory.py         WebDriver creation
  logger.py                 rotating file + console logs
  pages/                    page objects
  utils/                    test-data helpers
tests/
  conftest.py               fixtures and failure hooks
  data/                     JSON fixtures
  ui/                       UI specs
.github/workflows/          CI
docker-compose.yml          Selenium Grid (Chrome / Firefox)
```

## Prerequisites

- Python 3.11+
- Google Chrome (default), or Firefox / Edge
- Selenium Manager (bundled with Selenium 4.6+) downloads matching drivers

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
pytest tests -m smoke
```

Open `reports/report.html` after a run.

## Common commands

| Command | Purpose |
| --- | --- |
| `pytest tests` | Full suite, headless Chrome |
| `pytest tests -m smoke` | Fast critical-path set |
| `pytest tests --headed --browser chrome` | Visible browser |
| `pytest tests -n auto --reruns 1` | Parallel + one retry |
| `pytest tests --base-url https://staging.example.com` | Target another environment |
| `make lint` | Ruff check + format verify |

Allure (optional, if the CLI is installed):

```bash
pytest tests --alluredir=reports/allure-results
allure serve reports/allure-results
```

## Configuration

Copy `.env.example` to `.env`. CLI flags override env vars.

| Variable / flag | Meaning | Default |
| --- | --- | --- |
| `BASE_URL` / `--base-url` | App origin | `https://the-internet.herokuapp.com` |
| `BROWSER` / `--browser` | `chrome`, `firefox`, `edge` | `chrome` |
| `HEADLESS` / `--headed` | Headless unless `--headed` | `true` |
| `REMOTE_URL` / `--remote-url` | Selenium Grid URL | empty (local) |
| `EXPLICIT_WAIT_SECONDS` | Wait timeout for elements | `15` |
| `WINDOW_WIDTH` / `WINDOW_HEIGHT` | Viewport | `1920` x `1080` |

## Selenium Grid

```bash
docker compose up -d chrome
pytest tests --remote-url http://localhost:4444/wd/hub --browser chrome
```

Watch sessions at http://localhost:7900 (password `secret`).

## Writing tests

1. Add a page object under `src/selenium_framework/pages/`.
2. Keep locators and waits in the page class; keep assertions in the test.
3. Mark tests (`smoke`, `regression`, `login`, `forms`).
4. Store credentials and datasets in `tests/data/`, not in source.

Example:

```python
from selenium_framework.pages.login_page import LoginPage

def test_valid_login(driver, settings):
    page = LoginPage(driver, settings).open()
    secure = page.login("tomsmith", "SuperSecretPassword!")
    assert "Secure Area" in secure.heading()
```

Each test gets a **fresh browser**. Drivers are quit in the fixture teardown.

## CI

`.github/workflows/ui-tests.yml` lints, runs smoke tests, then the full suite on Ubuntu with headless Chrome. HTML reports, screenshots, and logs upload as artifacts.

## Extending to your product

- Set `BASE_URL` to your environment.
- Replace sample page objects with your screens (login, booking, etc.).
- Keep secrets in CI variables or a secret store; never commit `.env`.
- Add API setup/teardown if UI tests need seeded data.
- Use Grid in CI when you need Firefox/Edge matrix or more parallelism.
