import json
import matplotlib.pyplot as plt

filename = "Trips_Fri07072017T4 trip_miles gt1.json"

x_axis = []
y_axis = []
with open(filename) as file:
    data = json.load(file)

    for trip in data:
        x_axis.append(float(trip["fare"]))
        y_axis.append(float(trip["tips"]))


plt.scatter(x_axis, y_axis)

plt.title("Fare Amount vs Tip Amount")
plt.xlabel("Fare Amount")
plt.ylabel("Tip Amount")

plt.show()