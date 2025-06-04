def MaximumSubArray(nums):
    maximum = float("-inf")

    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            maximum = max(maximum, sum)
    return None if maximum == float('-inf') else maximum


if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(MaximumSubArray(arr))