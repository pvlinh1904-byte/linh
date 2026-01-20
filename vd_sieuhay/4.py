a, b, k = map(int, input().split())
t = 0
for i in range(a, b+1):
    if i % k == 0:
        t += i
print(t)
