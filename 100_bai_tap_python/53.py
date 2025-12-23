L = input("Nhập vào list số nguyên: ")
L = L.split(",")
L = map(int, L)
max = None
for i in L:
    if max == None or max < i:
        max = i
print(max)