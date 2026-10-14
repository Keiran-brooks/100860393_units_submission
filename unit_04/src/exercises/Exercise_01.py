# Place your answer to Exercise_01 in this file
# Do not rename or remove this file

print("This program calculates the average of a series of numbers entered.")
running = True
numbers = []

while running:
    i = input("Please enter a number. Enter 0 to stop\n")
    if(i=='0'):
        running = False
    else:
        numbers.append(float(i))

print(f"The average of the numbers entered is {sum(numbers)/len(numbers)}")