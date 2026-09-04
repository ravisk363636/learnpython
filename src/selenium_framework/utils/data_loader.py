from __future__ import annotations

import json
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[3]


def load_json(relative_path: str) -> Any:
    """Load JSON test data from a path relative to the project root."""
    path = PROJECT_ROOT / relative_path
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)
