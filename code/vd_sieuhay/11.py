a, b, d = map(int, input().split())
count = 0
for i in range(a, b+1):
    
    if i % 10 == d:
        count += 1
print(count)