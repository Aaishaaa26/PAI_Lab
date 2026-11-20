import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

employees = pd.DataFrame({
    "experience": [1, 2, 3, None, 5, 6, 7, 8, 9, 10, 3, 5],
    "education": ['BS', 'BS', 'MS', 'BS', 'MS', 'PhD', 'MS', 'PhD', 'BS', 'PhD', 'BS', 'MS'],
    "salary_k": [45, 50, 70, 58, 85, 120, 95, 140, 90, 160, 55, 88]
})

null_count = employees["experience"].isna().sum()
med = employees["experience"].median()
print(f"Found {null_count} missing value(s); filling with median = {med}")
employees["experience"] = employees["experience"].fillna(med)

encoded = pd.get_dummies(employees, columns=["education"], dtype=int)

inputs = encoded.drop(columns="salary_k")
output = encoded["salary_k"]

in_tr, in_te, out_tr, out_te = train_test_split(inputs, output, test_size=0.2, random_state=1)

mm = MinMaxScaler()
in_tr_s = mm.fit_transform(in_tr)
in_te_s = mm.transform(in_te)

lr_model = LinearRegression().fit(in_tr_s, out_tr)

preds = lr_model.predict(in_te_s)
print(f"Test samples: {len(out_te)}")
print(f"Actual: {out_te.tolist()}")
print(f"Predicted: {np.round(preds, 1).tolist()}")
print(f"Mean Absolute Error = {mean_absolute_error(out_te, preds):.2f}")
print(f"R-squared= {r2_score(out_te, preds):.4f}")

candidate = pd.DataFrame([{"experience": 4, "education_BS": 0, "education_MS": 1, "education_PhD": 0}])
candidate = candidate[inputs.columns]
result = lr_model.predict(mm.transform(candidate))[0]
print(f"Estimated salary for an MS graduate with 4 years of experience: {result:.1f}k")