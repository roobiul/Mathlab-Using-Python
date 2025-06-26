import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve

# Define the parameters of the BVP
def solve_bvp(N):
    # Step size
    h = 1 / (N + 1)

    # Discretize the domain
    x = np.linspace(0, 1, N + 2)

    # Initialize the coefficient matrix (A) and right-hand side vector (b)
    A = np.zeros((N, N))
    b = np.zeros(N)

    # Fill the coefficient matrix and right-hand side vector
    for i in range(N):
        if i == 0:
            # First internal node (i=1)
            A[i, i] = -2 / h**2 - 2 / (2 * h) + 1
            A[i, i + 1] = 1 / h**2 + 2 / (2 * h)
            b[i] = x[i + 1] - (1 / h**2 - 2 / (2 * h)) * 1  # y(0) = 1
        elif i == N - 1:
            # Last internal node (i=N)
            A[i, i - 1] = 1 / h**2 - 2 / (2 * h)
            A[i, i] = -2 / h**2 - 2 / (2 * h) + 1
            b[i] = x[i + 1] - (1 / h**2 + 2 / (2 * h)) * 2  # y(1) = 2
        else:
            # Internal nodes (i=2 to N-1)
            A[i, i - 1] = 1 / h**2 - 2 / (2 * h)
            A[i, i] = -2 / h**2 - 2 / (2 * h) + 1
            A[i, i + 1] = 1 / h**2 + 2 / (2 * h)
            b[i] = x[i + 1]

    # Solve the system of equations
    y_internal = spsolve(A, b)

    # Combine boundary conditions with internal solutions
    y = np.concatenate(([1], y_internal, [2]))

    return x, y

# Accept user input for the number of internal nodes
N = int(input("Enter the number of internal nodes (N): "))

# Solve the BVP
x, y = solve_bvp(N)

# Plot the numerical solution
plt.plot(x, y, marker='o', linestyle='-', label=f'N = {N}')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Numerical Solution of the BVP using Finite Difference Method')
plt.legend()
plt.grid(True)
plt.show()

# Display the solution
print("Numerical Solution:")
for xi, yi in zip(x, y):
    print(f"x = {xi:.4f}, y = {yi:.4f}")