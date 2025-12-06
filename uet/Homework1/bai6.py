import math
a, b, c = map(float, input("a, b, c = ").split(", "))
if (a+b>c) and (b+c>a) and (a+c>b):
    p = (a + b + c) / 2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"diện tích tam giác = {s:.1f}")
else:
    print("là 1 tam giác")