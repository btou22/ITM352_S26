age = 70
weekday = "Tuesday"     # e.g., "Monday", "Friday"
matinee = True          # True or False

price_options = [14]    # normal price always applies

# senior discount
if age >= 65:
    price_options.append(8)

# Tuesday special
if weekday == "Tuesday":
    price_options.append(10)

# matinee pricing overrides with potentially lower price
if matinee:
    if age >= 65:
        price_options.append(5)
    else:
        price_options.append(8)

final_price = min(price_options)

print("age:", age)
print("weekday:", weekday)
print("matinee:", matinee)
print("price:", final_price)
