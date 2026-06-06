import pandas as pd

df = pd.read_csv("data/apple_stock_features.csv")

df.to_csv("data/powerbi_stock_data.csv", index=False)

print("Power BI dataset created successfully!")