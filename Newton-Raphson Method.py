import numpy as np

# Define the function f(x) and its derivative f'(x)
def f(x):
    return x**3 - 6*x**2 + 11*x - 6

def f_prime(x):
    return 3*x**2 - 12*x + 11

# Newton-Raphson Method
def newton_raphson(initial_guess, tolerance, max_iterations):
    x = initial_guess
    iteration = 0

    while iteration < max_iterations:
        fx = f(x)
        fpx = f_prime(x)

        if abs(fx) < tolerance:
            print(f"Root found at x = {x:.6f} after {iteration} iterations.")
            return x

        if fpx == 0:
            print("Derivative is zero. No solution found.")
            return None

        x = x - fx / fpx
        iteration += 1

    print(f"Maximum iterations reached. Approximate root at x = {x:.6f}.")
    return x

# Accept user input
initial_guess = float(input("Enter the initial guess: "))
tolerance = float(input("Enter the tolerance (error): "))
max_iterations = int(input("Enter the maximum number of iterations: "))

# Find the root using Newton-Raphson method
root = newton_raphson(initial_guess, tolerance, max_iterations)

# Display the result
if root is not None:
    print(f"The approximate root is: {root:.6f}")