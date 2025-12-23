L = list(map(int, input("L = ").split()))
k = int(input("k = "))
for i in range(0, len(L)):
    if L[i] == k:
        break
    else:
        i = -1
print(i)