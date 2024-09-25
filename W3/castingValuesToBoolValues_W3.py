#casting values means changing values to another class
#e.g. a = '3'
#in this example `a` is a `str`
#int(a) will return the value 3, which is an integer.
# `a` was cast from a `str` to `int`

#in this example, we will cast the value 0 into a `bool`
bool(0)
>>> False

bool(4)
>>> True

bool(-6)
>>> True

#if you cast an `int` to a `bool` all values but 0 return `True`


bool("") #empty string
>>> False

bool(0.0)
>>> False

bool(-7.8)
>>> True

bool(3.0)
>>> True

bool("False") #not an empty string, therefore True
>>> True