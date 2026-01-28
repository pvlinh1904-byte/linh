def Median(nums):
    a,b,c,d,e = nums

    if a > b: a,b = b,a
    if c > d: c,d = d,c
    if a > c: a,c = c,a; b,d = d,b
    if b > e: b,e = e,b
    if b > c: b,c = c,b
    if d < b: return d
    if e < b: return e
    return b

nums = list(map(int, input().split()))
print(Median(nums))
