country_capitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa",
    "England": "London"}    

print(country_capitals)

print(country_capitals["Canada"])
print(country_capitals["England"])

country_capitals["Italy"] = "Rome"
print(country_capitals)

country_capitals["Italy"] = "Milan"
print(country_capitals)

print("Germany" in country_capitals)
print("Spain" in country_capitals)
