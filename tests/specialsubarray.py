# Problem Statement:
# Given an array of integers, find the number of special subarrays of size 3 where the sum of the first and third elements equals the middle element.

# Input Format

#    A single line containing space-separated integers

# Constraints

#    The array length (N) must be at least 3

#     All elements are integers

# Sample input 1:

# 1 3 2 4 6 5

# Sample output 1:

# 2



# Sample input 2:

# 1 2 3 4 5

# Sample output 2:

# 0


nums = list(map(int, input().split()))

count = 0

for i in range(len(nums) - 2):
    a = nums[i]
    b = nums[i+1]
    c = nums[i+2]

    if b == a + c:
        count += 1
print(count)