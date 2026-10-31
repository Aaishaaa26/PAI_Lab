import pandas as pd

df = pd.read_csv("Customer.csv")

df['Age'] = df['Age'].fillna(df['Age'].median())

df['Total_Spent'] = df['Total_Spent'].fillna(df['Total_Spent'].mean())

print(df)