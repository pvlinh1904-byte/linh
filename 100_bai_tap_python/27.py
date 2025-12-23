h = int(input("h = "))
khoangtrangngoai = h - 1
khoangtrangtrong = 1
for i in range(h):
    if i == 0:
        print(" " * khoangtrangngoai + "*")
    elif i < h - 1:
        print(" " * khoangtrangngoai + "*" + " " * khoangtrangtrong + "*")
        khoangtrangtrong += 2
    else:
        print("*" * (h * 2 - 1))
    khoangtrangngoai -= 1