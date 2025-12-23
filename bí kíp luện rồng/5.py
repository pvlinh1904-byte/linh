N = int(input())
a = N**2
count = 0
for i in range(1, a + 1):
    if N + 1 <= i <= a:
        count += 1
print(count)