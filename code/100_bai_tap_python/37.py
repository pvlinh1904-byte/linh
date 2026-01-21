a = int(input("Nhập vào a: "))
max = None
min = None
while a != 1:
    if max == None or max < a:
        max = a
    if min == None or min > a:
        min = a
    a = int(input("Nhập vào a: "))
print("Số lớn nhất là: ", max)
print("Số nhỏ nhất là: ", min)