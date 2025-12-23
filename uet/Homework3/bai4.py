h = int(input("h = "))
for i in range(1, h + 1):
    print(" " * (h - i), end = "")
    print("*" * (2 * i - 1))