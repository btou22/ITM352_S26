import json
import matplotlib.pyplot as plt

filename = "Trips from area 8.json"

x_axis = []
y_axis = []
with open(filename) as file:
    data = json.load(file)

    for trip in data:
        if float(trip["trip_miles"]) > 2:
            fare_number = float(trip["fare"])
            x_axis.append(fare_number)
            y_axis.append(float(trip["trip_miles"]))

plt.scatter(x_axis, y_axis)

plt.title("Fares by Trip Miles for Trips Longer than 2 Miles")
plt.xlabel("Fares")
plt.ylabel("Trip Miles")

plt.savefig("FaresXmiles.png")
plt.show()