L = input("Nhập vào list số nguyên: ")
L = L.split(",")
L = list(map(int, L))
kt = True
for i in L:
    if i != L[0]:
        kt = False
        break
if kt:
    print("List L có các phần tử bằng nhau!")
else:
    print("List L không có các phần tử bằng nhau!")