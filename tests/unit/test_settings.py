from pathlib import Path

from selenium_framework.config import get_settings


def test_default_base_url_is_practice_site() -> None:
    settings = get_settings()
    assert settings.base_url.startswith("https://")
    assert settings.browser.lower() in {"chrome", "firefox", "edge"}
    assert settings.explicit_wait_seconds > 0


def test_artifact_directories_exist() -> None:
    settings = get_settings()
    for folder in (
        settings.screenshot_dir,
        settings.log_dir,
        settings.reports_dir,
        settings.download_dir,
    ):
        assert isinstance(folder, Path)
        assert folder.is_dir()
