# Write your MySQL query statement below
with cte as(
Select reports_to,count(name) as reports_count,
round(avg(age),0) as average_age
from Employees
group by reports_to
)
Select e.employee_id, e.name, c.reports_count, c.average_age
from Employees e inner join cte c
on e.employee_id = c.reports_to
order by e.employee_id