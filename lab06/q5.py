import numpy as np

A = np.array([[2, 1, 3], [0, 4, 1], [5, 2, 6]])
B = np.array([[1, 2, 0], [3, 1, 4], [2, 5, 1]])
C = np.array([[1, 2], [3, 4], [5, 6]])
print("A shape:", A.shape, "| B shape:", B.shape, "| C shape:", C.shape)
print("\nAddition, shapes", A.shape, B.shape, "\n", A + B)
print("\nSubtraction, shapes", A.shape, B.shape, "\n", A - B)
print("\nElement-wise multiplication, shapes", A.shape, B.shape, "\n", A * B)
print("\nMatrix multiplication A @ B, shapes", A.shape, B.shape, "\n", A @ B)
print("\nMatrix multiplication A @ C, shapes", A.shape, C.shape, "->", (A @ C).shape, "\n", A @ C)
print("\nTranspose of C, shape before", C.shape, "after", C.T.shape, "\n", C.T)
print("\nDeterminant of A, shape", A.shape, ":", round(np.linalg.det(A), 4))
if not np.isclose(np.linalg.det(A), 0):
    print("\nInverse of A, shape", A.shape, "\n", np.round(np.linalg.inv(A), 4))
    print("A @ inv(A) is identity:", np.allclose(A @ np.linalg.inv(A), np.eye(3)))
print("\nDeterminant of C is not defined, shape", C.shape, "is not square")
try:
    A + C
except ValueError as e:
    print("A + C fails:", e)
try:
    C @ A
except ValueError as e:
    print("C @ A fails:", e)
print("\nCompatibility rules:")
print("Addition, subtraction, element-wise multiplication need equal or broadcastable shapes.")
print("Matrix multiplication needs inner dimensions to match: (m, n) @ (n, p) -> (m, p).")
print("Determinant and inverse need a square matrix, and inverse also needs det != 0.")
print("Transpose works on any shape.")

print()