#Problem2: A programmer would like to calculate the hourly wage of a job.
#Write a program that asks the user for the number of hours worked per day, number of days worked in a week, and the annual salary.
#Calculate and print the programmer's hourly wage with assumption that there are 52 weeks in a year.
#For example, the output should look like this when the program is run:
#Number of hours worked ber day: 7.5
#Number of days worked in a week: 5
#Annual salary: 60000
#Hourly wage = $30.76923076923077

hours_per_day = float(input("Number of hours worked per day: "))
days_per_week = float(input("Number of days worked in a week: "))
annual_salary = float(input("Annual salary: "))
hourly_wage = float(annual_salary / 52.0 / days_per_week / hours_per_day)
print("Hourly wage = $", hourly_wage)