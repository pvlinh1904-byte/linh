toan = float(input("nhập vào điểm toán: "))
van = float(input("nhập vào điểm văn: "))
anh = float(input("nhập vào điểm anh: "))
if (0 <= toan <= 10 and 0 <= van <= 10 and 0 <= anh <= 10):
    dtb = (toan + van + anh) / 3
    if dtb >= 8 and (toan >= 8 or van >= 8) and (toan >= 6.5 and van >= 6.5 and anh >= 6.5):
        print("Học sinh giỏi")
    elif dtb >= 6.5 and (toan >= 6.5 or van >= 6.5) and (toan >= 5 and van >= 5 and anh >= 5):
        print("Học sinh khá")
    elif dtb >= 5 and (toan >= 5 or van >= 5) and (toan >= 3.5 and van >= 3.5 and anh >= 3.5):
        print("Học sinh trung bình")
    elif dtb >= 3.5 and (toan >= 3.5 or van >= 3.5) and (toan >= 2 and van >= 2 and anh >= 2):
        print("Học sinh yếu")
    else:
        print("Học sinh kém")
else:
    print("Bạn đã nhập sai quy tắc")