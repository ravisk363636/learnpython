from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_framework.config import Settings
from selenium_framework.logger import get_logger

logger = get_logger("driver_factory")


class UnsupportedBrowserError(ValueError):
    """Raised when the configured browser is not supported."""


def _chrome_options(settings: Settings) -> ChromeOptions:
    options = ChromeOptions()
    if settings.headless:
        options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument(f"--window-size={settings.window_width},{settings.window_height}")
    options.add_argument("--ignore-certificate-errors")
    prefs = {
        "download.default_directory": str(settings.download_dir),
        "download.prompt_for_download": False,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    }
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    options.set_capability("goog:loggingPrefs", {"browser": "SEVERE"})
    return options


def _firefox_options(settings: Settings) -> FirefoxOptions:
    options = FirefoxOptions()
    if settings.headless:
        options.add_argument("-headless")
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.dir", str(settings.download_dir))
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
    return options


def _edge_options(settings: Settings) -> EdgeOptions:
    options = EdgeOptions()
    if settings.headless:
        options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument(f"--window-size={settings.window_width},{settings.window_height}")
    return options


def create_driver(settings: Settings) -> WebDriver:
    """Create a local or remote WebDriver based on settings."""
    browser = settings.browser.strip().lower()
    logger.info(
        "Creating %s driver (headless=%s, remote=%s)",
        browser,
        settings.headless,
        settings.is_remote,
    )

    if browser == "chrome":
        options = _chrome_options(settings)
        driver: WebDriver = (
            webdriver.Remote(command_executor=settings.remote_url, options=options)
            if settings.is_remote
            else webdriver.Chrome(service=ChromeService(), options=options)
        )
    elif browser == "firefox":
        options = _firefox_options(settings)
        driver = (
            webdriver.Remote(command_executor=settings.remote_url, options=options)
            if settings.is_remote
            else webdriver.Firefox(options=options)
        )
    elif browser == "edge":
        options = _edge_options(settings)
        driver = (
            webdriver.Remote(command_executor=settings.remote_url, options=options)
            if settings.is_remote
            else webdriver.Edge(options=options)
        )
    else:
        raise UnsupportedBrowserError(
            f"Unsupported browser '{settings.browser}'. Use chrome, firefox, or edge."
        )

    driver.set_page_load_timeout(settings.page_load_timeout_seconds)
    driver.set_window_size(settings.window_width, settings.window_height)
    return driver
