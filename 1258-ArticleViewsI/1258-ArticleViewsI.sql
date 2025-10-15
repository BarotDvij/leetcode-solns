-- Last updated: 10/15/2025, 3:03:07 AM
-- Write your PostgreSQL query statement below
Select DISTINCT author_id as id
From Views
Where
    author_id = viewer_id
Order by 
    id asc;
