import pandas as pd

df = pd.read_csv("Customer.csv")

city = df.groupby('City').agg({'Customer_ID': 'count', 'Total_Spent': 'mean', 'Order_Count': 'max'})
print(city)