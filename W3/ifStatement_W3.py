print("You win if you guess the magic number.")
num = int(input("Enter a number: "))
if (num == 7): #becareful of the == operator. Don't make the mistake of using =, as it'll change the value of num, which doesn't make sense in the if statement.
  print("Congratulations! Lucky number 7!")
print("if you didn't win, better luck next time!")  
