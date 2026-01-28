def count_occurrences(arr, x):
    i = 0
    count = 0
    while i < len(arr):
        if arr[i] == x:
            count += 1
        i += 1
    return count
arr = list(map(int, input().split()))
x = int(input())
print(count_occurrences(arr, x))
