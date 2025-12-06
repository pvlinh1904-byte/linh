n = int(input("n = "))
c = abs(n)
if c == 0:
    count = 1
else:
    count = 0
    while c > 0:
        c //= 10
        count += 1
print(count)