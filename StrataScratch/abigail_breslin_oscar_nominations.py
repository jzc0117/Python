https://platform.stratascratch.com/coding/10128-count-the-number-of-movies-that-abigail-breslin-nominated-for-oscar?code_type=2

# Import your libraries
import pandas as pd

# Start writing code
oscar_nominees.head()

res = len(oscar_nominees[oscar_nominees['nominee']=='Abigail Breslin'])
res
