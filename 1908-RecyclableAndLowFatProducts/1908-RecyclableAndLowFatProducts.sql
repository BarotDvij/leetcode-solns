-- Last updated: 10/15/2025, 3:02:55 AM
-- Write your PostgreSQL query statement below
SELECT product_id
FROM Products
WHERE 
    low_fats = 'Y' 
    AND recyclable = 'Y'