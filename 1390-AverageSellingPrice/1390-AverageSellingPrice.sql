-- Last updated: 10/15/2025, 3:03:05 AM
-- Write your PostgreSQL query statement below
Select 
    Prices.product_id, 
    coalesce(round(sum(UnitsSold.units * Prices.price)::decimal  / sum(UnitsSold.units), 2), 0) as average_price 
From Prices
Left Join UnitsSold
    on Prices.product_id = UnitsSold.product_id
    and unitssold.purchase_date BETWEEN prices.start_date and prices.end_date
Group by Prices.product_id;
