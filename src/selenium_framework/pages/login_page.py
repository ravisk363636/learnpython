from selenium.webdriver.common.by import By

from selenium_framework.pages.base_page import BasePage
from selenium_framework.pages.secure_area_page import SecureAreaPage


class LoginPage(BasePage):
    path = "/login"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH = (By.ID, "flash")

    def login(self, username: str, password: str) -> SecureAreaPage:
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)
        return SecureAreaPage(self.driver, self.settings)

    def flash_message(self) -> str:
        return self.get_text(self.FLASH)
