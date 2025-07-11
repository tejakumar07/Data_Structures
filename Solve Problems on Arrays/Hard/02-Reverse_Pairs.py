# Optimal Solution
# Using Merge Sort

def merge_sort(nums, low, mid, high):
    left = low
    right = mid + 1
    temp = []

    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1
    while left <= mid:
        temp.append(nums[left])
        left += 1
    while right <= high:
        temp.append(nums[right])
        right += 1
    nums[low:high+1] = temp


def count_pairs(nums, low, mid, high):
    right = mid + 1
    cnt = 0
    for i in range(low, mid + 1):
        while right <= high and nums[i] > 2 * nums[right]:
            right += 1
        cnt += (right - (mid + 1))
    return cnt


def merge(nums, low, high):
    cnt = 0
    if low >= high:
        return cnt
    mid = (low + high) // 2
    cnt += merge(nums, low, mid)
    cnt += merge(nums, mid + 1, high)
    cnt += count_pairs(nums, low, mid, high)
    merge_sort(nums, low, mid, high)
    return cnt


def ts(nums):
    n = len(nums)
    return merge(nums, 0, n - 1)


if __name__ == "__main__":
    a = [4, 1, 2, 3, 1]
    cnt = ts(a)
    print(cnt)
