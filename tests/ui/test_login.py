import pytest

from selenium_framework.pages.login_page import LoginPage
from selenium_framework.utils.data_loader import load_json

USERS = load_json("tests/data/login_users.json")


@pytest.mark.smoke
@pytest.mark.login
def test_valid_login_reaches_secure_area(driver, settings) -> None:
    login_page = LoginPage(driver, settings).open()
    secure = login_page.login(USERS["valid"]["username"], USERS["valid"]["password"])
    secure.wait_for_url_contains("/secure")

    assert "You logged into a secure area!" in secure.flash_message()
    assert "Secure Area" in secure.heading()


@pytest.mark.login
def test_logout_returns_to_login(driver, settings) -> None:
    login_page = LoginPage(driver, settings).open()
    secure = login_page.login(USERS["valid"]["username"], USERS["valid"]["password"])
    secure.wait_for_url_contains("/secure")
    secure.logout()
    login_page.wait_for_url_contains("/login")

    assert "You logged out of the secure area!" in login_page.flash_message()


@pytest.mark.login
@pytest.mark.regression
@pytest.mark.parametrize(
    "username,password,expected_flash",
    [(case["username"], case["password"], case["expected_flash"]) for case in USERS["invalid"]],
    ids=["bad-password", "bad-username"],
)
def test_invalid_login_shows_error(
    driver, settings, username: str, password: str, expected_flash: str
) -> None:
    login_page = LoginPage(driver, settings).open()
    login_page.login(username, password)

    assert expected_flash in login_page.flash_message()
    assert "/login" in driver.current_url
