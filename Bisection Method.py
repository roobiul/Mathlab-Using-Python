# Define the function f(x)
def f(x):
    return x**3 - 6*x**2 + 11*x - 6

# Bisection Method Implementation
def bisection_method(a, b, tolerance, max_iterations):
    if f(a) * f(b) >= 0:
        print("The interval does not bracket a root. Please try again with a different interval.")
        return None

    iteration = 0
    while (b - a) / 2 > tolerance and iteration < max_iterations:
        c = (a + b) / 2
        if f(c) == 0:
            break  # Exact root found
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iteration += 1

    root = (a + b) / 2
    return root, iteration

# Accept user input
a = float(input("Enter the start of the interval (a): "))
b = float(input("Enter the end of the interval (b): "))
tolerance = float(input("Enter the tolerance (error): "))
max_iterations = int(input("Enter the maximum number of iterations: "))

# Find the root using the Bisection Method
result = bisection_method(a, b, tolerance, max_iterations)

# Display the result
if result:
    root, iterations = result
    print(f"Approximate root: {root}")
    print(f"Number of iterations: {iterations}")
else:
    print("No root found in the given interval.")