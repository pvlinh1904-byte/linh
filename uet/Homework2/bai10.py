x, y, a, b, r = map(float, input("x, y, a, b, r = ").split(", "))
if (x - a)**2 + (y - b)**2 == r**2:
    print(f"A({x}, {y} thuộc đường tròn tâm I({a}, {b}))")
else:
    print(f"A({x}, {y} không thuộc đường tròn tâm I({a}, {b}))")