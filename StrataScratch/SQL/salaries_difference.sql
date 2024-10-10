-- https://platform.stratascratch.com/coding/10308-salaries-differences?code_type=3

select
    abs(max(case when db_dept.department = 'marketing' then db_employee.salary
        else 0 
        end
    ) - 
    max(case when db_dept.department = 'engineering' then db_employee.salary
        else 0
        end)
    )
from db_employee
join db_dept on db_employee.department_id = db_dept.id
;
