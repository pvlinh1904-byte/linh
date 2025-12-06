import math
def cv_dt_hinh_tron(r):
    if (r <= 0):
        return (-1, -1)
    else:
        cv = 2 * math.pi * r
        dt = math.pi * (r ** 2)
        return (cv, dt)

cv, dt = cv_dt_hinh_tron(float(input("Nhập r = ")))
if (cv == dt == -1):
    print("bán kính không hợp lệ")
else:
    print(f"chu vi, diện tích là {round(cv, 3)}, {round(dt, 3)}")