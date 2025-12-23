a = int(input("a = "))
if 50 <= a <= 100:
    if a % 3 == 0:
        print("True")
else:
    print("False")

print(a % 3 == 0 and 50 <= a <= 100)