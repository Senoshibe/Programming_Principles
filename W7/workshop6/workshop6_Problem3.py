import math

room_width = float(input("Enter room dimension 1 (m): "))
room_length = float(input("Enter room dimension 2 (m): "))

print("Width of room = {:.3f}m".format(room_width) )
print("Length of room = {:.3f}m".format(room_length))

multiplier_lengthways = (room_width - (room_width % 3.66))/3.66
total_carpet_lengthways = math.ceil(multiplier_lengthways * room_length)

multiplier_widthways = (room_length - (room_length % 3.66))/3.66
total_carpet_widthways = math.ceil(multiplier_widthways * room_width)

print ("Total carpet length required in lengthways manner = ", int(total_carpet_lengthways), "m")
print ("Total carpet length required in widthways manner = ", int(total_carpet_widthways), "m")
