import pandas as pd
df = pd.read_csv("Customer.csv")

filtered = df[df['category'].isin(['Electronics', 'Clothing'])]
top = filtered.nlargest(5, 'Time_spent')
print(top)
