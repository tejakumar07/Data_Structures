# Similar to the Lower Bound Proble
# Optimal Approach
# Brute Force is Linear Search

def upper_bound(nums, X):
    n = len(nums)
    ans = n
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > X:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
if __name__ == "__main__":
    arr = [3, 5, 8, 10, 15, 19, 19, 19]
    target = 10
    ans = upper_bound(arr, target)
    print(ans)
