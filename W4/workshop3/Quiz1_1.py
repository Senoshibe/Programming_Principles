fruit = input("Favourite fruit: ")
portions = int(input("How many fruit or vegetable portions did you eat today? "))

if (portions < 5):
    print("You should try to eat some more fruit or veggies...")

else:
    print("You are eating enough fruit and veggies!", end=" ")
    print("Keep it up!")
print("Fruit and veggies are good for you!")