L = input("Nhập vào L: ")
L = L.split(",")
L = list(map(int, L))
a = int(input("Nhập vào a: "))
b = int(input("Nhập vào b: "))
min = None
for i in range(a, b+1):
    if min == None or min > L[i]:
        min = L[i]
print(min)