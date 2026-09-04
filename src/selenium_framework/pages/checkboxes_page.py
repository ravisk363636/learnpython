from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from selenium_framework.pages.base_page import BasePage


class CheckboxesPage(BasePage):
    path = "/checkboxes"

    CHECKBOXES = (By.CSS_SELECTOR, "input[type='checkbox']")
    HEADING = (By.TAG_NAME, "h3")

    def heading(self) -> str:
        return self.get_text(self.HEADING)

    def checkboxes(self) -> list[WebElement]:
        return self.find_all(self.CHECKBOXES)

    def set_checked(self, index: int, checked: bool) -> None:
        box = self.checkboxes()[index]
        if box.is_selected() != checked:
            box.click()

    def is_checked(self, index: int) -> bool:
        return self.checkboxes()[index].is_selected()
