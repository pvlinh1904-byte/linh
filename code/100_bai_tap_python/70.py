L = input("Nhập vào L: ")
L = L.split(",")
for i in range(len(L)):
    if L[i].isnumeric():
        L[i] = int(L[i])
if len(L) % 2 == 0:
    kq = True
    for i in range(len(L) - 1):
        if not((type(L[i]) is str and type(L[i+1]) is int) or (type(L[i]) is int and type(L[i+1]) is str)):
            kq = False
            break
    if kq:
        k = []
        for i in range(0,len(L),2):
            k.append(L[i]*L[i+1])
        print("k =", k)
    else:
        print("Không thể xây dựng list k vì list L không phải là dạng chuỗi số xen kẽ!")
else:
    print("Không thể xây dựng được list k vì số phần tử của L là lẻ")