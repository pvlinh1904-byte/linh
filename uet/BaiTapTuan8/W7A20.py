def tinh_tong(N, k):
    tong = 0
    for x in N:
        if len(str(x)) == k:
            tong += x
    return tong
N = list(map(int, input().split()))
k = int(input())
print(tinh_tong(N, k))