coffee = 5.5

print("price of coffee = ", coffee)

print("price of four coffees = ", 4*coffee)

tea = 3.0 

#prints while separating 'price of tea = ', '3.0', 'price of coffee = ' and '5.5' with the ! symbol
print("price of tea = ", tea, " price of coffee = ", coffee, sep="!")

#same as above but adds a symbol at the end
print("price of tea = ", tea, "price of coffee = ", coffee, sep = "!", end = "!")

#can also add variables in the print function 
print("Cost of Tea and Coffee = ", tea+coffee)
