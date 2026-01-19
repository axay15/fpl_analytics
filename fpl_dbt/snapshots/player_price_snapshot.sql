{% snapshot player_price_snapshot %}
{{
    config(
      target_schema='snapshots',
      unique_key='player_id',
      strategy='check',
      check_cols=['price']
    )
}}

select
    player_id,
    price
from {{ ref('silver_players') }}

{% endsnapshot %}
