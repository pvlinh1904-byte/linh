nums = list(map(int, input().split(", ")))
result = []
seen = set()
    
for x in nums:
    if x not in seen:
        result.append(x)
        seen.add(x)
print(result)