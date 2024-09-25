#the `or` operator doesn't always behave as expected.
#this is because of short circuit comparisons

#other examples

a or 6 #Short-circuit behavior for or: In the expression a or 6, if a evaluates to True, Python does not evaluate 6 because the result will definitely be True regardless of 6. This is because or only returns False if both operands are False.
>>> True

b or 6 #Boolean Evaluation:
#b is False.
#2nd operand is 6. While it's true that 6 is a non-zero integer and thus considered True in boolean contexts, this isn't directly relevant to the or operator's behavior.
#Short-circuit Behavior:
#The or operator in Python returns the first operand if it's True (truthy). If the first operand is False (falsy), it returns the second operand, regardless of its truthiness.
#In this case, b is False (falsy), so the or operator moves to the second operand, which is 6.
#Return Value:
#Since b is False, b or 6 evaluates to 6. 
#In summary, b or 6 returns 6 because b is False, and the or operator returns the value of the second operand when the first operand is falsy. It doesn’t return a boolean value, but rather the actual value of the second operand.

>>> 6

#how do we resolve this unwanted result? 

bool(b or 6) #cast the value to bool
#remember, bool(6) returns True. This is for all integers that are not 0
#Also, b = False
#Therefore bool(b or 6) is bool(False or True) which is True
>>> True

#short circuit comparison example with `and` operator
c = True
d = 8
c and d #When you write c and d, here's what happens:
#The and operator first evaluates the expression c. Since c is True, the and operator then evaluates the second operand, which is d.
#In Python, the result of an and operation is the value of the second operand if the first operand evaluates to True. If the first operand were False, the result would be False, and the second operand wouldn't even be evaluated.
#So in c and d:
#c is True, so the expression c and d evaluates to the value of d.
#d is 8, so c and d evaluates to 8.
#Here’s a step-by-step breakdown:
#Evaluate c: True

#Since c is True, evaluate d: 8

#Result of c and d is 8

>>> 8

#to resolve, cast like the previous example
bool(c and d)
>>> True