arr = list(map(int, input().split()))
x = int(input())

left = 0
right = len(arr) - 1
result = -1

while left <= right:
    mid = (left + right) // 2
    if arr[mid] == x:
        result = mid
        right = mid - 1
    elif arr[mid] < x:
        left = mid + 1
    else:
        right = mid - 1
print(result)