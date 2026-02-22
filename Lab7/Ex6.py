data = ("hello", 10, "goodbye", 3, "goodnight", 5)
x = input("Enter a value to append: ")

temp = list(data)
temp.append(x)
data = tuple(temp)

print("Appended tuple:", data)


