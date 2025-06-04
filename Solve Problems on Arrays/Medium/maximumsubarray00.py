# Brute Force Approach

def MaximumSubArray(nums):
    maximum = float("-inf")

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sum = 0
            for k in range(i, j+1):
                sum += nums[k]
            maximum = max(maximum, sum)
    return maximum


if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(MaximumSubArray(arr))
