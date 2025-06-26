import numpy as np
import matplotlib.pyplot as plt
import math  # Import the math module for factorial

# Given data points
x_values = np.array([1, 2, 3, 4])
y_values = np.array([2, 8, 18, 32])

# Function to compute forward differences
def forward_differences(y_values):
    n = len(y_values)
    forward_diff = np.zeros((n, n))
    forward_diff[:, 0] = y_values

    for j in range(1, n):
        for i in range(n - j):
            forward_diff[i, j] = forward_diff[i + 1, j - 1] - forward_diff[i, j - 1]

    return forward_diff

# Function to perform Newton's Forward Interpolation
def newton_forward_interpolation(x_values, y_values, x):
    n = len(x_values)
    h = x_values[1] - x_values[0]  # Step size
    u = (x - x_values[0]) / h  # Scaling factor

    # Compute forward differences
    forward_diff = forward_differences(y_values)

    # Initialize the result with y0
    result = forward_diff[0, 0]

    # Compute the interpolation polynomial
    for i in range(1, n):
        term = forward_diff[0, i] / math.factorial(i)  # Use math.factorial
        for j in range(i):
            term *= (u - j)
        result += term

    return result

# Estimate y at x = 2.5
x_estimate = 2.5
y_estimate = newton_forward_interpolation(x_values, y_values, x_estimate)

# Display the estimated value
print(f"Estimated value of y at x = {x_estimate}: {y_estimate}")

# Display the coefficients of the interpolation polynomial
forward_diff = forward_differences(y_values)
print("Coefficients of the interpolation polynomial:")
for i in range(len(forward_diff)):
    print(f"Delta^{i} y0: {forward_diff[0, i]}")

# Plot the given data points and the interpolation polynomial
x_plot = np.linspace(min(x_values), max(x_values), 100)
y_plot = [newton_forward_interpolation(x_values, y_values, x) for x in x_plot]

plt.plot(x_values, y_values, 'ro', label='Data Points')
plt.plot(x_plot, y_plot, 'b-', label='Interpolation Polynomial')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Newton's Forward Interpolation")
plt.legend()
plt.grid(True)
plt.show()