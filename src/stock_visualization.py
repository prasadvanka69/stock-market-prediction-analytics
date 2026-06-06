import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/apple_stock.csv")

plt.figure(figsize=(12,6))
plt.plot(df["Close"])

plt.title("Apple Stock Closing Price (5 Years)")
plt.xlabel("Trading Days")
plt.ylabel("Closing Price ($)")
plt.grid(True)

plt.show()