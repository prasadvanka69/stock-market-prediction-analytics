import yfinance as yf

ticker = "AAPL"

print(f"Downloading data for {ticker}...")

stock = yf.Ticker(ticker)

data = stock.history(period="5y")

print(data.head())

data.to_csv("data/apple_stock.csv")

print("\nData saved successfully!")
print(f"Rows downloaded: {len(data)}")
print(f"Columns: {list(data.columns)}")