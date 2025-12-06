def cv_dt(a, b):
    if (a < 0) or (b < 0):
        return -1
    else:
        cv = 2 * (a + b)
        dt = a * b
        return cv, dt
a, b = map(float, input("a, b = ").split(", "))
chu_vi, dien_tich = cv_dt(a, b)
print(chu_vi)
print(dien_tich)