def tinh_chu_vi(a, b):
    if (a <= 0 or b <= 0):
        return -1
    else:
        cv = 2 * ( a + b)
        return cv
a, b = map(float, input("a, b = ").split(";"))
cv = tinh_chu_vi(a, b)
if (cv == -1):
    print("cạnh không hợp lệ")
else:
    print(f"chu vi hcn là: {cv}")