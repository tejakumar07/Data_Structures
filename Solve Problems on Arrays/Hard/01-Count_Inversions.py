# Brute Force Approach

def count_inversion(nums):
    cnt = 0
    n = len(nums)

    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] > nums[j]:
                cnt += 1
    return cnt

if __name__ == "__main__":
    arr = [5, 3, 2, 4, 1]