#Yêu thương chẳng là mãi mãi
L = input("Nhập vào 1 list số nguyên: ")
L = L.split(",")
L = list(map(int, L))
gt_am = 0
for i in L:
    if i < 0:
        if gt_am == 0 or gt_am < i:
            gt_am = i
print(gt_am)