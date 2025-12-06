a, b = map(int, input("a, b = ").split(", "))
while (a != b):
    if (a > b):
        a = a - b
    else:
        b = b -a
print(a)
