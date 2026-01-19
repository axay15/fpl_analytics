{{ config(materialized='table') }}

select
    id as team_id,
    name as team_name,
    short_name,
    strength
from {{ source('fpl_bronze', 'bronze_teams') }}
