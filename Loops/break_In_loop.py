monthly_sales = [10000, 3000, 2000,1000, 3000, 2500]
threshold = 2000
for sales_amount in monthly_sales:
    if sales_amount < threshold:
        print(f"Sales amount {sales_amount} is below the threshold.")
        break
    else:
        print(f"Sales amount {sales_amount} is greater than or equal to the threshold.")