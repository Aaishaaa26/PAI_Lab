import numpy as np

rng = np.random.default_rng(1)
X = rng.normal(loc=[10, 50, 100, 5], scale=[2, 10, 25, 1], size=(10, 4))
print("Feature matrix shape:", X.shape)
means = X.mean(axis=0)
stds = X.std(axis=0)
print("Feature means:", np.round(means, 3))
print("Feature standard deviations:", np.round(stds, 3))
Z = (X - means) / stds
print("Standardized means:", np.round(Z.mean(axis=0), 10))
print("Standardized stds:", np.round(Z.std(axis=0), 10))
print("Means approx 0:", np.allclose(Z.mean(axis=0), 0))
print("Stds approx 1:", np.allclose(Z.std(axis=0), 1))
print("X shape:", X.shape, "| means shape:", means.shape, "| stds shape:", stds.shape)
print("Broadcasting: means and stds have shape (4,), X has shape (10, 4).")
print("NumPy aligns shapes from the right, stretches (4,) to (1, 4), then virtually")
print("repeats it across all 10 rows, so each feature column is shifted and scaled")
print("by its own mean and std without loops or copying the statistics.")

print()