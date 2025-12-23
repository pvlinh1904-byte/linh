print("Chào mừng các bạn đến với nhà hàng thức ăn nhanh!")
print("Mời bạn nhập số lượng thức từng món ăn:")
print()
sl_garan = int(input("Gà rán: "))
sl_hamburger = int(input("Hamburger: "))
sl_cocacola = int(input("Cocacola: "))
print()

def dinhdang(s):
    while len(s) < 20:
        s += " "
    return s

print("Hóa đơn:")
print(dinhdang("Gà rán") + "30.000đ x " + str(sl_garan))
print(dinhdang("Humburger") + "25.000đ x " + str(sl_hamburger))
print(dinhdang("Cocacola") + "10.000đ x " + str(sl_cocacola))
print()
print("Tổng:")

def phancachngan(a):
    a = str(a)
    i = len(a) - 3
    while i > 0:
        a = a[:i] + "." + a[i:]
        i -= 3
    return a

print(dinhdang("Gà rán") + phancachngan(30000*sl_garan) + "đ")
print(dinhdang("Hamburger") + phancachngan(25000*sl_hamburger) + "đ")
print(dinhdang("Cocacola") + phancachngan(10000*sl_cocacola) + "đ")
tong = 30000*sl_garan + 25000*sl_hamburger + 10000*sl_cocacola
print(dinhdang("Tổng trước thuế") + phancachngan(tong) + "đ")
print(dinhdang("Thuế 5%") + phancachngan(int(tong*0.05)) + "đ")
print(dinhdang("Tổng sau thuế") + phancachngan(int(tong*1.05)) + "đ")