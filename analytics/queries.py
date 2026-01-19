import duckdb

DB_PATH = "duckdb/fpl.duckdb"


def get_top_captains(limit=10):
    query = """
    SELECT
        d.web_name,
        AVG(f.total_points) AS avg_points,
        COUNT(*) AS games_played
    FROM fact_player_performance f
    JOIN dim_player d
      ON f.player_id = d.player_id
    GROUP BY d.web_name
    HAVING COUNT(*) >= 3
    ORDER BY avg_points DESC
    LIMIT ?
    """
    with duckdb.connect(DB_PATH, read_only=True) as con:
        return con.execute(query, [limit]).df()


def get_differential_picks(max_ownership=10):
    query = """
    SELECT
        d.web_name,
        d.price,
        d.ownership_pct,
        SUM(f.total_points) AS total_points
    FROM fact_player_performance f
    JOIN dim_player d
      ON f.player_id = d.player_id
    WHERE d.ownership_pct < ?
    GROUP BY
        d.web_name,
        d.price,
        d.ownership_pct
    ORDER BY total_points DESC
    LIMIT 10
    """
    with duckdb.connect(DB_PATH, read_only=True) as con:
        return con.execute(query, [max_ownership]).df()
