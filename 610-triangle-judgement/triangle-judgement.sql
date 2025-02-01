# Write your MySQL query statement below
select x,y,z, (case when x+y>z then (case when y+z>x then
(case when x+z>y then 'Yes' else 'No'end) else 'No' end) else 'No' end) as triangle
from Triangle