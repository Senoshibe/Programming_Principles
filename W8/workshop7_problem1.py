import sys

def sort_string():
    input_string = input("Enter a string: ")

    if input_string == '':
        sys.exit

    if not all(char.isalpha() or char.isspace() for char in input_string):
        return
    else:
        input_string_lower = input_string.lower()
        split_string = input_string_lower.split()

    split_string.sort(reverse = True)
    print("Output: ", split_string)

while True: 
    sort_string()

    
