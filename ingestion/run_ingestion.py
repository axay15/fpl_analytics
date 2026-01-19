from ingestion.fpl_bootstrap import run as run_bootstrap
from ingestion.fpl_fixtures import run as run_fixtures
from ingestion.fpl_gameweek_stats import run as run_gameweeks


def main():
    print("🚀 Starting FPL ingestion")

    run_bootstrap()
    run_fixtures()
    run_gameweeks()

    print("✅ Ingestion complete")


if __name__ == "__main__":
    main()
