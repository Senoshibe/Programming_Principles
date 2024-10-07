def sum_function_first_list(first_list):

    first_list_split = first_list.split()

    if len(first_list_split) == 1:
        return int(first_list_split[0])

    else:
        return int(first_list_split[0]) + int (first_list_split[-1])

def sum_function_second_list(second_list):

    second_list_split = second_list.split()

    if len(second_list_split) == 1:
        return int(second_list_split[0])

    else:
        return int(second_list_split[0]) + int(second_list_split[-1])

while True:

    while True: 
        first_list = input("List 1: ")
        if not all(char.isnumeric() or char.isspace() for char in first_list):
            continue
        else: break
    sum_first_list = sum_function_first_list(first_list)

    while True:
        second_list = input("List 2: ")
        if not all(char.isnumeric() or char.isspace() for char in second_list):
            continue
        else:
            break
    sum_second_list = sum_function_second_list(second_list)

    if sum_first_list > sum_second_list:
        larger_sum = sum_first_list

    elif sum_second_list > sum_first_list:
        larger_sum = sum_second_list

    elif sum_first_list == sum_second_list:
        larger_sum = "Same"

    print("Output: ", larger_sum)
