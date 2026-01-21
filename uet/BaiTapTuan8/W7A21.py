def tinh_tong_so_ngay(N, T):
    so_ngay_trong_thang = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if T < 1 or T > 12:
        return None
    if N < 1 or N > so_ngay_trong_thang[T-1]:
        return None
    tong_ngay = 0
    for i in range(T-1):
        tong_ngay += so_ngay_trong_thang[i]
    tong_ngay += N
    return tong_ngay
N = int(input("Nhập số ngày: "))
T = int(input("nhập số tháng: "))
print(tinh_tong_so_ngay(N, T))