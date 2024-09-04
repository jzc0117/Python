# https://platform.stratascratch.com/coding/10176-bikes-last-used?code_type=2
# Bikes Last Used

# Find the last time each bike was in use. Output both the bike number and the date-timestamp of the bike's 
# last use (i.e., the date-time the bike was returned). Order the results by bikes that were most recently used.

# Import your libraries
import pandas as pd

# Start writing code
dc_bikeshare_q1_2012.head()

bike_df = dc_bikeshare_q1_2012[['bike_number','end_time']]
bike_df = bike_df.groupby(['bike_number']).last().reset_index()
bike_df = bike_df.sort_values(['end_time'],ascending=False)

bike_df
