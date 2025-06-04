# Optimal Approach
# Using Kadane's Algorithm


def MaximumSubArray(nums):
    sum = 0
    maximum = float("-inf")

    for i in range(len(nums)):
        sum += nums[i]

        maximum = max(sum, maximum)

        if sum < 0:
            sum = 0

    return maximum


if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(MaximumSubArray(arr))