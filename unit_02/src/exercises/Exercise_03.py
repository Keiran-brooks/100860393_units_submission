# Place your answer to Exercise_03 in this file
# Do not rename or remove this file


#  * Child tickets cost £5
#  * Adult tickets cost £10
#  * Senior tickets cost £8


# How many child tickets would you like?
# 3
# How many adult tickets would you like?
# 4
# How many senior tickets would you like?
# 2
# Total Price: £71\
childTickets = int(input("How many child tickets would you like?\n"))
adultTickets = int(input("How many adult tickets would you like?\n"))
seniorTickets = int(input("How many senior tickets would you like?\n"))

childCost = childTickets*5
adultCost = adultTickets*10
seniorCost = seniorTickets*8
totalCost = childCost+adultCost+seniorCost

print(f"Total Price: £{totalCost}")
