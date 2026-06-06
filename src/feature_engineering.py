import pandas as pd

df = pd.read_csv("data/apple_stock.csv")

df["Daily_Return"] = df["Close"].pct_change()


df["MA20"] = df["Close"].rolling(20).mean()
df["MA50"] = df["Close"].rolling(50).mean()

df["Volatility"] = df["Daily_Return"].rolling(20).std()


df.dropna(inplace=True)


df.to_csv("data/apple_stock_features.csv", index=False)

print("Feature engineering completed!")
print(df.head())