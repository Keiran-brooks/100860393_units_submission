# Place your answer to Exercise_01 in this file
# Do not rename or remove this file
def celsius_to_fahrenheit(Celsius):
    return (9/5) * Celsius + 32


i = float(input("Please enter the temperature in Celsius:\n"))
if not i<0:
    print(f"{i} Celsius is equivalent to {celsius_to_fahrenheit(i)} Fahrenheit.")