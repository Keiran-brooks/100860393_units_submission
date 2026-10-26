# Place your answer to Exercise_04 in this file
# Do not rename or remove this file
amount = int(input("Please enter the number of copies of the software you wish to purchase:\n"))
discount = 0
# 5 – 9	10%
# 10 – 19	20%
# 20 – 49	30%
# 50 – 99	40%
# 100 or more	50%

if amount >= 100:
    discount = 50
elif amount >= 50:
    discount = 40
elif amount >= 20:
    discount = 30
elif amount >= 10:
    discount = 20
elif amount >= 5:
    discount = 10
else:
    discount = 0

print(f"You have been given a {discount}% discount on the normal price of £99.")
costWithDiscount = 99*(100-discount)/100
amountAfterDiscount = amount*costWithDiscount


print(f"The total cost is £{amountAfterDiscount:.2f}.")