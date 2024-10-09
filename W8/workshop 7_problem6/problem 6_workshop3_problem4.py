hours_week = input("How many hours were worked? ")
cars_sold = input("Total number of cars sold for the week? ")

def salary_week(hours,sold):
    if int(hours) > 37:
        wage = (36.25 * 37) + ((int(hours) - 37) * 36.25 * 1.5)
    else: 
        wage = 36.25 * int(hours)

    if int(sold) > 5:
        bonus = (int(sold)-5) * 200
    else:
        bonus = 0
    
    return (wage + bonus)

salary_week(hours_week, cars_sold)

print(f"The salary is {salary_week(hours_week, cars_sold)}")