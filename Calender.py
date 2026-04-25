import calendar

# Read month, day, and year from input
month, day, year = map(int, input().split())

# Get the day of the week (0 is Monday, 6 is Sunday)
day_index = calendar.weekday(year, month, day)

# Look up the day name and convert to uppercase
print(calendar.day_name[day_index].upper())
