def Max_Of_Two(a, b):
    if a > b:
        return a
    else:
        return b
a, b = map(int, input().split())
print(Max_Of_Two(a, b))