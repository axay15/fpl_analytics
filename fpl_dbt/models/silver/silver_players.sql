{{ config(materialized='table') }}

select
    id as player_id,
    first_name,
    second_name,
    web_name,
    team as team_id,
    element_type as position_id,
    now_cost / 10.0 as price,
    selected_by_percent::double as ownership_pct,
    minutes,
    total_points
from {{ source('fpl_bronze', 'bronze_players') }}