# Create a function called midpoint.

def midpoint(num1, num2):
    """Calculate the midpoint between two numbers."""
    mid = (num1 + num2) / 2
    return mid

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
result = midpoint(number1, number2)
print(f"The midpoint between {number1} and {number2} is {result}.")

