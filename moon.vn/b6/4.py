n = int(input("n = "))
if n < 0:
    print("Không hợp lệ")
else:
    giai_thua = 1
    for i in range (1, n + 1):
        giai_thua = giai_thua * i
    print(f"{n}! = {giai_thua}")