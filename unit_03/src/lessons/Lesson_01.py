# Place your answer to Lesson_01 in this file
# Do not rename or remove this file

# Your program should work as follows:
# ```
# Please enter a whole number:
# 7
# Your number is odd!
# ```

# ```
# Please enter a whole number:
# 4
# Your number is even!

i = input("Please enter a whole number:\n")
if int(i) % 2 == 0:
    print("Your number is even!")
else:
    print("Your number is odd!")