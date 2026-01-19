{{ config(materialized='table') }}

select
    team_id,
    team_name,
    strength
from {{ ref('silver_teams') }}