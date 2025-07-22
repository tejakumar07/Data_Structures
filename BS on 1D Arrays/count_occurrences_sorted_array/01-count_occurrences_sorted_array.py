# Optimal Solution
# using the Binary Search

from typing import List

def first_occurence(nums, X):
    first = -1
    n = len(nums)
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == X:
            first = mid
            high = mid - 1
        elif nums[mid] < X:
            low = mid + 1
        else:
            high = mid - 1
    return first

def second_occurence(nums, X):
    n = len(nums)
    second = -1
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == X:
            second = mid
            low = mid + 1
        elif nums[mid] < X:
            low = mid + 1
        else:
            high = mid - 1
    return second
def searchRange(nums: List[int], target: int) -> List[int]:
    ff = first_occurence(nums, target)
    if ff == -1:
        return 0
    else:
        ss = second_occurence(nums, target)
        return (ss - ff) + 1

if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    ans = searchRange(nums, target)
    print(ans)