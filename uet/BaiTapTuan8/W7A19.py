def merge_sorted_arrays(A, B):
    n = len(A)
    m = len(B)

    i = 0 # con trỏ mảng A
    j = 0 # con trỏ mảng B
    C = [] # mảng kết quả
    
    # xác định kiểu sắp xếp (tăng hay giảm)
    if n > 1 and A[0] <= A[1]:
        tang_dan = True
    else:
        giam_dan = False
    
    # trộn 2 mảng
    while i < n and j < m:
        if tang_dan:
            # Trường hợp tăng dần
            if A[i] <= B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
    # nếu A còn phần tử
    while i < n:
        C.append(A[i])
        i += 1

    # nếu B còn phần tử
    while j < m:
        C.append(B[j])
        j += 1

    return C
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*merge_sorted_arrays(A, B))