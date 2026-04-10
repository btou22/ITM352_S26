recent_purchase = [36.13, 23.87, 183.35, 22.93, 11.62]

budget = 150
total_spent = 0

for purchase in recent_purchase:
    total_spent += purchase
    if total_spent > budget:
        print("This purchase is over budget: ", purchase)
    else:
        print("This purchase is within budget: ", purchase)