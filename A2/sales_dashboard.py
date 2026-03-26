import pandas as pd
import time
import sys

# Show all columns and use full terminal width when printing DataFrames
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)


def load_csv(file_path):
    print(f"\nLoading file: {file_path} ...")
    start_time = time.time()

    try:
        data = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error: Could not load file. {e}")
        sys.exit()

    end_time = time.time()

    print("File loaded successfully.")
    print(f"Load time: {end_time - start_time:.2f} seconds")
    print(f"Rows loaded: {len(data)}")
    print("Columns:")
    print(list(data.columns))

    # Replace missing values with 0
    data = data.fillna(0)

    required_columns = [
        "sales_region",
        "order_type",
        "customer_type",
        "customer_state",
        "product_category",
        "quantity",
        "unit_price",
        "employee_name"
    ]

    missing_columns = [col for col in required_columns if col not in data.columns]

    if missing_columns:
        print("\nWarning: Missing required columns:")
        for col in missing_columns:
            print(f"- {col}")
        print("Some analytics may not work.\n")

    return data


def display_initial_rows(data):
    total_rows = len(data)

    print(f"\nEnter rows to display:")
    print(f"- Enter a number from 1 to {total_rows}")
    print("- Enter 'all' to display all rows")
    print("- Press Enter to skip preview")

    choice = input("Your choice: ").strip()

    if choice == "":
        print("Skipping preview.")
        return

    if choice.lower() == "all":
        print("\nFirst rows of sales data:")
        print(data.to_string())
        return

    if choice.isdigit():
        num = int(choice)
        if 1 <= num <= total_rows:
            print("\nFirst rows of sales data:")
            print(data.head(num).to_string())
        else:
            print("Invalid row number.")
    else:
        print("Invalid input.")


def total_sales_by_region_order_type(data):
    required = ["sales_region", "order_type", "unit_price"]
    for col in required:
        if col not in data.columns:
            print(f"Cannot run this analytic. Missing column: {col}")
            return

    pivot = pd.pivot_table(
        data,
        index="sales_region",
        columns="order_type",
        values="unit_price",
        aggfunc="sum",
        fill_value=0
    )

    print("\nTotal sales by region and order type:")
    print(pivot.to_string())


def average_sales_by_region_state_sale_type(data):
    required = ["sales_region", "customer_state", "order_type", "unit_price"]
    for col in required:
        if col not in data.columns:
            print(f"Cannot run this analytic. Missing column: {col}")
            return

    pivot = pd.pivot_table(
        data,
        index="sales_region",
        columns=["customer_state", "order_type"],
        values="unit_price",
        aggfunc="mean",
        fill_value=0
    )

    print("\nAverage sales by region with average sales by state and sale type:")
    print(pivot.to_string())


def sales_by_customer_type_order_type_by_state(data):
    required = ["customer_state", "customer_type", "order_type", "unit_price"]
    for col in required:
        if col not in data.columns:
            print(f"Cannot run this analytic. Missing column: {col}")
            return

    pivot = pd.pivot_table(
        data,
        index="customer_state",
        columns=["customer_type", "order_type"],
        values="unit_price",
        aggfunc="sum",
        fill_value=0
    )

    print("\nSales by customer type and order type by state:")
    print(pivot.to_string())


def total_sales_quantity_price_by_region_product(data):
    required = ["sales_region", "product_category", "quantity", "unit_price"]
    for col in required:
        if col not in data.columns:
            print(f"Cannot run this analytic. Missing column: {col}")
            return

    pivot = pd.pivot_table(
        data,
        index=["sales_region", "product_category"],
        values=["quantity", "unit_price"],
        aggfunc="sum",
        fill_value=0
    )

    print("\nTotal sales quantity and price by region and product:")
    print(pivot.to_string())


