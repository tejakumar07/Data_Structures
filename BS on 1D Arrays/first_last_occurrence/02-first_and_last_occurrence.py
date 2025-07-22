# Using Binary Search
# Using Upper Bound and Lower Bound
# Not an Optimal Solution

def lower_bound(nums, X):
    n = len(nums)
    ans = n
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= X:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


def upper_bound(nums, X):
    n = len(nums)
    ans = n
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > X:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


def first_and_last_occurence(nums, target):
    lb = lower_bound(nums, target)
    up = upper_bound(nums, target)
    if lb == len(nums) or nums[lb] != target:
        return [-1, -1]
    else:
        return[lb, up - 1]


if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    ans = first_and_last_occurence(nums, target)
    print(ans)