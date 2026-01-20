arr = list(map(int, input("arr = ").split()))
trai = 0
phai = len(arr) - 1
doi_xung = True
while trai < phai:
    if arr[trai] != arr[phai]:
        doi_xung = False
        break
    trai += 1
    phai -= 1
if doi_xung:
    print("yes")
else:
    print("no")