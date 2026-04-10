def leap_expr(year):
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)

# Example tests (replace 2003/2004 with your birth year + closest leap year)
birth_year = 2003
closest_leap_year = 2004

print(birth_year, "=>", "Leap year" if leap_expr(birth_year) else "Not a leap year")
print(closest_leap_year, "=>", "Leap year" if leap_expr(closest_leap_year) else "Not a leap year")

def isLeapYear(year):
    if year % 400 == 0:
        return "Leap year"
    if year % 100 == 0:
        return "Not a leap year"
    if year % 4 == 0:
        return "Leap year"
    return "Not a leap year"

print(isLeapYear(2003))  # Not a leap year
print(isLeapYear(2004))  # Leap year

# Tests (replace with your birth year and closest leap year)
birth_year = 2003
closest_leap_year = 2004

print(birth_year, "=>", isLeapYear(birth_year))
print(closest_leap_year, "=>", isLeapYear(closest_leap_year))

def isLeapYear_safe(year):
    if not isinstance(year, int):
        raise TypeError("year must be an integer")
    if year <= 0:
        raise ValueError("year must be a positive integer")

    if year % 400 == 0:
        return "Leap year"
    if year % 100 == 0:
        return "Not a leap year"
    if year % 4 == 0:
        return "Leap year"
    return "Not a leap year"
