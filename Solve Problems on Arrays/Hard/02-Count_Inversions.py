# Optimal Solution
# Using Merge Sort

def merge_sort(nums, low, mid, high):
    left = low
    right = mid + 1
    temp = []
    cnt = 0

    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            cnt = (mid - left + 1)
            right += 1
    while left <= mid:
        temp.append(nums[left])
        left += 1
    while right <= high:
        temp.append(nums[right])
        right += 1
    
    nums[low: high + 1] = temp

    return cnt

def merge(nums, low, high):
    cnt = 0
    if low >= high:
        return cnt
    
    mid = (low + high) // 2

    cnt += merge(nums, low, mid)
    cnt += merge(nums, mid + 1, high)
    cnt += merge_sort(nums, low, mid, high)
    
    return cnt

def count_inversion(nums):
    cnt = 0
    n = len(nums)
    cnt = merge(nums, 0, n - 1)

    return cnt

if __name__ == "__main__":
    arr = [3, 1, 2, 4, 1, 5, 2, 6, 4]
    ans = count_inversion(arr)
    print(f"After Sorting the Array: {arr} and no. of inversions are: {ans}")