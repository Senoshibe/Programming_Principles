#Problem: The grades at a university are awarded based on the marks awarded for the course out of 100.
#Marks of 85 or above receive the grade of 7. Marks less than 85 but that are 75 or above receive the
#grade of 6. Marks less than 75 but that are 65 or above receive the grade of 5. Marks less than 65 but
#that are 50 or above receive the grade of 4. Anything less than 50 gets the grade of F. Write a program
#that asks the user to input the marks and prints the grade awarded.

num = float(input("How many marks? "))

if 85 <= num <= 100:
    print("Grade awarded: ", 7)

if 75 <= num < 85:
    print("Grade awarded: ", 6)

if 65 <= num < 75: 
    print("Grade awarded: ", 5)

if 50 <= num < 65: 
    print("Grade awarded: ", 4)

if 0 <= num < 50:
    print ("Grade awarded: F")
