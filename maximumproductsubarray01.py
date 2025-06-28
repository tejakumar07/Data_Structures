def MaximumProductSubArray(nums):
    max_prod = 1
    for i in range(len(nums)):
        prod = 1
        for j in range(i, len(nums)):
            prod *= nums[j]
            max_prod = max(max_prod, prod)
    return max_prod
if __name__ == "__main__":
    nums = [2,3,-2,4]
    print(MaximumProductSubArray(nums))