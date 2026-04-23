import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("taxi trips Fri 7_7_2017.csv")

df = df.dropna(subset=["pickup_community_area", "dropoff_community_area"])

heatmap_data = df.pivot_table(
    index="pickup_community_area",
    columns="dropoff_community_area",
    aggfunc="size",
    fill_value=0
)

plt.figure(figsize=(12, 10))

sns.heatmap(heatmap_data, cmap="coolwarm") 

plt.title("Taxi Trips Heatmap")
plt.xlabel("Dropoff Community Area")
plt.ylabel("Pickup Community Area")

plt.show()