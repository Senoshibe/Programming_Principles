input_string = str(input("Input a String? "))
convert_integers = input_string.maketrans("0123456789", "__________")

while True:
    print(input_string.translate(convert_integers))
    input_string = str(input("Input a String? "))