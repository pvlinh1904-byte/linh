a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j] and a[i] not in c:
            c.append(a[i])
print(c)

for x in a:
    if x in b and x not in c:
        c.append(x)

print(c)