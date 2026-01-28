path = input().strip()

try:
    f = open(path, 'r')
    print("YES")
    f.close()
except:
    print("NO")
