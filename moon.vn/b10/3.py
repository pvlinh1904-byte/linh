def ham_mu(a, b):
    if (type(a) != float or type(b) != int):
        return -1
    t = a ** b
    return t
a = float(input("a = "))
b = int(input("b = "))
print(round(ham_mu(a, b), 3))
