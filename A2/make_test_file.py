import pandas as pd

# Put your direct CSV link here if you have one
csv_url = "PASTE_DIRECT_CSV_LINK_HERE"

try:
    df = pd.read_csv(csv_url)
    df.head(10).to_csv("sales_data_test.csv", index=False)
    print("sales_data_test.csv created successfully")
except Exception as e:
    print("Error:", e)