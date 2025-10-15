-- Last updated: 10/15/2025, 3:03:16 AM
-- Write your PostgreSQL query statement below
SELECT name
From Customer
Where 
    referee_id != 2
    or referee_id is null