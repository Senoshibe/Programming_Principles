length_of_park = input("Length of park (m): ")
width_of_park = input("Width of park (m): ")
litres_per_squarem = input("Litres per square metre: ")

def concrete_needed(length, width, litres):
    return float(length) * float(width) * float(litres)

litres_required = concrete_needed(length_of_park, width_of_park, litres_per_squarem)

print(f"Litres required = {litres_required}")