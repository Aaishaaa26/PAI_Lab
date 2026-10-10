import numpy as np

rng = np.random.default_rng(7)
image = rng.integers(0, 256, size=(6, 8), dtype=np.uint8)
print("Image:\n", image)
print("Min intensity:", image.min())
print("Max intensity:", image.max())
print("Mean intensity:", round(float(image.mean()), 2))
threshold = 128
mask = image > threshold
print(f"Binary mask (pixel > {threshold}):\n", mask)
thresholded = np.where(image > threshold, 255, 0).astype(np.uint8)
print("Thresholded image:\n", thresholded)

print()