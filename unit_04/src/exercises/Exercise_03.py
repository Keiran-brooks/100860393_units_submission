# Place your answer to Exercise_03 in this file
# Do not rename or remove this file
running = True
numbers = []
print("This program calculates the largest number from a series of numbers entered.")


while running:
    i = int(input("Please enter a number. Enter 0 to stop\n"))
    if(i!=0):
        numbers.append(i)
    else:
        running = False

if(numbers != []):
    print(f"The largest of the numbers entered is {max(numbers)}")
else:
    print("No numbers entered.")