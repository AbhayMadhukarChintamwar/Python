monthly_sales = [10000, 3000, 2000,1000, 3000, 2500]
months = ["January", "February", "March", "April", "May", "June"]
threshold = 2000
for sales_amount, month in zip(monthly_sales,months):
    
    if sales_amount < threshold:
        print(f"Sales amount {sales_amount} is below the threshold in {month}.")
        break
    else:
        print(f"Sales amount {sales_amount} is greater than or equal to the threshold in {month}.")