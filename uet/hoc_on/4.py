#cho N là ngày, T là tháng năm 2020. 
#Tính xem đó là ngày thứ bao nhiêu của năm đó là ngày hợp lệ, ngược lại in ra "invalid"
N, T = map(int, input("N, T = ").split())
ngay = [31, 29, 31, 30 , 31, 30, 31, 31, 30, 31, 30, 31]
if T < 1 or T > 12:
    print("invalid")
else:
    if N < 1 or N > ngay[T-1]:
        print("invalid")
    else:
        tong_ngay = sum(ngay[:T-1]) + N
        print(tong_ngay)