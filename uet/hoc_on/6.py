n = int(input("n = "))
temp = n
rev = 0
while n > 0:
    rev = rev*10 + temp%10
    temp //= 10
if rev == n:
    print("yes")
else:
    print("no")