nums = list(map(int, input().split()))
so_chan = []
so_le = []
for x in nums:
    if x % 2 == 0:
        so_chan.append(x)
    else:
        so_le.append(x)
so_chan.sort()
so_le.sort(reverse=True)
result = so_chan + so_le
print(result)