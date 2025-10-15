-- Last updated: 10/15/2025, 3:03:14 AM
-- Write your PostgreSQL query statement below
Select id, movie, description, rating
From Cinema
Where
    id % 2 !=0
    and description != 'boring'
order by rating DESC;