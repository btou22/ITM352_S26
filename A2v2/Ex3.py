# Read in a  file from a URL and save a local CSV file with the first 10 rows.
# 

import time

import pandas as pd
import numpy as np
import pyarrow


pd.set_option('display.max_columns', None)  # Show all columns in the output


def load_csv(filepath):
    print(f"Loading data from {filepath}...")
    start_time = time.time()
    try:
        df = pd.read_csv(filepath, engine='python')
        end_time = time.time()
        load_time = end_time - start_time
        print(f"CSV file loaded succesfully in {load_time:.2f} seconds.")
        print(f"number of rows: {len(df)}")
        print(f"Columns: {df.columns.tolist()}")
        df['order_date'] = pd.to_datetime(df['order_date'], format='%m/%d/%Y', errors='coerce')  # Convert order_date to datetime, coercing errors to NaT
#        df.fillna(0, inplace=True)  # Fill NaN values with 0 for numeric columns
        df['sales'] = df['quantity'] * df['unit_price']  # Create a new 'sales' column as quantity * unit_price

        required_columns = ['quantity', 'unit_price', 'order_date']
        # Check if required columns are present
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"Warning: Missing required columns: {missing_columns}")        
        else: 
            print("All required columns are present.")

        return df
    
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None


def display_initial_rows(dataframe):
    print("Enter rows to display:")
    print(f"- Enter a number 1 to {len(dataframe)}")
    print("- Enter 'all' to display all rows")
    print("- to skip preview, press Enter")
    user_input = input("Your choice: ").strip().lower()

    if user_input == '':
        print("Skipping preview.")
        return
    elif user_input == 'all':
        print("Displaying all rows:")
        print(dataframe)
    elif user_input.isdigit and 1 <= int(user_input) <= len(dataframe):
        print(f"Displaying first {user_input} rows:")
        print(dataframe.head(int(user_input)))
    else:
        print("Invalid input. Please try again.")


# Call load_csv to load the data and print the first 10 rows
#filename = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"
filename = "sales_data_test.csv"
sales_data = load_csv(filename)


# Run the main processing loop
def main():
    while True:
        print("Sales Data Dashboard")
        display_initial_rows(sales_data)

# Check if this is the main module being run
if __name__ == "__main__":
    main()