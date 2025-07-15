# Brute Force Approach
def LongestSubArray(arr, k):
    n = len(nums)
    maxi = 1

    for i in range(n):
        for j in range(i+1, n):
            current_sum = 0
            for k in range(i, j + 1):
                current_sum += nums[k]
            
            if current_sum == target:
                maxi = max(maxi, j - i + 1)
    return maxi

if __name__ == "__main__":
    arr = [1,2,3,1,1,1,1,4,2,3]
    k = 3
    print(LongestSubArray(arr, k))
