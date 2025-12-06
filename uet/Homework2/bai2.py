import math
def cv_dt(r):
    if r < 0:
        return (-1, -1)
    else: 
        cv = 2 * math.pi * r
        dt = math.pi * (r ** 2)
        return (cv, dt)
r = float(input("r = "))
cv, dt = cv_dt(r)
if (cv == dt == -1):
    print("cạnh không hợp lệ")
else:
    print("chu vi = ", round(cv, 2))
    print("diện tích", round(dt, 2))