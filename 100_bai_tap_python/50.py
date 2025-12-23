chuoi = input("Nhập mật khẩu: ")
ktdodai = len(chuoi) > 6
ktdacbiet = ktinhoa = ktinthuong = ktso = False
for i in chuoi:
    if i.isnumeric():
        ktso = True
    elif i.isupper():
        ktinhoa = True
    elif i.islower():
        ktinthuong = True
    else:
        ktdacbiet = True
if ktdodai and ktdacbiet and ktinhoa and ktinthuong and ktso:
    print("Đây là mật khẩu mạnh")
else:
    print("Đây là mật khẩu yếu")