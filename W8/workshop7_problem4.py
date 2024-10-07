
while True: 
    enter_degrees = input("Enter the degrees and the unit (C/F): ")
    degrees_unit = float(enter_degrees[:-1])
    degrees_measurement = enter_degrees[-1:]

    if degrees_measurement == "F":
        celcius_conversion = (degrees_unit - 32) * (5/9)
        if celcius_conversion.is_integer():
            print(int(degrees_unit), "F is ", int(celcius_conversion), "C")
        else:
            print(f"{degrees_unit:.2f} F is {celcius_conversion:.2f} C")

    elif degrees_measurement == "C":
        farenheit_conversion = float((degrees_unit * 1.8) + 32)
        if farenheit_conversion.is_integer():
            print(int(degrees_unit), "C is", int(farenheit_conversion), "F")
        else:
            print(f"{degrees_unit:.2f} C is {farenheit_conversion:.2f} F")

    