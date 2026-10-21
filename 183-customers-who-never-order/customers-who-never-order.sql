-- Write your PostgreSQL query statement below
select name as Customers
from Customers c
left join Orders o
    ON o.customerId = c.id
where o.id is null