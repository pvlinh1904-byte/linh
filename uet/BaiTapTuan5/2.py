from typing import Tuple

def swap(a: int, b: int) -> Tuple[int, int]:
    return b, a

a, b = map(int, input().split())
print(swap(a, b))