def bubble_sort(arr):
    n = len(arr)
    
    for i in range(0, n):
        kq = False
        for j in range(0, n - i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j +1], arr[j]
                kq = True
        if  not kq:
            break
    return arr
arr = list(map(int, input("arr = ").split()))
arr = bubble_sort(arr)
print(*arr)



def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
#arr = list(map(int, input("arr = ").split()))
    
#arr = selection_sort(arr)
print(*arr)