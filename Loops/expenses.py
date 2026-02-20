expenses = [1200, 1300, 1250, 1400, 1350]
total_expense = 0

# for i in range(len(expenses)):
for i, expense in enumerate(expenses):
    expense = expenses[i]
    print(f"Month {i+1}, Expense:{expense}")
    total_expense += expense
print(f"Total Expense: {total_expense}")

   