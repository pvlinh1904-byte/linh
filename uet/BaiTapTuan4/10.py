def collatz_length(x):
    length = 1
    while x != 1:
        if x % 2 == 0:
             x //= 2
        else:
            x = 3 * x + 1
        length += 1
    return length
n = int(input())
max_len = 0
best_x = 1
for x in range(1, n + 1):
    L = collatz_length(x)
    if L > max_len or (L == max_len and x < best_x):
        max_len = L
        best_x = x
print(best_x, max_len)