
# Place your answer to Exercise_02 in this file
# Do not rename or remove this file

speed = input("What is the speed of the vehicle in mph?\n")

print("Hour | Distance Travelled")
print("-----------------------")
for i in range(1, 4):
    print(f'{i}    | {i*int(speed)}')