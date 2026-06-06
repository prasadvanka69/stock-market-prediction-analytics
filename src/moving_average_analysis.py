import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/apple_stock.csv")

df["MA20"] = df["Close"].rolling(window=20).mean()
df["MA50"] = df["Close"].rolling(window=50).mean()


plt.figure(figsize=(14,7))

plt.plot(df["Close"], label="Close Price")
plt.plot(df["MA20"], label="20-Day Moving Average")
plt.plot(df["MA50"], label="50-Day Moving Average")

plt.title("Apple Stock Price with Moving Averages")
plt.xlabel("Trading Days")
plt.ylabel("Price ($)")
plt.legend()
plt.grid(True)

plt.show()