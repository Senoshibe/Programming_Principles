#Problem1: A tradie needs to estimate how much concrete is needed for a rectangular-sized car park.
#Write a program that asks the user for the length of the park in metres, the width of the park in metres, and the volume of concrete required in litres per square metre.
#Calculate and print the total litres of concrete required for the car park. 
#For example, the output should look like this when the program is run:
#Length of park (m): 45.5
#Width of park (m): 35
#Litres per square metre: 5.1
#Litres required = 8.121.749999999999

length = float(input("Length of park (m): "))
width = float(input("Width of park (m): "))
litres_per_square_metre = float(input("Litres per square metre: "))
litres_required = float(length*width*litres_per_square_metre)
print("Litres required = ", litres_required)