def find_total(expenses):
    total = 0
    for expense in expenses:
        total += expense
        return total
    
    
expenses_abhay = [1200, 1300, 1250, 1400, 1350]
expenses_sundar = [1100, 1200, 1150, 1300, 1250]
total_expenses_abhay = find_total(expenses_abhay)
total_expenses_sundar = find_total(expenses_sundar)
print(f"Total expenses for Abhay: {total_expenses_abhay}")
print(f"Total expenses for Sundar: {total_expenses_sundar}")