user_input = input("Enter a whole number between 1 and 100: ")
number = int(user_input)
square = number ** 2

print("You entered", number, "and the square is", square)

CURRENT_YEAR = 2019

year_input = input("Enter your birth year (4 digits): ")
birth_year = int(year_input)

age = CURRENT_YEAR - birth_year

print("You entered", birth_year, "and your age is", age)

user_input = input("Enter a decimal number between 1 and 100: ")
number = float(user_input)
square = number ** 2

print("You entered", number, "and the square is", square)

user_input = input("Enter a decimal number between 1 and 100: ")
number = float(user_input)

square = number ** 2

print("You entered", round(number, 2), "and the square is", round(square, 2))

sentence = input("Enter a sentence: ")
length = len(sentence)

print("Your sentence has", length, "characters.")

print("Pounds:", float(input("Enter weight in pounds: ")), "Kilograms:", float(input("Enter weight in pounds: ")) * 0.453592)

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * (5 / 9)

print("Fahrenheit:", fahrenheit)
print("Celsius:", celsius)

def fahrenheit_to_celsius(f_temp):
    return (f_temp - 32) * (5 / 9)

print("32°F =", fahrenheit_to_celsius(32), "°C")
print("212°F =", fahrenheit_to_celsius(212), "°C")
