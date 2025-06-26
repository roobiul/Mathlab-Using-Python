import numpy as np
import matplotlib.pyplot as plt

# Given data points
x_data = np.array([1, 2, 3, 4])
y_data = np.array([2, 8, 18, 32])

# Function to perform Lagrange Interpolation
def lagrange_interpolation(x, x_data, y_data):
    n = len(x_data)
    y = 0.0
    coefficients = []

    for i in range(n):
        # Calculate the Lagrange basis polynomial (L_i)
        L_i = 1.0
        for j in range(n):
            if j != i:
                L_i *= (x - x_data[j]) / (x_data[i] - x_data[j])
        coefficients.append(L_i)
        y += y_data[i] * L_i

    return y, coefficients

# Estimate y at x = 2.5
x_target = 2.5
y_estimated, lagrange_weights = lagrange_interpolation(x_target, x_data, y_data)

# Display the result
print(f"Estimated y at x = {x_target}: {y_estimated}")
print("Lagrange weights (coefficients):", lagrange_weights)

# Plot the given data points and the interpolation polynomial
x_vals = np.linspace(min(x_data), max(x_data), 100)  # Range for plotting
y_vals = np.array([lagrange_interpolation(x, x_data, y_data)[0] for x in x_vals])

plt.scatter(x_data, y_data, color='red', label='Data Points')
plt.plot(x_vals, y_vals, label='Interpolation Polynomial', color='blue')
plt.scatter([x_target], [y_estimated], color='green', label=f'Estimated Point (x={x_target}, y={y_estimated:.2f})')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Interpolation')
plt.legend()
plt.grid(True)
plt.show()