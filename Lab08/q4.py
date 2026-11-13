import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

data = df[df['scenario'] == '04_CustAgeDist']

sns.histplot( data=data, x='prep_course', bins=5, hue='study_hours', kde=True )

plt.title("Customer Age Distribution by Gender")
plt.xlabel("Age")
plt.ylabel("Customer Count")

plt.show()