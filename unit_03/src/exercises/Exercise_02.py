# Place your answer to Exercise_02 in this file
# Do not rename or remove this file
# Place your answer to Exercise_01 in this file
# Do not rename or remove this file
def celsius_to_fahrenheit(Celsius):
    return (9/5) * Celsius + 32


i = float(input("Please enter the temperature in Celsius:\n"))
if(i<0):
    print("ERROR: You must enter a value of 0 or greater.")
else:
    print(f"{i} Celsius is equivalent to {celsius_to_fahrenheit(i)} Fahrenheit.")