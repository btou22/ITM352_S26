# Name: Brandon
# Class: ITM 352
# Assignment: Assignment 2 - Sales Dashboard
#
# Description:
# This program loads a sales dataset from a CSV file and provides an interactive
# command-line dashboard. Users can analyze the data using predefined pivot tables
# or create custom pivot tables. The program also allows exporting results to Excel
# and storing previously generated analytics for later viewing.

import pandas as pd
import time
import sys

# These settings make sure pandas prints full tables instead of cutting off columns
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)


# ---------------------------
# Data Loading Function
# ---------------------------
def load_csv(file_path):
    """
    Loads the CSV file into a pandas DataFrame.
    Displays load time, row count, and column names.
    Replaces missing values with 0 to avoid issues in pivot tables.
    """
    print(f"\nLoading file: {file_path} ...")
    start_time = time.time()

    try:
        data = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading file: {e}")
        sys.exit()

    end_time = time.time()

    print("File loaded successfully.")
    print(f"Load time: {end_time - start_time:.2f} seconds")
    print(f"Rows: {len(data)}")
    print("Columns:", list(data.columns))

    # Replace missing values so analytics don't break
    return data.fillna(0)


# ---------------------------
# Preview Data
# ---------------------------
def display_initial_rows(data):
    """
    Allows the user to preview the dataset.
    User can enter a number, 'all', or skip.
    """
    total_rows = len(data)

    choice = input(f"\nEnter rows (1–{total_rows}), 'all', or Enter: ").strip()

    if choice == "":
        return None

    if choice.lower() == "all":
        print(data.to_string())
        return data

    if choice.isdigit():
        n = int(choice)
        if 1 <= n <= total_rows:
            result = data.head(n)
            print(result.to_string())
            return result

    print("Invalid input.")
    return None


# ---------------------------
# Predefined Analytics
# ---------------------------

# Total sales grouped by region and order type
def total_sales_by_region_order_type(data):
    pivot = pd.pivot_table(
        data,
        index="sales_region",
        columns="order_type",
        values="unit_price",
        aggfunc="sum",
        fill_value=0
    )
    print(pivot.to_string())
    return pivot


# Average sales grouped by region, state, and order type
def average_sales_by_region_state_sale_type(data):
    pivot = pd.pivot_table(
        data,
        index="sales_region",
        columns=["customer_state", "order_type"],
        values="unit_price",
        aggfunc="mean",
        fill_value=0
    )
    print(pivot.to_string())
    return pivot


# Sales grouped by customer type and order type per state
def sales_by_customer_type_order_type_by_state(data):
    pivot = pd.pivot_table(
        data,
        index="customer_state",
        columns=["customer_type", "order_type"],
        values="unit_price",
        aggfunc="sum",
        fill_value=0
    )
    print(pivot.to_string())
    return pivot


# Total quantity and price grouped by region and product
def total_sales_quantity_price_by_region_product(data):
    pivot = pd.pivot_table(
        data,
        index=["sales_region", "product_category"],
        values=["quantity", "unit_price"],
        aggfunc="sum",
        fill_value=0
    )
    print(pivot.to_string())
    return pivot


# Total quantity and price grouped by customer type
def total_sales_quantity_price_by_customer_type(data):
    pivot = pd.pivot_table(
        data,
        index="customer_type",
        values=["quantity", "unit_price"],
        aggfunc="sum",
        fill_value=0
    )
    print(pivot.to_string())
    return pivot


# Max and min price per product category
def max_min_sales_price_by_category(data):
    pivot = pd.pivot_table(
        data,
        index="product_category",
        values="unit_price",
        aggfunc=["max", "min"],
        fill_value=0
    )
    print(pivot.to_string())
    return pivot


# Count unique employees in each region
def number_of_unique_employees_by_region(data):
    pivot = pd.pivot_table(
        data,
        index="sales_region",
        values="employee_name",
        aggfunc=pd.Series.nunique,
        fill_value=0
    )
    print(pivot.to_string())
    return pivot


