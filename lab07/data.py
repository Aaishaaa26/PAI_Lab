import pandas as pd
import numpy as np

np.random.seed(42)
n_rows = 150

data = {
    'Customer_ID': [f'CUST_{1000 + i}' if i % 12 != 0 else np.nan for i in range(n_rows)],
    'Join_Date': pd.date_range(start='2023-01-01', periods=n_rows, freq='2D'),
    'Age': [np.random.randint(18, 65) if i % 7 != 0 else np.nan for i in range(n_rows)],
    'Gender': np.random.choice(['Male', 'Female', 'Other'], size=n_rows, p=[0.48, 0.48, 0.04]),
    'City': np.random.choice(['Karachi', 'Lahore', 'Islamabad', 'Peshawar'], size=n_rows),
    'Category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Books'], size=n_rows),
    'Order_Count': np.random.randint(1, 30, size=n_rows),
    'Total_Spent': [round(np.random.uniform(500, 50000), 2) if i % 9 != 0 else np.nan for i in range(n_rows)],
    'Is_VIP': np.random.choice([True, False], size=n_rows, p=[0.2, 0.8])
}

df = pd.DataFrame(data)
df.to_csv("Customer.csv", index = False)
