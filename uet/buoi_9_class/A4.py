class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def cong(self):
        return self.a + self.b
    
    def tru(self):
        return self.a - self.b
    
    def nhan(self):
        return self.a * self.b
    
    def chia(self):
        return self.a / self.b
    
    def hammu(self):
        return self.a ** self.b
    
    def layphandu(self):
        if self.b == 0:
            print("invalid")
        return self.a % self.b
     
    def capnhat(self, a, b):
        self.a = a
        self.b = b

a, b = map(float, input().split())
calc = Calculator(a, b)

while True:
    print("\n-----MENU-----")
    print("1: cong")
    print("2: tru")
    print("3: nhan")
    print("4: chia")
    print("5: mu")
    print("6: lay phan du")
    print("7: cap nhat 2 so moi")

    choice = input("chon 1 - 7: ")

    if choice == "1":
        print(calc.cong())
    elif choice == "2":
        print(calc.tru())
    elif choice == "3":
        print(calc.nhan())
    elif choice == "4":
        print(calc.chia())
    elif choice == "5":
        print(calc.hammu())
    elif choice == "6":
        print(calc.layphandu())
    elif choice == "7":
        a, b = map(float, input("nhap 2 so moi: ").split())
        calc.capnhat(a, b)
        print("da cap nhat 2 so moi")
    else:
        print("lua chon khong hop le")

    thoat_choice = input("ban co muon thoat? ")

    if thoat_choice.lower() == "yes":
        break