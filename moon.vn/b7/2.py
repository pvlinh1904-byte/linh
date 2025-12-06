numbers = list(map(int, input("nhập dãy: ").split(",")))
numbers.sort(reverse=True)
t = tuple(numbers)
print(t)