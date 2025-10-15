-- Last updated: 10/15/2025, 3:03:16 AM
-- Write your PostgreSQL query statement below
SELECT 
    name, 
    population, 
    area
From World
Where 
    area >= 3000000
    or population >= 25000000;
