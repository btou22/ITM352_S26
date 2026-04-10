# Read in a CSV file and create a dataframe.
# Pivot the dataframe, aggregating sales by region, with columns defined by order_type and totals.

import pandas as pd
import numpy as np
import pyarrow

filename = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

pd.set_option('display.max_columns', None)  # Show all columns in the output

df = pd.read_csv(filename, engine='pyarrow')
df['order_date'] = pd.to_datetime(df['order_date'], format='%m/%d/%Y', errors='coerce')  # Convert order_date to datetime, coercing errors to NaT

# Coerce quantiy and unit_price to numeric, setting errors to NaN
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')
df['sales'] = df['quantity'] * df['unit_price']  # Calculate sales as quantity multiplied by unit price
 
pivot_table = pd.pivot_table(df,
                             index='sales_region',
                             values='sales',
                             columns='order_type',
                             aggfunc=np.sum,
                             margins=True,
                             margins_name='Total Sales')
print(pivot_table)