# ---------------------------
# Custom Pivot Table Builder
# ---------------------------

# Handles user input selection for rows, columns, values, etc.
def get_user_selection(options, prompt, allow_empty=False):
    print(f"\n{prompt}")
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")

    choice = input("Enter numbers separated by commas: ").strip()

    if choice == "":
        return [] if allow_empty else None

    try:
        return [options[int(x.strip()) - 1] for x in choice.split(",")]
    except:
        print("Invalid input.")
        return None


# Builds a pivot table based on user-selected fields
def generate_custom_pivot_table(data):
    rows = get_user_selection(list(data.columns), "Select rows:")
    if not rows:
        print("Must select at least one row.")
        return None

    cols = get_user_selection(
        [c for c in data.columns if c not in rows],
        "Select columns (optional):",
        True
    )

    values = get_user_selection(
        list(data.select_dtypes(include=["number"]).columns),
        "Select values:"
    )

    agg = get_user_selection(["sum", "mean", "count"], "Select aggregation:")

    if not values or not agg:
        print("Invalid selection.")
        return None

    try:
        pivot = pd.pivot_table(
            data,
            index=rows,
            columns=cols if cols else None,
            values=values,
            aggfunc=agg[0],
            fill_value=0
        )

        print("\nCustom Pivot Table:")
        print(pivot.to_string())
        return pivot

    # Prevent crash on invalid combinations
    except:
        print("\nInvalid combination. Try fewer fields.")
        return None


# ---------------------------
# Extra Features
# ---------------------------

# Allows user to export results to Excel
def export_to_excel(pivot):
    if input("Export to Excel? (y/n): ").lower() == "y":
        filename = input("Filename: ")
        try:
            pivot.to_excel(filename)
            print("Saved.")
        except Exception as e:
            print("Export failed:", e)


# Displays stored analytics results
def show_stored_results(data, stored_results):
    if not stored_results:
        print("No stored results.")
        return

    for k, v in stored_results.items():
        print(f"\nResult {k}:")
        print(v.to_string())


# Exit function
def exit_program(data):
    sys.exit()


# ---------------------------
# Menu System
# ---------------------------

# Displays menu and returns selected option index
def display_menu(menu_options):
    print("\n--- Sales Data Dashboard ---")
    for i, (text, _) in enumerate(menu_options, 1):
        print(f"{i}. {text}")

    choice = input("Select option: ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(menu_options):
            return choice - 1

    print("Invalid choice")
    return None


# ---------------------------
# Main Program Loop
# ---------------------------
def main():
    file_name = input("Enter CSV file name: ")
    data = load_csv(file_name)

    # Stores results of analytics so user can view later
    stored_results = {}

    # Menu structure maps text to functions
    menu_options = (
        ("Show rows", display_initial_rows),
        ("Total sales by region/order type", total_sales_by_region_order_type),
        ("Average sales by region/state/type", average_sales_by_region_state_sale_type),
        ("Sales by customer/order/state", sales_by_customer_type_order_type_by_state),
        ("Quantity & price by region/product", total_sales_quantity_price_by_region_product),
        ("Quantity & price by customer", total_sales_quantity_price_by_customer_type),
        ("Max/min price by category", max_min_sales_price_by_category),
        ("Unique employees by region", number_of_unique_employees_by_region),
        ("Custom pivot table", generate_custom_pivot_table),
        ("Show stored results", lambda d: show_stored_results(d, stored_results)),
        ("Exit", exit_program)
    )

    # Runs continuously until user exits
    while True:
        selection = display_menu(menu_options)

        if selection is not None:
            result = menu_options[selection][1](data)

            # Store result and optionally export
            if result is not None:
                stored_results[len(stored_results) + 1] = result
                export_to_excel(result)


if __name__ == "__main__":
    main()