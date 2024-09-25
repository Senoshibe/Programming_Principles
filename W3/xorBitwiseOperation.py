c ^ d #`^` is the xor operator
>>> 9 #** refer to image to the right for reason. Basically it's due to the `^` operator is the xor bitwise operator. This operation converts the values into their binary representations, therefore returning an unwanted result

bool(c^d) #The bool() function converts a value to its Boolean representation. Any non-zero integer converts to True, while 0 converts to False.
#Since 1 ^ 8 evaluates to 9 and 9 is non-zero, bool(9) will be True.
#This is the case even though Truthy xor Truthy equals Falsey

>>> True
