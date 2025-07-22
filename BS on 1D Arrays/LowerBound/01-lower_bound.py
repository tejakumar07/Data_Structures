# This is the Optimal Approach
# Brute Forca approach can be solved using linear search

def lower_bound(nums, X):
    n = len(nums)
    ans = n
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= X:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
if __name__ == "__main__":
    arr = [1, 2, 3, 3, 5, 8, 8, 10, 10, 11]
    target = 9
    ans = lower_bound(arr, target)
    print(ans)
