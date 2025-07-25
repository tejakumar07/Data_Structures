from typing import List
import math


class Solution:
    def divide(self, nums, div):
        _sum = 0
        for num in nums:
            _sum += math.ceil(num / div)
        return _sum


    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        maxi = max(nums)
        low = 1
        high = maxi

        while low <= high:
            mid = (low + high) // 2
            ans = self.divide(nums, mid)
            if ans <= threshold:
                high = mid - 1
            else:
                low = mid + 1
        return low


if __name__ == "__main__":
    teja = Solution()
    nums = [1,2,5,9]
    threshold = 6
    result = teja.smallestDivisor(nums, threshold)
    print(result)