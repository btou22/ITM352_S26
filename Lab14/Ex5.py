import json
import matplotlib.pyplot as plt

filename = "Trips from area 8.json"

x_axis = []
y_axis = []
with open(filename) as file:
    data = json.load(file)

    for trip in data:
        x_axis.append(float(trip["fare"]))
        y_axis.append(float(trip["trip_miles"]))


# plt.scatter(x_axis, y_axis)
# plt.plot(x_axis, y_axis, linestyle= "none", marker = ".")
plt.plot(x_axis, y_axis, linestyle = "none", marker = "v", color = "cyan", alpha = 0.2) #alpha is for transparency

plt.title("Fare Amount vs Trip Miles")
plt.xlabel("Fare Amount")
plt.ylabel("Trip Miles")

plt.show()