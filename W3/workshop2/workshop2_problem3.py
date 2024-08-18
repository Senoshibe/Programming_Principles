#Problem3: A primary school needs to arrange their students to sit for the National Assessment Program - Literacy and Numeracy test in multiple exam halls at Griffith University.
#Each school class has 25 students. A big exam hall can accomodate 45 students, and a small exam hall can accomodate 22 students. 
#Write a program for the school to calculate how many full classes can be accomodated given the input numbers of the number of big exam halls and small exam halls. 
#For example, the output should look like this when the program is run:
#How many big exam halls? 10
#How many small exam halls? 20
#Number of classes = 35

big_hall = int(input("How many big exam halls? "))
small_hall = int(input("How many small exam halls? "))
number_classes = (45*big_hall + 22*small_hall)//25
print("Number of classes = ", number_classes)
