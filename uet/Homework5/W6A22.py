def index_max(arr):
    # Giả sử phần tử đầu tiên là lớn nhất
    max_value = arr[0]
    max_index = 0

    # Duyệt từ phần tử thứ 2
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
            max_index = i

    return max_index
arr = list(map(int, input().split()))
print(index_max(arr))