from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_json("Trips from area 8.json")

# Drop missing values (important for 3D plots)
df = df.dropna(subset=["fare", "trip_miles", "dropoff_centroid_latitude"])

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot
ax.scatter(
    df["fare"],
    df["trip_miles"],
    df["dropoff_centroid_latitude"]
)

# Labels
ax.set_xlabel("Fare ($)")
ax.set_ylabel("Trip Miles")
ax.set_zlabel("Dropoff Area")

plt.title("3D Plot of Fare, Trip Miles, and Dropoff Area")

plt.show()