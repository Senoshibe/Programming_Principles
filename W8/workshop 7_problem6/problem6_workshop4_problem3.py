import sys

enter_num = input("Enter a positive number: ")

def check_palindrome(num):

    reversed_num = 0
    original_num = int(num)

    if num.isnumeric():
        while original_num > 0:
            digit = original_num%10
            reversed_num = reversed_num*10 + digit
            original_num = original_num//10
    else:
        sys.exit()
    
    return reversed_num
        

reversed_number = check_palindrome(enter_num)

if int(enter_num) == reversed_number:
    print(f"{enter_num} is a palindrome")

else:
    print(f"{enter_num} is not a palindrome")