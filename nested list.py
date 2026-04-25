if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # 1. Get all unique scores and sort them to find the second lowest
    unique_scores = sorted(list(set([s[1] for s in students])))
    second_lowest_score = unique_scores[1]
    
    # 2. Collect names of students who have that second lowest score
    low_scorers = [s[0] for s in students if s[1] == second_lowest_score]
    
    # 3. Sort the names alphabetically and print them
    low_scorers.sort()
    for name in low_scorers:
        print(name)
