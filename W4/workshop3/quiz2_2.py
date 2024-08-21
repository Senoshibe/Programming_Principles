cost = int(input("Cost of items: "))

if cost == 0:
    print("You did not buy anything. You still need to add something to your cart to the value of $100.")

elif 0 < cost < 100:
    print("You do not qualify yet! You still need to add something to your cart to the value of $", 100.0 - float(cost))

if 100 <= cost < 200:
    discountDecimal = 0.05
    discount = 5

if 200 <= cost < 250:
    discountDecimal = 0.1
    discount = 10

if 250 <= cost < 300:
    discountDecimal = 0.15
    discount = 15

if cost > 300:
    discountDecimal = 0.15
    discount = 15

if cost >= 100:
    revisedCost = cost*(1.0-discountDecimal)
    print("You qualify for a ", discount, "% discount! The new discounted cost of your items is $", revisedCost)

