print("You win if you gues the magic number.")
num = int(input("Enter a number: "))
if (num == 7):
    print("Congratulations! Lucky number 7!")
elif (num < 7):
    print("Wrong number! Number is too small")
else:
    print("Wrong number! Number is too big!")