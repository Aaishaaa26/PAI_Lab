import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

data = df[df['scenario'] == '02_MonthlySales']

techstore = data[data['school_type'] == 'TechStore']
apparelco = data[data['school_type'] == 'ApparelCo']

plt.plot(techstore['study_hours'], techstore['exam_score'], marker='o', label='TechStore')
plt.plot(apparelco['study_hours'], apparelco['exam_score'], marker='o', label='ApparelCo')

plt.title("Monthly Revenue Trends (Jan - Jun 2023)")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")

plt.legend()
plt.grid(True)

plt.show()