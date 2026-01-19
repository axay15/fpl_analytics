from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data"
BRONZE_DIR = DATA_DIR / "bronze"
DUCKDB_DIR = BASE_DIR / "duckdb"

BRONZE_DIR.mkdir(parents=True, exist_ok=True)
DUCKDB_DIR.mkdir(parents=True, exist_ok=True)

INGESTION_DATE = datetime.utcnow().strftime("%Y-%m-%d")

FPL_BASE_URL = "https://fantasy.premierleague.com/api"
