# Ask the user to enter a temperature in Fahrenheit.
# Convert the temperature to Celsius using the formula: C - F = (F - 32) * (5/9)
# Name: Brandon Tou
# Date: Jan. 22, 2026

farenheit_input = input("Please enter a temperature in Fahrenheit: ")
farenheit_float = float(farenheit_input)
celsius_value = (farenheit_float - 32) * (5 / 9)
celsius_value_rounded = round(celsius_value,1)

print("You entered:", farenheit_value)
print(f"The temperature in Celsius is {celsius_value_rounded}")