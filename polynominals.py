import numpy

# Read the polynomial coefficients as a list of floats
coefficients = list(map(float, input().split()))

# Read the value of x
x = float(input())

# Evaluate the polynomial at point x and print the result
print(numpy.polyval(coefficients, x))
