hours_per_day = input("Number of hours worked per day: ")
days_per_week = input("Number of days worked in a week: ")
salary = input("Annual salary: ")

def hourly_wage(hours, days, salary):
    return float(salary)/(float(hours) * float(days) * 52)

hourly_wage_dollars = hourly_wage(hours_per_day, days_per_week, salary)

print(f"Hourly wage = ${hourly_wage_dollars}")