if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # 1. Retrieve the list of scores for the specific student
    marks = student_marks[query_name]
    
    # 2. Calculate the average
    # sum(marks) adds them up, len(marks) counts how many there are
    average = sum(marks) / len(marks)
    
    # 3. Print the result formatted to 2 decimal places
    print("{:.2f}".format(average))
