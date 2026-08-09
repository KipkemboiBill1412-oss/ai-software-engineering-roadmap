price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

discount = price * (discount_percentage / 100)
discounted_price = price - discount

print("Original price:", price)
print("Discount:", discount)
print("Discounted price:", discounted_price)