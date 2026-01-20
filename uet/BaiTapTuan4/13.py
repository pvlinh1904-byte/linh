def sum_proper_diviors(n):
    if n == 1:
        return 0
    
    s = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
        i += 1
    return s
a, b = map(int, input().split())
if sum_proper_diviors(a) == b and sum_proper_diviors(b) == a:
    print("true")
else:
    print("false")