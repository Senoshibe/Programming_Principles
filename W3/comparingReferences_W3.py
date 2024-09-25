#COMPARING REFERENCES
a = 3
b = -9

a == b #compares value of a and b, returning a boolean value.
>>> False

#what if you want to compare the references? 
id(a)
>>> 130718256159224 #reference will differ in different instances and environments of the terminal
id (b)
>>> 2469113691728

a is b
>>> False #because the reference numbers aren't the same


a is not b
>>> True
