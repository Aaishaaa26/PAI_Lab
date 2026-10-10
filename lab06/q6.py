import numpy as np

def simulate(seed):
    rng = np.random.default_rng(seed)
    data = rng.normal(loc=100, scale=15, size=1000)
    mean = data.mean()
    std = data.std()
    inside = np.mean(np.abs(data - mean) <= std) * 100
    return {
        "mean": mean,
        "median": np.median(data),
        "std": std,
        "min": data.min(),
        "max": data.max(),
        "within_1_std_pct": inside,
    }


r1 = simulate(42)
r2 = simulate(2024)
print(f"{'Statistic':<20}{'Seed 42':>12}{'Seed 2024':>12}{'Difference':>12}")
for key in r1:
    print(f"{key:<20}{r1[key]:>12.3f}{r2[key]:>12.3f}{abs(r1[key] - r2[key]):>12.3f}")
print("Both runs use the same distribution, so the statistics are close but not identical.")
print("Both percentages should be near 68.27% as expected for a normal distribution.")

print()