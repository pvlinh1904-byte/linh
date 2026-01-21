def snt(a):
    for i in range(2, a//2+1):
        if a % 2 == 0:
            return False
    if a > 1:
        return True
    return False

print(snt(7))