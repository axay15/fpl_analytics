{{ config(materialized='table') }}

select
    p.player_id,
    p.web_name,
    p.position_id,
    t.team_name,
    p.price,
    p.ownership_pct
from {{ ref('silver_players') }} p
join {{ ref('silver_teams') }} t
  on p.team_id = t.team_id
