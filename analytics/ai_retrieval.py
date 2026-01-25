import duckdb

DB_PATH = "duckdb/fpl.duckdb"


def get_captain_context():
    query = """
    SELECT
        d.web_name,
        d.team_name,
        AVG(f.total_points) AS avg_points,
        COUNT(*) AS matches
    FROM fact_player_performance f
    JOIN dim_player d
      ON f.player_id = d.player_id
    GROUP BY d.web_name, d.team_name
    HAVING COUNT(*) >= 3
    ORDER BY avg_points DESC
    LIMIT 5
    """
    with duckdb.connect(DB_PATH, read_only=True) as con:
        return con.execute(query).df().to_dict(orient="records")


def get_differentials_context():
    query = """
    SELECT
        web_name,
        team_name,
        price,
        ownership_pct,
        total_points
    FROM dim_player
    WHERE ownership_pct < 10
    ORDER BY total_points DESC
    LIMIT 5
    """
    with duckdb.connect(DB_PATH, read_only=True) as con:
        return con.execute(query).df().to_dict(orient="records")
