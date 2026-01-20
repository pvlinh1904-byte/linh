def xuat_hien_nhieu_nhat(ds):
    dem = {}
    max_count = 0
    kq = None
    for x in ds:
        dem[x] = dem.get(x, 0) + 1
        if dem[x] > max_count:
            max_count = dem[x]
            kq = x
    return kq, dem[x]
ds = list(map(int, input().split()))
print(xuat_hien_nhieu_nhat(ds))