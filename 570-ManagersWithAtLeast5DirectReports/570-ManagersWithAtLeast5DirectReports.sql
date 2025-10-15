-- Last updated: 10/15/2025, 3:03:17 AM
-- Write your PostgreSQL query statement below
Select manager.name
From Employee as manager
Join Employee as worker 
    on manager.id = worker.managerId -- Self Join
Group By
    manager.id, manager.name
Having 
    count(worker.managerid) >= 5