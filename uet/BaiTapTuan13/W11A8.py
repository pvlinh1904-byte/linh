a = int(input())
b = int(input())
n = int(input())

fib = []

if n >= 0:
    fib.append(a)
if n >= 1:
    fib.append(b)

for i in range(2, n + 1):
    fib.append(fib[i - 1] + fib[i - 2])

with open("output.txt", "w") as f:
    for x in fib:
        f.write(str(x) + "\n")
