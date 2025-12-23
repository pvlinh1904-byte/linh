ngay = int(input("Nhập vào ngày: "))
thang = int(input("Nhập vào tháng: "))
if thang <= 8:
    sothang30ngay = (thang-1)//2
    sothang31ngay = thang // 2
else:
    sothang30ngay = thang // 2 - 1
    sothang31ngay = (thang + 1) // 2
songay = ngay + sothang30ngay*30 + sothang31ngay*31
if thang > 2:
    songay -= 2
print(songay)