import bisect

def findRadius(houses, heaters):
    houses.sort()
    heaters.sort()
    res = 0
    for h in houses:
        i = bisect.bisect_left(heaters, h)
        left = abs(h - heaters[i-1]) if i-1 >= 0 else float('inf')
        right = abs(heaters[i] - h) if i < len(heaters) else float('inf')
        res = max(res, min(left, right))
    return res

houses = list(map(int, input().split()))
heaters = list(map(int, input().split()))
print(findRadius(houses, heaters))
