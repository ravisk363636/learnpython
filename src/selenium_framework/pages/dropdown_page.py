from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium_framework.pages.base_page import BasePage


class DropdownPage(BasePage):
    path = "/dropdown"

    DROPDOWN = (By.ID, "dropdown")
    HEADING = (By.TAG_NAME, "h3")

    def heading(self) -> str:
        return self.get_text(self.HEADING)

    def select_option(self, text: str) -> None:
        self.select_by_visible_text(self.DROPDOWN, text)

    def selected_option(self) -> str:
        return Select(self.find(self.DROPDOWN)).first_selected_option.text.strip()
