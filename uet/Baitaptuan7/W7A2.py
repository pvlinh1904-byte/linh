def count_occurrences(arr, x) -> int:
    i = 0
    count = 0
    while i < len(arr):
        if arr[i] == x:
            count += 1
        i += 1
    return count
arr = list(map(int, input("arr = ").split()))
x = int(input("x = "))
print(count_occurrences(arr, x))