n = int(input())
if n % 2 != 0:
    print("Werid")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not werid")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Werid")
elif n % 2 == 0 and n > 20:
    print("Not werid")
else:
    print(-1)