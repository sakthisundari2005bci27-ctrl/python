import numpy

# Read the dimension of the square matrix
n = int(input())

# Read the matrix elements and convert to a NumPy array
# We use float to handle decimal inputs
matrix = numpy.array([input().split() for _ in range(n)], float)

# Calculate the determinant
determinant = numpy.linalg.det(matrix)

# Print the result rounded to 2 decimal places
# Using round() or formatting ensures the output matches the required precision
print(round(determinant, 2))
