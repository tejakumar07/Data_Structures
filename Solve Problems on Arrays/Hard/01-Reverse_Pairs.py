# Brute Force Approach

def reverse_pairs(nums):
    n = len(nums)
    cnt = 0
    for i in range(n-1):
        for j in range(i + 1, n):
            if nums[i] > 2 * nums[j]:
                cnt += 1
    return cnt
if __name__ == "__main__":
    arr = [40, 25, 19, 12, 9, 6, 2]
    ans = reverse_pairs(arr)
    print(f"The No.of reverse pairs are: {ans}")