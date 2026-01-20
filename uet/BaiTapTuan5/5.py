from typing import List
def find_first_index(lst: List[int], k: int) -> int:
    for i, val in enumerate(lst):
        if val == k:
            return i
    return -1
numbers = list(map(int, input().split()))
k = int(input())
print(find_first_index(numbers, k))