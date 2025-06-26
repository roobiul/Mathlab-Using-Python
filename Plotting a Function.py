import numpy as np
import matplotlib.pyplot as plt

# Step 1: Get user input
start = float(input("Enter the start value of x: "))
end = float(input("Enter the end value of x: "))
step = float(input("Enter the step size: "))

# Step 2: Generate x values
x = np.arange(start, end + step, step)

# Step 3: Compute y values using the function f(x)
y = x**3 - 6*x**2 + 11*x - 6

# Step 4: Plot the function
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r'$f(x) = x^3 - 6x^2 + 11x - 6$', color='b', marker='o')

# Step 5: Add labels, title, and grid
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Plot of f(x) = x³ - 6x² + 11x - 6")
plt.legend()
plt.grid(True)

# Step 6: Show the plot
plt.show()
