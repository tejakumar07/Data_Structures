# Brute Force Approach

from typing import List
import math

def smallestDivisor(nums: List[int], threshold: int) -> int:
    n = len(nums)
    mini = float("inf")
    maxi = float("-inf")
    for i in range(n):
        mini = min(mini, nums[i])
        maxi = max(maxi, nums[i])
    
    for i in range(mini, maxi + 1):
        _sum = 0
        for j in range(n):
            _sum += math.ceil(nums[j] / i)
        if _sum <= threshold:
            return i
nums = [1,2,5,9]
threshold = 6
print(smallestDivisor(nums, threshold))