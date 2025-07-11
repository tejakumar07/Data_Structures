# Better Solution

def maximum_product(nums):
    n = len(nums)
    maxi = float("-inf")

    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= nums[j]

            maxi = max(maxi, prod)
    return maxi

if __name__ == "__main__":
    arr = [2, 3, -5, 8, 6, 0, 10, 12, -6, 0, -8, 13, 0, 19]
    ans = maximum_product(arr)
    print(f"Maximum Product is: {ans}")