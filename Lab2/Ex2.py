# ask the user to enter their birth year. Calculate their age
# age based on the current year (2026) and print it out.
# Name: Brandon Tou
# Date : Jan. 20, 2026

birth_year = input("Please enter your birth year: ")
birth_year_int = int(birth_year)
CURRENT_YEAR = 2026
age = CURRENT_YEAR - birth_year
print("You entered", birth_year) 
print(f"you are {age} years old.")
      