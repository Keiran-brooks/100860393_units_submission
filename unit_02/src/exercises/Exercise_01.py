# Place your answer to Exercise_01 in this file
# Do not rename or remove this file
# Please enter the temperature in Celsius:
# 20.2
# 20.2 Celsius is equivalent to 68.36 Fahrenheit.
# Fahrenheit = (9/5) * Celsius + 32
def convertToFahrenheit(celsius):
    return (9/5) * celsius + 32
numInCelsius = float(input('Please enter the temperature in Celsius:\n'))
print(f"{numInCelsius} Celsius is equivalent to {convertToFahrenheit(numInCelsius)} Fahrenheit")