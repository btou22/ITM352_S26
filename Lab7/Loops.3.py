health = 100

while health > 0:
    print(f"Current health: {health}")
    damage = int(input("Enter damage taken: "))
    health -= damage

    print("I'm in the loop now")

print("Game over!")