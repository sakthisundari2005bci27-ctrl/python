# Read input N and M
n, m = map(int, input().split())

# 1. Top Pattern
# The pattern '.|.' repeats 1, 3, 5... times
for i in range(1, n, 2):
    pattern = ".|." * i
    print(pattern.center(m, '-'))

# 2. Middle WELCOME Line
print("WELCOME".center(m, '-'))

# 3. Bottom Pattern
# The pattern repeats in reverse: (n-2), (n-4)... 1
for i in range(n-2, -1, -2):
    pattern = ".|." * i
    print(pattern.center(m, '-'))
