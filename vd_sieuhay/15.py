arr = list(map(int, input().split()))

freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1

max_len = 0
for x in freq:
    if x + 1 in freq:
        max_len = max(max_len, freq[x] + freq[x+1])
print(max_len)