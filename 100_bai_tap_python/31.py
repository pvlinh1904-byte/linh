a = int(input("a = "))
b = int(input("b = "))
for i in range(1, a + 1):
    if i > b:
        break
    if a % i == 0 and b % i == 0:
        print(i)