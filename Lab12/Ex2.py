# Grab 1 month interest rate data from the Treasury website
import ssl
import pandas as pd
import urllib.request
import lxml

url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202603"

# Open the URL and use read_html to read the data into a DataFrame
ssl._create_default_https_context = ssl._create_unverified_context

print("Opening URL: " + url)
web_page = urllib.request.urlopen(url)
data_frame = pd.read_html(web_page)

# print(data_frame[0].info())
#print(data_frame[0])

# Print the column names to understand the structure of the DataFrame
print("Column names in the DataFrame:")
print(data_frame[0].columns)

# Extract the 1 month interest rate data
int_rate_table = data_frame[0]  # Assuming the first table is the one we want

# Print the table of 1 month interest rates
print("\n1 Month Treasury Rates:\n")
for index, row in int_rate_table.iterrows():
    print(f"Index: {index}, Date: {row['Date']}, 1 Month Rate: {row['1 Mo']}")