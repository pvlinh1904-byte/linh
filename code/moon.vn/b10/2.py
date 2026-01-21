def dao_chuoi(s):
    tmp = ""
    for i in range(len(s)-1, -1, -1):
        tmp = tmp + s[i]
    return tmp
s = input("nhập chuỗi: ")
print(dao_chuoi(s))