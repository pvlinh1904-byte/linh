import math 
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
n = int(input("n = "))
for i in range(2, n + 1):
    if is_prime(i):
        print(i, end = (" ; "))