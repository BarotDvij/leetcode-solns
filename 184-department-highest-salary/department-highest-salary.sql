-- Write your PostgreSQL query statement below
select 
    Department.name as Department, 
    Employee.name as Employee, 
    Employee.salary as Salary
from  Department
inner join Employee
    on Employee.departmentId = Department.id
Where (Employee.departmentId, Employee.salary) in (
    select departmentID, max(salary)
    from Employee
    group by departmentID
)