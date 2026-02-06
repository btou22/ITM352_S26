miles = [1.1, 0.8, 2.5, 2.6]
fares = (6.25, 5.25, 10.50, 8.05)   # numbers, not strings

trip_records = [{"miles": m, "fare": f} for m, f in zip(miles, fares)]

print(trip_records)

# Print the 3rd trip properly formatted
third = trip_records[2]
print(f"3rd trip miles: {third['miles']}")
print(f"3rd trip fare: ${third['fare']:.2f}")
