# To track the Entire Sub Array

def MaximumSubArray(nums):
    sum = 0
    maximum = float("-inf")
    start = 0
    ans_start = -1
    ans_end = -1

    for i in range(len(nums)):
        if sum == 0:
            start = i
        sum += nums[i]

        if sum > maximum:
            maximum = sum
            ans_start = start
            ans_end = i

        if sum < 0:
            sum = 0
    return nums[ans_start:ans_end+1]


if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(MaximumSubArray(arr))
