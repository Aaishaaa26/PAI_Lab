import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

data = df[df['scenario'] == '05_AdVsRevenue'].copy()

data['study_hours'] = pd.to_numeric(data['study_hours'])

sns.regplot( data=data, x='study_hours', y='exam_score', scatter_kws={'color': 'darkgreen', 'marker': '+'})

plt.title("Impact of Advertising Spend on Total Revenue")
plt.xlabel("Ad Spend ($)")
plt.ylabel("Revenue ($)")
plt.grid(True)

plt.show()