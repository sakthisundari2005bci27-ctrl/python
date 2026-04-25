import numpy

# Read N and M
n, m = map(int, input().split())

# Construct the 2D array
my_array = numpy.array([input().split() for _ in range(n)], int)

# Calculate the sum along axis 0 (columns)
sum_axis_0 = numpy.sum(my_array, axis=0)

# Calculate the product of the resulting sums
print(numpy.prod(sum_axis_0))
