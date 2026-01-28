def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n):
        kq = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                kq = True
        if not kq:
            break
    return arr
arr = list(map(int, input("arr = ").split()))
arr = bubble_sort(arr)
print(*arr)
