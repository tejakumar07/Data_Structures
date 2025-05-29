# Optimal Solution
# Only Work for +VE Integers and 0's

def LongestSubArray(nums, k):
    n = len(nums)
    left, right = 0, 0
    MaxLen = 0
    total_sum = nums[0]

    while right < n:
        while left <= right and total_sum > k:
            total_sum -= nums[left]
            left += 1
        if total_sum == k:
            MaxLen = max(MaxLen, right-left +1)
        right += 1
        if right < n:
             total_sum += nums[right]
    return MaxLen

if __name__ == "__main__":
    arr = [1,2,3,1,1,1,1,3,3]
    d = 6
    print(LongestSubArray(arr, d))
