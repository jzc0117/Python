# https://platform.stratascratch.com/coding/10299-finding-updated-records?code_type=2
# Finding Updated Records

# We have a table with employees and their salaries, however, some of the records are old and contain outdated 
# salary information. Find the current salary of each employee assuming that salaries increase each year. Output 
# their id, first name, last name, department ID, and current salary. Order your list by employee ID in ascending order

current_salaries = current_salaries.sort_values(['id'])

# Import your libraries
import pandas as pd

# Start writing code
# ms_employee_salary.head()
current_salaries = ms_employee_salary.sort_values(['salary'], ascending=False)
current_salaries = current_salaries.drop_duplicates(['id'])
current_salaries = current_salaries.sort_values(['id'])
current_salaries

