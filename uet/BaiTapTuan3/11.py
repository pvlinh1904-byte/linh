# Nhập độ dài ba cạnh
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

# Kiểm tra tam giác hợp lệ
if a <= 0 or b <= 0 or c <= 0:
    print("Không phải tam giác")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Không phải tam giác")
else:
    # Phân loại tam giác
    if a == b == c:
        print("Tam giác đều")
    elif a == b or a == c or b == c:
        print("Tam giác cân")
    else:
        print("Tam giác thường")
