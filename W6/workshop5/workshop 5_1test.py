x = 0
y = 1
z = 1
m = 0

while True:
    f = z + y
    print(x, y, z, f, sep = " ")
    x = z + f
    y = f + x
    z = x + y
    m += 1
    if m == 3:
        break
