import pandas as pd

df = pd.read_csv("Customer.csv")

print(df.shape)
print(df.dtypes)
print(df.isnull().sum())