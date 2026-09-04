import pytest

from selenium_framework.pages.dropdown_page import DropdownPage


@pytest.mark.forms
@pytest.mark.regression
def test_dropdown_selects_option_two(driver, settings) -> None:
    page = DropdownPage(driver, settings).open()

    assert page.heading() == "Dropdown List"
    page.select_option("Option 2")

    assert page.selected_option() == "Option 2"
