# Write a query that calculates the difference between the highest salaries found in the marketing 
# and engineering departments. Output just the absolute difference in salaries.

# Import your libraries
import pandas as pd

# Start writing code
db_employee.head()

df = pd.merge(db_employee,db_dept, how = 'left', left_on=['department_id'],
    right_on = ['id'])

max_marketing_salary = df.where(df['department']=='marketing')['salary'].max()
max_engineering_salary = df.where(df['department']=='engineering')['salary'].max()

output = abs(max_marketing_salary-max_engineering_salary)
output
