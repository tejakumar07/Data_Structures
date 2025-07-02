# Problem Statement:
# Take an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
#
# Examples:
# Input:
# 4
#
#
# -2 0 1 3
#  2
#
# Output:
#
# 2
#
# Explanation: Because there are two triplets which sums are less than 2:
#
# [-2,0,1]
#
# [-2,0,3]
#
# Input:
# 1
#
# 0
#
# 0
#
# Output:
#
# 0
#
# Explanation:The array have only one element, so no valid triplets exist.
#
# n == nums.length
# 0 <= n <= 3500
# -100 <= nums[i] <= 100
# -100 <= target <= 100



n = int(input())
nums = list(map(int, input().split()))
target = int(input())

count = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if nums[i] + nums[j] + nums[k] < target:
                count += 1

print(count)
