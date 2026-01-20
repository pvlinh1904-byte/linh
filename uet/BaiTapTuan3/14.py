def giai_phuong_trinh_bac_nhat(a, b):
    if a == 0 and b == 0:
        return "vo so nghiem"
    elif a == 0:
        return "vo nghiem"
    else:
        x = -b / a
        return f"{x:.2f}"
a, b = map(int, input().split())
print(giai_phuong_trinh_bac_nhat(a, b))