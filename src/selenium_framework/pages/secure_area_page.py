from selenium.webdriver.common.by import By

from selenium_framework.pages.base_page import BasePage


class SecureAreaPage(BasePage):
    path = "/secure"

    FLASH = (By.ID, "flash")
    HEADING = (By.TAG_NAME, "h2")
    LOGOUT = (By.CSS_SELECTOR, "a.button.secondary")

    def flash_message(self) -> str:
        return self.get_text(self.FLASH)

    def heading(self) -> str:
        return self.get_text(self.HEADING)

    def logout(self) -> None:
        self.click(self.LOGOUT)
