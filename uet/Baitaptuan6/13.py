# Nhập dictionary (key: value)
d = {}

n = int(input())   # số lượng phần tử

for _ in range(n):
    key = input().strip()
    value = input().strip()
    d[key] = value

# Đảo ngược key và value
new_dict = {}

for key, value in d.items():
    new_dict[value] = key

print(new_dict)
