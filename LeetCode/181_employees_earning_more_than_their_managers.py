# https://leetcode.com/problems/employees-earning-more-than-their-managers/description/
import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    manager_df = employee.copy()

    merged = pd.merge(employee,manager_df, how='left', left_on=['managerId'],right_on=['id'])
    merged['difference_salaries'] = merged['salary_x']-merged['salary_y']
    # print(merged)
    res = merged[['name_x','difference_salaries']]
    res = res[res['difference_salaries']>0]
    res = res.drop(columns=['difference_salaries'])
    res = res.rename(columns={'name_x':'Employee'})

    return res
