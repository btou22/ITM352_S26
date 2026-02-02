shopping_list = []

shopping_list.append("apples")
shopping_list.append("bananas")
shopping_list.append("carrots")
shopping_list.insert(0, "eggs")
shopping_list.append("eggs")
shopping_list.sort()
shopping_list.remove("apples")
shopping_list.pop()

print("Current shopping list:", shopping_list)