
n = int(input("Enter a positive number: "))
    
if n < 0:
    print("Error")

original  = n 
reversedNum = 0 

while n > 0: 
    digit = n%10 #Gets last digit 
    reversedNum = reversedNum * 10 + digit 
    n //= 10 # Removes last digit

if original == reversedNum:
    print(original, " is a palindrome.")
    
else:
    print(original, "is not a palindrome.")