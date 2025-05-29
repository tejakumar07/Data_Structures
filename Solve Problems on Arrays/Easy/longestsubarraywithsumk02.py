# Better Approach
# Only for Postive Integers

def LongestSubArray(nums, k):
    length = 0
    sum = 0
    presum = {}
    for i in range(0, len(nums)):
        sum += nums[i]

        rem = sum - k

        if sum == k:
            length = max(length, i+1)

        if rem in presum:
            le = i - presum[rem]
            length = max(length, le)

        if sum not in presum:
            presum[sum] = i
    return length


if __name__ == "__main__":
    arr = [1,2,3,1,1,1,1,4,2,3]
    k = 3
    print(LongestSubArray(arr, k))

