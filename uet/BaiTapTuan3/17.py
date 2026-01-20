a, b, c, d = map(int, input().split())
if a == 0:
    print("No")
else:
    if b % a != 0:
        print("No")
    else:
        q = b // a
        if b * q == c and c * q == d:
            print("Yes")
        else:
            print("No")