import pandas as pd

df = pd.read_csv("Customer.csv")
df.dropna(subset =['Customer_ID'], inplace=True)
print(df)