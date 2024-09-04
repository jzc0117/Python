# https://platform.stratascratch.com/coding/9782-customer-revenue-in-march?code_type=2&via=keith
# Customer Revenue in March

# Calculate the total revenue from each customer in March 2019. Include only customers who were active in March 2019.
# Output the revenue along with the customer id and sort the results based on the revenue in descending order.

# Import your libraries
import pandas as pd

# Start writing code

orders['order_year'] = orders['order_date'].dt.year
orders['order_month'] = orders['order_date'].dt.month

march_orders = orders[(orders['order_year']==2019) & (orders['order_month']==3)]

res = march_orders.groupby(['cust_id'])['total_order_cost'].sum().reset_index()
res = res.sort_values(by='total_order_cost',ascending=False)
res
