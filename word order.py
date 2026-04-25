from collections import OrderedDict

# Read the number of words
n = int(input())

# Initialize an ordered dictionary to store counts
word_counts = OrderedDict()

for _ in range(n):
    word = input().strip()
    # Increment count if word exists, otherwise initialize at 1
    word_counts[word] = word_counts.get(word, 0) + 1

# Output the number of distinct words
print(len(word_counts))

# Output the counts in order of appearance
print(*(word_counts.values()))
