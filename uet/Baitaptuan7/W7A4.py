def phan_tu_xuat_hien_nhieu_nhat(ds):
    dem = {}
    max_count = 0
    ket_qua = None
    for x in ds:
        dem[x] = dem.get(x, 0) + 1

        if dem[x] > max_count:
            max_count = dem[x]
            ket_qua = x
    return ket_qua, max_count
ds = list(map(int, input("Nhập các số: ").split()))

pt, so_lan = phan_tu_xuat_hien_nhieu_nhat(ds)

print(f"{pt} xuất hiện nhiều nhất, sớm nhất, {so_lan} lần")