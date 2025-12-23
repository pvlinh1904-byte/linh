def bangcuuchuong(a, b):
    if a > b:
        for i in range(1, 11):
          print(f"{a} x {i} = {a*i}")
    else:
       for i in range(1, 11):
          print(f"{b} x {i} = {b*i}")
a = int(input("a = "))
b = int(input("b = "))
c = bangcuuchuong(a, b)
print(c)