# Optimal Solution

def three_sum_closest(nums, target):
    nums.sort()
    n = len(nums)
    closest = nums[0] + nums[1] + nums[2]
    
    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            _sum = nums[i] + nums[left] + nums[right]
            
            if (abs(target - _sum) < abs(target - closest)) or \
               (abs(target - _sum) == abs(target - closest) and _sum < closest):
                closest = _sum

            if _sum < target:
                left += 1
            elif _sum > target:
                right -= 1
            else:
                return target
    return closest

if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1
    print(three_sum_closest(nums, target))  # Output: 2
