import re

# Read N (rows) and M (columns)
n, m = map(int, input().split())

# Read the matrix rows
matrix = [input() for _ in range(n)]

# Transpose the matrix to read column by column
# zip(*matrix) takes each row and groups characters by their column index
decoded_string = "".join(["".join(column) for column in zip(*matrix)])

# Use Regex to replace symbols/spaces between alphanumeric characters
# \w represents [A-Za-z0-9]
# [^\w]+ represents one or more non-alphanumeric characters
# (?<=\w) is a lookbehind: checks if preceded by an alphanumeric
# (?=\w) is a lookahead: checks if followed by an alphanumeric
pattern = r'(?<=\w)[^\w]+(?=\w)'
final_output = re.sub(pattern, ' ', decoded_string)

print(final_output)
