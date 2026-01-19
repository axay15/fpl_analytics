import pandas as pd
from ingestion.config import FPL_BASE_URL, BRONZE_DIR, INGESTION_DATE
from ingestion.utils import fetch_json, write_parquet

SEASON = "2025-2026"


def run():
    url = f"{FPL_BASE_URL}/fixtures/"
    data = fetch_json(url)

    fixtures = pd.DataFrame(data)

    write_parquet(
        fixtures,
        BRONZE_DIR,
        "bronze_fixtures",
        SEASON,
        INGESTION_DATE
    )


if __name__ == "__main__":
    run()
