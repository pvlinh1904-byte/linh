m, n = map(int, input("m, n = ").split(", "))
for i in range(max(m, n), 0, -1):
    if m % i == 0 and n % i == 0:
        print(i)
        break