# Optimal Approach
# Using Binary Search

from typing import List
import math
def solve(nums, speed):
    total_hours = 0
    for num in nums:
        total_hours += math.ceil(num / speed)
    return total_hours
def minEatingSpeed(piles: List[int], h: int) -> int:
    low  = 1
    high = max(piles)
    while low <= high:
        mid = (low + high) // 2
        ans = solve(piles, mid)

        if ans <= h:
            high = mid - 1
        else:
            low = mid + 1
    return low

if __name__ == "__main__":
    piles = [3,6,7,11]
    h = 8
    print(minEatingSpeed(piles, h))