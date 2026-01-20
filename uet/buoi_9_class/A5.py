class Shoppingcart:
    def __init__(self):
        self.items = []
    
    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})
    
    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                return True
        return False
    
    def is_emty(self):
        return len(self.items) == 0
    
    def total_price(self):
        total = 0
        for item in self.items:
            total += item["price"]
        return total
    
    def show_items(self):
        if self.is_emty():
            print("Gio hang rong")
        else:
            for item in self.items:
                print(item["name"], item["price"])
    
    def clear_cart(self):
        self.items.clear()

cart = Shoppingcart()
while True:
    print("\n----- MENU -----")
    print("2.them san pham")
    print("3. xoa san pham")
    print("4. kiem tra gio hang rong")
    print("5. tinh tong tien")
    print("6. hien thi gio hang")
    print("7. xoa toan bo gio hang")

    choice = input("chon chuc nang (2-7): ")

    if choice == "2":
        name = input("nhap ten san pham: ")
        price = float(input("nhap gia: "))
        cart.add_item(name, price)
        print("da them san pham")

    elif choice == "3":
        name = input("nhap ten san pham can xoa")
        if cart.remove_item(name):
            print("da xoa san pham")
        else:
            print("khong tim thay san pham")

    elif choice == "4":
        if cart.is_emty():
            print("gio hang rong")
        else:
            print("gio hang khong rong")

    elif choice == "5":
        print(f"tomg tiem: {cart.total_price():.2f}")

    elif choice == "6":
        cart.show_items()
    
    elif choice == "7":
        cart.clear_cart()
        print("da xoa toan bo gio hang")

    else:
        print("lua chon ko hop le")

    exit_choice = input("co muon thoat khong? ")
    if exit_choice.lower() == "yes":
        break