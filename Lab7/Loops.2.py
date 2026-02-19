prices = [100, 50, 20, 356]

total = 0
item_count = 0

for price in prices:
    item_count += 1
    if item_count > 2:
        discounted_price = price * 0.9  # Apply a 10% discount
    else:
        discounted_price = price
    total += discounted_price

rounded_total = round(total, 2)  # Round to 2 decimal places
print(f"Total price: ${rounded_total:.2f}")