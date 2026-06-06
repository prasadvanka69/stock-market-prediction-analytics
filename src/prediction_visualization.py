import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data/apple_stock_features.csv")

df["Target"] = df["Close"].shift(-1)
df.dropna(inplace=True)

X = df[
    ["Open", "High", "Low", "Volume", "MA20", "MA50", "Volatility"]
]

y = df["Target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

plt.figure(figsize=(12,6))

plt.plot(y_test.values[:100], label="Actual Price")
plt.plot(predictions[:100], label="Predicted Price")

plt.title("Actual vs Predicted Stock Prices")
plt.xlabel("Observations")
plt.ylabel("Price ($)")
plt.legend()
plt.grid(True)

plt.show()