def floor(nums, X):
    n = len(nums)
    ans = -1
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] <= X:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

def ceil(nums, X):
    ans = -1
    n = len(nums)
    low, high = 0, n - 1
    
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= X:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def getFloorAndCeil(nums, X):
    f = floor(nums, X)
    c = ceil(nums, X)
    return [f, c]

if __name__ == "__main__":
    arr = [3, 4, 4, 7, 8, 10]
    X = 5
    ans = getFloorAndCeil(arr, X)
    print("The floor and ceil are:", ans[0], ans[1])