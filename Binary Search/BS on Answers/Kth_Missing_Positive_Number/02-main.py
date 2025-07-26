# Optimal Approach
# Using Binary Search

from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            missing = arr[mid] - (mid + 1)

            if missing < k:
                low = mid + 1
            else:
                high = mid -1 
        return low + k         # We can also return high + 1 + k

if __name__ == "__main__":
    teja = Solution()
    arr = [2,3,4,7,11]
    k = 5
    ans = teja.findKthPositive(arr, k)
    print(ans)