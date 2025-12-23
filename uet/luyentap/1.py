#W5A1
while True:
    def Max_Of_Two(a: int, b: int):
        return max(a, b)

    try:
        a, b = map(int, input("a, b = ").split(", "))
        print(Max_Of_Two(a, b))
        break
    except ValueError:
        print("nhập sai")
