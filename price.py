import sys

n = int(sys.argv[1])
total = 0

for i in range(n):
    price = float(sys.argv[i + 2])
    total += price

print("Total Bill =", total)

if total > 1000:
    discount = total * 10 / 100
else:
    discount = 0

final = total - discount

print("Discount =", discount)
print("Final Bill =", final)