#Example palindrome: 121

num = int(input("Enter a positive number: "))
reversedNumber = 0
original = num

while num > 0:
    
    digit = num % 10
    reversedNumber = reversedNumber * 10 + digit
    num //= 10

if original == reversedNumber:
    print(original, " is a palindrome")

else:
    print(original, " is not a palindrome")