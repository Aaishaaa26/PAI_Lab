import pandas as pd
df = pd.read_csv("Customer.csv")

vip_customers = df[(df['IS_VIP'] == True) & df['City'].isin(['Karachi', 'Lahore'])]

print(vip_customers.groupby('City')['Order_Count'].mean())
