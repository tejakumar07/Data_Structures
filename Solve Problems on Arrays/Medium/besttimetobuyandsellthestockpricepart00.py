# This is the Dynamic Programming Problem

def BestTimeToBuyAndSellTheStock(nums):
    minimum = nums[0]
    maxprofit = 0

    for i in range(len(nums)):
        cost = nums[i] - minimum
        maxprofit = max(maxprofit, cost)
        minimum = min(minimum, nums[i])
    return maxprofit


if __name__ == "__main__":
    arr = [7, 1, 5, 3, 6, 4]
    print(BestTimeToBuyAndSellTheStock(arr))
