from typing import List

def search(nums: List[int], target: int) -> int:
    n = len(nums)
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return True
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1
            continue
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
    return False

if __name__ == "__main__":
    nums = [2,5,6,0,0,1,2]
    target = 0
    ans = search(nums, target)
    print(ans)