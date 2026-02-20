indian = ["samosa", "daal", "naan"]
chinese = ["egg role","pot sticker","fried rice"]
italian = ["pizza","pasta","risotto"]

dish = input("Enter a dish : ")
if dish in indian:
    print(f"{dish} is an indian")
elif dish in chinese:
    print(f"{dish} is a chinese dish")
elif dish in italian:
    print(f"{dish} is an italian dish")
else:
    print(f"Based on my knowledge, I don't know what cuisine {dish} belongs to.")