#Problem: A shipping company charges its customer based on the weight of goods and the distance of
#shipping. A discount is given based on the distance of shipping as follows:
#distance < 250km, no discount
#250km ≤ distance < 500km, 10% discount
#500km ≤ distance < 1000km, 15% discount
#1000km ≤ distance < 2000km, 20% discount
#2000km ≤ distance < 3000km, 35% discount
#3000km ≤ distance, 50% discount
#The shipping cost is calculated based on the following equation:
#cost = basePrice * weight * distance * (1 - discount).
#Write a program that takes as inputs the base price, weight, and distance, and prints the shipping cost to be
#charged to the customer.

basePrice = float(input("How much is the base price "))


weight = float(input("What is the weight? "))


distance = float(input("What is the distance? "))
if 0 <= distance < 250:
    discount = 0.0

if 250 <= distance < 500:
    discount = 0.1

if 500 <= distance < 1000:
    discount = 0.15

if 1000 <= distance < 2000:
    discount = 0.2

if 2000 <= distance < 3000:
    discount = 0.35

if distance >= 3000:
    discount = 0.5

print("The shipping cost is ", basePrice*weight*distance*(1 - discount))