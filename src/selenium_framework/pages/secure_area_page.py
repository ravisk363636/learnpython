from selenium.webdriver.common.by import By

from selenium_framework.pages.base_page import BasePage


class SecureAreaPage(BasePage):
    path = "/secure"

    FLASH = (By.ID, "flash")
    HEADING = (By.TAG_NAME, "h2")
    LOGOUT = (By.CSS_SELECTOR, "a[href='/logout']")

    def flash_message(self) -> str:
        return self.get_text(self.FLASH)

    def heading(self) -> str:
        return self.get_text(self.HEADING)

    def logout(self) -> None:
        self.find(self.HEADING)
        self.click(self.LOGOUT)
