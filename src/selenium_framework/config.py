from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    """Runtime settings loaded from environment variables and optional `.env`."""

    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    base_url: str = "https://the-internet.herokuapp.com"
    browser: str = "chrome"
    headless: bool = True
    window_width: int = 1920
    window_height: int = 1080
    explicit_wait_seconds: int = 15
    page_load_timeout_seconds: int = 30
    remote_url: str = ""
    download_dir: Path = Field(default=PROJECT_ROOT / "downloads")
    screenshot_dir: Path = Field(default=PROJECT_ROOT / "screenshots")
    log_dir: Path = Field(default=PROJECT_ROOT / "logs")
    reports_dir: Path = Field(default=PROJECT_ROOT / "reports")
    log_level: str = "INFO"

    @property
    def is_remote(self) -> bool:
        return bool(self.remote_url.strip())


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    settings = Settings()
    settings.download_dir.mkdir(parents=True, exist_ok=True)
    settings.screenshot_dir.mkdir(parents=True, exist_ok=True)
    settings.log_dir.mkdir(parents=True, exist_ok=True)
    settings.reports_dir.mkdir(parents=True, exist_ok=True)
    return settings
