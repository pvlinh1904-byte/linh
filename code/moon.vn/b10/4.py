def tranform_list(l):
    new_list = list()
    for x in l:
        y = 2*(x**3) + 3*x + 1
        # Thêm y vào new_list
        new_list.append(y)
    return new_list
l = list(map(int, input("nhập dãy: ").split(",")))
print(tranform_list(l))