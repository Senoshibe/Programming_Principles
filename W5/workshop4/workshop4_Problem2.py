n = int(input("Enter a mark: "))
m = 1 ## number of grades
totalMarks = 0 
totalGrades = 0

while m != 5:

    if 85 <= n <= 100:
        g = 7
        print("Grade is: ", g)

    if 75 <= n < 85:
        g = 6
        print("Grade is: ", g)

    if 65 <= n < 75: 
        g = 5
        print("Grade is: ", g)
    
    if 50 <= n < 75: 
        g = 4
        print("Grade is: ", g)

    totalMarks += n 
    totalGrades += g

    m += 1
    if m != 5:
        n = int(input("Enter a mark: "))

    else:
        break

print("Average mark=", totalMarks/4)
print("Average grade=", totalGrades/4)