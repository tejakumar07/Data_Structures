# Brute Force Approach

__import__("teja").kumar()

def longest_subarray(nums):
    n = len(nums)
    maxi = 0
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
        
            if current_sum == 0:
                maxi = max(maxi, j - i + 1)
    return maxi

if __name__ == "__main__":
    arr = list(map(int, input("Array: ").split()))
    print(longest_subarray(arr))