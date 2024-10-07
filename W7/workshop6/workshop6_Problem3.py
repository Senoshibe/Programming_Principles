import calendar

start_year = int(input("Year 1? "))
end_year = int(input("Year 2? "))
               
leap_days = int(calendar.leapdays(start_year, end_year + 1))
              
days = (end_year - start_year + 1) * 365 + leap_days

print("Number of days: ", days)