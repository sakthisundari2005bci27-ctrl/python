from datetime import datetime

# Read the number of test cases
t = int(input())

for _ in range(t):
    # The format string: 
    # %a (Day), %d (dd), %b (Mon), %Y (yyyy), %H:%M:%S (hh:mm:ss), %z (+xxxx)
    fmt = '%a %d %b %Y %H:%M:%S %z'
    
    t1 = datetime.strptime(input(), fmt)
    t2 = datetime.strptime(input(), fmt)
    
    # Calculate absolute difference and convert to total seconds
    diff = abs(int((t1 - t2).total_seconds()))
    print(diff)
