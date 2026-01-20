L = input("Nhập vào L: ")
L = L.split(",")
L = list(map(int, L))

for i in range(len(L)):
    kt = True
    for j in range(i):
        if L[j] >= L[i]:
            kt = False
            break
    if kt:
        dem += 1
        
print(dem)