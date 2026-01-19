{{ config(materialized='table') }}

select
    id as fixture_id,
    event as gameweek,
    team_h as home_team_id,
    team_a as away_team_id,
    kickoff_time::timestamp as kickoff_time,
    finished
from {{ source('fpl_bronze', 'bronze_fixtures') }}
