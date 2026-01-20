n = int(input())
kq = []
k = 1
while k * k <= n:
    x = k * k
    s = str(x)
    
    if len(s) == len(set(s)):
        kq.append(x)
    k += 1
if len(kq) == 0:
    print("no number")
else:
    for x in kq:
        print(x, end=" ")