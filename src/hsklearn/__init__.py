import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).parent.parent.parent

load_dotenv(dotenv_path=PROJECT_ROOT / ".env")

CONFIG_ROOT = PROJECT_ROOT.joinpath(os.environ["CONFIG_ROOT"])
DATA_ROOT = PROJECT_ROOT.joinpath(os.environ["DATA_ROOT"])
EXPERIMENTS_ROOT = PROJECT_ROOT.joinpath(os.environ["EXPERIMENTS_ROOT"])
