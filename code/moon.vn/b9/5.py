s = input("s = ")

#mặc định coi chuỗi là đối xứng
rs = True
j = len(s) - 1

for i in range(0, len(s) // 2):
    if (i == j):
        break
    if(s[i] != s[j]):
        rs = False
        break
    j = j - 1
print(rs)