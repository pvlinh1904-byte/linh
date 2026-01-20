def phan_tu_ben_phai_nho_hon(ds):
    n = len(ds)
    ds_dem = []
    
    for i in range(n):
        dem = 0
        for j in range(i+1, n):
            if ds[i] > ds[j]:
                dem += 1
        ds_dem.append(dem)
    return ds_dem
ds = list(map(int, input("ds = ").split()))
print(phan_tu_ben_phai_nho_hon(ds))