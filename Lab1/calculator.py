def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def get_number(prompt):
    while True:
        try:
            value = input(prompt)
            if value.strip().lower() in ("q", "quit", "exit"):
                raise KeyboardInterrupt
            return float(value)
        except ValueError:
            print("Invalid number. Please try again.")


def choose_operation():
    ops = {
        "1": ("Add", add),
        "2": ("Subtract", subtract),
        "3": ("Multiply", multiply),
        "4": ("Divide", divide),
        "+": ("Add", add),
        "-": ("Subtract", subtract),
        "*": ("Multiply", multiply),
        "/": ("Divide", divide),
    }
    print("Choose operation (type number or symbol, or 'h' for history, 'q' to quit):")
    print("  1. Add (+)")
    print("  2. Subtract (-)")
    print("  3. Multiply (*)")
    print("  4. Divide (/)")
    while True:
        choice = input("Enter choice: ").strip().lower()
        if choice in ("q", "quit", "exit"):
            return None
        if choice in ("h", "history"):
            return "HISTORY"
        if choice in ops:
            return ops[choice]
        # also accept words
        if choice in ("add", "subtract", "multiply", "divide"):
            mapping = {"add": "1", "subtract": "2", "multiply": "3", "divide": "4"}
            return ops[mapping[choice]]
        print("Invalid choice. Enter 1/2/3/4 or + - * /. Enter 'h' to view history or 'q' to quit.")


def main():
    print("Simple Calculator (type 'q' at prompts to quit)")
    history = []
    try:
        while True:
            try:
                a = get_number("Enter first number: ")
            except KeyboardInterrupt:
                print("\nExiting.")
                break

            try:
                b = get_number("Enter second number: ")
            except KeyboardInterrupt:
                print("\nExiting.")
                break

            op = choose_operation()
            if op is None:
                print("Exiting.")
                break
            if op == "HISTORY":
                if not history:
                    print("History is empty.")
                else:
                    print("History:")
                    for i, entry in enumerate(history, 1):
                        print(f"  {i}. {entry}")
                continue

            op_name, op_func = op
            try:
                result = op_func(a, b)
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
                history.append(f"{a} {op_name} {b} = ERROR(div-by-zero)")
            else:
                print(f"Result ({op_name}): {result}")
                history.append(f"{a} {op_name} {b} = {result}")

    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")


if __name__ == "__main__":
    main()
