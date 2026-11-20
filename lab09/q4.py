
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = load_breast_cancer()
X = data.data
y = data.target

print("Dataset has", X.shape[0], "samples and", X.shape[1], "features")
print("Class 0 (malignant):", np.sum(y == 0))
print("Class 1 (benign):", np.sum(y == 1))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)[:, 1]

print(f"Accuracy on test set: {accuracy_score(y_test, predictions):.2%}")

print("cut-off   #class 1   accuracy")

for threshold in [0.3, 0.5, 0.7]:
    predicted_class = (probabilities >= threshold).astype(int)
    count = np.sum(predicted_class == 1)
    accuracy = accuracy_score(y_test, predicted_class)

    print(f"{threshold:<9} {count:<10} {accuracy:.2%}")

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

decision_values = model.decision_function(X_test)
my_sigmoid = sigmoid(decision_values)

probability_values = model.predict_proba(X_test)[:, 1]

print("First 5 from my_sigmoid: [" + " ".join(f"{v:.6f}" for v in my_sigmoid[:5]) + "]")
print("First 5 from predict_proba: [" + " ".join(f"{v:.6f}" for v in probability_values[:5]) + "]")

print("All values identical:", np.allclose(my_sigmoid, probability_values))
