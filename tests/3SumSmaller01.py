n = int(input())
nums = list(map(int, input().split()))
target = int(input())

nums.sort()
count = 0

for i in range(n - 2):
    left = i + 1
    right = n - 1

    while left < right:
        total = nums[i] + nums[left] + nums[right]
        if total < target:
            # All triplets from left to right-1 are valid
            count += (right - left)
            left += 1
        else:
            right -= 1

print(count)
