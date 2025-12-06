x = int(input("x giây =  "))
gio = x // 3600
phut = (x % 3600) // 60
giay = x % 60
print(f"{x} giây = {gio}h {phut}p {giay}s")