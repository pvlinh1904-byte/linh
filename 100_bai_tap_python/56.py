L = input("Nhập vào một list số nguyên: ")
L = L.split(",")
L = list(map(int, L))

for i in L:
    if i > 0: 
        break
    else:
        i = -1
print(i)


gt_duong = -1
for i in L:
    if i > 0:
        gt_duong = i
        break
print(gt_duong)