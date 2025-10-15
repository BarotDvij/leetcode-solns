-- Last updated: 10/15/2025, 3:02:54 AM
-- Write your PostgreSQL query statement below
Select 
    s.user_id, 
    round(count(case when action = 'confirmed' Then 1 end)::decimal / count(s.time_stamp), 2) as confirmation_rate
From Signups as s 
Full Outer Join confirmations as c
    On s.user_id = c.user_id
Group By s.user_id
