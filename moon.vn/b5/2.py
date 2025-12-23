#đk1: Lịch Gregorius bắt đầu tính từ năm 1582
#đk2: là năm chia hết cho 4
#đk3: nếu năm đó chia hết cho 100 và không chia hết cho 400 thì không phải năm nhuận,
#     còn nếu năm đó đồng thời chia hết cho 100 và 400 thì năm đó là năm nhuận
y = int(input("y = "))
if y >= 1582:
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        print(f"{y} là năm nhuận")
    else:
        print(f"{y} không là năm nhuận")
else:
    print("Không tính theo lịch Gregorius")