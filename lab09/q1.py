import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

study_data = pd.DataFrame({
    "study_hrs": [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 7.0],
    "score": [32, 40, 41, 50, 54, 60, 62, 70, 78, 88]
})

features = study_data[["study_hrs"]]
target = study_data["score"]
reg = LinearRegression().fit(features, target)

print(f"Model equation: score = {reg.coef_[0]:.3f} * hours + {reg.intercept_:.3f}")

new_students = pd.DataFrame({"study_hrs": [5.5, 8.0]})
new_scores = reg.predict(new_students)
for hrs, sc in zip(new_students["study_hrs"], new_scores):
    print(f"A student studying {hrs} hrs is expected to score {sc:.1f}")
fitted = reg.predict(features)

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(study_data["study_hrs"], target, color="green", marker="x", s=70, label="Observed")
ax.plot(study_data["study_hrs"], fitted, color="orange", linewidth=2, label="Fitted line")
ax.set_xlabel("Number of Study Hours")
ax.set_ylabel("Marks")
ax.set_title("Linear Regression: Marks vs Study Hours")
ax.grid(True, linestyle="--", alpha=0.5)
ax.legend()
plt.show()

mae_val = mean_absolute_error(target, fitted)
mse_val = mean_squared_error(target, fitted)
r2_val = r2_score(target, fitted)
print(f"MAE = {mae_val:.3f}, MSE = {mse_val:.3f}, RMSE = {np.sqrt(mse_val):.3f}, R2 = {r2_val:.4f}")