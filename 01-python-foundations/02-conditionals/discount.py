price = float(input("Enter the price: "))

if price >= 1000:
    discount = price * 0.10
else:
    discount = 0

final_price = price - discount

print("Discount:", discount)
print("Final price:", final_price)