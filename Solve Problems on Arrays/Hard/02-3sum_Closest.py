# Optimal Solution

def three_sum_closest(nums, target):
    n = len(nums)
    if n < 3:
        return nums
    nums.sort()

    closest = nums[0] + nums[1] + nums[2]

    for i in range(n - 2):
        left, right = i + 1, n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if abs(target -current_sum) < abs(target - closest):
                closest = current_sum
            
            if current_sum < target:
                left += 1
            
            elif current_sum > target:
                right -= 1
            
            else:
                return target
    return closest

if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1
    print(three_sum_closest(nums, target))  # Output: 2
