import pandas as pd

df = pd.read_csv("Customer.csv")

df['Avg_Order_Value'] = df['Total_Spent'] / df['Order_Count']
print(df)
df.to_csv("Customer.csv", index=False)
