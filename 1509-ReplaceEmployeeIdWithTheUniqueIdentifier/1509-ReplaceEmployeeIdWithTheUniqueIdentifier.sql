-- Last updated: 10/15/2025, 3:03:04 AM
-- Write your PostgreSQL query statement below
Select EmployeeUNI.unique_id, Employees.name
from
    Employees
left join EmployeeUNI
    on Employees.id = EmployeeUNI.id;