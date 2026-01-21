def giatri_tb(L):
    tong = 0
    for i in L:
        tong += i
    return tong/len(L)

def main(L,k):
    dodai_max = None
    kq = None
    for i in range(len(L)):
        for j in range(i+1, len(L)+1):
            L_con = L[i:j]
            if giatri_tb(L_con) == k:
                if dodai_max == None or dodai_max < len(L_con):
                    dodai_max = len(L_con)
                    kq = L_con
    return kq
print(main([2,4,3,5,3,5,6,3,4],3))