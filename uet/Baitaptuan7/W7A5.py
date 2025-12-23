def dem_cap_tong_bang_x(ds, x):
    n = len(ds)
    dem = 0
    for i in range(n):
        for j in range(i+1, n):
            if ds[i] + ds[j] == x:
                dem += 1
    return dem
ds = list(map(int, input("ds = ").split()))
x = int(input("x = "))
print(dem_cap_tong_bang_x(ds, x))