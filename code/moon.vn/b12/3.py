while True:
    try:
        n = int(input("n = "))
        if (n < 0):
            raise ValueError()
        else:
            print(bin(n)[2:])
            break
    except ValueError:
        print("ValueError: Vui lòng nhập số nguyên dương")