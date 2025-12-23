T = tuple(map(int, input("T = ").split()))
a1 = []
a2 = []
for i in range(len(T)):
    if T[i] % 2 == 0:
        a1.append(T[i])
    else:
        a2.append(T[i])
print(tuple(a1))
print(tuple(a2))