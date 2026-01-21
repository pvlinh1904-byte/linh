a = int(input("a = "))
b = int(input("b = "))
UCLN = 1
for i in range(1, a+1):
    if i > b:
        break
    if a % i == 0 and b % i == 0:
            UCLN = i
print(UCLN)


while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print(a)