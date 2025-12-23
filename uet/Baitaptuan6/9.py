def nhap_dict():
    d = {}
    n = int(input())  # số lượng phần tử

    for _ in range(n):
        key = input().strip()
        value = int(input())
        d[key] = value

    return d


# Nhập hai dictionary
dict1 = nhap_dict()
dict2 = nhap_dict()

# Gộp hai dictionary
result = {}

for key, value in dict1.items():
    result[key] = result.get(key, 0) + value

for key, value in dict2.items():
    result[key] = result.get(key, 0) + value

# In ra theo thứ tự key tăng dần
result = dict(sorted(result.items()))
print(result)
