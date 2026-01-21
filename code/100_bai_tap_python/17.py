a, b, c = map(float, input("a, b, c = ").split())
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print(a, b, c)