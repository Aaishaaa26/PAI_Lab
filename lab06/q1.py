import numpy as np

rng = np.random.default_rng(42)
marks = rng.integers(30, 100, size=(10, 5))
print("Marks (10 students x 5 subjects):\n", marks)
totals = marks.sum(axis=1)
averages = marks.mean(axis=1)
subject_averages = marks.mean(axis=0)
print("Student totals:", totals)
print("Student averages:", np.round(averages, 2))
print("Subject averages:", np.round(subject_averages, 2))
best = np.argmax(averages)
print(f"Top student: Student {best + 1} with average {averages[best]:.2f}")
print("Students with average >= 50:", np.sum(averages >= 50))
status = np.where(averages >= 50, "Pass", "Fail")
print("Pass/Fail:", status)

print()