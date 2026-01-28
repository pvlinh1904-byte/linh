d = {}
n = int(input())
for _ in range(n):
    key = input().strip()
    value = input().strip()
    d[key] = value
new_dict = {}
for key, value in d.items():
    new_dict[value] = key
print(new_dict)
print(d)