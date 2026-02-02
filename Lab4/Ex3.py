# Manipulate a list in various ways
# Name: Brandon Tou
# Date: Feb. 1, 2026

responseValues = [5, 7, 3, 8]
responseValues.append(0)
print("After appending 0:", responseValues)

# responseValues.insert(2, 6)
responseValues = responseValues[:2] + [6] + responseValues[2:]
print("After inserting 6 at index 2:", responseValues)


