n = int(input("Enter number of items: "))
total = 0

for i in range(n):
    price = float(input("Enter item price: "))
    total = total + price

print("Total Bill =", total)
if total > 1000:
    discount = total * 10 / 100
else:
    discount = 0

final = total - discount

print("Discount =", discount)
print("Final Bill =", final)