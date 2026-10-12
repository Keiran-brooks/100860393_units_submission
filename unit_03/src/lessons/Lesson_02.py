# Place your answer to Lesson_02 in this file
# Do not rename or remove this file
# ```
# Please enter a number:
# 15
# Your number is divisible by 3 and 5.
# ```
# 
# ```
# Please enter a number:
# 12
# Your number is divisible by 3 and NOT by 5.
# ```
# 
# ```
# Please enter a number:
# 20
# Your number is NOT divisible by 3 and is divisible by 5.
# 
number = input("Please enter a number:\n")
number = int(number)

if number % 3 == 0 and number % 5 == 0:
    print("Your number is divisible by 3 and 5.")
elif number % 3 == 0 and number % 5 != 0:
    print("Your number is divisible by 3 and NOT by 5.")
elif number % 3 != 0 and number % 5 == 0:
    print("Your number is NOT divisible by 3 and is divisible by 5.")
else:
    print("Your number is NOT divisible by 3 and 5.")