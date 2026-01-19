{{ config(materialized='table') }}

select
    pg.player_id,
    pg.gameweek,
    pg.minutes,
    pg.goals_scored,
    pg.assists,
    pg.expected_goals,
    pg.expected_assists,
    pg.total_points
from {{ ref('silver_player_gameweek') }} pg
