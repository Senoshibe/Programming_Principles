price = 5.5

#Suppose you want to add the below two values to create the string 'The price of coffee = 5.5'

"The price of coffee = " + price

#the above expression will return an error, as "The price of coffee" is a string, and price is an int
#One way to resolve this is to re-define price as "5.5" making it a string
#Another way is to use the str() function, for example:

"The price of coffee = " + str(price)
#this won't return an error