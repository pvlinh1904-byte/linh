def binary_search(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
arr = list(map(int, input().split()))
target = int(input())
result = binary_search(arr, 0, len(arr) - 1, target)
print(result)