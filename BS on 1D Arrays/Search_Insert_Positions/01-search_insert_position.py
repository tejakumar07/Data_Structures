# Optimal Solution
# Using Lower Bound Binary Search Method

def search_insert_position(nums, X):
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

if __name__ == "__main__":
    arr = [1, 3, 5, 6]
    target = 5
    ans = search_insert_position(arr, target)
    print(ans)