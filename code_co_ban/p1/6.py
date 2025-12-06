import math
def cv_dt_htg(a, b, c):
    chu_vi = a + b + c
    p = chu_vi/2
    dien_tich = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return chu_vi, dien_tich
a, b, c = map(float, input("a, b, c = ").split(", "))
chu_vi, dien_tich = cv_dt_htg(a, b, c)
print(chu_vi, dien_tich)