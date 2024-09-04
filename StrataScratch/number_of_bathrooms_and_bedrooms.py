# https://platform.stratascratch.com/coding/9622-number-of-bathrooms-and-bedrooms?code_type=2
# Number of Bathrooms and Bedrooms

# Find the average number of bathrooms and bedrooms for each city’s property types. Output the result along with the city name and the property type.

# Import your libraries
import pandas as pd

# Start writing code
airbnb_search_details.head()

details = airbnb_search_details[['city','property_type','bathrooms','bedrooms']]
details = details.groupby(['city','property_type']).mean().reset_index()
details
