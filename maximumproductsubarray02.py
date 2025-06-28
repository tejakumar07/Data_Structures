def MaximumProductSubArray(nums):
    n = len(nums)
    max_prod = float("-inf")
    prefix, suffix = 1, 1

    for i in range(n):
        if prefix == 0:
            prefix = 1
        
        if suffix == 0:
            suffix = 1
        
        prefix *= nums[i]
        suffix *= nums[(n-1)-i]
        max_prod = max(max_prod, max(prefix, suffix))
    return max_prod

if __name__ == "__main__":
    nums = [2,3,-2,4]
    print(MaximumProductSubArray(nums))