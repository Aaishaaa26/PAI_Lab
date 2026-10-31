import pandas as pd
df = pd.read_csv("Customer.csv")
#Customer distribution: Lahore has the highest number of customers, with 41 customers.
print("Customers per city:")
print(df['City'].value_counts())

#Spending behavior: Karachi has the highest average customer spending, approximately Rs. 27,379.05.
print("\nAverage spending per city:")
print(df.groupby('City')['Total_Spent'].mean())

#Product revenue: Books generate the highest total revenue (approximately Rs. 1,003,473.64), slightly more than Electronics.
print("\nRevenue per category:")
print(df.groupby('Category')['Total_Spent'].sum())