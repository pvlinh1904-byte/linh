a, b, c = map(float, input("a, b, c = ").split())
if a + b > c and a + c > b and b + c > a:
    if a == b ==c:
        print("tam giac deu")
    elif a == b or b == c or a == c:
        if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or c ** 2 + b ** 2 == a ** 2 :
            print("tam giac vuong can")
        else:
            print("tam giac can")
    elif  a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or c ** 2 + b ** 2 == a ** 2 :
        print("tam giac vuong")
    else:
        print("tam giac thuong")
else:
    print("khong tao thanh tam giac")