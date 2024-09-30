num = int(input("Enter a positive number: "))

for row in range(1, num + 1):

    spaces = ' ' * (num - row)

    numOfX = 2 * row - 1

    print(spaces, end="")
    print("x" * numOfX)

for row in range(num - 1, 0, -1):

    spaces = ' ' * (num - row)

    numOfX = 2 * row - 1

    print(spaces, end="")
    print("x" * numOfX)

    