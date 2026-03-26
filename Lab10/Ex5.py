# Read in a CSV file of homes data and create a dataframe.
# Do some filtering and statistics on the data.
import pandas as pd

df_homes = pd.read_csv("homes_data.csv")

# Print out the shape of the dataframe and the first few rows.
shape = df_homes.shape
print(f"The homes data has {shape[0]} rows and {shape[1]} columns.")
print(df_homes.head(10))

# Select only the properties with 500 or more units
df_big_properties = df_homes[df_homes["units"] >= 500]
df_big_properties = df_big_properties.drop(columns=["id", "easement"])
print(df_big_properties.head(10))

# Convert columns to appropriate data types
df_big_properties["sale_price"] = pd.to_numeric(df_big_properties["sale_price"], errors="coerce")
df_big_properties["land_sqft"] = pd.to_numeric(df_big_properties["land_sqft"], errors="coerce")
df_big_properties["gross_sqft"] = pd.to_numeric(df_big_properties["gross_sqft"], errors="coerce")

# Drop rows with missing values in the numeric columns
df_big_properties = df_big_properties.dropna() 

# Drop duplicate rows 
df_big_properties = df_big_properties.drop_duplicates()

# Print out the first 10 rows after cleansing
print("After cleaning:")
print(df_big_properties.head(10))

print("After dropping 0 sales:")
df_big_properties = df_big_properties[df_big_properties["sale_price"] > 0]
print(df_big_properties.head(10))

# caldulate the average sale price per square foot for the big properties
average_price = df_big_properties["sale_price"].mean()
print(f"The mean sales price for the big properties is ${average_price:.2f}")