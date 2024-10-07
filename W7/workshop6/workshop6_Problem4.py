import math

roomWidth = float(input("Enter room dimension 1 (m): "))
roomLength = float(input("Enter room dimension 2 (m): "))

print("Length of room = {:.3f} m".format(roomLength))
print("Width of room = {:.3f} m".format(roomWidth))

carpetMultiplierLengthways = math.ceil(roomWidth/3.66)
totalCarpetLengthways = round(carpetMultiplierLengthways * roomLength)

carpetMultiplierWidthways = math.ceil(roomLength/3.66)
totalCarpetWidthways = round(carpetMultiplierWidthways * roomWidth)

print("Total carpet length required in lengthways manner = ", totalCarpetLengthways, " m")
print("Total carpet length required in widthways manner = ", totalCarpetWidthways, " m")