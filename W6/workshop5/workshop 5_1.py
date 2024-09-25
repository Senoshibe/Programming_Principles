# Think of while loop that creates a Fibonacci number sequence. 


m = input("Enter a positive number:" )

for range(0, m) in n: 
    
    x = 0 #1st number in the sequence
    y = 1
    print(x, y, sep=" ")

    x += y
    y = y + x 

