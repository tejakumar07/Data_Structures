# Optimal Solution
# Using the Binary Search

from typing import List

def search(nums: List[int], target: int) -> int:
    n = len(nums)
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    ans = search(nums, target)
    print(ans)