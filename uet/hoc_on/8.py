arr = list(map(int, input().split()))
n = len(arr)
if n < 2:
    print("Vo danh")
else:
    a = True
    b = True
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            a = False
        if arr[i] < arr[i-1]:
            b = False
    if a:
        print("Giam")
    elif b:
        print("Tang")
    else:
        print("Vo danh")