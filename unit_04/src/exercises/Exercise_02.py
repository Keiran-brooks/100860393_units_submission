
# Place your answer to Exercise_02 in this file
# Do not rename or remove this file

speed = input("What is the speed of the vehicle in mph?\n")
if(int(speed)<= 0):
    print("ERROR: Speed must be a positive number.")  
    exit()


time = input("How many hours has it travelled?\n")
if(int(time)<= 0):
    print("ERROR: Hours travelled must be a positive number.")
    exit()

print("Hour | Distance Travelled")
print("-----------------------")
for i in range(1, int(time)+1):
    
    print(f'{i}    | {i*int(speed)}')