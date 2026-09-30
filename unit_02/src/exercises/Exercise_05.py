# Place your answer to Exercise_05 in this file
# Do not rename or remove this file
# Please enter the length of the wall:
# 10
# Please enter the height of the wall:
# 3
# You require 2 cans of paint.
# The length and height are specified in metres and the painter knows that 1 can of paint covers 20 square metres. 

import math

def calcPaintNeeded(length, height):
    surfaceArea = length*height
    paintNeeded = surfaceArea/20
    paintNeeded = math.ceil(paintNeeded)

    return paintNeeded


length = float(input("Please enter the length of the wall:\n"))
height = float(input("Please enter the height of the wall:\n"))
print(f"You require {calcPaintNeeded(length,height)} cans of paint.")
