# Optimal Solution
# Using Binary Search

from typing import List

def findMin(nums: List[int]) -> int:
    n = len(nums)
    low = 0
    high = n - 1
    ans = float("inf")

    while low <= high:
        mid = (low + high) // 2
        
        if nums[low] <= nums[high]:
            ans = min(ans, nums[low])
            break

        elif nums[low] <= nums[mid]:
            ans = min(ans, nums[low])
            low = mid + 1
        else:
            ans = min(ans, nums[mid])
            high = mid - 1
    return ans

if __name__ == "__main__":
    nums = [3,4,5,1,2]
    print(findMin(nums))