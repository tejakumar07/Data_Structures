from typing import List

def singleNonDuplicate(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    
    if nums[0] != nums[1]:
        return nums[0]
    elif nums[n -1] != nums[n - 2]:
        return nums[n - 1]
    else:
        low, high = 1, n - 2

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            elif (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 == 1 and nums[mid] == nums[mid -1]):
                low = mid + 1
            else:
                high = mid - 1

if __name__ == "__main__":
    nums = [7,7,10,11,11,12,12]
    print(singleNonDuplicate(nums))