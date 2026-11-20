import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

study_hours = np.array([1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 7.0])
obtained_marks = np.array([32, 40, 41, 50, 54, 60, 62, 70, 78, 88])

def train_gd(inputs, targets, learning_rate, total_epochs):
    slope = 0
    intercept = 0
    error_history = []
    count = len(inputs)

    for current_epoch in range(1, total_epochs + 1):
        estimates = slope * inputs + intercept
        slope_gradient = (2 / count) * np.sum((estimates - targets) * inputs)
        intercept_gradient = (2 / count) * np.sum(estimates - targets)

        slope -= learning_rate * slope_gradient
        intercept -= learning_rate * intercept_gradient

        if current_epoch % 100 == 0:
            current_error = np.mean((targets - (slope * inputs + intercept)) ** 2)
            error_history.append(current_error)
            print("Rate", learning_rate, "at iteration", current_epoch, "has MSE", round(current_error, 4))

    return slope, intercept, error_history

rates = (0.001, 0.01, 0.05)
plt.figure(figsize=(8, 5))

for current_rate in rates:
    final_slope, final_intercept, errors = train_gd(
        study_hours, obtained_marks, current_rate, 1000
    )
    print("For rate", current_rate, "the learned line is y =", round(final_slope, 4),
          "* x +", round(final_intercept, 4))
    plt.plot(np.arange(100, 1001, 100), errors, marker="o", label=f"Rate {current_rate}")

check_model = LinearRegression()
check_model.fit(study_hours.reshape(-1, 1), obtained_marks)

print("Reference slope:", round(check_model.coef_[0], 4))
print("Reference intercept:", round(check_model.intercept_, 4))

plt.xlabel("Training Epoch")
plt.ylabel("MSE")
plt.title("Error Reduction During Training")
plt.legend()
plt.show()
