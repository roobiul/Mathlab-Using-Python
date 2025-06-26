import math

# Define the integrand function f(x) = e^(-x^2)
def f(x):
    return math.exp(-x**2)

# Implement Simpson's 1/3 Rule
def simpsons_rule(a, b, n):
    # Ensure n is even
    if n % 2 != 0:
        raise ValueError("Number of subintervals (n) must be even.")

    # Calculate step size
    h = (b - a) / n

    # Initialize result with f(a) + f(b)
    result = f(a) + f(b)

    # Iterate over subintervals
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            result += 2 * f(x)  # Even-indexed points
        else:
            result += 4 * f(x)  # Odd-indexed points

    # Multiply by h/3 to get the final approximation
    result *= h / 3
    return result

# Accept user input
a = float(input("Enter the lower limit of integration (a): "))
b = float(input("Enter the upper limit of integration (b): "))
n = int(input("Enter the number of subintervals (must be even): "))

# Approximate the integral using Simpson's 1/3 Rule
approximation = simpsons_rule(a, b, n)

# Display the result
print(f"Approximation of the integral using Simpson's 1/3 Rule: {approximation}")