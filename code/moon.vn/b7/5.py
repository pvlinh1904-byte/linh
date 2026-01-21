numbers = input().split()
numbers = [int(num) for num in numbers]
numbers.sort(reverse = True)
print(numbers)