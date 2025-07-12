# Using the While Loop

def binary_search(nums, k):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == k:
            return mid
        elif k > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    arr = [3, 4, 6, 7, 9, 12, 16, 17]
    target = 70
    ans = binary_search(arr, target)
    print(f"Element {target} is at index {ans}") if ans != - \
        1 else print(f"Element {target} not found in the array")
