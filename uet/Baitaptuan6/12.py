# Nhập danh sách số nguyên
lst = list(map(int, input().split()))

# Tạo dictionary đếm số lần xuất hiện
count = {}

for x in lst:
    count[x] = count.get(x, 0) + 1

# Tìm số xuất hiện nhiều nhất
max_freq = max(count.values())

# Các số có số lần xuất hiện bằng max_freq
candidates = [x for x in count if count[x] == max_freq]

# In ra số nhỏ nhất trong số đó
print(min(candidates))
