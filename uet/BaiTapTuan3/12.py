def nam_nhuan(n):
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        return "Yes"
    return "No"
n = int(input())
print(nam_nhuan(n))