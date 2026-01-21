a, b, c = map(float, input("a, b, c = ").split())
if a + b > c and a + c > b and b + c > a:
    print("co tao thanh tam giac")
else:
    print("khong tao thanh tam giac")