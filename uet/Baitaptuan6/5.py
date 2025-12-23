
# Input a list of integers and output a dictionary counting positives, negatives, and zeros

nums = list(map(int, input("Nhập danh sách số nguyên (cách nhau bởi dấu cách): ").split()))

result = {
    'positives': sum(1 for x in nums if x > 0),
    'negatives': sum(1 for x in nums if x < 0),
    'zeros': sum(1 for x in nums if x == 0)
}

print(result)
