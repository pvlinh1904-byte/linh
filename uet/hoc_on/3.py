#Cho dãy N số nguyên dương, tính tổng các số có k chữ số. 
#Dãy được nhập trên 1 dòng, mỗi phần tử cách nhau 1 dấu cách, dòng sau là số nguyên dương k.
arr = list(map(int, input("arr = ").split()))
k = int(input("k = "))
tong = 0
for i in arr:
   
    if len(str(i)) == k:
        tong += i
print(tong)