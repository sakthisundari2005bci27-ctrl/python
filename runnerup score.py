if __name__ == '__main__':
    n = int(input())
    # Map the input strings to integers and put them in a list
    arr = map(int, input().split())
    
    # 1. Convert to a set to remove duplicates (e.g., [6, 6, 5] becomes {6, 5})
    # 2. Convert back to a list so we can sort it
    unique_scores = list(set(arr))
    
    # 3. Sort the list in ascending order
    unique_scores.sort()
    
    # 4. The runner-up is the second-to-last element
    print(unique_scores[-2])
