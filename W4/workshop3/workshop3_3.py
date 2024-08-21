#Problem: Write a program that takes as input 3 integers and outputs them in descending order.

num1 = int(input("Integer 1? "))
num2 = int(input("Integer 2? "))
num3 = int(input("Integer 3? "))

if num1 < num2:
    num1, num2 = num2, num1

if num1 < num3:
    num1, num3 = num3, num1

if num2 < num3:
    num2, num3, = num3, num2

print("Sorted: ", num1, num2, num3)