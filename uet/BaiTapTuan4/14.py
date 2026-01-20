def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
m, n = map(int, input().split())
print(gcd(m, n))