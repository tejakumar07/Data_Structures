# Brute Force Approach - II

def LongestSubArray(nums, target):
    n = len(nums)
    maxi = 1

    for i in range(n):
        current_sum = 0
        for j in range(i+1, n):
            current_sum += nums[j]

            if current_sum == target:
                maxi =  max(maxi, j - i)
    return maxi

if __name__ == "__main__":
    arr = [1,2,3,1,1,1,1,4,2,3]
    k = 3
    print(LongestSubArray(arr, k))
