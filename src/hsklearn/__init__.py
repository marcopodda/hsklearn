import os
from pathlib import Path


def get_path(key: str, default: Path) -> Path:
    """Retrieves path from environment or uses default."""
    if key not in os.environ:
        return default
    return Path(os.environ[key])


PROJECT_ROOT = Path(__file__).parent.parent.parent

DEFAULT_DATA_ROOT = PROJECT_ROOT / "data"
DEFAULT_EXPERIMENTS_ROOT = PROJECT_ROOT / "experiments"
DEFAULT_CONFIG_ROOT = PROJECT_ROOT / "config"

CONFIG_ROOT = get_path("CONFIG_ROOT", default=DEFAULT_CONFIG_ROOT)
EXPERIMENTS_ROOT = get_path("EXPERIMENTS_ROOT", default=DEFAULT_EXPERIMENTS_ROOT)
DATA_ROOT = get_path("DATA_ROOT", default=DEFAULT_DATA_ROOT)
