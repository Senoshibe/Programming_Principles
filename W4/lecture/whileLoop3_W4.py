print("You win if you guess the magic number.")
n = int(input("Enter a number:"))
while n != 3: ## while n is not 3 (continue the while loop)
    if n == 7:
        print("Some people think so, but not me.") 
    
    if n < 3: 
        print("Try higher.")

    else:
        print("Try lower.")

    n = int(input("Enter a number:"))
    
print("You win!")
print("It is the first odd prime Yay!")

## in this example, the 'Sentinel Value' is 3, as it stops the loop. 