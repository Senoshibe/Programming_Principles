import math
import sys

roomWidth = float(input("Enter room dimension 1 (m): "))
if roomWidth == 0:
    sys.exit()
roomLength = float(input("Enter room dimension 2 (m): "))
if roomLength == 0:
    sys.exit()

print("Length of room = {:.3f} m".format(roomLength))
print("Width of room = {:.3f} m".format(roomWidth))

def f(): 
    multiplier = math.ceil(roomWidth/3.66)
    totalCarpetLengthways = math.ceil(multiplier * roomLength)

    multiplier = math.ceil(roomLength/3.66)
    totalCarpetWidthways = math.ceil(multiplier * roomWidth)

    print("Total carpet length required in lengthways manner = ", totalCarpetLengthways, " m")
    print("Total carpet length required in widthways manner = ", totalCarpetWidthways, " m")

f()