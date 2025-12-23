pairs = input().split()
d = {}
for p in pairs:
    key, value = p.split(":")
    if key not in d:
        d[key] = []
    d[key].append(value)

print(d)