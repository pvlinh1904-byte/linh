import math
def cv_dt(r):
    chu_vi = 2 * math.pi * r
    dien_tich = math.pi * (r ** 2)
    return chu_vi, dien_tich
r = float(input("r = "))
chu_vi, dien_tich = cv_dt(r)
print(f"chu vi hinh tron = {chu_vi:.2f}")
print(f"dien tich hinh tron = {dien_tich:.2f}")