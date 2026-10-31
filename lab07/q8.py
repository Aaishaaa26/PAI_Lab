import pandas as pd

df = pd.read_csv("Customer.csv")

pivot = pd.pivot_table(df, index = 'Category', columns = 'Is_VIP', values = 'Total_Spent', aggfunc = 'sum')
print(pivot)

#index displays categories as row. columns display vip status, either true or false column. values is the column being analyzed, which is total spent. aggfunc is the function being applied to the values, which is sum.   