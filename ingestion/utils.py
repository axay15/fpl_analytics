import requests
import pandas as pd
from pathlib import Path

def fetch_json(url: str) -> dict:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.json()


def write_parquet(
    df: pd.DataFrame,
    output_dir: Path,
    table_name: str,
    season: str,
    ingestion_date: str,
    gameweek: int | None = None
):
    # Base path without ingestion_date
    path = output_dir / table_name / f"season={season}"

    if gameweek is not None:
        path = path / f"gameweek={gameweek}"

    # 🔥 IMPORTANT: remove existing files for idempotency
    if path.exists():
        for file in path.glob("*.parquet"):
            file.unlink()

    path.mkdir(parents=True, exist_ok=True)

    file_path = path / f"{table_name}.parquet"
    df.to_parquet(file_path, index=False)

    print(f"♻️ Overwrote {file_path}")
