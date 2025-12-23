N = int(input())
a = (N - 1) / 2
count = 0
for i in range(1, N + 1):
    if i > a:
        count += 1
print(count)