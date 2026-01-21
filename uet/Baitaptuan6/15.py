d = eval(input("Nhập dictionary"))
k = int(input("k = "))
new_dict = {}
for key, value in d.items():
    if value > k:
        new_dict[key] = value
print(new_dict)