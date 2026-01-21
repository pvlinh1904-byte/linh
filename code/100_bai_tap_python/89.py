U = float(input("Nhập vào U dola: "))
V = float(input("Nhập vào V Euro: "))
L_A = input(("Nhập vào list A: "))
L_A = L_A.split(",")
L_A = list(map(float,L_A))
L_B = input(("Nhập vào list B: "))
L_B = L_B.split(",")
L_B = list(map(float,L_B))

def vitri_min(L):
    kq = None
    for i in range(len(L)):
        if kq == None or L[kq] > L[i]:
            kq = i
    return kq

cty_dola = vitri_min(L_A)
cty_euro = vitri_min(L_B)

def giarenhi(L):
    L = L.copy()
    vt_min = vitri_min(L)
    L.pop(vt_min)
    kq = None
    for i in L:
        if kq == None or kq > i:
            kq = i
    return kq

if cty_dola != cty_euro:
    s = U/L_A[cty_dola] + V/L_B[cty_euro]
else:
    gianhi_dola = giarenhi(L_A)
    gianhi_euro = giarenhi(L_B)
    s1 = U/L_A[cty_dola] + V/gianhi_euro
    s2 = U/gianhi_dola + V/L_B[cty_euro]
    if s1 > s2:
        s = s1
    else:
        s = s2
print(s)