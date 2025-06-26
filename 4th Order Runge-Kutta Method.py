import numpy as np
import matplotlib.pyplot as plt

# Define the ODE function dy/dx = -2xy
def ode(x, y):
    return -2 * x * y

# Implement the 4th Order Runge-Kutta Method
def runge_kutta(x0, y0, h, num_steps):
    x_values = [x0]
    y_values = [y0]

    for _ in range(num_steps):
        x = x_values[-1]
        y = y_values[-1]

        # Compute k1, k2, k3, k4
        k1 = h * ode(x, y)
        k2 = h * ode(x + h/2, y + k1/2)
        k3 = h * ode(x + h/2, y + k2/2)
        k4 = h * ode(x + h, y + k3)

        # Update y and x
        y_next = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x_next = x + h

        # Store values
        x_values.append(x_next)
        y_values.append(y_next)

    return x_values, y_values

# Accept user input
x0 = float(input("Enter the initial value of x (a): "))
y0 = float(input("Enter the initial condition y0: "))
b = float(input("Enter the end value of x (b): "))
h = float(input("Enter the step size h: "))
num_steps = int((b - x0) / h)  # Calculate number of steps based on interval and step size

# Solve the ODE using Runge-Kutta method
x_values, y_values = runge_kutta(x0, y0, h, num_steps)

# Plot the solution curve
plt.plot(x_values, y_values, label='Solution Curve', color='b')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of dy/dx = -2xy using 4th Order Runge-Kutta Method')
plt.legend()
plt.grid(True)
plt.show()

# Display final values
print(f"Final x value: {x_values[-1]}")
print(f"Final y value: {y_values[-1]}")