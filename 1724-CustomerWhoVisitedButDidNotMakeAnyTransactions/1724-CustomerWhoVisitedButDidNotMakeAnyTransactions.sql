-- Last updated: 10/15/2025, 3:03:01 AM
-- Write your PostgreSQL query statement below
Select 
    v.customer_id, 
    count(*) as count_no_trans 
From Visits as v
Left Join Transactions as t
    On v.visit_id = t.visit_id
Where
    transaction_id is Null
Group By 
    v.customer_id;
