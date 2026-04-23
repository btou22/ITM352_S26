# Use payment method as the X axis and (sum of) tips as the Y axis.  
# drop rows with na values

import json
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_json("Trips from area 8.json")

df = df.dropna(subset=["payment_type", "tips"])

tips_by_payment = df.groupby("payment_type")["tips"].sum()

tips_by_payment.plot(kind="bar")

plt.xlabel("Payment Method")
plt.ylabel("Total Tips")
plt.title("Total Tips by Payment Method")

plt.show()

pivot = pd.pivot_table(
    df,
    values="tips",
    index="payment_type",
    aggfunc="sum"
)

print(pivot)