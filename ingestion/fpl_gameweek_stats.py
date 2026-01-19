import pandas as pd
from ingestion.config import FPL_BASE_URL, BRONZE_DIR, INGESTION_DATE
from ingestion.utils import fetch_json, write_parquet

SEASON = "2024-2025"


def run():
    bootstrap = fetch_json(f"{FPL_BASE_URL}/bootstrap-static/")
    events = bootstrap["events"]

    finished_gws = [e["id"] for e in events if e["finished"]]

    all_data = []

    for gw in finished_gws:
        print(f"📥 Fetching GW {gw}")
        gw_data = fetch_json(f"{FPL_BASE_URL}/event/{gw}/live/")

        elements = gw_data["elements"]

        for el in elements:
            stats = el["stats"]
            stats["element"] = el["id"]
            stats["gameweek"] = gw
            all_data.append(stats)

    df = pd.DataFrame(all_data)

    write_parquet(
        df,
        BRONZE_DIR,
        "bronze_player_gameweek",
        SEASON,
        INGESTION_DATE
    )


if __name__ == "__main__":
    run()
