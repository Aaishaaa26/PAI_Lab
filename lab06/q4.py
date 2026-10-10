import numpy as np

rng = np.random.default_rng(3)
readings = rng.normal(loc=50, scale=12, size=(5, 12))
print("Sensor readings (5 sensors x 12 time points):\n", np.round(readings, 2))
print("Per-sensor mean:", np.round(readings.mean(axis=1), 2))
print("Per-sensor min:", np.round(readings.min(axis=1), 2))
print("Per-sensor max:", np.round(readings.max(axis=1), 2))
print("Per-sensor std:", np.round(readings.std(axis=1), 2))
top_sensor = np.argmax(readings.mean(axis=1))
print(f"Sensor with highest average: Sensor {top_sensor + 1}")
limit = 65
above = readings > limit
print(f"Readings above {limit}:\n", above)
print("Count per sensor:", above.sum(axis=1))
for s, t in np.argwhere(above):
    print(f"Sensor {s + 1}, time {t + 1}: {readings[s, t]:.2f}")

print()