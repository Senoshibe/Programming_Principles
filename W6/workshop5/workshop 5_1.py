
# Think of while loop that creates a Fibonacci number sequence. 

num = int(input("Enter a positive number: "))
a = 0
b = 1
count = 0

while count < num:
    print(a, end = " ")

    a, b = b, a + b

    count += 1

    if count % 4 == 0:
        print() 
 
