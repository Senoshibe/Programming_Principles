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
litresPerSquareMetre = float(input("Litres per square metre: "))
litresRequired = float(length*width*litresPerSquareMetre)
print("Litres required = ", litresRequired)


#Problem2: A programmer would like to calculate the hourly wage of a job.
#Write a program that asks the user for the number of hours worked per day, number of days worked in a week, and the annual salary.
#Calculate and print the programmer's hourly wage with assumption that there are 52 weeks in a year.
#For example, the output should look like this when the program is run:
#Number of hours worked ber day: 7.5
#Number of days worked in a week: 5
#Annual salary: 60000
#Hourly wage = $30.76923076923077

hoursPerDay = float(input("Number of hours worked per day: "))
daysPerWeek = float(input("Number of days worked in a week: "))
annualSalary = float(input("Annual salary: "))
hourlyWage = ((annualSalary/52)/daysPerWeek)/hoursPerDay
print("Hourly wage = $", hourlyWage)