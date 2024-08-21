#Problem: A car dealer earns a base wage of $36.25 per hour up to their normal work week of 37 hours.
#Only whole hours are counted. If he works more hours than that (overtime) he gets paid at 1.5 times his
#normal rate for the overtime. If he sells more than 5 cars in a week, he gets a bonus of $200 per car from
#the 6th car sold. Write a program that takes as input the number of hours worked and the total number
#of cars sold for the week, and outputs the car dealer’s total salary for the week.

hoursWorked = int(input("How many hours were worked? "))
carsSoldPerWeek = int(input("Total number of cars sold for the week? "))
if hoursWorked > 37.0:
    baseSalary = (36.25*37.0) + (float(hoursWorked - 37)*36.25*1.5)

if hoursWorked < 37.0:
    baseSalary = 36.25*hoursWorked

if carsSoldPerWeek > 5:
    bonus = (float(carsSoldPerWeek) - 5.0)*200

if carsSoldPerWeek < 5: 
    bonus = 0.0

totalSalary = baseSalary + bonus

print("The salary is ", totalSalary)