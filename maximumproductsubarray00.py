def MaximumProductSubArray(nums):
    max_prod = 1
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            prod = 1
            for k in range(i, j+1):
                prod *= nums[k]
            max_prod = max(prod, max_prod)
    return max_prod
if __name__ == "__main__":
    nums = [2,3,-2,4]
    print(MaximumProductSubArray(nums))