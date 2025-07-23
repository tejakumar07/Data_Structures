# Opimal Solution
# Using Binary Search

from typing import List

def findPeakElement(nums: List[int]) -> int:
    n = len(nums)
    if n < 2:
        return n - 1
    if nums[0] > nums[1]:
        return 0
    elif nums[n-1] > nums[n - 2]:
        return n - 1
    low = 1
    high = n - 2

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid -1]:
            return mid
        elif nums[mid - 1] < nums[mid]:
            low = mid + 1
        else:
            high = mid -1

if __name__ == "__main__":
    nums = [1,2,3,1]
    print(findPeakElement(nums))