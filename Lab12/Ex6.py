# Name: Cassiddy Ginoza
# Date: Apr. 7, 2026

# use requests package to retrieve page of mortgage rate info and extract each row.

import pandas as pd
import requests

# Step 1: Access the Hawaii mortgage rates page (like example #5)
url = "https://www.hicentral.com/hawaii-mortgage-rates.php"
response = requests.get(url)

# Step 2: Read the HTML table into a DataFrame (like example #2)
data_frame = pd.read_html(response.text)
df = data_frame[0]

# Step 3: Print column names (to check table structure)
print("Column names in the DataFrame:")
print(df.columns)
print("\n")  # extra space

# Step 4: Create a list to store each row (like example #3)
mortgage_rows = []

# Step 5: Loop through each row, append to the list, and print nicely
for index, row in df.iterrows():
    # Append the row as a list
    mortgage_rows.append(row.tolist())
    
    # Extract each value for a clean output
    lender = row["Lender"]
    term = row["Term/Type"]
    rate = row["Interest Rate"]
    points = row["% Points"]
    apr = row["% *APR"]
    
    # Print each bank's current rates per row
    print(f"Bank: {lender}, Term: {term}, Rate: {rate}%, Points: {points}, APR: {apr}%")