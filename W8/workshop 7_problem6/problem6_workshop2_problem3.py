big_hall = input("How many big exam halls? ")
small_hall = input("How many small exam halls? ")

def num_of_classes(big_hall, small_hall):
    return (int(big_hall) * 45 + int(small_hall) * 22)//25

print(f"Number of classes = {num_of_classes(big_hall, small_hall)}")