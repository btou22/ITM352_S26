# Ask the user to enter their weight in pounds.
# Convert the weight to kilograms (1 pound = 0.453592 kg).
# Name: Brandon Tou
# Date: Jan. 22, 2026

kg_to_pounds = 0.453592

weight_in_pounds = input("Please enter your weight in pounds: ")
weight_in_pounds_float = float(weight_in_pounds)
weight_in_kg = weight_in_pounds_float * kg_to_pounds
weight_in_kg_rounded = round(weight_in_kg)

print("You entered:", weight_in_pounds_float)
print(f"Your weight in kilograms is {weight_in_kg_rounded}")

