s = input().strip()
d, m , y = map(int, s.split())
def nam_nhuan(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
so_ngay = [31, 28, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31]
if nam_nhuan(y):
    so_ngay[1] = 29
if m < 1 or m > 12 or d < 1 or d > so_ngay[m-1]:
    print("INVALID")
else:
    d += 1
    if d > so_ngay[m -1]:
        d = 1
        m += 1
        if m > 12:
            m = 1
            y += 1
    print(f"{d:02d}/{m:02d}/{y}")
        