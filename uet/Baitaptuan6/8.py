# Nhập một dòng gồm các chuỗi, cách nhau bởi dấu cách
lst = input().split()

# Tạo dictionary rỗng
L = {}

# Đếm số lần xuất hiện
for i in lst:
    if i in L:
        L[i] += 1
    else:
        L[i] = 1

# In kết quả
print(L)
