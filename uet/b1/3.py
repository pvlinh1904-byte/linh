import math
def prime_number(n: int) -> bool:
    for i in range(2, math.sqrt(n) + 1):
        if n % i == 0:
            return False
    return n >= 2