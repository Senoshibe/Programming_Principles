#python is unable to print the following function

print("Hello", end="\")
      
#this is because the backslash character `\` is a special character in python that is used to introduce escape sequences like `\n` for newline
#therefore the correct way to print the backslash `\` is...

print("Hello", end"\\")

#what if you want to print two backaslashes `\`? 

print("Hello", end="\\\")
      
    