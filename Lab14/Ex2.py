import json
import matplotlib.pyplot as plt

filename = "Trips from area 8.json"

x_axis = []
with open(filename) as file:
    data = json.load(file)

    for trip in data:
        x_axis.append(float(trip["trip_miles"]))

plt.hist(x_axis, bins=10)

plt.title("Trip Miles Distribution")
plt.xlabel("Trip Miles")
plt.ylabel("Frequency")

plt.show()