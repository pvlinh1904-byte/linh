h = int(input("h = "))
m = int(input("m = "))
if (h < 0 or h >= 24):
    print("Giờ không hợp lệ")
elif (m < 0 or m >= 60):
    print("Phút không hợp lệ")
else:
    if (h < 12):
        print(f"{h} : {m} AM")
    elif (h == 12):
        print(f"{h} : {m} PM")
    else:
        h = h % 12
        print(f"{h} : {m} PM")