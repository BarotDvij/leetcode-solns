-- Write your PostgreSQL query statement below
With first_date as (
    -- Need to select the first days
    select 
        player_id,
        min(event_date) as initial_login 
    from Activity
    group by player_id
)
--final select statement
--divide the numbers to find out 
select
    Round((count(a.player_id)::numeric / count(f.player_id)), 2) as fraction
from first_date f
left join Activity a
    on a.player_id = f.player_id
    and a.event_date = (f.initial_login + 1)