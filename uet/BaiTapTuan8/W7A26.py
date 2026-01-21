def tach_so_va_tinh(s):
    ds_so = [] # Danh sách các số tìm được
    so_hien_tai = "" # Lưu các chữ số đang ghép
    for ky_tu in s:
        if ky_tu.isdigit():
            # Nếu là chữ số thì ghép lại
            so_hien_tai += ky_tu
        else:
            # Nếu không phải chữ số 
            if so_hien_tai != "":
                ds_so.append(int(so_hien_tai))
                so_hien_tai = ""
    if so_hien_tai != "":
        ds_so.append(int(so_hien_tai))
    if len(ds_so) > 0:
        tong = sum(ds_so)
        trung_binh = tong / len(ds_so)
        return ds_so, tong, trung_binh
    else:
        return [], 0, 0
chuoi = input()
ds, tong, tb = tach_so_va_tinh(chuoi)
print(ds, tong, tb)