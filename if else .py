import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    # Check if n is odd
    if n % 2 != 0:
        print("Weird")
    else:
        # n is even, check the specific ranges
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        else: # n is even and greater than 20
            print("Not Weird")
