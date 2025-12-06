c = input("Nhập 1 ký tự: ")
if len(c) != 1:
    print("chỉ nhập 1 ký tự")
else:
    if c.isalpha():
        print(f"{c} là ký tự alphabet")
    else:
        print(f"{c} không phải ký tự alphabet")