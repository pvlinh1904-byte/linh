n = int(input())
S = 0
k = 0
while S < n:
    for i in range(1, k):
        S += k
        k += 1
print(k)