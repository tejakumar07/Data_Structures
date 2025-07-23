# Brute Force Approach
# Using Linear Search

def find_minimum(nums):
    minimum = nums[0]
    
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum

if __name__ == "__main__":
    nums = [3,4,5,1,2]
    print(find_minimum(nums))