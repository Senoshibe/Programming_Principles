enter_num = input("Enter a number: ")

def positivenum_checker(num):

    positivenums = 0

    while True:

        if float(num) == 0: 
            break
        if float(num) % int(num) != 0 or float(num) < 0:
            num = input("Enter a number: ")
        elif float(num) > 0:
            positivenums += 1
            num = input("Enter a number: ")
    return positivenums

positive_numbers = positivenum_checker(enter_num)

print(f"{positive_numbers} positive numbers were entered.")