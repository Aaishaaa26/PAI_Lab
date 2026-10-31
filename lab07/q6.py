import pandas as pd

df = pd.read_csv("Customer.csv")

df["High_Value_Customer"] = df["Total_Spent"] > 1000

df.to_csv("Customer.csv", index=False)