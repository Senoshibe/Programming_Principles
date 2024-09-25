#input function allows you to input a value in an object
input("Enter a number: ")
>>> Enter a number:
#if you type 2 and hit enter, you get...
>>> '2'
#notice how the value is a string? As it's in single quotation marks

#Let's say you want get the input value and increase it by the power of 3
#There are two ways to go about this

#1st WAY
#convert the input value into a float when printing
#(First we will assign a variable to the input function for convenience)

num = input("Enter a number: ")
#now if you recall 'num', it returns..
num
>>> '2' 
#same as the first example
#If you try and increase 'num' to the power of 3, you'll return an error, 'num' is a str
#For example...

print("The number to the power of 3 = ", num**3)
>>> TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

#so in the princt function above, we'll convert the num**3 expression into a float using float()

print("The number to the power of 3 = ", float(num)**3)
>>> The number to the power of 3 =  8.0


#2nd WAY
#convert the input function into a float --- personally looks messy (?)

num = float(input("Enter a number: "))
>>> Enter a number: 
#let's type 4 and hit enter > Enter a number: 4
>>> 4.0 
#because the value of num is now a float and not a str, we can proceed to print the two objects with the ** operation

print("The number to the power of 3 = ", num**3)
>>> 64.0
#4**3 = 64, so the returned value is correct.

