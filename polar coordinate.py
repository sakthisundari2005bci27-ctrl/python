import cmath

# Read the complex number input
z = complex(input().strip())

# Calculate r (modulus) and phi (phase)
r = abs(z)
phi = cmath.phase(z)

# Print the results
print(r)
print(phi)
