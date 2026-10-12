# Place your answer to Lesson_03 in this file
# Do not rename or remove this file
# Write a program that outputs whether a number is positive, negative, or zero. Your program should accept numbers of type ``float``.

# * If the number is positive it should output ``Your number is positive!``
# * If the number is negative it should output ``Your number is negative!``
# * If the number is zero it should output ``Your number is zero!``
# &nbsp;

# For example, your program should output the following given these inputs:
# ```
# Please enter a number:
# 2.3
# Your number is positive!
# ```

number = float(input("Please enter a number:\n"))
if(number>0):
    print("Your number is positive!")
elif(number<0):
    print("Your number is negative!")
else:
    print("Your number is zero!")