# Brute Force Approach

from typing import List

def singleNonDuplicate(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    
    for i in range(len(nums)):
        if i == 0:
            if nums[i] != nums[i + 1]:
                return nums[i]
        if i == n - 1:
            if nums[i] != nums[i -1]:
                return nums[i]
        else:
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]

if __name__ == "__main__":
    nums = [1,1,2,3,3,4,4,8,8]
    print(singleNonDuplicate(nums))