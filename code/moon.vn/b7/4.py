l = input().split()
l = [int(num) for num in l]
t = 0
for i in l:
    num = float(i)
    if (type(i) == int or type(i) == float):
        if i > 0:
            t = t + num
print(l)
if ( t == 0):
    t = -1
print(t)