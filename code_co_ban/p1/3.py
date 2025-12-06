def cv_dt_hcn(a,b):
    chu_vi = (a + b) *2
    dien_tich = a * b
    return chu_vi, dien_tich
a, b = map(float, input("a, b =").split(", "))
chu_vi, dien_tich = cv_dt_hcn(a,b)
print(f"chu vi, dien tich cua hcn = {chu_vi:.2f}, {dien_tich:.2f}")