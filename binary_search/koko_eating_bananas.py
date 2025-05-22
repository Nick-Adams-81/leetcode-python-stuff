import math

def minEatingSpeed(piles: list[int], h: int) -> int:
    left, right = 1, max(piles)
    result = right

    while left <= right:
        k = left + (right - left) // 2
        total_time = 0
        for p in piles:
            total_time += math.ceil(float(p) / k)
        if total_time <= h:
            result = k
            right = k -1
        else:
            left = k +1
    return result

piles = [1,4,3,2]
print(minEatingSpeed(piles, 9))