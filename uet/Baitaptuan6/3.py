t = tuple(map(int, input().split(", ")))
k = int(input())
k = k % len(t)
rotated = t[k:] + t[:k]
print(rotated)