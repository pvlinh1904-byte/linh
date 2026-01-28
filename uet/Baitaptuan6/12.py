lst = list(map(int, input().split()))
count = {}
for x in lst:
    count[x] = count.get(x, 0) + 1

max_freq = max(count.values())
candidates = [x for x in count if count[x] == max_freq]
print(min(candidates))
print(count)