# https://platform.stratascratch.com/coding/9814-counting-instances-in-text?code_type=2
# Counting Instances in Text

# Find the number of times the words 'bull' and 'bear' occur in the contents. We're counting 
# the number of times the words occur so words like 'bullish' should not be included in our count.
# Output the word 'bull' and 'bear' along with the corresponding number of occurrences.


# Import your libraries
import pandas as pd
import re
# Start writing code
google_file_store.head()

# contains_bear = google_file_store[google_file_store['contents'].str.contains(r"\bbear\b", flags=re.I, regex=True)]
# contains_bull = google_file_store[google_file_store['contents'].str.contains(r"\bbull\b", flags=re.I, regex=True)]

# print(len(google_file_store))
# print(len(contains_bear))
# print(len(contains_bull))

# gfs['bear'] = google_file_store['contents'].apply(lambda x : len(re.findall(r'\bbear\b',x)))
# gfs['bull'] = google_file_store['contents'].apply(lambda x : len(re.findall(r'\bbull\b',x)))

# gfs.groupby(['bear','bull']).sum().reset_index()

# result = gfs[['bear','bull']].sum().reset_index()
# result

bear_count = google_file_store['contents'].str.count('bear').sum()
bull_count = google_file_store['contents'].str.count('bull').sum()

res = [['bull',bull_count], ['bear',bear_count]]
res
