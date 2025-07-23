# Optimal Solution
# Using Binary Search

from typing import List

def findMin(nums: List[int]) -> int:
    n = len(nums)
    low = 0
    high = n - 1
    ans = float("inf")
    indx = -1
    while low <= high:
        mid = (low + high) // 2
        
        if nums[low] <= nums[high]:
            if nums[low] < ans:
                ans = nums[low]
                indx = low
            break

        elif nums[low] <= nums[mid]:
            if nums[low] < ans:
                ans = nums[low]
                indx = low
            low = mid + 1
        else:
            if nums[mid] < ans:
                ans = nums[mid]
                indx = mid
            high = mid - 1
    return ans, indx

if __name__ == "__main__":
    nums = [3,4,5,1,2]
    print(findMin(nums))