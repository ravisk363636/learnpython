import pytest

from selenium_framework.pages.checkboxes_page import CheckboxesPage


@pytest.mark.forms
@pytest.mark.smoke
def test_checkboxes_can_be_toggled(driver, settings) -> None:
    page = CheckboxesPage(driver, settings).open()

    assert page.heading() == "Checkboxes"
    assert len(page.checkboxes()) == 2

    page.set_checked(0, True)
    page.set_checked(1, False)

    assert page.is_checked(0) is True
    assert page.is_checked(1) is False
