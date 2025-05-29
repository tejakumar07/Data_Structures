# Brute Force Approach - II

def LongestSubArray(nums, k):
    length = 0
    for i in range(0, len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum == k:
                length  = max(length, j - i + 1)
    return length

if __name__ == "__main__":
    arr = [1,2,3,1,1,1,1,4,2,3]
    k = 3
    print(LongestSubArray(arr, k))
