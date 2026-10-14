# Place your answer to Exercise_01 in this file
# Do not rename or remove this file

print("This program calculates the average of a series of numbers entered.")
running = True
numbers = []

while running:
    i = float(input("Please enter a number. Enter 0 to stop\n"))
    if(i==0.0):
        running = False
        
    else:
        numbers.append(i)

if(numbers==[]):
    print('No numbers entered.')
    exit()
print(f"The average of the numbers entered is {sum(numbers)/len(numbers)}")