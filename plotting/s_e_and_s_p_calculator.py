import numpy as np

# Constants a, b, c
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# Coefficient matrix A
A = np.array([[1, 1/a], [a, 1], [1, -a]])

# Result vector B
B = np.array([b, c, 0])

# Solve using least squares (because the system has 3 equations and 2 unknowns)
solution, residuals, rank, s = np.linalg.lstsq(A, B, rcond=None)

x, y = solution
print(f"The solution is: x = {x}, y = {y}")