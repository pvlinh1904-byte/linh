while True:
    try:
        a, b = map(float, input("a, b = ").split(", "))
        c = a + b
        print(c)
        break
    except ValueError:
        print(" ValueError: Lỗi - không phải là số")
        print(" Vui lòng nhập lại")
