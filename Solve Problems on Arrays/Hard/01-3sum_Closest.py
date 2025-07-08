# Brute Force Approach

def sum_closest(nums, target):
    n = len(nums)
    closest = nums[0] + nums[1] + nums[2]

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j + 1, n):
                current_sum = nums[i] + nums[j] + nums[k]

                if abs(target - current_sum) < abs(target - closest):
                    closest = current_sum
    return closest

if __name__ == "__main__":
    nums = [-1,2,1,-4]
    target = 1
    print(sum_closest(nums, target))