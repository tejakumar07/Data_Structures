# Using Recursion

def binary_search(nums, low, high, k):
    if low > high:
        return -1

    mid = (low + high) // 2

    if nums[mid] == k:
        return mid
    elif nums[mid] < k:
        return binary_search(nums, mid + 1, high, k)
    else:
        return binary_search(nums, low, mid - 1, k)


if __name__ == "__main__":
    arr = [3, 4, 6, 7, 9, 12, 16, 17]
    target = 9
    ans = binary_search(arr, 0, len(arr) - 1, target)
    print(f"Element {target} is at index {ans}") if ans != - \
        1 else print(f"Element {target} not found in the array")
