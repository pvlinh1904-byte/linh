L = list(map(int, input("L = ").split()))
x = int(input("x = "))
kq = False
for i in range(0, len(L)):
    if L[i] < x:
        print(i, end=" ")
        kq = True
if not kq:
    print(-1)