def total_sales_quantity_price_by_customer_type(data):
    required = ["customer_type", "quantity", "unit_price"]
    for col in required:
        if col not in data.columns:
            print(f"Cannot run this analytic. Missing column: {col}")
            return

    pivot = pd.pivot_table(
        data,
        index="customer_type",
        values=["quantity", "unit_price"],
        aggfunc="sum",
        fill_value=0
    )

    print("\nTotal sales quantity and price by customer type:")
    print(pivot.to_string())


def max_min_sales_price_by_category(data):
    required = ["product_category", "unit_price"]
    for col in required:
        if col not in data.columns:
            print(f"Cannot run this analytic. Missing column: {col}")
            return

    pivot = pd.pivot_table(
        data,
        index="product_category",
        values="unit_price",
        aggfunc=["max", "min"],
        fill_value=0
    )

    print("\nMax and min sales price by category:")
    print(pivot.to_string())


def number_of_unique_employees_by_region(data):
    required = ["sales_region", "employee_name"]
    for col in required:
        if col not in data.columns:
            print(f"Cannot run this analytic. Missing column: {col}")
            return

    pivot = pd.pivot_table(
        data,
        index="sales_region",
        values="employee_name",
        aggfunc=pd.Series.nunique,
        fill_value=0
    )

    print("\nNumber of unique employees by region:")
    print(pivot.to_string())


def get_user_selection(options, prompt, allow_empty=False):
    print(f"\n{prompt}")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    choice = input("Enter number(s) separated by commas: ").strip()

    if choice == "":
        if allow_empty:
            return []
        print("You must choose at least one option.")
        return None

    try:
        selected_indexes = [int(x.strip()) - 1 for x in choice.split(",")]
        selected_items = []

        for index in selected_indexes:
            if index < 0 or index >= len(options):
                print("Invalid selection.")
                return None
            selected_items.append(options[index])

        return selected_items
    except ValueError:
        print("Invalid input.")
        return None


def generate_custom_pivot_table(data):
    row_options = list(data.columns)
    value_options = list(data.select_dtypes(include=["number"]).columns)
    agg_options = ["sum", "mean", "count"]

    rows = get_user_selection(row_options, "Select rows:", allow_empty=False)
    if rows is None:
        return

    col_options = [col for col in row_options if col not in rows]
    cols = get_user_selection(col_options, "Select columns (optional):", allow_empty=True)
    if cols is None:
        return

    values = get_user_selection(value_options, "Select values:", allow_empty=False)
    if values is None:
        return

    agg = get_user_selection(agg_options, "Select aggregation function:", allow_empty=False)
    if agg is None:
        return

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
    except Exception as e:
        print(f"Error creating pivot table: {e}")


def exit_program(data):
    print("Exiting program.")
    sys.exit()


def display_menu(menu_options):
    print("\n--- Sales Data Dashboard ---")
    for i, (menu_text, _) in enumerate(menu_options, start=1):
        print(f"{i}. {menu_text}")

    choice = input("Select an option: ").strip()

    if not choice.isdigit():
        print("Invalid input. Enter a number.")
        return None

    choice = int(choice)

    if 1 <= choice <= len(menu_options):
        return choice - 1

    print("Invalid menu choice.")
    return None


def main():
    file_name = input("Enter CSV file name: ").strip()
    data = load_csv(file_name)

    menu_options = (
        ("Show the first n rows of sales data", display_initial_rows),
        ("Total sales by region and order_type", total_sales_by_region_order_type),
        ("Average sales by region with average sales by state and sale type", average_sales_by_region_state_sale_type),
        ("Sales by customer type and order type by state", sales_by_customer_type_order_type_by_state),
        ("Total sales quantity and price by region and product", total_sales_quantity_price_by_region_product),
        ("Total sales quantity and price by customer type", total_sales_quantity_price_by_customer_type),
        ("Max and min sales price by category", max_min_sales_price_by_category),
        ("Number of unique employees by region", number_of_unique_employees_by_region),
        ("Create a custom pivot table", generate_custom_pivot_table),
        ("Exit", exit_program)
    )

    while True:
        selection = display_menu(menu_options)
        if selection is not None:
            menu_options[selection][1](data)


if __name__ == "__main__":
    main()