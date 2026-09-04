from pathlib import Path

from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from selenium_framework.config import Settings
from selenium_framework.logger import get_logger

logger = get_logger("pages")

Locator = tuple[str, str]


class BasePage:
    """Shared page-object helpers: navigation, waits, and element actions."""

    path = ""

    def __init__(self, driver: WebDriver, settings: Settings) -> None:
        self.driver = driver
        self.settings = settings
        self.wait = WebDriverWait(driver, settings.explicit_wait_seconds)

    @property
    def url(self) -> str:
        return f"{self.settings.base_url.rstrip('/')}/{self.path.lstrip('/')}"

    def open(self) -> "BasePage":
        logger.info("Opening %s", self.url)
        self.driver.get(self.url)
        return self

    def find(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_all(self, locator: Locator) -> list[WebElement]:
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def click(self, locator: Locator) -> None:
        logger.debug("Click %s", locator)
        element = self.find_clickable(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except ElementClickInterceptedException:
            logger.warning("Native click intercepted for %s; using JavaScript click", locator)
            self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator: Locator, text: str, *, clear: bool = True) -> None:
        element = self.find(locator)
        if clear:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator: Locator) -> str:
        return self.find(locator).text.strip()

    def is_visible(self, locator: Locator, timeout: int | None = None) -> bool:
        wait = WebDriverWait(self.driver, timeout or self.settings.explicit_wait_seconds)
        try:
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def select_by_visible_text(self, locator: Locator, text: str) -> None:
        Select(self.find(locator)).select_by_visible_text(text)

    def wait_for_url_contains(self, fragment: str) -> None:
        self.wait.until(EC.url_contains(fragment))

    def take_screenshot(self, name: str) -> Path:
        path = self.settings.screenshot_dir / f"{name}.png"
        self.driver.save_screenshot(str(path))
        logger.info("Saved screenshot: %s", path)
        return path
