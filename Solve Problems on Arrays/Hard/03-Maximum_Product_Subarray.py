# Optimal Solution

def maximum_product(nums):
    n = len(nums)
    preffix = 1
    suffix = 1
    maxi = float("-inf")

    for i in range(n):
        if preffix == 0:
            preffix = 1
        elif suffix == 0:
            suffix = 1
        preffix *= nums[i]
        suffix *= nums[n-1-i]
        maxi = max(maxi, max(preffix, suffix))
    return maxi

if __name__ == "__main__":
    arr = [2, 3, -5, 8, 6, 0, 10, 12, -6]
    ans = maximum_product(arr)
    print(f"Maximum Product is: {ans}")