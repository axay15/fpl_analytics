import pandas as pd
from ingestion.config import FPL_BASE_URL, BRONZE_DIR, INGESTION_DATE
from ingestion.utils import fetch_json, write_parquet

SEASON = "2025-2026"


def run():
    url = f"{FPL_BASE_URL}/bootstrap-static/"
    data = fetch_json(url)

    players = pd.DataFrame(data["elements"])
    teams = pd.DataFrame(data["teams"])
    element_types = pd.DataFrame(data["element_types"])

    write_parquet(
        players,
        BRONZE_DIR,
        "bronze_players",
        SEASON,
        INGESTION_DATE
    )

    write_parquet(
        teams,
        BRONZE_DIR,
        "bronze_teams",
        SEASON,
        INGESTION_DATE
    )

    write_parquet(
        element_types,
        BRONZE_DIR,
        "bronze_element_types",
        SEASON,
        INGESTION_DATE
    )


if __name__ == "__main__":
    run()
