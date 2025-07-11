# Brute Force Approach

def maximum_product(nums):
    maxi = float("-inf")
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            prod = 1
            for k in range(i, j + 1):
                prod *= nums[k]
            maxi = max(maxi, prod)
    return maxi

if __name__ == "__main__":
    arr = [2, 3, -5, 8, 6, 0, 10, 12, -6]
    ans = maximum_product(arr)
    print(f"Maximum Product is: {ans}")