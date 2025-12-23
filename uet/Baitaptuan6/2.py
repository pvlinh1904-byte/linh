nums = list(map(int, input().split(", ")))
result = []
current_sum = 0
for x in nums:
    current_sum += x
    result.append(current_sum)
print(result)
