L = list(map(int, input("L = ").split()))

max = None
for i in range(0, len(L)):
    if max == None or L[max] < L[i]:
        max = i
print(max)