# Brute Force Approach
# Using Linear Search

def findPeek(nums):
    n = len(nums)

    for i in range(n):
        left = float("-inf") if i == 0 else nums[i-1]
        right = float("-inf") if i == n - 1 else nums[i + 1]
        if left < nums[i] and nums[i] > right:
            return i
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
    print(findPeek(arr))