# Place your answer to Exercise_03 in this file
# Do not rename or remove this file
def cTof(temp):
    return (9/5) * temp + 32
def fToc(temp):
    return (5/9) * (temp - 32)

celsuisOrFahrenheit = input("Enter 1 to convert Celsius to Fahrenheit or 2 to convert Fahrenheit to Celsius:")

if celsuisOrFahrenheit == "1":
    tempToConvert = float(input("Please enter the temperature in Celsius:\n"))
    if tempToConvert<0:
        print("ERROR: You must enter a value of 0 or greater.")
        exit()
    print(f"{tempToConvert} Celsius is equivalent to {cTof(tempToConvert)} Fahrenheit.")
elif celsuisOrFahrenheit == "2":
    tempToConvert = float(input("Please enter the temperature in Fahrenheit:\n"))
    if tempToConvert<0:
        print("ERROR: You must enter a value of 0 or greater.")
        exit()
    print(f"{tempToConvert} Fahrenheit is equivalent to {fToc(tempToConvert)} Celsius.")
else:
    print("ERROR: Invalid option")