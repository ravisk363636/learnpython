from __future__ import annotations

import re
from datetime import UTC, datetime

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_framework.config import Settings, get_settings
from selenium_framework.driver_factory import create_driver
from selenium_framework.logger import get_logger

logger = get_logger("conftest")


def pytest_configure(config: pytest.Config) -> None:
    settings = get_settings()
    settings.reports_dir.mkdir(parents=True, exist_ok=True)
    settings.screenshot_dir.mkdir(parents=True, exist_ok=True)
    settings.log_dir.mkdir(parents=True, exist_ok=True)


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--browser", action="store", default=None, help="chrome | firefox | edge")
    parser.addoption("--base-url", action="store", default=None, help="Application base URL")
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run browsers with a visible window (overrides HEADLESS)",
    )
    parser.addoption(
        "--remote-url",
        action="store",
        default=None,
        help="Selenium Grid / remote WebDriver URL",
    )


@pytest.fixture(scope="session")
def settings(pytestconfig: pytest.Config) -> Settings:
    runtime = get_settings()
    browser = pytestconfig.getoption("--browser")
    base_url = pytestconfig.getoption("--base-url")
    headed = pytestconfig.getoption("--headed")
    remote_url = pytestconfig.getoption("--remote-url")

    updates: dict[str, object] = {}
    if browser:
        updates["browser"] = browser
    if base_url:
        updates["base_url"] = base_url
    if headed:
        updates["headless"] = False
    if remote_url:
        updates["remote_url"] = remote_url
    if updates:
        runtime = runtime.model_copy(update=updates)
    return runtime


@pytest.fixture
def driver(settings: Settings, request: pytest.FixtureRequest) -> WebDriver:
    instance = create_driver(settings)
    logger.info("Started driver for %s", request.node.nodeid)
    yield instance
    instance.quit()
    logger.info("Quit driver for %s", request.node.nodeid)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo) -> None:
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)

    if report.when != "call" or not report.failed:
        return

    driver: WebDriver | None = item.funcargs.get("driver")
    settings: Settings | None = item.funcargs.get("settings")
    if driver is None or settings is None:
        return

    stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    safe_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", item.name)
    screenshot = settings.screenshot_dir / f"{safe_name}_{stamp}.png"
    driver.save_screenshot(str(screenshot))
    logger.error("Failure screenshot saved: %s", screenshot)

    allure.attach.file(
        str(screenshot), name="screenshot", attachment_type=allure.attachment_type.PNG
    )
    allure.attach(
        driver.page_source,
        name="page_source",
        attachment_type=allure.attachment_type.HTML,
    )
    allure.attach(driver.current_url, name="url", attachment_type=allure.attachment_type.TEXT)
