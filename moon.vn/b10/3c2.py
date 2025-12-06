def ham_mu(a, b):
    t = 1
    if (b == 0):
        return t
    elif (b > 0):
        for i in range(0, b):
            t = t * a
    else:
        for i in range(0, abs(b)):
            t = t * a
        t = 1/t
    return round(t, 3)
a = float(input("a = "))
b = int(input("b = "))
print(ham_mu(a, b))