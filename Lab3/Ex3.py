def sqrt(number):
    """Calculate the square root of a number."""
    if number < 0:
        return None 
    return number ** 0.5

number_in = float(input("Enter a number to find its square root: "))

result = sqrt(number_in)
if result is not None:
    print("Cannot calculate the square root of a negative number.")
else:
    print(f"The square root of {number_in} is {result}.")



