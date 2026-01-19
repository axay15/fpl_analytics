{{ config(materialized='table') }}

select
    element as player_id,
    gameweek,
    minutes,
    goals_scored,
    assists,
    clean_sheets,
    goals_conceded,
    expected_goals,
    expected_assists,
    total_points
from {{ source('fpl_bronze', 'bronze_player_gameweek') }}