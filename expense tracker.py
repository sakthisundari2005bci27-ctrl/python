import csv
from datetime import datetime

def add_expense(amount, category, description):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])
    print("Expense added successfully!")

def view_total():
    total = 0
    try:
        with open('expenses.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[1])
        print(f"Total Expenses: ${total:.2f}")
    except FileNotFoundError:
        print("No expenses recorded yet.")

if __name__ == "__main__":
    print("1. Add Expense\n2. View Total")
    choice = input("Choice: ")
    if choice == '1':
        amt = input("Amount: ")
        cat = input("Category: ")
        desc = input("Description: ")
        add_expense(amt, cat, desc)
    else:
        view_total()
