import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

data = df[df['scenario'] == '03_SalaryDiff']

order = ['Entry', 'Mid', 'Senior']

sns.boxplot(data=data, x='prep_course', y='exam_score', order=order, palette='Set2')

plt.title("Salary Spread Across Experience Levels")
plt.xlabel("Experience Level")
plt.ylabel("Salary ($)")

plt.show()